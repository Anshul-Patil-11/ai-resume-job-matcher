# backend/app/routes/resume_routes.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/hello")
def hello():
    return {"message": "Hello from resume_routes!"}
