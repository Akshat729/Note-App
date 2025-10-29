📝 Notes App — FastAPI, MongoDB & Jinja2

A simple and lightweight CRUD (Create, Read, Update, Delete) Notes application built using FastAPI, MongoDB, and Jinja2 templates.
It demonstrates full-stack development with server-side rendering, form handling, and database operations.

🚀 Features

➕ Add Note — Create new notes with title and description
✏️ Edit Note — Update an existing note on the same page
❌ Delete Note — Remove unwanted notes from the database
👀 View Notes — Display all notes on a clean UI
💬 Pop-up Notifications — Shows success messages for actions like Add, Update, and Delete
⚡ Responsive Design using Bootstrap

| Component        | Technology                  |
| ---------------- | --------------------------- |
| **Backend**      | FastAPI                     |
| **Frontend**     | Jinja2 Templates, Bootstrap |
| **Database**     | MongoDB                     |
| **ORM / Driver** | PyMongo                     |
| **Language**     | Python 3.x                  |


📂 Project Structure

Note-App/
│
├── main.py
├── config/
│   └── db.py
├── models/
│   └── note.py
├── routes/
│   └── note.py
├── schemas/
│   └── note.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── requirements.txt
└── README.md

🧰 Requirements

Python 3.8+
MongoDB running locally or cloud (e.g., MongoDB Atlas)
FastAPI
Jinja2
Uvicorn
python-dotenv
pymongo

📜 API Endpoints

| Method | Endpoint            | Description         |
| ------ | ------------------- | ------------------- |
| `GET`  | `/`                 | View all notes      |
| `POST` | `/add`              | Add new note        |
| `GET`  | `/edit/{note_id}`   | Open note edit page |
| `POST` | `/update/{note_id}` | Update note         |
| `GET`  | `/delete/{note_id}` | Delete note         |


👨‍💻 Author

Akshat Rastogi

💼 Python Developer

📍 Mumbai, India

📧 akshatrastogi09@gmail.com

🌐 [LinkedIn](https://www.linkedin.com/in/akshat-rastogi-83a347178/)
