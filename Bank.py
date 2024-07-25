class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = {}
        self.accounts = {}

    def add_customer(self, customer):
        if customer.customer_id not in self.customers:
            self.customers[customer.customer_id] = customer
            print(f'Customer {customer.name} added.')
        else:
            print('Customer already exists.')

    def create_account(self, account_number, customer_id, initial_deposit=0.0):
        if customer_id in self.customers:
            customer = self.customers[customer_id]
            if account_number not in self.accounts:
                new_account = Account(account_number, customer, initial_deposit)
                self.accounts[account_number] = new_account
                print(f'Account {account_number} created for {customer.name}.')
            else:
                print('Account number already exists.')
        else:
            print('Customer not found.')

    def get_account(self, account_number):
        return self.accounts.get(account_number, 'Account not found')

    def __str__(self):
        return f'Bank [Name: {self.name}, Customers: {len(self.customers)}, Accounts: {len(self.accounts)}]'



