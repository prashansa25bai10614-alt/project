# Beginner-friendly Shopping List Program

def show_menu():
    print("\n--- Shopping List Menu ---")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

shopping_list = []

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(f"✅ {item} added to your shopping list.")

    elif choice == "2":
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"❌ {item} removed from your shopping list.")
        else:
            print("Item not found in the list.")

    elif choice == "3":
        if shopping_list:
            print("\n🛒 Your Shopping List:")
            for i, item in enumerate(shopping_list, start=1):
                print(f"{i}. {item}")
        else:
            print("Your shopping list is empty.")

    elif choice == "4":
        print("Goodbye! 🛍️")
        break

    else:
        print("Invalid choice. Please enter 1-4.")