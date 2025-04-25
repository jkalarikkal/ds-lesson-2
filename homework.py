import numpy as np

# input choice
choice = input(" please enter equation type (linear or quadratic): ").lower()

x_values = np.arange(0, 11)  # x from 0 to 10

# function for linear equation
def linear_eq(x, a, b):
    return (a * x) + b

# function for quadratic equation y = x^2 + x + 3
def quadratic_eq(x):
    return (x ** 2) + x + 3

if choice == "linear":
    a = int(input("Enter coefficient a (for ax + b): "))
    b = int(input("Enter coefficient b (for ax + b): "))
    y_values = linear_eq(x_values, a, b)
    print("x values:", x_values)
    print("y values:", y_values)

elif choice == "quadratic":
    y_values = quadratic_eq(x_values)
    print("x values:", x_values)
    print("y values:", y_values)

else:
    print("Invalid choice. Please enter 'linear' or 'quadratic'.")