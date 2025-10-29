from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.db.database import get_db

router = APIRouter()

@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # temporary response until DB auth is implemented
    return {"access_token": "fake-token", "token_type": "bearer"}

@router.get("/me")
def read_users_me():
    return {"username": "test_user"}
