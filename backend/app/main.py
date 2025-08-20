# backend/app/main.py

from fastapi import FastAPI
from app.routes import resume_routes   # import the new router

app = FastAPI()

# Include the router
app.include_router(resume_routes.router)
