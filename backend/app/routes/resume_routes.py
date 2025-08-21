# backend/app/routes/resume_routes.py

from fastapi import APIRouter

router = APIRouter()

from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@router.get("/about")
def about():
    return {"info": "This is the about page."}

@router.post("/submit")
def submit(data: dict):
    return {"received": data}