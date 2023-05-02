# Vídeo: How To Write Unit Tests For Existing Python Code // Part 1 of 2
# https://github.com/ArjanCodes/2022-test-existing-code

from pay.order import Order
from pay.processor import PaymentProcessor

def pay_order(order: Order):
    if order.total == 0:
        raise ValueError("Can't pay an order with total 0.")
    card = input("Coloca o nuymero do cartao: ")
    month = int(input("Coloque o mes do vencimento do cartao: "))
    year = int(input("Coloque o ano que vence o cartao: "))
    payment_processor = PaymentProcessor("6cfb67f3-6281-4031-b893-ea85db0dce20")
    payment_processor.charge(card, month, year, amount=order.total)
    order.pay()