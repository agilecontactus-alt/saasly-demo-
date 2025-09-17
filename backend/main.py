from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to SaaSly Demo 🚀"}

@app.get("/users")
def get_users():
    return [
        {"id": 1, "name": "Bob", "role": "Scrum Master"},
        {"id": 2, "name": "Harini", "role": "Developer"},
    ]
