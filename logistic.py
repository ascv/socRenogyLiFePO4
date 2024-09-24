import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Step 1: Read the CSV data
# Assuming your CSV has columns 'x' and 'y'
data = pd.read_csv('data1.csv')

x_data = data['x'].values
y_data = data['y'].values

# Step 2: Define the logistic function (S-curve)
def logistic_function(x, L, x0, k):
    """
    L: maximum value of the curve (upper asymptote)
    x0: x-value of the sigmoid's midpoint
    k: steepness of the curve
    """
    return L / (1 + np.exp(-k * (x - x0)))

# Step 3: Fit the logistic function to the data
# Provide initial guesses for L, x0, and k
initial_guesses = [max(y_data), np.median(x_data), 1]

params, _ = curve_fit(logistic_function, x_data, y_data, p0=initial_guesses)

# Step 4: Extract fitted parameters
L, x0, k = params
print(f"L: {L}, x0: {x0}, k: {k}")

# Step 5: Generate fitted values
x_fit = np.linspace(min(x_data), max(x_data), 100)
y_fit = logistic_function(x_fit, L, x0, k)

# Step 6: Plot the original data and the fitted curve
plt.scatter(x_data, y_data, label='Data', color='red')
plt.plot(x_fit, y_fit, label='Fitted S-Curve', color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Battery Remaining 1')
plt.show()

