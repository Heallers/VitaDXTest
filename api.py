# api.py

import uvicorn
from fastapi import FastAPI

import database

app = FastAPI()
m_host = "localhost"
m_port = 8080


@app.get("/annotations")
async def read_annotations():
    return database.get_annotations()


@app.get("/number_annotations_by_user")
async def read_number_annotations_by_user():
    return database.get_number_annotations_by_user()


@app.get("/number_annotations_by_project")
async def read_number_annotations_by_project():
    return database.get_number_annotations_by_project()


@app.get("/assets_with_majority_different_labels")
async def read_assets_with_majority_different_labels(_project_id: str):
    return database.get_assets_with_majority_different_labels(_project_id)


def run():
    database.initialize()
    uvicorn.run(app, host=m_host, port=m_port)
