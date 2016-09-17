import hashlib

def md5(pwd):
    m = hashlib.md5()
    m.update(pwd.encode("utf-8"))
    password = (m.hexdigest())
    return password
    #print(password)

if __name__ == "__main__":
    md5(input())
