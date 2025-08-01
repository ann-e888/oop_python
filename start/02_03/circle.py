"""
A class for representing a circle
"""

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def display_circumference(self):
        print(f'Circumeference of the circle is: {2*3.14*self.radius} units.')

    def display_area(self):
        print(f'The area of the circle is: {3.14*(self.radius**2)} square units.')

circle = Circle(4)
circle.display_circumference()
circle.display_area()