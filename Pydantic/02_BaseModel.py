from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int
    grade: str

student1 = Student(
    name='Vaibhav',
    age=20,
    grade='A'
)

print(student1)
print(student1.name)
print(student1.age)
print(student1.grade)