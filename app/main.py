#!/usr/bin/env python3

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import json
import os
import MySQLdb
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static", html = True), name="static")

# db config stuff
DBHOST = os.environ.get('DBHOST')
DBUSER = os.environ.get('DBUSER')
DBPASS = os.environ.get('DBPASS')
DB = "nem2p"

@app.get("/")  # zone apex
def zone_apex():
    return {"What's up": "What's up API", "album_endpoint":"/albums","static_endpoint":"/static"}
    return {"How are you doing": "I am well", "album_endpoint":"/albums","static_endpoint":"/static"}
    return {"Hey there boss": "Hey there API", "album_endpoint":"/albums","static_endpoint":"/static"}
    return {"I hope you're happy": "I am!", "album_endpoint":"/albums","static_endpoint":"/static"}

