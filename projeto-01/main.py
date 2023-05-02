# Vídeo: How To Write Unit Tests For Existing Python Code // Part 1 of 2
# https://github.com/ArjanCodes/2022-test-existing-code

from pay.order import LineItem, Order
from pay.payment import pay_order

def main():
    # Test card number: 1249190007575059
    order = Order()
    order.line_items.append(LineItem(name="Shoes", price=100_00, quantity=2))
    order.line_items.append(LineItem(name="Hat", price=50_00))
    pay_order(order)

if __name__ == "__main__":
    main()
