import csv
import os
from datetime import datetime

FILENAME = "expenses.csv"

# create the csv if it's not there yet, otherwise first run breaks
def setup_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Description", "Amount", "Category", "Date"])


def add_expense():
    desc = input("Enter expense description: ")

    # keep asking till they type an actual number
    while True:
        amt = input("Enter amount: ")
        try:
            amt = float(amt)
            break
        except ValueError:
            print("That's not a valid number, try again.")

    category = input("Enter category (Food/Travel/Shopping/etc): ").strip().title()
    today = datetime.now().strftime("%Y-%m-%d")

    with open(FILENAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([desc, amt, category, today])

    print("Added: {} - Rs.{} ({}) on {}".format(desc, amt, category, today))


def view_expenses():
    setup_file()
    with open(FILENAME, "r") as f:
        rows = list(csv.reader(f))

    if len(rows) <= 1:
        print("No expenses recorded yet.")
        return

    print("\n--- All Expenses ---")
    print(f"{'Description':<20}{'Amount':<10}{'Category':<15}{'Date':<12}")
    print("-" * 57)
    for row in rows[1:]:
        print(f"{row[0]:<20}{row[1]:<10}{row[2]:<15}{row[3]:<12}")


def search_by_category():
    setup_file()
    cat = input("Enter category to search: ").strip().title()
    found = False

    with open(FILENAME, "r") as f:
        reader = csv.reader(f)
        next(reader, None)  # skip header

        print(f"\n--- Expenses under '{cat}' ---")
        for row in reader:
            if row[2] == cat:
                print(row)
                found = True

    if not found:
        print("No expenses found in this category.")


def category_totals():
    setup_file()
    totals = {}

    with open(FILENAME, "r") as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            cat = row[2]
            tmp = float(row[1])  # just converting amount to number
            totals[cat] = totals.get(cat, 0) + tmp

    if not totals:
        print("No data to calculate totals.")
        return

    print("\n--- Category-wise Totals ---")
    for cat, total in totals.items():
        print(f"{cat}: Rs.{total}")


def monthly_total():
    setup_file()
    month = input("Enter month (YYYY-MM) e.g 2026-06: ").strip()
    total = 0

    with open(FILENAME, "r") as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            if row[3].startswith(month):
                total += float(row[1])

    print(f"Total spent in {month}: Rs.{total}")


def main():
    setup_file()
    while True:
        print("\n====== EXPENSE TRACKER 2.0 ======")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Search by Category")
        print("4. Category-wise Totals")
        print("5. Monthly Total")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            search_by_category()
        elif choice == "4":
            category_totals()
        elif choice == "5":
            monthly_total()
        elif choice == "6":
            print("Exiting... Thanks for using Expense Tracker 2.0!")
            break
        else:
            print("Invalid choice, please enter a number between 1-6.")


if __name__ == "__main__":
    main()
