from datetime import date
print("=== expense tracker ===")
print("1. Add expense")
print("2. View expenses")
print("3. Total spent")
print("4. Category-wise summary" )
print("5. Exit")
choice = input("Enter your choice: ")

if choice == "1":
    from utils import add_expense
    amount = input("Enter amount: ")
    category = input("Enter category: ")
    description = input("Enter description: ")
    add_expense(float(amount), category, description)
elif choice == "2":
    from utils import view_expenses
    view_expenses()
elif choice == "3":
    from utils import total_spent
    total_spent()
elif choice == "4":
    from utils import category_summary
    category_summary()
elif choice == "5":
    print("Exiting the program.")