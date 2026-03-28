import json
import os
from datetime import datetime

FILE_NAME = "expenses.json"

# Load expenses from file
def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

# Save expenses to file
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

# Add new expense
def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food, Travel, etc.): ")
    note = input("Enter note: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    expense = {
        "amount": amount,
        "category": category,
        "note": note,
        "date": date
    }

    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)

    print("✅ Expense added successfully!\n")

# View all expenses
def view_expenses():
    expenses = load_expenses()

    if not expenses:
        print("No expenses found.\n")
        return

    print("\n--- All Expenses ---")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. ₹{exp['amount']} | {exp['category']} | {exp['note']} | {exp['date']}")
    print()

# Total spending
def total_expense():
    expenses = load_expenses()
    total = sum(exp["amount"] for exp in expenses)
    print(f"\n💰 Total Spending: ₹{total}\n")

# Category-wise summary
def category_summary():
    expenses = load_expenses()
    summary = {}

    for exp in expenses:
        category = exp["category"]
        summary[category] = summary.get(category, 0) + exp["amount"]

    print("\n--- Category Summary ---")
    for cat, amt in summary.items():
        print(f"{cat}: ₹{amt}")
    print()

# Main menu
def main():
    while True:
        print("==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Spending")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
