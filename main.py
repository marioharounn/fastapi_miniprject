from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CalculationRequest(BaseModel):
    number1: float
    number2: float

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI"}

@app.get("/random-endpoint")
def read_dummy():
    return {"message": "Hello from Append Consulting!"}

@app.post("/calculate-sum")
def calculate_sum(request: CalculationRequest):
    result = request.number1 + request.number2
    return {
        "Number 1 was": request.number1,
        "Number 2 was": request.number2,
        "And the sum becomes": result
    }