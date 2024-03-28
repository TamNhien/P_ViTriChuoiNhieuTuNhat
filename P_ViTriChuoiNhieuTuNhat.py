L = input("Nhập vào danh sách các chuỗi, cách nhau bởi dấu phẩy: ").split(',')
max_word_count, max_word_index = max(((len(string.split()), i) for i, string in enumerate(L)), default=(0, -1))

if max_word_index != -1:
    print(f"Chuỗi có nhiều từ nhất ở vị trí {max_word_index}: {L[max_word_index]}")
else:
    print("Danh sách không có chuỗi nào.")
