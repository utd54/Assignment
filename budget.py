from .models import Expense
from .db import SessionLocal

def add_expense(user_id, category, amount, date):
    db = SessionLocal()
    expense = Expense(user_id=user_id, category=category, amount=amount, date=date)
    db.add(expense)
    db.commit()
    db.close()