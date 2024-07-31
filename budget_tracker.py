def add_amount(expenses, amount, description):
    expenses.append({"description": description, "amount": amount})
    print(f"Added Expense : {description} , Amount : {amount}")


def get_total_expense(expenses):
    sum = 0
    for expense in expenses:
        sum += expense["amount"]

    return sum


def get_balance(budget, expenses):
    return budget - get_total_expense(expenses)


def show_budget_details(budget, expenses):
    print(f"Total Budget : {budget}")
    print("Expenses :")

    for expense in expenses:
        print(f" {expense['description']} : {expense['amount']}")

    print(" ")
    print(f"Total Spent : {get_total_expense(expenses)}")
    print(" ")
    print(f"Remaning Balance ; {get_balance(budget,expenses)}")
    print("")
    input("")


def main():
    print("Welcome to Budgetting App")
    initial_budget = float(input("Please Enter Your Initial Budget : "))
    budget = initial_budget

    expenses = []

    while True:
        print("\n What would you like to do?")
        print("1. Add an Expense")
        print("2. Show Budget Detials")
        print("3. Exit")
        choice = input("Select an option : ")

        if choice == "1":
            description = input("Enter expense description : ")
            amount = float(input("Enter amount you need to add : "))
            add_amount(expenses, amount, description)

        elif choice == "2":
            print("")
            show_budget_details(budget, expenses)

        elif choice == "3":
            print("Good Bye!")
            break

        else:
            print("Invalid Option")


if __name__ == "__main__":
    main()
