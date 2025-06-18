![Open Source](https://img.shields.io/badge/Open%20Source-Yes-brightgreen)
![Status](https://img.shields.io/badge/Status-Active-blue)
![Python](https://img.shields.io/badge/Python-3.1-blue)


# 📂 Python File Server with Auto-Restart Feature

This project is a lightweight file server built using Python’s built-in `http.server` module. It serves files from a `files/` directory and features a sleek web interface with a **refresh server** button that restarts the server process on demand.

---

## 🚀 Features

- 📁 Serves files from a local `files/` folder
- 💻 Clean and responsive HTML/CSS interface
- 🔄 One-click server restart via web UI
- ⚙️ Built with Python standard libraries (no external dependencies)
- 🧠 Automatically lists files in the UI with download links

---

## 📂 Project Structure

```
your_project/
├── server.py         # Main server script
└── files/            # Directory to store and serve files
```

---

## 🔧 Requirements

- Python 3.x

> ✅ No external packages are needed — everything runs using Python’s built-in modules.

---

## ▶️ How to Run

1. **Create a folder** named `files` in the same directory as `server.py`.

2. **Place any files** you want to share in the `files` folder.

3. **Run the server** by executing:

   ```bash
   python server.py
   ```

4. **Open your browser** and go to:

   ```
   http://localhost:8080
   ```

---

## 💡 How It Works

- `server.py` uses Python’s `http.server` module with a custom handler.
- The server serves files from the `files/` directory.
- It generates an HTML interface with:
  - A welcome message
  - A list of downloadable files
  - A button to "Refresh Server"
- The `/refresh` route restarts the server process via `subprocess` and `os._exit`.

---

## 🛑 Stopping the Server

To stop the server at any time, press:

```bash
Ctrl + C
```

---



## 📃 License

This project is open source and free to use. Feel free to modify or extend it.

---

## ✍️ Author
[Rahul Kuzur](https://www.facebook.com/rahul.kuzur.1) — Made with ❤️ using Python.
