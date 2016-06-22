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
