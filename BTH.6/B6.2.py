print("Nguyen Van An")
print("Msv:235752021610082")
class Hinhchunhat:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Ví dụ sử dụng
rectangle = Hinhchunhat(4, 5)
print("Diện tích hình chữ nhật:", rectangle.area())