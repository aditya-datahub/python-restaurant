menu = {
    'Pizza': 40,
    'Pasta': 50,
    'Burger': 60,
    'Salad': 70,
    'Coffee': 80,
}

proceed = input("Do you want to place an order? (yes/no): ").strip().lower()

if proceed == 'yes':
    pass  # continue with the program
elif proceed == 'no':
    print("Thank you for visiting! Have a great day!")
    exit()
else:
    print("Please type only 'yes' or 'no'.")
    exit()

print("\nWelcome to the PYTHON Restaurant!")
print("Menu:")
for item, price in menu.items():
    print(f"{item}: Rs{price}")

order_total = 0

while True:
    item = input("\nEnter the name of the item you want to order: ").strip().title()
    if item in menu:
        order_total += menu[item]
        print(f"{item} has been added to your order.")
    else:
        print(f"Sorry, {item} is not available in the menu.")

    another_item = input("Do you want to order another item? (yes/no): ").strip().lower()

    if another_item == 'yes':
        continue
    elif another_item == 'no':
        print(f"\nThe total amount to pay is: Rs{order_total}")
        print("Thank you for your order! Have a great day!")
        break
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
        break
