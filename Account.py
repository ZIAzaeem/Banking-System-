class Account:
    def __init__(self, account_number, customer, balance):
        self.account_number = account_number
        self.customer = customer
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'Deposited ${amount}. New balance: ${self.balance}')
        else:
            print('Invalid deposit amount')

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f'Withdrew ${amount}. New balance: ${self.balance}')
        else:
            print('Invalid withdrawal amount or insufficient funds')

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f'Account [Number: {self.account_number}, Balance: ${self.balance}]'
