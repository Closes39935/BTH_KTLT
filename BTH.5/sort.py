# sort.py

def bubbleSort(nlist):
    """Hàm sắp xếp nổi bọt cho danh sách nlist."""
    n = len(nlist)
    for i in range(n):
        # Duyệt qua các phần tử còn lại chưa được sắp xếp
        for j in range(0, n - i - 1):
            # Đổi chỗ nếu phần tử hiện tại lớn hơn phần tử kế tiếp
            if nlist[j] > nlist[j + 1]:
                nlist[j], nlist[j + 1] = nlist[j + 1], nlist[j]
    return nlist
