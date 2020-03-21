import json

class UsersRepository:
    def contains(self, name: str) -> bool:
        accounts = json.load(open("DataBase/accounts.json", "r"))
        for account in accounts:
            if account["name"] == name:
                return True
        return False

    def add(self, name: str, password: str, email: str)-> bool:
        if self.contains(name):
            return False
        accounts_file = open("DataBase/accounts.json", "r")
        accounts = json.load(accounts_file)
        accounts_file.close()
        accounts.append({"name":name, "password": password, "email": email})
        accounts_file = open("DataBase/accounts.json", "w")
        json.dump(accounts, accounts_file)
        accounts_file.close()
        return True

    def validate(self, name:str, password: str):
        accounts = json.load(open("DataBase/accounts.json", "r"))
        for account in accounts:
            if account["name"] == name and account["password"] == password:
                return True
        return False
