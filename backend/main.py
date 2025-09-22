from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to SaaSly Demo 🚀"}

@app.get("/users")
def get_users():
    return [
        {"id": 1, "name": "Krishna", "role": "Scrum Master"},
        {"id": 2, "name": "Harini", "role": "Developer"},
    ]
