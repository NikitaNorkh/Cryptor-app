# 🔐 Secure Encryption Tool & Password Generator

This project is a **multi-functional website application** built with Python `eel` for the backend and plain HTML/CSS/JS for the frontend.

It was developed for a huge programming competition in 2024 in my city, where it successfully secured me a place in the finals. ( I was 16 years old at the moment )
<p align="center">
  <img src="src/assets/sert.jpg" alt="Certificate" width="550px" align="center">
</p>

---

## 📸 Screenshots

### Main Page

<p align="center">
  <img src="src/assets/main.png" alt="Main Page Screenshot" width="600px">
</p>

### Password Generator in Action

<p align="center">
  <img src="src/assets/password.gif" alt="Password Generator Demo" width="550px">
</p>

### Text Encryption Example

<p align="center">
  <img src="src/assets/enc1.gif" alt="Text Encryption Demo" width="550px">
</p>


---

## ⚙️ Features

✅ Password generator with character set selection (lowercase, uppercase, numbers, symbols)  
✅ Multiple encryption algorithms supported: `md5`, `crc32`, `sha1`, `sha256`, `sha512`  
✅ My own custom method — **DUCK encryption** that rearranges letters and adds "duck" in between for fun 🦆  

<p align="center">
  <img src="src/assets/enc2.gif" alt=" Duck Encryption Example" width="550px">
</p>

✅ User registration and login system  
✅ Session management across pages  
✅ Modal windows for registration and login  
✅ Smooth page transitions with jQuery  
✅ Logs created automatically for tracking activity  
✅ SQLite3 database for user storage  
✅ Fully compatible with all OS where Python runs (Windows, Linux, macOS)  

---

## 🚀 Usage

### Requirements:

- Python 3.9+  
- `eel` library  
- No extra dependencies needed for DB (uses built-in `sqlite3`)  

### Run project:

```bash
cd src
python main.py
```


The web interface will open and provide access to password generation, encryption tools, and user management.

For Windows users, a precompiled .exe file is available inside the dist folder.

## 🗂️ Project Structure

📦 Project Root
├── logs/ # Automatically created logs folder
├── db/ # SQLite database files
├── src/
│ ├── main.py # Main backend script with eel
│ ├── main_oop.py # Alternative OOP-style backend (optional)
│ └── web/ # All front-end files
│ ├── bootstrap/ # Bootstrap framework files
│ ├── css/ # Custom stylesheets
│ ├── icons/ # Icons for the UI
│ ├── jquery/ # jQuery library
│ ├── js/ # JavaScript files
│ ├── encrypt.html# Text encryption tool
│ ├── main.html # Main page
│ ├── pass.html # Password generator
│ └── pic1.png # Image for the main page
├── .gitignore
├── README.md

yaml
Copy
Edit

💡 **Notes:**  
- `logs` and `db` folders are auto-created at runtime if missing  
- All UI, pages and assets live inside `src/web/`  
- `.gitignore` ensures temp files and builds don't clutter your repo  

---

🎉 Special Thanks
Thanks to ItSTEP for organizing the coding competition where this project originally started!

PS: This project was designed with educational purposes in mind and showcases basic encryption principles combined with fun custom features like "Duck Encryption".
