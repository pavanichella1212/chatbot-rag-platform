import os

from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

app = FastAPI(title="Chatbot RAG Platform")


@app.get("/")
def read_root() -> dict:
    return {"message": "Chatbot RAG Platform is running"}


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "src.main:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8000)),
        reload=True,
    )
