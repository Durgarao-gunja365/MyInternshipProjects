import json
import os

class Expense:
    def __init__(self, amount, description, category):
        self.amount = amount
        self.description = description
        self.category = category

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories = set()

    def add_expense(self, amount, description, category):
        expense = Expense(amount, description, category)
        self.expenses.append(expense)
        self.categories.add(category)

    def save_to_file(self, filename):
        data = {"expenses": [vars(expense) for expense in self.expenses], "categories": list(self.categories)}
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    def load_from_file(self, filename):
        if os.path.exists(filename):
            with open(filename, "r") as file:
                data = json.load(file)
                self.expenses = [Expense(**expense) for expense in data["expenses"]]
                self.categories = set(data["categories"])
        else:
            print(f"File '{filename}' not found. Creating a new Expense Tracker.")

def main():
    tracker = ExpenseTracker()

    # Load data from file if it exists
    tracker.load_from_file("expenses.json")

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Save and Quit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            amount = float(input("Enter the amount spent: "))
            description = input("Enter a brief description: ")
            category = input("Enter the category: ")
            tracker.add_expense(amount, description, category)
            print("Expense added successfully.")

        elif choice == "2":
            print("\nExpenses:")
            for expense in tracker.expenses:
                print(f"Amount: ${expense.amount}, Description: {expense.description}, Category: {expense.category}")

        elif choice == "3":
            tracker.save_to_file("expenses.json")
            print("Expense data saved. Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
