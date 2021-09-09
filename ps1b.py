#Problem Set 1b
#Name:Sheetal kumari
#Time: spent: 4hours


balance = float(input('Enter the outstanding balance on your credit card:'))
annual_interest_rate=float(input('Enter the annual credit card interest rate as a decimal:'))

min_monthly_pay=.5*balance 
balance=balance
while balance>=0:
    month=1
    min_monthly_pay=min_monthly_pay+500
    balance=balance

    while month<=12 and balance>0:
        month=month+1
        monthly_interest_rate=annual_interest_rate/12.0
        balance=balance*(1+monthly_interest_rate)-min_monthly_pay
print("RESULT")
print("Monthly payment to pay off debt in 1 year:",min_monthly_pay)
print("Number of months needed:",month)
print("Balance:",balance)
