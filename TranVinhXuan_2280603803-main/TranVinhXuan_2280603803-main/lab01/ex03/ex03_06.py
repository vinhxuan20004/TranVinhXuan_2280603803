def xoa_phan_tu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False
# Su dung ham va in ket qua
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
key_to_delete = 'b'
if result:
    print("Phan tu da duoc xoa tu Dirictionary:", my_dict)
else:
    print("Khong tim thay phan tu can xoa trong Dirictionary.")