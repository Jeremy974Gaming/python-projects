basic_salary = 1500
bonus_rate = 200
commision_rate = 0.02
numberofunits = int(input("Enter the number of sold units: "))
price = float(input("Enter the total price: "))
bonus = (bonus_rate * numberofunits)
commision = (commision_rate * numberofunits * price)
print("Bonus        = %6.2f" % bonus)
print("Commision    = %6.2f" % commision)
print("Gross Salary = %6.2f" % (basic_salary + bonus + commision))