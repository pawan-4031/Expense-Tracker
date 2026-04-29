from db import get_connection

def add_expense(amount, category, description, date):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO expenses (amount, category, description, date) VALUES (%s, %s, %s, %s)",
        (amount, category, description, date)
    )
    conn.commit()
    conn.close()
    print("Expense aded sucessfully!")

def view_expenses():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    conn.close()

    if len(rows) == 0:
        print("No expenses found.")
        return

    print(f"\n{'ID':<5} {'Amount':<10} {'Category':<15} {'Description':<25} {'Date'}")
    print("-" * 65)
    for row in rows:
        print(f"{row[0]:<5} {row[1]:<10} {row[2]:<15} {row[3]:<25} {row[4]}")

def filter_by_category(category):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses WHERE category = %s", (category,))
    rows = cursor.fetchall()
    conn.close()

    if len(rows) == 0:
        print(f"No expenses found for category: {category}")
        return

    print(f"\n{'ID':<5} {'Amount':<10} {'Category':<15} {'Description':<25} {'Date'}")
    print("-" * 65)
    for row in rows:
        print(f"{row[0]:<5} {row[1]:<10} {row[2]:<15} {row[3]:<25} {row[4]}")

def filter_by_month(month, year):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM expenses WHERE MONTH(date) = %s AND YEAR(date) = %s",
        (month, year)
    )
    rows = cursor.fetchall()
    conn.close()

    if len(rows) == 0:
        print(f"No expenses found for {month}/{year}")
        return

    print(f"\n{'ID':<5} {'Amount':<10} {'Category':<15} {'Description':<25} {'Date'}")
    print("-" * 65)
    for row in rows:
        print(f"{row[0]:<5} {row[1]:<10} {row[2]:<15} {row[3]:<25} {row[4]}")

def show_summary():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    rows = cursor.fetchall()
    conn.close()

    print("\n===== Expense Summary =====")
    for row in rows:
        print(f"{row[0]:<15} Rs. {row[1]}")
    print("-" * 30)
    print(f"{'Total':<15} Rs. {total}")