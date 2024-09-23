import math
import sys

def SOC(x):
    L = 105.966717
    x0 = 52.49304544
    k = 2.07051358

    if 51.5 <= x and x <= 54.5:
        return(L / (1 + 2.718282**(-k * (x - x0))))
    elif x < 51.5:
        return(1.44729942*x - 58.45726272)
    else:
        print(f"{x} not in [0, 54.5]")


print(SOC(float(sys.argv[1])))
