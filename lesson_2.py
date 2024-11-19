#!/opt/homebrew/bin/python3
import math

# Constants
v = 44  # Initial velocity in m/s
g = 9.8  # Acceleration due to gravity in m/s^2
theta = 80  # Launch angle in degrees
y_0 = 1  # Initial barrel height in meters

# Convert angle to radians
theta_rad = math.radians(theta)

# Function to calculate height at a given horizontal distance
def calculate_height(x):
    return y_0 + x * math.tan(theta_rad) - (g * x**2) / (2 * (v * math.cos(theta_rad))**2)

# Text-based simulation
x = 0  # Start at x = 0
step = 0.1  # Increment for x

print(f"{'Horizontal Distance (m)':<25}{'Height (m)':<15}")
print("-" * 40)

while True:
    y = calculate_height(x)
    if y < 0:  # Stop when the object hits the ground
        print(f"{x:<25.2f}{0.00:<15.2f} - Bang! Object hit the ground.")
        break
    print(f"{x:<25.2f}{y:<15.2f}")
    x += step