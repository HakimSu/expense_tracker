import json
import datetime

def add_expense(amo, cat, desc):
    with open ("expenses.json", "r") as file:
        exps = json.load(file)

    exp = {
        "date" : str(datetime.date.today()),
        "amount" : amo,
        "category" : cat,
        "description" : desc
    }

    exps.append(exp)

    with open("expenses.json", "w") as file:
        json.dump(exps, file, indent = 4)

    print("Successfully Added !")    

def view_expenses():
    with open("expenses.json", "r") as file:
        exps = json.load(file)

    if exps:
        for exp in exps:
            print(f"Date: {exp["date"]}")
            print(f"Amount: {exp["amount"]}")
            print(f"Category: {exp["category"]}")
            print(f"Description: {exp["description"]}")
    else:
        print("No Data about your expenses")
        return

def total_spent():
    with open ("expenses.json", "r") as file:
        exps = json.load(file)

    for exp in exps:
        total = sum(exp["amount"])

    print(f"Total Expense: {total}")

def category_summary():
    with open ("expenses.json", "r") as file:
        exps = json.load(file)

    if exps:
        print(f"Date        Category  Amount   Description")
        for exp in exps:
            print(f"{exp["date"]}    {exp["category"]}    {exp["amount"]}    {exp["description"]}")
    else:
        print("You have no Expenses")
        return
    
def delete_expenses():
    with open ("expenses.json", "w") as file:
        json.dump({}, file)
    print("Expenses Deleted Successfully")
    
print("+-------------------+")
print("|  Expense Tracker  |")
print("+-------------------+")
print("1. Add expense")
print("2. View expenses")
print("3. Total spent")
print("4. Category Summary" )
print("5. Delete all expenses" )
print("6. Exit")
while True:

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        description = input("Enter description: ")
        add_expense(amount, category, description)

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_spent()

    elif choice == "4":
        category_summary()

    elif choice == "5":
        delete_expenses()
        
    elif choice == "6":
        print("Exited")
        break

    else:
        print("Invalid Choice, Choose a valid Input.")