from envs.langchain.Lib import json
from fastapi import FastAPI

app = FastAPI()

def load_data():
    with open('patients.json', 'r') as file:
        data = json.load(file)
    return data

@app.get("/")
def hello():
    return{'message':'Patient management System API'}

@app.get("/about")
def about():
    return{'message':'Fully functional API to manage your patient records'}

@app.get('/view')
def view():
    data = load_data()
    return data