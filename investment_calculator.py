amount = float(input("Enter amount: "))
inrate = float(input("Enter Interest rate: "))
period = int(input("Enter period: "))
value = 0
year = 1
while year <= period:
    value = amount + (inrate * amount)
    print("Year %d | CHF %.2f" % (year,value))
    amount = value
    year = year + 1

#N = amount
#sum = 0
#count = period
#while count < N:
#    number = float(N)
#    sum = sum + number
#    count = count + 1
#average = float(sum) / N

import datetime
from datetime import datetime
now = datetime.now()

#print("AVG Total = %f" % average)
print(f"Investments calculated on: ", now)
#print("Total Invested = %d" % N), print("Sum of Investments = %f" % sum)
