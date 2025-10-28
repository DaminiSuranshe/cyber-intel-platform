from fastapi import FastAPI
from app.api import auth

app = FastAPI(title="Cyber Intelligence Platform API")

# Include auth router
app.include_router(auth.router, prefix="/auth", tags=["auth"])

@app.get("/health")
async def health_check():
    return {"status": "ok", "message": "Backend is running!"}
