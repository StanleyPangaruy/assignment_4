# #Create a program that will ask for name, age and address. 
# #Display those details in the following format.
# #Hi, my name is _____. I am ____ years old and I live in _____ .

def getNameAgeAddress():
    _name = input("Name: ")
    _age = int(input("Age: "))
    _add = input("Address: ")
    return _name, _age, _add

def display(nameF, ageF, addF):
    print(f'Hi, my name is {nameF}. I am {ageF} years old and I live in {addF}.')

name, age, add = getNameAgeAddress()
display(name, age, add)