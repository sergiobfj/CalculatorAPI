from fastapi import FastAPI

app = FastAPI(title="Calculator API")

API_PREFIX =  "/api"

@app.get("/")
def healt_check():
    return {
        "stauts": "ok",
        "message": "Calculator API running..."
    }