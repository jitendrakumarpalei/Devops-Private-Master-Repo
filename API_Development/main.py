import requests as req
from typing import Optional
from fastapi import FastAPI
import json


app = FastAPI()
f = open("empty.dat", 'r')
secret = json.load(f)
f.close()


@app.get("/")
async def get_data():
    return {"message": "Welcome to FastAPI UI"}

@app.get("/users")
async def all_users():
    respo = req.get("http://192.168.1.104:8080/asynchPeople/api/json?depth=1", auth=('jenkins', secret['code']))
    return respo.json()

@app.post("/add_user")
async def add_user():
    respo = req.get("http://192.168.1.104:8080/roles/", auth=('jenkins', secret['code']))
