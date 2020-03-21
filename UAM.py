from UsersRepository import UsersRepository
from password_validation import validate_password
from password_encoder import encode_password
from mail_sender import send_mail

def main():
    repository=UsersRepository()
    while True:
        action=input("Select action: \n 1-register 2-log in 3- quit ")
        if action=="1":
            name=input("Please enter your username ")
            if repository.contains(name):
                print("Username is already taken. Please try again")
                continue
            mail=input("Please enter your e-mail address ")
            password=input("Please select your password. Password must contains at least 8 character and one number. ")
            if not validate_password(password):
                print("Password does not meet specified requirements")
                continue
            confirmation=input("Confirm your password ")
            if password!=confirmation:
                print("Wrong password. Try again")
                continue  
            if repository.add(name, encode_password(password), mail):
                print("User created successfully")
                send_mail(mail, name)
        elif action=="2":
            name=input("Please enter your username ")
            password=input("Please select your password ")
            if repository.validate(name, encode_password(password)):
                print("You have been logged in successfully")
            else:
                print("Invalid username or password")
        elif action=="3":
            print("See you soon")
            return 
        else:
            print("Invalid action. Try again")

if __name__ == "__main__":
    main()