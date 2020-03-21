from hashlib import md5

def encode_password(password: str):
    m=md5(bytes(password,"ascii"))
    return m.hexdigest()