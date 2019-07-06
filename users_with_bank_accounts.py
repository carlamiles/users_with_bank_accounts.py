class BankAccount:
    def __init__(self, int_rate=0.01, checking_balance=0, savings_balance=0):
        self.interest_rate = int_rate
        self.account_balance_checking = checking_balance
        self.account_balance_savings = savings_balance
        
    def deposit(self, acct_type, amount):
        if acct_type == "checking":
            self.account_balance_checking += amount
        elif acct_type == "savings":
            self.account_balance_savings += amount
        return self

    def withdraw(self, acct_type, amount):
        if acct_type == "checking":
            self.account_balance_checking -= amount
            if self.account_balance_checking < 0:
                print("Insufficient funds: Charging a $5 fee")
                self.account_balance_checking -= 5
        elif acct_type == "savings":
                self.account_balance_savings -= amount
                if self.account_balance_savings < 0:
                    print("Insufficient funds: Charging a $5 fee")
                    self.account_balance_savings -= 5
        return self

    def display_account_info(self, acct_type):
        if acct_type == "checking":
            print("Checking Balance: $", self.account_balance_checking)
        if acct_type == "savings":
            print("Savings Balance: $", self.account_balance_savings)
        return self

    def yield_interest(self, acct_type):
        if acct_type == "checking" and self.account_balance_checking > 0:
            self.account_balance_checking = self.account_balance_checking + (self.account_balance_checking * self.interest_rate) 
        elif acct_type == "savings" and self.account_balance_savings > 0:
            self.account_balance_savings = self.account_balance_savings + (self.account_balance_savings * self.interest_rate) 
        return self


class User:
    def __init__(self,username,email_address,other_user):
        self.name = username
        self.email = email_address
        self.account = BankAccount(int_rate=0.02, checking_balance=0, savings_balance=0)
        self.other_user = other_user
        
    def make_deposit(self, acct_type, amount):
        if acct_type == "checking":
            self.account.deposit("checking", amount)
        elif acct_type == "savings":
            self.account.deposit("savings", amount)
        return self
    def make_withdrawal(self, acct_type, amount):
        if acct_type == "checking":
            self.account.withdraw("checking", amount)
        elif acct_type == "savings":
            self.account.withdraw("savings", amount)
        return self
    def display_user_balance(self, acct_type):
        if acct_type == "checking":
            print("user: ", self.name, self.account.display_account_info("checking"))
        elif acct_type == "savings":
            print("user: ", self.name, self.account.display_account_info("savings"))
        return self
    def transfer_money(self, acct_type, other_user_account, amount):
        if acct_type == "checking":
            self.account.withdraw("checking", amount)
            other_user_account.deposit("checking", amount)
        elif acct_type == "savings":
            self.account.withdraw("savings", amount)
            other_user_account.deposit("checking", amount)
        return self


king = User("king jaffe joffer", "rullerofzamunda@comcast.net", "hakeem")
king_account = BankAccount(0.05, 25000, 100000)

print(king.name)
king_account.deposit("savings", 25000).withdraw("checking", 500).withdraw("checking", 1500).withdraw("checking", 3500).display_account_info("savings").display_account_info("checking")

hakeem = User("prince hakeem", "onlyjuicesandberries@yahoo.com", "king")

print(hakeem.name)
hakeem.make_deposit("checking", 250).make_withdrawal("checking", 50).transfer_money("savings", king_account, 100).display_user_balance("checking").display_user_balance("savings")

print(king.name)
king_account.display_account_info("checking")
