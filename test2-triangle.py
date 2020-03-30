import math

class Triangle:
    base = 0
    height = 0
    
    def __init__(self):
        self.base = 0
        self.height = 0
    
    def set_length(self, a, b):
        self.base = a
        self.height = b
    
    def print_area(self):
        return self.base * self.height / 2
        
    
class RATriangle(Triangle):
    def print_hypotenuse(self):
        return math.sqrt(self.base * self.base + self.height * self.height)

Tri = Triangle()
Tri.set_length(10, 20) # base(밑변):10 height(높이):20
print(Tri.print_area())

RAT = RATriangle()
RAT.set_length(3, 4) # base(밑변):3 height(높이):4
print(RAT.print_hypotenuse())
