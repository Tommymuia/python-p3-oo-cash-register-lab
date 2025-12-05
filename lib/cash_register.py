#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0.0
        self.discount = discount
        self.items = []
        self._last_transaction_amount = 0.0
        self._last_transaction_items = []

    def add_item(self, title, price, quantity=1):
        """Add item(s) to the register and update total."""
        transaction_amount = price * quantity
        self.total += transaction_amount
        self._last_transaction_amount = transaction_amount
        self._last_transaction_items = [title] * quantity
        self.items.extend(self._last_transaction_items)

    def apply_discount(self):
        """Apply discount if available and print message."""
        if self.discount > 0:
            self.total = self.total * (1 - self.discount / 100)
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        """Remove the last transaction from total and items."""
        self.total -= self._last_transaction_amount
        for item in self._last_transaction_items:
            if item in self.items:
                self.items.remove(item)
        # Reset last transaction info
        self._last_transaction_amount = 0.0
        self._last_transaction_items = []
