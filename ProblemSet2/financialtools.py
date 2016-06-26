'''
PROBLEM 1: PAYING THE MINIMUM
Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.
'''

#balance - the outstanding balance on the credit card
#annualInterestRate - annual interest rate as a decimal
#monthlyPaymentRate - minimum monthly payment rate as a decimal

def payMinimum(balance,annualInterestRate,monthlyPaymentRate):
    month = 0
    totalPaid = 0
    for month in range(1,13):
       minPayment = balance * monthlyPaymentRate #Compute the monthly payment, based on the previous month's balance.
       balance -=  minPayment #Update the outstanding balance by removing the payment
       balance += (annualInterestRate/12.0)*balance #then charging interest on the result.
       print 'Month:', month
       print 'Minimum monthly payment:',round(minPayment,2)
       print 'Remaining balance:',round(balance,2)
       totalPaid += minPayment
    print 'Total paid:', round(totalPaid,2)
    print 'Remaining balance:', round(balance,2)


'''
PROBLEM 2: PAYING DEBT OFF IN A YEAR
Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months.
By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.
'''
'''
    balance - the outstanding balance on the credit card
    annualInterestRate - annual interest rate as a decimal
'''

def payDebtOff(balance,annualInterestRate):
    fixed = 10
    while True:
        newbalance = balance
        for month in range(1,13):
            newbalance -= fixed
            newbalance += (annualInterestRate/12.0)*newbalance
        if newbalance > 0:
            fixed += 10
        else:
            break
    return fixed
