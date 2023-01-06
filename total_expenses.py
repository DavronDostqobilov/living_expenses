# Calculate the total expenses
import json
def total_expenses(monthly_expenses: dict) -> int:
    """
    Calculate the total expenses
    Args:
        monthly_expenses: dictionary of monthly expenses
    Returns:
        total_expenses: total expenses
    """
    sum=0
    for i in monthly_expenses.values():
        sum=sum+i
    return sum
f = open('data.json', 'r')
a=f.read()
a=json.loads(a)
print(total_expenses(a))