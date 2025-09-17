from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to SaaSly Demo 🚀"}

@app.get("/users")
def get_users():
    return [
        {"id": 2, "name": "Krishna", "role": "Scrum Master"},
        {"id": 3, "name": "Harini", "role": "Developer"},
    ]
