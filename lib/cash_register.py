#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction_amount = 0

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.last_transaction_amount = price * quantity
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction_amount
        self.last_transaction_amount = 0

# Example usage
if __name__ == "__main__":
    cash_register = CashRegister()
    cash_register_with_discount = CashRegister(20)
    
    # Test discount attribute
    assert(cash_register.discount == 0)
    assert(cash_register_with_discount.discount == 20)
    
    # Test total attribute
    assert(cash_register.total == 0)
    assert(cash_register_with_discount.total == 0)
    
    # Test items attribute
    assert(cash_register.items == [])
    assert(cash_register_with_discount.items == [])
    
    # Test add_item method
    cash_register.add_item("eggs", 0.98)
    assert(cash_register.total == 0.98)
    
    # Test add_item with optional quantity
    cash_register.add_item("book", 5.00, 3)
    assert(cash_register.total == 15.98)
    
    # Test add_item with multiple items
    cash_register.add_item("Lucky Charms", 4.5)
    assert(cash_register.total == 20.48)
    cash_register.add_item("Ritz Crackers", 5.0)
    assert(cash_register.total == 25.48)
    cash_register.add_item("Justin's Peanut Butter Cups", 2.50, 2)
    assert(cash_register.total == 30.48)
    
    # Test apply_discount method
    cash_register_with_discount.add_item("macbook air", 1000)
    cash_register_with_discount.apply_discount()   
    assert(cash_register_with_discount.total == 800)
    
    # Test apply_discount success message
    import io
    import sys
    captured_out = io.StringIO()
    sys.stdout = captured_out
    cash_register_with_discount.apply_discount()
    sys.stdout = sys.__stdout__
    assert(captured_out.getvalue() == "After the discount, the total comes to $800.\n")
    
    # Test apply_discount when no discount
    captured_out = io.StringIO()
    sys.stdout = captured_out
    cash_register.apply_discount()
    sys.stdout = sys.__stdout__
    assert(captured_out.getvalue() == "There is no discount to apply.\n")
    
    # Test items list without multiples
    new_register = CashRegister()
    new_register.add_item("eggs", 1.99)
    new_register.add_item("tomato", 1.76)
    assert(new_register.items == ["eggs", "tomato"])
    
    # Test items list with multiples
    new_register.add_item("eggs", 1.99, 2)
    new_register.add_item("tomato", 1.76, 3)
    assert(new_register.items == ["eggs", "eggs", "tomato", "tomato", "tomato"])
    
    # Test void_last_transaction
    cash_register.add_item("apple", 0.99)
    cash_register.add_item("tomato", 1.76)
    cash_register.void_last_transaction()
    assert(cash_register.total == 0.99)
    
    # Test void_last_transaction with multiples
    cash_register.add_item("tomato", 1.76, 2)
    cash_register.void_last_transaction() 
    assert(cash_register.total == 0.0)
