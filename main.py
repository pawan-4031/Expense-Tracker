from expenses import add_expense, view_expenses, filter_by_category, filter_by_month, show_summary

def main():
    while True:
        print("\n======= Expense Tracker =======")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. Filter by category")
        print("4. Filter by month")
        print("5. View summary")
        print("6. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            amount = float(input("Amount: "))
            category = input("Category: ")
            description = input("Description: ")
            date = input("Date (YYYY-MM-DD): ")
            add_expense(amount, category, description, date)

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            category = input("Enter category: ")
            filter_by_category(category)

        elif choice == "4":
            month = int(input("Enter month (1-12): "))
            year = int(input("Enter year (YYYY): "))
            filter_by_month(month, year)

        elif choice == "5":
            show_summary()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")

main()