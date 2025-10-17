from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from config.db import conn
from schemas.note import noteEntity, notesEntity
from bson import ObjectId


noteRouter = APIRouter()
templates  =  Jinja2Templates(directory="templates")
collection = conn.notes.notes

@noteRouter.get("/", response_class=HTMLResponse)
def home(request: Request):
    docs = collection.find({})
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
    note = collection.insert_one(formDict)
    return {"msg": "Note added successfully"}

@noteRouter.get("/delete/{note_id}")
async def delete_note(note_id: str):
    note = collection.delete_one({"_id": ObjectId(note_id)})
    return RedirectResponse("/", status_code=303)

@noteRouter.get("/edit/{note_id}")
async def edit_note(request: Request, note_id: str):
    notes_cursor = collection.find({})
    notes = notes_cursor.to_list(length=100)
    note = collection.find_one({"_id": ObjectId(note_id)})
    return templates.TemplateResponse("index.html", {"request": request, "notes": notes, "edit_note": note})
