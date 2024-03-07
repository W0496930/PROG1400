#Author: William Taylor
#Student ID: W0496930
#Course: PROG1400
#Date: 2024-03-05
#Project: OOP_Concepts_Practice
#Repository: https://github.com/W0496930/PROG1400
#Programming language: Python 3

#Task 1: Abstraction
#Creating the class "shape" which will be the parent class of the circle and rectangle class
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    #Calculating the area of the circle
    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    #Calculating the area of the rectangle
    def area(self):
        return self.width * self.height

#Instantiating the objects
rectangle_obj = Rectangle(3, 4)
circle_obj = Circle(5)

#Printing the output of the shapes areas
print("The area of the rectangle is:", rectangle_obj.area())
print("The area of the circle is:", circle_obj.area())

#Task 2: Encapsulation
#Making a class called student
class Student:
    def __init__(self, name, age, grade):
        self.name = name 
        self.age = age 
        self.grade = grade 

    #Method to set student details
    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_grade(self, grade):
        self.grade = grade

    #Methods to get student details
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_grade(self):
        return self.grade

student1 = Student("Shelby", 18, "A")

print("\nStudent 1 Details:")
print("Name:", student1.get_name())
print("Age:", student1.get_age())
print("Grade:", student1.get_grade())

#Method to change the details of the student
student1.set_name("John")
student1.set_age(19)
student1.set_grade("B")

print("After Modification:")
print("Name:", student1.get_name())
print("Age:", student1.get_age())
print("Grade:", student1.get_grade())

#Task 3: Inheritance
#Creating a base class named animal, and then implementing the speak and move methods
class Animal:
    def speak(self):
        pass

    def move(self):
        pass
          
#Creating the dog, cat, and bird subclasses and then overriding their speak method to reflect their sound
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Bird(Animal):
    def speak(self):
        return "Chirp!"
    
#Printing the output
dog = Dog()
print("The dog says:", dog.speak())

cat = Cat()
print("The cat says:", cat.speak())

bird = Bird()
print("The bird says:", bird.speak())

#Task 4: Polymorphism
#Creating a class named vehicle and then implementing the travel method within it
class Vehicle:
    def travel(self):
        pass

#Creating the car, bike, and plane subclasses and then overriding the travel method to reflect how they travel
class Car(Vehicle):
    def travel(self):
        return "four wheels"
    
class Bike(Vehicle):
    def travel(self):
        return "two wheels"
    
class Plane(Vehicle):
    def travel(self):
        return "in the air"
    
#Printing the output
car = Car()
print("A car travels on", car.travel())

bike = Bike()
print("A bike travels on", bike.travel())

plane = Plane()
print("A plane travels", plane.travel())





