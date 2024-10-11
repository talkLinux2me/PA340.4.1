# 1. Check if x is less than 10
x = 7
if x < 10:
    print("Less than 10")

x = 15  # No output expected here


# 2. If-else statement
x = 7
if x < 10:
    print("Less than 10")
else:
    print("Greater than 10")

x = 15  # No output expected here


# 3. If...elif...else statement
x = 15
if x < 10:
    print("Less than 10")
elif 10 < x < 20:
    print("Between 10 and 20")
else:
    print("Greater than or equal to 20")

x = 50  # No output expected here


# 4. In-range check with if-else statement
x = 15
if x < 10 or x > 20:
    print("Out of range")
else:
    print("In range")

x = 5  # No output expected here


# 5. Grade calculation based on user input
score = int(input("Enter your score (0-100): "))
if score < 0 or score > 100:
    print("Score out of range")
elif 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 60 <= score < 70:
    print("Grade: D")
else:
    print("Grade: F")


# 6. Tax calculation based on filing status and income
filing_status = input("Enter your filing status (Single, Married Filing Jointly, Married Filing Separately, Head of Household): ")
income = float(input("Enter your income: "))

tax = 0

if filing_status == "Single":
    if income <= 8350:
        tax = income * 0.10
    elif income <= 33950:
        tax = 835 + (income - 8350) * 0.15
    elif income <= 82250:
        tax = 4675 + (income - 33950) * 0.25
    else:
        tax = 16725 + (income - 82250) * 0.28
elif filing_status == "Married Filing Jointly":
    if income <= 16700:
        tax = income * 0.10
    elif income <= 67900:
        tax = 1670 + (income - 16700) * 0.15
    elif income <= 137050:
        tax = 9400 + (income - 67900) * 0.25
    else:
        tax = 24040 + (income - 137050) * 0.28
elif filing_status == "Married Filing Separately":
    if income <= 8350:
        tax = income * 0.10
    elif income <= 33950:
        tax = 835 + (income - 8350) * 0.15
    elif income <= 68525:
        tax = 4675 + (income - 33950) * 0.25
    else:
        tax = 12020 + (income - 68525) * 0.28
elif filing_status == "Head of Household":
    if income <= 11950:
        tax = income * 0.10
    elif income <= 45500:
        tax = 1195 + (income - 11950) * 0.15
    elif income <= 117450:
        tax = 6445 + (income - 45500) * 0.25
    else:
        tax = 19800 + (income - 117450) * 0.28
else:
    print("Invalid filing status")

if tax > 0:
    print(f"Your tax amount is: ${tax:.2f}")
