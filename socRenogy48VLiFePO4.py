def SOC(v):
    """ Gets an approximation of the state of charge.

    Note that not all batteries are the same and they can have minor variations
    in voltages. This function was created using data from a battery that may
    differ slightly than your battery.

    As a simple hack to account for some of this variance at the top and low
    ends, there is a small voltage buffer (+/- 2V) that will cause this
    function to return 100 (at the top) or 0 (at the bottom) if your input
    voltage is outside the range of data used to fit this function.

    Args:
        v (float): input voltage
    Returns:
        (float): state of charge i.e. battery remaining percent
    """
    soc = None

    # Handle slightly higher voltages not seen in the training data
    if 54.4 < v and v < 56.4:
        soc = 100

    # Use a logistic function at the top end
    elif 52.4 <= v and v <= 54.4:
        L = 101.191451
        x0 = 52.537895
        k = 3.16037696
        soc = L / (1 + 2.718282**(-k * (v - x0)))
        soc = soc if soc < 100 else 100 # ensure we don't get values above 100

    # Use a linear function in the middle
    elif 51.6 <= v and v < 52.4:
        soc = 25*v - 1270

    # Use a logistic function at the bottom end
    elif 40 < v < 51.6:
        soc = 1.4473*v - 58.457263
        L = 36.440261
        x0 = 51.29112
        k = 0.3567057
        soc = L / (1 + 2.718282**(-k * (v - x0)))

    # Handle slightly lower voltages not seen in the training data
    elif 38 < v and v <= 40:
        soc = 0

    # Data too far out of range to reliably estimate
    else:
        raise Exception(f"{v} not in [38V, 56.4V]: re-fit functions")

    return soc



