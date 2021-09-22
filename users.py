from bankaccount import BankAccount

class User:
    
    def __init__(self,name):
        self.name = name
        self.account = BankAccount(0.0,0.15)
    
    def deposit(self, amount):
        self.account.balance += amount
    
    def withdraw (self,amount):
        if amount < self.account.balance:
            self.account.balance -= amount
        else:
            print(f"Balance is not sufficient to withdraw {amount}")
    
    def transfer(self, destination, amount):
        if amount < self.account.balance:
            self.account.balance -= amount
            destination.account.balance += amount
        else:
            print(f"Balance is not sufficient to transfer {amount}")

    def display_user_balance(self):
        print(f'User: {self.name}, Balance:{self.account.balance}')

