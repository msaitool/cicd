from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from routers import route

config =  dotenv_values(".env")

app = FastAPI()
# client = MongoClient(uri)
@app.on_event("startup")
def startup():
    app.mongodb_client = MongoClient(config["mongodb_uri"])
    app.database= app.mongodb_client[config["MONGO_DB"]]

@app.on_event("shutdown")
def shutdown():
    app.mongodb_client.close()


app.include_router(route.router)

