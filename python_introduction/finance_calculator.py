monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
project_savings = int(monthly_savings * 12 + (monthly_savings * 12 * 0.05))
print("Your monthly savings are ${0}.".format(monthly_savings))
print("Projected savings after one year, with interest, is: ${0}.".format(project_savings))
