from datetime import datetime

class Location:
    def __init__(self, city, country):
        self.city = city
        self.country = country

class Job:
    def __init__(self, title, salary):
        self.title = title  
        self.salary = salary

class Person:
    def __init__(self, name, age, job=None, location=None, email=None, phone=None, birthdate=None):
        self.name = name
        self.age = age
        self.job = job
        self.location = location
        self.email = email
        self.phone = phone
        self.birthdate = birthdate

    def myfunc(self):
        print("Hello, my name is " + self.name + " and I am " + str(self.age) + " years old.")
        if self.job:
            print("I work as a " + self.job.title + " earning $" + str(self.job.salary) + " a year.")
        if self.location:
            print("I currently live in " + self.location.city + ", " + self.location.country + ".")
        else:
            print("I don't have a specified location.")
        if self.email:
            print("Contact me via email: " + self.email)
        if self.phone:
            print("Contact me via phone: " + self.phone)
        if self.birthdate:
            print("My birthdate is: " + str(self.birthdate))

    def update_info(self, job=None, location=None, email=None, phone=None, birthdate=None):
        if job:
            self.job = job
        if location:
            self.location = location
        if email:
            self.email = email
        if phone:
            self.phone = phone
        if birthdate:
            self.birthdate = birthdate

    def summary(self):
        summary = f"{self.name}, {self.age} years old"
        if self.job:
            summary += f", {self.job.title} earning ${self.job.salary} a year"
        if self.location:
            summary += f", living in {self.location.city}, {self.location.country}"
        if self.email:
            summary += f", contact me via email: {self.email}"
        if self.phone:
            summary += f", contact me via phone: {self.phone}"
        if self.birthdate:
            summary += f", born on {self.birthdate}"
        return summary

class Student(Person):
    def __init__(self, name, age, major, location=None, email=None, phone=None, birthdate=None):
        super().__init__(name, age, location=location, email=email, phone=phone, birthdate=birthdate)
        self.major = major

    def myfunc(self):
        super().myfunc()
        print("I am a student majoring in " + self.major + ".")

class Manager(Person):
    def __init__(self, name, age, department, location=None, email=None, phone=None, birthdate=None):
        super().__init__(name, age, location=location, email=email, phone=phone, birthdate=birthdate)
        self.department = department

    def myfunc(self):
        super().myfunc()
        print("I am a manager in the " + self.department + " department.")

# Creating instances of the classes
job1 = Job("Software Engineer", 80000)
location1 = Location("Halifax", "Canada")
p1 = Person("John", 36, job1, location1, email="john@example.com", phone="123-456-7890", birthdate="1990-01-15")

student1 = Student("Alice", 21, "Computer Science", location=Location("Boston", "USA"), email="alice@example.com", birthdate="2000-05-20")
manager1 = Manager("Bob", 45, "IT Management", location=Location("New York", "USA"), phone="987-654-3210", birthdate="1976-09-08")

# Add three more people with different roles
student2 = Student("Eva", 22, "Mathematics", location=Location("London", "UK"))
manager2 = Manager("Charlie", 40, "Finance", location=Location("Paris", "France"), email="charlie@example.com")
p3 = Person("Diana", 30, birthdate="1992-11-25")

# Print information for each person
p1.myfunc()
print("\n")
student1.myfunc()
print("\n")
manager1.myfunc()
print("\n")
student2.myfunc()
print("\n")
manager2.myfunc()
print("\n")
p3.myfunc()

# Updating information for a person
p3.update_info(location=Location("Berlin", "Germany"), email="diana@example.com", phone="555-1234")

# Displaying a summary for a person
print("\nSummary for Diana:")
print(p3.summary())
