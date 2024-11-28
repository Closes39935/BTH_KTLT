import math
print("Nguyen Van An")
print("Msv:235752021610082")
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

# Ví dụ sử dụng
circle = Circle(5)
print("Diện tích hình tròn:", circle.area())
