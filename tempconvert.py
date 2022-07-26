FAHRENHEIT = 0.0
C_MAX = 250
FC_OFFSET = 32.0
DIVIDER = 1.8
print("Fahrenheit | Celsius")
while FAHRENHEIT <= C_MAX:
    celsius = (FAHRENHEIT - FC_OFFSET) / DIVIDER
    print("%5.1f  >  > %7.2f" % (FAHRENHEIT, celsius))
    FAHRENHEIT = FAHRENHEIT + 25