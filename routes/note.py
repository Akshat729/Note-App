from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models.note import Note
from config.db import conn
from schemas.note import noteEntity, notesEntity


noteRouter = APIRouter()
templates  =  Jinja2Templates(directory="templates")


@noteRouter.get("/", response_class=HTMLResponse)
def home(request: Request):
    docs = conn.notes.notes.find({})
    showDocs = []
    for doc in docs:
        showDocs.append({
            "id": doc["_id"],
            "title" : doc["title"],
        "description" : doc["description"],
        "important" : doc["important"],
        })
    return templates.TemplateResponse("index.html", {"request": request, "showDocs": showDocs})

@noteRouter.post("/")
async def add_note(request: Request):
    form = await request.form()
    formDict = dict(form)
    formDict["important"] = "true" if formDict.get("important") == "on" else "false"
    note = conn.notes.notes.insert_one(formDict)
    return {"msg": "Note added successfully"}