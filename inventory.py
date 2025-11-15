from fruit import Fruit
from constants import DISPLAY_LENGTH

class Inventory:
    items: dict[int, Fruit] = {
        1: Fruit(1, "Apples", 250, 100),
        2: Fruit(2, "Cherry", 650, 100),
        3: Fruit(3, "Chickoo", 50, 100),
        4: Fruit(4, "Grapes", 90, 100),
        5: Fruit(5, "Mangoes", 150, 100),
    }

    @classmethod
    def get_item(cls, product_id: int, quantity: int) -> Fruit:
        item = cls.items.get(product_id)
        if item and item.quantity >= quantity:
            item.quantity -= quantity
            return Fruit(item.product_id, item.name, item.price_per_kg, quantity)
        
        raise ValueError(f"Insufficient quantity for product ID {product_id}")
    
    @classmethod
    def update_quantity(cls, product_id: int, quantity: int):
        item = cls.items.get(product_id)
        if item:
            item.quantity += quantity
            cls.items[product_id] = item
        else:
            raise ValueError(f"Product ID {product_id} not found in inventory")
    
    @classmethod
    def add_item(cls, product_id: int, name: str, price_per_kg: float, quantity: int):
        if product_id in cls.items:
            new_item = cls.items[product_id]
            new_item.quantity += quantity
            cls.items[product_id] = new_item
        else:
            cls.items[product_id] = Fruit(product_id, name, price_per_kg, quantity)

    @classmethod
    def display_inventory(cls):
        print("+" * DISPLAY_LENGTH)
        print(f"{'Fruit Sellers Inventory'.center(DISPLAY_LENGTH)}")
        print("+" * DISPLAY_LENGTH)
        print(f"{'Product ID':<15}{'Name':<20}{'Price Per KG':<10}{'Quantity Available':<15}")
        print("-" * DISPLAY_LENGTH)

        for item in cls.items.values():
            print(f"{item.product_id:<15} {item.name:<20} ${item.price_per_kg:<10.2f} {item.quantity:<15}")
        print("-" * DISPLAY_LENGTH)
