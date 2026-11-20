expenses = []
def load_expenses():
    try:
        file = open("expenses.txt", "r")

        for line in file:
            data = line.strip().split("|")

            expense = {
                "amount": float(data[0]),
                "category": data[1],
                "description": data[2]
            }

            expenses.append(expense)

        file.close()

    except FileNotFoundError:
        pass


def save_expense(expense):
    file = open("expenses.txt", "a")

    file.write(
        str(expense["amount"]) + "|" +
        expense["category"] + "|" +
        expense["description"] + "\n"
    )

    file.close()


def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)

    save_expense(expense)

    print("Expense added successfully!")


def view_expenses():
    if len(expenses) == 0:
        print("No expenses found.")
        return

    print("\n----- All Expenses -----")

    for i, expense in enumerate(expenses, start=1):
        print("Expense", i)
        print("Amount:", expense["amount"])
        print("Category:", expense["category"])
        print("Description:", expense["description"])
        print()


def total_expenses():
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("Total Expenses:", total)


def category_expenses():
    category = input("Enter category: ")
    total = 0

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            total = total + expense["amount"]

    print("Total spent on", category, ":", total)


# Load old expenses when program starts
load_expenses()


while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Category Expenses")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expenses()

    elif choice == "4":
        category_expenses()

    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")