import matplotlib.pyplot as plt

# Sample data: x-axis values and corresponding y-axis values
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create the plot
plt.plot(x, y, marker='o', linestyle='-', color='b', label='y = 2x')

# Add labels and title
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Basic Line Plot')
plt.legend()  # Show the label

# Display the plot
plt.grid(True)  # Optional: adds a grid
plt.show()