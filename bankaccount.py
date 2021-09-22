class BankAccount:

    Allinstances = []

    def __init__ (self, balance = 0.0, int_rate = 0.01): 
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.Allinstances.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print(f"Your balance is not sufficient to withdraw ${amount}.")
        return self
        
    def display_account_info(self):
        print(f"Balace: ${self.balance}.")
        return self

    def yield_interest(self):
        interest = self.balance * self.int_rate
        self.balance = self.balance + interest
        print(f"Interest: ${interest}.")
        return self

    @classmethod
    def instances(cls):
        for instance in cls.Allinstances:
            instance.display_account_info()

