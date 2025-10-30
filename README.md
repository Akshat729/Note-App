# 📝 FastAPI Notes App

A simple and efficient **Note Taking Application** built using **FastAPI**, **MongoDB**, and **Jinja2** templates.  
Users can **create**, **edit**, **delete**, and **view** notes directly from the web interface.  

---

## 🚀 Features

- 🗒️ Create and manage personal notes  
- ✏️ Edit existing notes on the same page  
- 🗑️ Delete notes easily  
- 💾 MongoDB for data storage  
- ⚡ FastAPI backend for high performance  
- 🎨 Jinja2 templates for dynamic HTML rendering  
- 🔔 Popup alert on successful note edit  

---

## 🏗️ Tech Stack  

| Component        | Technology                  |
| ---------------- | --------------------------- |
| **Backend**      | FastAPI                     |
| **Frontend**     | Jinja2 Templates, Bootstrap |
| **Database**     | MongoDB                     |
| **ORM / Driver** | PyMongo                     |
| **Language**     | Python 3.x                  |

---

## 📦 Installation


## 📦 Installation

Follow these steps to set up the project locally 👇

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/fastapi-notes-app.git
cd fastapi-notes-app
```

### 2️⃣ Create a Virtual Environment  
```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up MongoDB  
- Make sure MongoDB is running locally or use a cloud service like MongoDB Atlas.
- Update your MongoDB connection string in your FastAPI app if required.


### 5️⃣ Run the Application  
```bash
uvicorn main:app --reload
```

---

## 🌐 Access the App
Once the server starts, open your browser and visit:  
👉 http://127.0.0.1:8000  

---

## 📁 Project Structure
```csharp
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
```

---

## 👨‍💻 Author  

Akshat Rastogi  
💼 Python Developer  
📍 Mumbai, India  
📧 akshatrastogi09@gmail.com  
🌐 [LinkedIn](https://www.linkedin.com/in/akshat-rastogi-83a347178/)
