#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        transaction_amount = price * quantity
        self.total += transaction_amount
        self.last_transaction = transaction_amount
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount * self.total) // 100
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total}.")  # Print instead of return
        else:
            print("There is no discount to apply.")  # Print for no discount case

    def get_items(self):
        return self.items

    def void_last_transaction(self):
        if self.last_transaction > 0:
            self.total -= self.last_transaction
            self.last_transaction = 0
            self.items = self.items[:-1] if self.items else []