import math
import sys

def SOC(x):
    """ Gets an approximation of the state of charge.

    Note that not all batteries are the same and can have minor variations in
    voltages. This function was created using data from a battery that might
    be slightly different than your battery so the output might be a few
    points off.

    As a simple hack to account for some of this variance, there is a small
    voltage buffer at the top and low end that will cause this function to
    return 100 or 0 respectively if your voltages are outside the range of
    data used to fit this function.

    Args:
        x (float): input voltage
    Returns:
        (float): state of charge i.e. battery remaining percent
    """
    soc = None

    if 54.5 < x and x < 56: # handle higher voltages not fit by our data
        soc = 100
    elif 51.5 <= x and x <= 54.5: # use a logistic fit
        L = 105.966717
        x0 = 52.49304544
        k = 2.07051358
        soc = L / (1 + 2.718282**(-k * (x - x0)))
        soc = soc if soc < 100 else 100 # ensure we don't get values above 100
    elif 52.4 <= x and x <= 51.6: # use a linear fit
        print('not implemented')
        pass
    elif 40 < x < 51.6: # use a logistic fit
        soc = 1.44729942*x - 58.45726272
    elif 38 < x and x <= 40: # handle lower voltages not fit by our data
        soc = 0
    else:
        print(f"ERROR: {x} not in [38, 56]")
        print(f"ERROR: function should be re-fit to your data")

    return soc


battery_remaining = SOC(float(sys.argv[1]))

if battery_remaining is not None:
    battery_remaining = round(battery_remaining, 2)
    print(f"{battery_remaining}%")
