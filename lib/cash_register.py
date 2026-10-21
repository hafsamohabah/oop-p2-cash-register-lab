
#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        # Initialize the discount and the register's records.
        self._discount = 0
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        # Return the current discount percentage.
        return self._discount

    @discount.setter
    def discount(self, value):
        # Accept only integer discounts between 0 and 100.
        if type(value) is int and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity=1):
        # Update the total and record each item purchased.
        self.total += price * quantity

        for _ in range(quantity):
            self.items.append(item)

        # Keep the transaction details so the purchase can be voided.
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        # Apply the discount to the current total.
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        self.total = self.total * (1 - self.discount / 100)
        print(f"After the discount, the total comes to ${self.total:g}.")

    def void_last_transaction(self):
        # Do nothing if there are no transactions to reverse.
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        # Remove the last transaction and reverse its item and price changes.
        transaction = self.previous_transactions.pop()
        self.total -= transaction["price"] * transaction["quantity"]

        for _ in range(transaction["quantity"]):
            self.items.remove(transaction["item"])
