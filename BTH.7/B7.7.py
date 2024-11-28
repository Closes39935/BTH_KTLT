print("Nguyen Van An")
print("Msv:235752021610082")
def count_lines_in_file(file_path):
    with open(file_path, 'r') as file:
        num_lines = sum(1 for line in file)
    print(f"Số dòng trong tệp: {num_lines}")

# Ví dụ sử dụng
count_lines_in_file('file.txt')  # Thay 'file.txt' bằng tên file của bạn
