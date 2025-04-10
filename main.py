from app.db import Base, engine, Session
from app.models import User
from app.expense import add_expense
from app.budget import set_budget
from app.reports import total_monthly_spending, compare_budget

def init_db():
    Base.metadata.create_all(engine)

def get_or_create_user(session, username):
    user = session.query(User).filter_by(name=username).first()
    if not user:
        user = User(name=username)
        session.add(user)
        session.commit()
        print(f"👤 Created new user: {username}")
    return user

def main():
    init_db()
    session = Session()

    print("Welcome to Expense Tracker!")
    username = input("Enter your username: ").strip()
    user = get_or_create_user(session, username)

    while True:
        print("\nChoose an option:")
        print("1. Add Expense")
        print("2. Set Budget")
        print("3. View Monthly Spending")
        print("4. Compare Budget vs Spending")
        print("5. Exit")
        choice = input("Your choice: ")

        if choice == '1':
            category = input("Category: ")
            amount = float(input("Amount: "))
            date = input("Date (YYYY-MM-DD) or press Enter for today: ")
            add_expense(session, user.id, category, amount, date if date else None)

        elif choice == '2':
            category = input("Category: ")
            amount = float(input("Budget Amount: "))
            month = input("Month (YYYY-MM) or press Enter for current month: ")
            set_budget(session, user.id, category, amount, month if month else None)

        elif choice == '3':
            month = input("Month (YYYY-MM): ")
            total_monthly_spending(session, user.id, month)

        elif choice == '4':
            month = input("Month (YYYY-MM): ")
            compare_budget(session, user.id, month)

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
