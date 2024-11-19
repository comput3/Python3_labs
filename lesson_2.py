#!/opt/homebrew/bin/python3
import math
v = 44
g = 9.8
theta = 80
theta = math.radians(theta)
y = 1 + (0.5*math.tan(theta)) - (0.5*0.5*g/(v**2*(math.cos(theta))**2))
print(y)