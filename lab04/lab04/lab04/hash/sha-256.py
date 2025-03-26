import hashlib

def caculate_sha256_hash(data):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(data.encode('utf-8'))
    return sha256_hash.hexdigest()

data_to_hash = input("nhap chuoi du lieu de hash: ")
hash_value = caculate_sha256_hash(data_to_hash)
print("gia tri cua hash la: ",hash_value)