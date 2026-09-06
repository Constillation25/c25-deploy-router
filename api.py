import os
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="c25-deploy-router API", version="1.0.0")

class HealthResponse(BaseModel):
    status: str
    service: str

@app.get("/health", response_model=HealthResponse)
def health():
    return {"status": "operational", "service": "c25-deploy-router"}

@app.get("/")
def root():
    return {"message": "c25-deploy-router API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", "8000")))
