from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

app = FastAPI()

conn = MongoClient(os.getenv("MONGODB_URI"))
