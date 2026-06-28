# 💰 Expense Tracker

A simple command-line Expense Tracker built with Python. This project allows users to record daily expenses, store them in a JSON file, and view spending information.

## Features

* Add a new expense
* Store expenses in a JSON file
* View all expenses
* Calculate total expenses
* View category-wise expense summary
* Simple menu-driven interface
* Data persistence using JSON

## Project Structure

```
expense_tracker/
│
├── main.py          # Main program
├── utils.py         # Helper functions
├── expenses.json    # Stores all expense data
└── README.md
```

## Technologies Used

* Python 3
* JSON
* Datetime Module
* Git & GitHub

## How to Run

1. Clone the repository

```bash
git clone https://github.com/your-username/expense_tracker.git
```

2. Navigate to the project

```bash
cd expense_tracker
```

3. Run the program

```bash
python main.py
```

## Sample Expense

```json
{
    "amount": 250,
    "category": "Food",
    "description": "Burger",
    "date": "2026-06-27"
}
```

## Future Improvements

* Edit existing expenses
* Delete expenses
* Monthly reports
* Expense filtering
* Data visualization
* GUI version

## Author

Om Subham Pradhan
