from datetime import date
print("+-------------------+")
print("|  Expense tracker  |")
print("+-------------------+")
print("1. Add expense")
print("2. View expenses")
print("3. Total spent")
print("4. Category-wise summary" )
print("5. Exit")
while True:
    choice = input("Enter your choice: ")

    match(choice):
        case "1":
            from utils import add_expense
            amount = input("Enter amount: ")
            category = input("Enter category: ")
            description = input("Enter description: ")
            add_expense(float(amount), category, description)
            break
        case "2":
            from utils import view_expenses
            view_expenses()
            break
        case "3":
            from utils import total_spent
            total_spent()
            break
        case "4":
            from utils import category_summary
            category_summary()
            break
        case "5":
            print("Exiting the program.")
            break
        case _:
            print("Invalid Choice")