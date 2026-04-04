from fastapi import FastAPI
from routers.calculator_router import router as calculator_router

app = FastAPI(
    title="Calculator API",
    description="API que realiza operações matemáticas básicas",
    version="1.0.0"
)

app.include_router(calculator_router)