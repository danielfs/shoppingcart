from inventory import Inventory
from fruit import Fruit
from constants import DISPLAY_LENGTH

class Cart:
    def __init__(self):
        self.items: dict[int, Fruit] = {}

    def add_item(self, product_id: int, quantity: int):
        if quantity <= 0:
            return

        try:
            item = Inventory.get_item(product_id, quantity)
            self.items[product_id] = item
            print("Item added to cart successfully.")
        except ValueError as e:
            print(e)
            return
        

    def remove_item(self, product_id: int):
        if product_id in self.items:
            item = self.items.pop(product_id)
            Inventory.update_quantity(product_id, item.quantity)
            print("Item removed from cart successfully.")
        else:
            print(f"Item with product ID {product_id} not found in cart.")

    def total_cost(self):
        total = sum(item.price_per_kg * item.quantity for item in self.items.values())
        return total

    def display_cart(self):
        if not self.items:
            print("Your cart is empty.")
            return

        print("+" * DISPLAY_LENGTH)
        print(f"{'Your Cart'.center(DISPLAY_LENGTH)}")
        print("+" * DISPLAY_LENGTH)
        print(f"{'Product ID':<15}{'Name':<20}{'Price Per KG':<10}{'Quantity':<10}")
        print("-" * DISPLAY_LENGTH)

        for item in self.items.values():
            print(f"{item.product_id:<15} {item.name:<20} ${item.price_per_kg:<10.2f} {item.quantity:<10}")
        print("-" * DISPLAY_LENGTH)
