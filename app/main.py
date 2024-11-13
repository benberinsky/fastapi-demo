#!/usr/bin/env python3
from fastapi import Request, FastAPI
from typing import Optional
from pydantic import BaseModel
import pandas as pd
import json
import os

app = FastAPI()

@app.get("/")  # zone apex
def zone_apex():
<<<<<<< HEAD
    return {"Hello": "Hello API", "album_endpoint":"/albums","static_endpoint":"/static"}

@app.get("/multiply/{c}/{d}")
def multiply(c: int, d: int):
    return {product: c*d}

@app.get("/customer/{idx}")
def get_customer(idx: int):
    #Read in data from CSV file
    df = pd.read_csv("../customers.csv")
    #Filter data based on the index
    customer = df.iloc[idx]
    return customer.to_dict()

@app.post("/get_payload")
async def get_payload(request:Request):
    response = request.json()
    geo = response.get("geo")
    url = "https://maps.google.com/?q={geo}".format(geo=geo)
    #return await request.json
=======
    return {"What's up": "What's up API", "album_endpoint":"/albums","static_endpoint":"/static"}
    return {"How are you doing": "I am well", "album_endpoint":"/albums","static_endpoint":"/static"}
    return {"Hey there boss": "Hey there API", "album_endpoint":"/albums","static_endpoint":"/static"}
    return {"I hope you're happy": "I am!", "album_endpoint":"/albums","static_endpoint":"/static"}

>>>>>>> 9e14f30f15847878f14d0dd3f68e66a38bc632d7
