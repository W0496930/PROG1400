class Shape:
    def calculate_area(self):
        pass
    def calculate_perimeter(self):
        pass
    def calculate_volume(self):
        pass
    def __str__(self):
        return self.__class__.__name__

class Rectangle(Shape):
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    def calculate_volume(self):
        return self.length * self.width * self.height

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(length=side_length, width=side_length, height=side_length)

class Circle(Shape):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    
    def calculate_area(self):
        return (3.14 * self.radius ** 2)
    
    def calculate_perimeter(self):
        return (2 * 3.14 * self.radius)
    
    def calculate_volume(self):
        return (3.14 * self.radius ** 2) * self.height

def print_area(shape):
    print(f"Area of the {shape} is {shape.calculate_area()}")

def print_circumference(shape):
    print(f"Circumference of the {shape} is {shape.calculate_perimeter()}")

def print_volume(shape):
    print(f"Volume of the {shape} is {shape.calculate_volume()}")

rect1 = Rectangle(length=5, width=3, height=5)
rect2 = Rectangle(length=8, width=3, height=4)
square1 = Square(side_length=5)
circle1 = Circle(radius=5, height=5)

print_area(rect1)
print_circumference(rect2)
print_volume(circle1)

