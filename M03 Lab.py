"""
Name: Ross Gandy
File Name: "M03 Lab.py
Desc: takes in user input and neatly presents the informationa about a car
"""
#handles the main vehicle type
class Vehicle():
    def __intit__(self, type):
        self.type = type

#subtype of vehicle, handles object creation
class Car(Vehicle):
    def __init__ (self, type, year, make, model, door, roof):
        self.type = type
        self.year = year
        self.make = make
        self.model = model
        self.door = door
        self.roof = roof

        Vehicle.__init__(type)
    #handles printing info about the car object
    def printInfo(self):
        print('Vehichle Type: ', self.type)
        print("Year: ", self.year)
        print('Make: ', self.make)
        print('Model: ', self.model)
        print('Number of doors: ', self.door)
        print('Type of roof: ', self.roof)
#user input and object creation
car_type = str(input("What type of vehicle?"))
car_year =str(input("What year is the car from?"))
car_make = str(input("What is the make?"))
car_model = str(input("What is the model?"))
car_door = str(input("How many doors?"))
car_roof = str(input("Solid or sun roof?"))
test = Car(car_type, car_year, car_make, car_model, car_door, car_roof)
test.printInfo()