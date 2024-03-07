# 1. **Encapsulation**: Data and methods are encapsulated within classes. Each class (`Person`, `Driver`, `Rider`, `Route`, `Trip`) encapsulates relevant attributes and methods.
# 2. **Inheritance**: `Driver` and `Rider` inherit from `Person`, inheriting its attributes and methods.
# 3. **Polymorphism**: The `details()` method is polymorphic - it behaves differently based on the object calling it. Each class implements its own version of the `details()` method, tailored to its specific attributes.
# 4. **Abstraction**: Users interact with the classes through their interfaces (`details()` method), hiding the complexities of their implementations.
 
from datetime import datetime
 
# Encapsulation: Attributes and methods are encapsulated within classes
class Person:
    def __init__(self,first_name,last_name,mobile,email):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile = mobile
        self.email = email
   
    def details(self):
        return f"Name: {self.first_name} {self.last_name}, Mobile: {self.mobile}, Email: {self.email}"
 
# Inheritance: Driver and Rider inherit from Person, inheriting its attributes and methods
   
class Driver(Person):
    def __init__(self, first_name, last_name, mobile, email,v_make,v_model,v_color,v_type):
        super().__init__(first_name, last_name, mobile, email)
        self.v_make = v_make
        self.v_model = v_model
        self.v_type = v_type
        self.v_color = v_color
   
    def details(self):
        return f"Driver {super().details()}, Vehicle: {self.v_color} {self.v_make} {self.v_model} {self.v_type}"
 
class Rider(Person):
    def __init__(self, first_name, last_name, mobile, email):
        super().__init__(first_name, last_name, mobile, email)
   
    def details(self):
        return f"Rider {super().details()}"
 
# Abstraction: Users interact with the classes through their interfaces (details() method),
# hiding the complexities of their implementations.
   
class Route:
    def __init__(self, origin, midway_stop,destination) -> None:
        self.origin = origin
        self.midway_stop = midway_stop
        self.destination = destination
   
    def details (self):
        return f"Origin: {self.origin}, Midway Stop: {self.midway_stop}, Destination: {self.destination}"
 
# Polymorphism: The details() method is polymorphic - it behaves differently based on the object calling it.
class Trip(Route):
    def __init__(self, origin, midway_stop, destination, leaving_time, stop_time, arrival_time) -> None:
        super().__init__(origin, midway_stop, destination)
        self.leaving_time = leaving_time
        self.stop_time = stop_time
        self.arrival_time = arrival_time
   
    def details(self):
        return f"Trip Details: {super().details()}, Leaving Time: {self.leaving_time}, Stop Time: {self.stop_time}, Arrival Time: {self.arrival_time}"
 
def run():
    # Create instances of the classes
    driver1 = Driver("Davis","Boudreau","902-555-1234","davis.boudreau@nscc.ca","Toyota","Camry","Silver","Car")
    rider1 = Rider("Joe","Smith","902-555-9999","joe.smith@nscc.ca")
    trip1 = Trip("Antigonish","Tim Hortons","Strait Area Campus", datetime(2024,2,15,7,0),datetime(2024,2,15,7,30),datetime(2024,2,15,8,0))
    # Store instances in a list for iteration
    journey1 = [driver1, rider1, trip1]
 
    # Iterate over entities and print their details
    for i in journey1:
        print("\n")
        print(i.details())
 
# The __name__ variable is a special variable that holds the name of the current
# module. When a Python script is executed, Python sets the __name__ variable
# for that script to "__main__", indicating that the script is being run directly,
# and not imported as a module.
# The line if __name__ == "__main__": is a common idiom used in Python scripts.
# It checks if the current script is being run directly by the Python interpreter.
# If so, it executes the block of code inside the if statement.
# This is useful when you have a Python file that can be both imported as a module
# in other scripts and run as a standalone script.
 
if __name__ == "__main__":
    run()
 
 