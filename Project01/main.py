from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return{'message':'Hello India'}

@app.get("/about")
def about():
    return{'message':'India is the best country'}