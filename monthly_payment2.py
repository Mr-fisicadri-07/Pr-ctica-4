# this is a program that calculates the monthly payment rate for a loan

# M = P[r(1+r)^n] / [(1+r)^n - 1]

# M is the monthly payment.
# P is the principal loan amount.
# r is the monthly interest rate (annual interest rate divided by 12 months).
# n is the total number of months.

P = float(input("Enter your principal loan amount: "))
r = float(input("Enter the annual interest rate (as a percentage, e.g., 5 for 5%): "))
r = r / 100 / 12  # convert annual rate to monthly and percentage to decimal
n = int(input("Enter the total number of years: ")) * 12  # convert years to months

M = P * (r * (1 + r) ** n) / ((1 + r) ** n - 1) # monthly payment

print (f"The calculated monthly payment is: {M: .2f}")

gross_salary = float(input("Enter your gross yearly salary: "))
monthly_salary = (gross_salary * 0.7) / 12 # assuming 30% deductions for taxes and social security

if monthly_salary * 0.3 < M:
    print("Your monthly salary is less than 30 of your monthly payment. Loan may no be approved.")
elif monthly_salary * 0.5 < M:
    print("Your monthly salary is less than 50 of your monthly payment. Loan will not be approved.")
else:
    print("Your monthly salary is more than 30 of your monthly payment. Loan may be approved.")