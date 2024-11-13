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