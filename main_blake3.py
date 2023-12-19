import os
BUF_SIZE = 65536 
from blake3 import blake3



dict = {}
hashes = []
duplicates = 0

def hash_func(directory):
    global duplicates
    for filename in os.listdir(directory):
        ans = blake3()
        f = os.path.join(directory, filename)
        with open(f, "rb") as f:
            data = f.read()
            if not data:
                break
            ans.update(data)
        try:
            hashes.index(ans.hexdigest())
            print("File already exists:", filename)
            duplicates+=1
        except:
            hashes.append(ans.hexdigest())
            dict[filename] = ans.hexdigest()


directory1 = 'folder-1'  
directory2 = 'folder-2'

hash_func(directory1)
hash_func(directory2)
print("No. of Duplicate Files found: ", duplicates)