a = float(input("Please, enter the value of 'a': "))
b = float(input("Please, enter the value of 'b': "))
c = float(input("Please, enter the value of 'c': "))

x1 = ((-b) + ((b**2) - (4*a*c))**0.5)/(2*a)

x2 = ((-b) - ((b**2) - (4*a*c))**0.5)/(2*a)

print ("Your value for X are " + str(round(x1,2)) + " and " + str(round(x2,2)))