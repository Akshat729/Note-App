from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from pymongo import MongoClient

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates  =  Jinja2Templates(directory="templates")

conn = MongoClient("mongodb+srv://akshatrastogi:Akr1729@cluster1.f2xk0vf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    docs = conn.notes.notes.find({})
    for doc in docs:
        print(doc)
    return templates.TemplateResponse("index.html", {"request": request})
