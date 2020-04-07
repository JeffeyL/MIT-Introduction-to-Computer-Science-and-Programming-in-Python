import math

#Presets

#Semi-annual raise
semi_annual_raise = .07
#Annual return rate
r = 0.04
#Down payment percentage
portion_down_payment = 0.25
#Cost of house
cost_of_house = float(1000000)

#Inputs

#Total annual salary
annual_salary = float(input("Enter your annual salary: "))

#Required money for down payment
down_payment = portion_down_payment*cost_of_house

#Number of guesses so far
num_guesses = 0
#Margin of error
margin = 100

#Low range
low = 0
#High range
high = 10000
#Guess as a percent
guess = (high + low)/2

def calculateMoney(portion, salary):
    portion_saved = float(portion/10000)
    current_salary = salary
    i = 0
    temp = 0
    while i < 36:
        temp = temp + portion_saved*(current_salary/12) + (r/12)*(temp)
        if (i % 6 == 0) and (i > 0):
            current_salary += current_salary*semi_annual_raise
        i += 1
    return temp

possibilityCheck = calculateMoney(10000, annual_salary)

while possibilityCheck >= down_payment:
    guessvalue = calculateMoney(guess, annual_salary)
    if abs(guessvalue - down_payment) >= margin:
        num_guesses += 1
        if guessvalue < down_payment:
            low = guess
        else:
            high = guess
        guess = int((high + low)/2)
    else: break


if possibilityCheck >= down_payment:
    print("Steps in bisection search: " + str(num_guesses))
    print("Best savings rate: " + str(float(guess/10000)))
else:
    print("Impossible goal")
