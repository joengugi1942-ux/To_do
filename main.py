from fastapi import FastAPI

app = FastAPI()

@app.get("/user")
def get_user():
    return {
        "name": "joe",
        "description": "Today I am learning how to make files and arrangement"
    }
