def display_menu(menu):
    print("\n- Clark's Food Menu -")
    i = 1
    for item in menu:
        print(f"{i}. {item} - ₱{menu[item]:.2f}")
        i += 1

def user_choice(menu):
    selected_items = []
    while True:
        choice = input("\nEnter the number of the item you want to order (or type 'done' to finish): ")
        if choice.lower() == 'done':
            if selected_items:
                return selected_items
            else:
                print("You must select at least one item.")
                continue
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(menu):
                item = list(menu)[choice - 1]
                selected_items.append((item, menu[item]))
                print(f"Added {item} - ₱{menu[item]:.2f} to your order.")
            else:
                print("Invalid choice. Please select an item number from the menu.")
        else:
            print("Invalid input. Please enter a valid item number or 'done'.")

def is_valid_number(value):
    for char in value:
        if not (char.isdigit() or char == '.'):
            return False
    return value.count('.') <= 1 and len(value) > 0

def payment(total):
    total_paid = 0.0
    while total_paid < total:
        remaining = total - total_paid
        cash = input(f"\nYour total is ₱{total:.2f}. You still need to pay ₱{remaining:.2f}. Enter payment amount: ₱")
        if is_valid_number(cash):
            cash = float(cash)
            total_paid += cash
            if total_paid >= total:
                change = total_paid - total
                print(f"Payment received! Your change is ₱{change:.2f}. Thank you!")
                return
            else:
                print(f"Insufficient payment. You still need to pay ₱{total - total_paid:.2f}.")
        else:
            print("Invalid input. Please enter a valid amount.")

def main():
    menu = {
        "Burger": 174.99,
        "Hotdog": 67.99,
        "Pizza": 385.99,
        "Chicken Wings (12 pcs)": 559.99,
        "Coke (1.5L)": 80.00,
        "Iced Tea (1L)": 45.00,
    }

    display_menu(menu)

    selected_items = user_choice(menu)
    total_price = sum(price for _, price in selected_items)

    print("\nYou selected the following items:")
    for item, price in selected_items:
        print(f"- {item} - ₱{price:.2f}")
    print(f"Total: ₱{total_price:.2f}")

    payment(total_price)

if __name__ == "__main__":
    main()
