from .models import Expense, Budget
from .db import SessionLocal
from sqlalchemy.sql import func

def monthly_summary(user_id, month):
    db = SessionLocal()
    summary = db.query(
        Expense.category,
        func.sum(Expense.amount).label("total_spent")
    ).filter(
        Expense.user_id == user_id,
        func.strftime("%Y-%m", Expense.date) == month
    ).group_by(Expense.category).all()
    db.close()
    return summary

def budget_vs_spending(user_id, month):
    db = SessionLocal()
    budgets = db.query(Budget).filter_by(user_id=user_id, month=month).all()
    expenses = monthly_summary(user_id, month)
    result = []
    for b in budgets:
        spent = next((e.total_spent for e in expenses if e.category == b.category), 0)
        result.append({"category": b.category, "budget": b.amount, "spent": spent})
    db.close()
    return result