import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Read the CSV data
# Assuming your CSV has columns 'x' and 'y'
data = pd.read_csv('data2.csv')

x_data = data['x'].values
y_data = data['y'].values

# Step 2: Fit a 1st-degree polynomial (linear fit)
coefficients = np.polyfit(x_data, y_data, 1)  # 1st-degree polynomial (linear)
print(coefficients)

# Step 3: Generate the polynomial function (linear in this case)
linear_fit = np.poly1d(coefficients)
print(linear_fit)

# Step 4: Generate fitted values for plotting
x_fit = np.linspace(min(x_data), max(x_data), 100)
y_fit = linear_fit(x_fit)

# Step 5: Plot the original data and the fitted line
#plt.scatter(x_data, y_data, label='Data', color='red')
#plt.plot(x_fit, y_fit, label='Fitted Line (Linear)', color='blue')
#plt.xlabel('x')
#plt.ylabel('y')
#plt.legend()
#plt.title('Battery Remaining 2')
#plt.show()

