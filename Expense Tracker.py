import json
from datetime import datetime

def load_data(file_name="expenses.json"):
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_data(data, file_name="expenses.json"):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

def add_expense(data):
    try:
        date = input("Enter the date (YYYY-MM-DD): ")
        datetime.strptime(date, "%Y-%m-%d")  # Validate date format
        category = input("Enter the category (e.g., Food, Transport, Entertainment): ").capitalize()
        description = input("Enter a brief description: ")
        amount = float(input("Enter the amount: "))

        if date not in data:
            data[date] = []

        data[date].append({"category": category,"description": description,"amount": amount})
        print("\nExpense added successfully!")
    except ValueError:
        print("\nInvalid input. Please try again.")

def view_expenses(data):
    date = input("Enter the date (YYYY-MM-DD) to view expenses: ")
    if date in data:
        print(f"\nExpenses for {date}:")
        for expense in data[date]:
            print(f"- {expense['category']}: {expense['description']} - ${expense['amount']:.2f}")
    else:
        print("\nNo expenses recorded for this date.")

def view_category_summary(data):
    summary = {}
    for expenses in data.values():
        for expense in expenses:
            category = expense["category"]
            summary[category] = summary.get(category, 0) + expense["amount"]

    print("\nCategory-wise spending:")
    for category, total in summary.items():
        print(f"- {category}: ${total:.2f}")

def view_monthly_summary(data):
    monthly_summary = {}
    for date, expenses in data.items():
        month = date[:7]
        for expense in expenses:
            monthly_summary[month] = monthly_summary.get(month, 0) + expense["amount"]

    print("\nMonthly spending summary:")
    for month, total in monthly_summary.items():
        print(f"- {month}: ${total:.2f}")

def main():
    data = load_data()
    while True:
        print("\n--- Expense Tracker Menu ---")
        print("1. Add Expense")
        print("2. View Expenses by Date")
        print("3. View Category-wise Summary")
        print("4. View Monthly Summary")
        print("5. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_expense(data)
            elif choice == 2:
                view_expenses(data)
            elif choice == 3:
                view_category_summary(data)
            elif choice == 4:
                view_monthly_summary(data)
            elif choice == 5:
                save_data(data)
                print("\nThank you for using the Expense Tracker. Goodbye!")
                break
            else:
                print("\nInvalid choice. Please select a valid option.")
        except ValueError:
            print("\nInvalid input. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()