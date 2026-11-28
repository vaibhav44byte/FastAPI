## Problem in Python

"""def insert_patient_data(name: str,age:int):
    print(name)
    print(age)
    print("Inserted into database")

insert_patient_data('Kelly',"33")"""


## This method is good but not Scalable
def insert_patient_data(name: str,age:int):
    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print("Inserted into database")
    else:
        raise TypeError('Invalid data format')

insert_patient_data('Kelly',"33")