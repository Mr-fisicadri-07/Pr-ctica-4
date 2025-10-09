# this is a program that calculates the monthly payment rate for a loan

# M = P[r(1+r)^n] / [(1+r)^n - 1]

# M is the monthly payment.
# P is the principal loan amount.
# r is the monthly interest rate (annual interest rate divided by 12 months).
# n is the total number of months.

P = float(input("Enter the principal loan amount: "))
r = float(input("Enter the annual interest rate (as a percentage, e.g., 5 for 5%): "))

r = r / 100 / 12  # convert annual rate to monthly and percentage to decimal
n = int(input("Enter the total number of years: "))
n = n * 12  # convert years to months

M = P * (r * (1 + r) ** n) / ((1 + r) ** n - 1)

print(f"The calculated monthly payment is: {M:.2f}")

gross_salary = float(input("Enter your gross yearly salary: "))
monthly_salary = (gross_salary * 0.7) / 12 # assuming 30% deductions for taxes and social security

if M > monthly_salary * 0.3:
    print("The monthly payment exceeds 30% of your salary. Loan may not be approved.")

else:
    print("The monthly payment is within 30% of your salary. Loan may be approved.")