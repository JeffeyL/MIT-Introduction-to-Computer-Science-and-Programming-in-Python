import math

#Cost of down payment
portion_down_payment = 0.25
#Savings increases each month by monthly salary + investment
current_savings = 0.0
#Rate of investment return
r = 0.04

#Inputs

#Total annual salary
annual_salary = float(input("Enter your annual salary: "))
#Portion of salary saved each month for down payment
portion_saved = float(input("Enter the portion of your salary to be saved, as a decimal: "))
#Cost of your dream home
total_cost = float(input("Enter the cost of your dream home: "))

down_payment = total_cost*portion_down_payment
months = 0

while current_savings < down_payment:
    current_savings = current_savings + portion_saved*(annual_salary/12) + (r/12)*(current_savings)
    months += 1

print("Number of months: " + str(months))


