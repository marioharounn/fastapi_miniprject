from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return{"message:": "Welcome to FastAPI"}

@app.get("/random-endpoint")
def read_dummy():
    return {"message": "Hello from Append Consulting!"}
