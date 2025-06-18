import os
import sys
import time
import threading
import subprocess
from http.server import SimpleHTTPRequestHandler, HTTPServer

FILES_DIR = os.path.join(os.getcwd(), "files")


class CustomHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=FILES_DIR, **kwargs)

    def do_GET(self):
        try:
            # Handle the refresh button request
            if self.path == "/refresh":
                self.send_response(200)
                self.send_header("Content-type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write(self.get_html_page("🔄 Restarting Server..."))
                threading.Thread(target=self.restart_server).start()
                return

            # Serve the default page
            if self.path == "/":
                self.send_response(200)
                self.send_header("Content-type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write(self.get_html_page())
                return

            # Serve the CSS content directly
            if self.path == "/style.css":
                self.send_response(200)
                self.send_header("Content-type", "text/css; charset=utf-8")
                self.end_headers()
                self.wfile.write(self.get_css().encode('utf-8'))
                return

            # Call the default request handler for other GET requests
            super().do_GET()

        except Exception as e:
            print(f"Error while processing request for {self.path}: {e}")

    def get_html_page(self, message="Welcome to the File Server!"):
        """Generate HTML page content."""
        html = f"""
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>File Server</title>
                <link rel="stylesheet" href="/style.css">
            </head>
            <body>
                <div class="container">
                    <h1>📂 File Server</h1>
                    <p>{message}</p>
                    <button onclick="window.location.href='/refresh'">🔄 Refresh Server</button>
                    <h2>📁 Available Files</h2>
                    <ul>
        """
        
        # List files in the 'files' directory
        for filename in os.listdir(FILES_DIR):
            file_path = os.path.join(FILES_DIR, filename)
            if os.path.isfile(file_path):
                html += f'<li><a href="/{filename}" download>{filename}</a></li>'
        
        html += """
                    </ul>
                </div>
            </body>
        </html>
        """
        return html.encode('utf-8')

    def get_css(self):
        """Return the CSS as a string."""
        css = """
        body {
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f7fc;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .container {
            text-align: center;
            padding: 20px;
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            width: 80%;
            max-width: 800px;
        }

        h1 {
            font-size: 2.5em;
            color: #4CAF50;
        }

        h2 {
            color: #555;
            margin-bottom: 15px;
        }

        p {
            font-size: 1.2em;
            color: #888;
            margin-bottom: 30px;
        }

        button {
            background-color: #4CAF50;
            color: white;
            font-size: 1.2em;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        button:hover {
            background-color: #45a049;
        }

        ul {
            list-style-type: none;
            padding: 0;
        }

        ul li {
            margin: 10px 0;
        }

        ul li a {
            color: #007BFF;
            text-decoration: none;
            font-size: 1.1em;
        }

        ul li a:hover {
            text-decoration: underline;
        }
        """
        return css

    def restart_server(self):
        """Restart the server."""
        print("🔁 Restarting server...")
        time.sleep(2)
        
        python = sys.executable
        script = os.path.abspath(sys.argv[0])
        
        # Start a new process for the server
        try:
            subprocess.Popen([python, script])
            print("New server process started successfully.")
        except Exception as e:
            print(f"Error restarting the server: {e}")
        
        # Terminate the current server process
        os._exit(0)


def run(server_class=HTTPServer, handler_class=CustomHandler, port=8080):
    """Start the server and handle requests."""
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"🚀 Server started at: http://localhost:{port}")
    print(f"📁 Serving directory: {FILES_DIR}")
    try:
        httpd.serve_forever()
    except Exception as e:
        print(f"Server stopped due to error: {e}")


if __name__ == "__main__":
    run()
