class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, amount, category):
        if category not in self.expenses:
            self.expenses[category] = []
        self.expenses[category].append(amount)

    def show_summary(self):
        total_expense = 0
        print("\nExpense Summary:")
        for category, amounts in self.expenses.items():
            category_total = sum(amounts)
            total_expense += category_total
            print(f"{category}: ${category_total}")

        print("\nTotal Expense: ${}".format(total_expense))

    def run_tracker(self):
        while True:
            print("\nExpense Tracker Menu:")
            print("1. Add Expense")
            print("2. Show Summary")
            print("3. Exit")

            choice = input("Enter your choice (1/2/3): ")

            if choice == "1":
                amount = float(input("Enter the expense amount: $"))
                category = input("Enter the expense category: ")
                self.add_expense(amount, category)
                print("Expense added successfully!")

            elif choice == "2":
                self.show_summary()

            elif choice == "3":
                print("Exiting Expense Tracker. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run_tracker()
