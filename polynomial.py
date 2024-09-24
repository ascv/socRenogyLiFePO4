import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Read the CSV data
# Assuming your CSV has columns 'x' and 'y'
data = pd.read_csv('data.csv')

x_data = data['x'].values
y_data = data['y'].values

# Step 2: Fit a 3rd-degree polynomial (cubic polynomial)
coefficients = np.polyfit(x_data, y_data, 2)  # 3rd-degree polynomial

# Step 3: Generate the polynomial function
polynomial = np.poly1d(coefficients)

# Step 4: Generate fitted values for plotting
x_fit = np.linspace(min(x_data), max(x_data), 100)
y_fit = polynomial(x_fit)

# Step 5: Plot the original data and the fitted polynomial
plt.scatter(x_data, y_data, label='Data', color='red')
plt.plot(x_fit, y_fit, label='Fitted Polynomial (3rd degree)', color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('3rd Degree Polynomial Fitting')
plt.show()

