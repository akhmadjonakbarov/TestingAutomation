import uvicorn
from fastapi import FastAPI

app = FastAPI(
    title="Web Testing",
    description="Web Testing",
    version="1.0",
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8080)
