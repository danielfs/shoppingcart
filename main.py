from fruit import Fruit
from inventory import Inventory
from cart import Cart
from menu import display_menu, clear_terminal, wait_enter
from constants import ADD_ITEMS, CALCULATE_TOTAL, REMOVE_ITEM, EXIT

my_cart = Cart()

def main():
    while True:
        clear_terminal()
        Inventory.display_inventory()
        my_cart.display_cart()

        try:
            display_menu()
            user_choice = int(input())
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if(user_choice == ADD_ITEMS[0]):
            item_id = int(input("Enter the Product ID of the item you wish to add to the cart : "))
            quantity = int(input("Enter the quantity (in kgs) you wish to add to the cart : "))
            my_cart.add_item(item_id, quantity)
            wait_enter()

        elif(user_choice == CALCULATE_TOTAL[0]):
            total = my_cart.total_cost()
            print(f"The total cost of items in your cart is: ${total:.2f}")
            wait_enter()

        elif(user_choice == REMOVE_ITEM[0]):
            product_id = int(input("Please enter the Product ID of the item you want to remove from the cart : "))
            my_cart.remove_item(product_id)
            wait_enter()

        elif(user_choice == EXIT[0]):
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
