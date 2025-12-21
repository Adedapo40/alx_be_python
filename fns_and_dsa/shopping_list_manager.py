def display_menu():
    print("\n=== Shopping List Manager ===")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    print("=" * 30)

def main():
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to your shopping list.")
            else:
                print("Item name cannot be empty.")
                
        elif choice == '2':
            # Prompt for and remove an item
            if not shopping_list:
                print("Your shopping list is empty.")
            else:
                item = input("Enter item to remove: ").strip()
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"'{item}' has been removed from your shopping list.")
                else:
                    print(f"'{item}' was not found in your shopping list.")
                    
        elif choice == '3':
            # Display the shopping list
            if not shopping_list:
                print("Your shopping list is empty.")
            else:
                print("\n--- Your Shopping List ---")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
                print("---------------------------")
                
        elif choice == '4':
            print("Goodbye! Happy shopping!")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
