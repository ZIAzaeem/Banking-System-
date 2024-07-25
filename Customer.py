class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id

    def __str__(self):
        return f'Customer [ID: {self.customer_id}, Name: {self.name}]'
