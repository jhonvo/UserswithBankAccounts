from bankaccount import BankAccount
from users import User



# Account1 = BankAccount(10.0,0.15)
# Account2 = BankAccount(100.0,0.15)

# Account1.deposit(100.0).deposit(50.0).withdraw(30).yield_interest().display_account_info()
# Account2.deposit(50.5).deposit(50.0).withdraw(20.0).withdraw(20.0).yield_interest().display_account_info()
# print(".....")
# BankAccount.instances()

Michael = User("Michael Jordan")
Benny = User("Benny Bob")
Chris = User("Chris Patt")

Michael.deposit(1000.00)
Michael.deposit(500.00)
Michael.withdraw(300.00)
Michael.display_user_balance()

Benny.deposit(1000.00)
Benny.deposit(500.00)
Benny.withdraw(200.00)
Benny.withdraw(200.00)
Benny.display_user_balance()

Chris.deposit(1000.00)
Chris.withdraw(500.00)
Chris.withdraw(300.00)
Chris.display_user_balance()

Michael.transfer(Chris,100.00)
Michael.display_user_balance()
Chris.display_user_balance()

