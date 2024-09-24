import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the CSV files
data = pd.read_csv('data.csv')
test_data = pd.read_csv('data_test.csv')

# Step 2: Plot the data
plt.plot(data['x'], data['y'], label='measured', marker='o')
plt.plot(test_data['x'], test_data['y'], label='estimated', marker='x')

# Step 3: Add labels and title
plt.xlabel('V')
plt.ylabel('% battery remaining')
plt.title('Real vs Estimated')

# Step 4: Add legend
plt.legend()

# Step 5: Show the plot
plt.show()

