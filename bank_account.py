
class bankAccount:
    def __init__(self):
        self.balance = 0
        self.id = ""

    def create(self, id, amount):

        if not isinstance(id, str):
            raise TypeError("id must be of type string")

        if not isinstance(amount, float):
            raise TypeError("amount must be of type float")

        if id !="":
            self.id = id
        else:
            raise ValueError("id cannot be empty")

        if amount > 0:
            self.balance = amount
        else:
            raise ValueError("Amount must be greater than zero")

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient funds")

    def showBalance(self):
        return self.balance


