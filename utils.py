from datetime import date
import json

def add_expense(amount, category, description):
    # Read existing expenses
    with open("expenses.json", "r") as file:
        expenses = json.load(file)

    # Create new expense
    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": str(date.today())
    }

    # Add it to the list
    expenses.append(expense)

    # Save updated list back to the file
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

    print("Expense added successfully!")

def view_expenses():
    # Read existing expenses
    with open("expenses.json", "r") as file:
        expenses = json.load(file)

    if not expenses:
        print("No expenses recorded.")
        return

    for expense in expenses:
        print(f"Date: {expense['date']}\nAmount: {expense['amount']}\nCategory: {expense['category']}\nDescription: {expense['description']}\n")

def total_spent():
    # Read existing expenses
    with open("expenses.json", "r") as file:
        expenses = json.load(file)

    total = sum(expense["amount"] for expense in expenses)
    print(f"Total spent: {total}")

def category_summary():
    # Read existing expenses
    with open("expenses.json", "r") as file:
        expenses = json.load(file)

    category_totals = {}
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        category_totals[category] = category_totals.get(category, 0) + amount
    for category, total in category_totals.items():
        print(f"In {category} total spent is {total}")
