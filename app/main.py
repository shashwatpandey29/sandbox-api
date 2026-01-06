from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="HTTP Sandbox API")

app.include_router(router, prefix="/api")

@app.get("/")
def root():
    return {"status": "sandbox running"}

