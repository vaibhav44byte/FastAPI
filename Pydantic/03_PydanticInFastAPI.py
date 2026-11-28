from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name:str
    age:int
    grade:str


@app.get('/students')
def create_student(student:Student):
    return student