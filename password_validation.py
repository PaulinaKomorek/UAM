def validate_password(password: str):
    if len(password)<8:
        return False
    for i in password:
        if i.isdigit():
            return True
    return False