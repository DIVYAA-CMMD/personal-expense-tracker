import csv
import os


expenses = []
file_path = os.path.join(os.path.dirname(__file__), "expenses.csv")

if os.path.exists(file_path):
    with open(file_path, "r", newline="") as file:
        reader = csv.reader(file)

        for row in reader:
            expense = {
                "name": row[0],
                "amount": float(row[1]),
                "category": row[2]
            }

            expenses.append(expense)
def add_expense():
    name = input("Enter expense name: ")
    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    category = input("Enter category: ")

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)

    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, amount, category])

    print("\n✓ Expense added successfully!")
def view_expenses():
    if len(expenses) == 0:
        print("\nNo expenses recorded yet.")
    else:
        print("\n========== YOUR EXPENSES ==========")

        for i, expense in enumerate(expenses, start=1):
            print(f"\n{i}. {expense['name']}")
            print(f"   Amount: ₹{expense['amount']}")
            print(f"   Category: {expense['category']}")
def search_by_category():
    search_category = input("Enter category to search: ")

    found = False

    for expense in expenses:
        if expense["category"].lower() == search_category.lower():
            print("\nExpense:", expense["name"])
            print("Amount: ₹", expense["amount"])
            print("Category:", expense["category"])
            found = True

    if not found:
        print("\nNo expenses found in this category.")
def show_total():
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("\nTotal Spending: ₹", total)
def show_highest():
    if len(expenses) == 0:
        print("\nNo expenses recorded yet.")
    else:
        highest = expenses[0]

        for expense in expenses:
            if expense["amount"] > highest["amount"]:
                highest = expense

        print("\n========== HIGHEST EXPENSE ==========")
        print("Expense:", highest["name"])
        print("Amount: ₹", highest["amount"])
        print("Category:", highest["category"])
def delete_expense():
    if len(expenses) == 0:
        print("\nNo expenses to delete.")
        return

    print("\n========== YOUR EXPENSES ==========")

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['name']} - ₹{expense['amount']} - {expense['category']}")

    try:
        choice = int(input("\nEnter the expense number to delete: "))

        if choice < 1 or choice > len(expenses):
            print("\nInvalid expense number.")
            return

    except ValueError:
        print("\nPlease enter a valid number.")
        return

    deleted = expenses.pop(choice - 1)

    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)

        for expense in expenses:
            writer.writerow([
                expense["name"],
                expense["amount"],
                expense["category"]
            ])

    print(f"\n✓ Deleted: {deleted['name']}")
def category_summary():
    if len(expenses) == 0:
        print("\nNo expenses recorded yet.")
        return

    category_totals = {}

    for expense in expenses:
        category = expense["category"]

        if category in category_totals:
            category_totals[category] += expense["amount"]
        else:
            category_totals[category] = expense["amount"]

    print("\n========== CATEGORY SUMMARY ==========")

    for category, total in category_totals.items():
        print(f"{category}: ₹{total}")

while True:
    print("================================")
    print("      PERSONAL EXPENSE TRACKER")
    print("================================")

    print("\n1. Add Expense")
    print("2. View All Expenses")
    print("3. Search by Category")
    print("4. Show Total Spending")
    print("5. Show Highest Expense")
    print("6. Delete an Expense")
    print("7. Category Summary")
    print("8. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        search_by_category()

    elif choice == "4":
        show_total()

    elif choice == "5":
        show_highest()
    elif choice == "6":
        delete_expense()
    elif choice == "7":
        category_summary()
    elif choice == "8":
        print("\nThank you for using Personal Expense Tracker!")
        break