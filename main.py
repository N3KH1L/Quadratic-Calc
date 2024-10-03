import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve

# Function to graph a quadratic equation
def graph_quadratic(a, b, c):
    x = np.linspace(-10, 10, 400)  # Generating points between -10 and 10
    y = a * x ** 2 + b * x + c  # Quadratic equation

    # Plotting the quadratic function
    plt.plot(x, y, label=f'Quadratic: {a:.2f}x² + {b:.2f}x + {c:.2f}', color='blue')

    # Mark x and y intercepts
    x_intercepts = find_x_intercepts(a, b, c)
    y_intercept = find_y_intercept(c)
    plt.scatter(x_intercepts, [0] * len(x_intercepts), color='red', zorder=5, label="x-intercepts")
    plt.scatter(0, y_intercept, color='green', zorder=5, label="y-intercept")

    # Mark and label the vertex
    vertex = find_vertex(a, b, c)
    plt.scatter(*vertex, color='purple', zorder=5, label=f'Vertex: {vertex}')

    # Plot axis of symmetry
    x_vertex = vertex[0]
    plt.axvline(x=x_vertex, color='gray', linestyle='--', label=f'Axis of Symmetry: x={x_vertex}')

    # Set graph limits
    plt.xlim([-10, 10])
    plt.ylim([-10, 10])

    # Plotting design enhancements
    plt.axhline(0, color='black', linewidth=1)  # x-axis
    plt.axvline(0, color='black', linewidth=1)  # y-axis
    plt.title(f'Graph of {a:.2f}x² + {b:.2f}x + {c:.2f}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()

# Function to find the x-intercepts (roots)
def find_x_intercepts(a, b, c):
    x = symbols('x')
    equation = Eq(a * x ** 2 + b * x + c, 0)
    roots = solve(equation, x)
    return [float(root) for root in roots]  # Return roots as floating point numbers

# Function to find the y-intercept
def find_y_intercept(c):
    return c  # The y-intercept is just the constant term 'c'

# Function to find the vertex
def find_vertex(a, b, c):
    x_vertex = -b / (2 * a)  # x = -b/2a
    y_vertex = a * x_vertex ** 2 + b * x_vertex + c  # Plugging x_vertex into the quadratic equation
    return (x_vertex, y_vertex)

# Function to calculate the coefficients of a quadratic equation from 3 points
def find_quadratic_coefficients(x1, y1, x2, y2, x3, y3):
    # Setting up the matrix A and vector b
    A = np.array([[x1 ** 2, x1, 1],
                  [x2 ** 2, x2, 1],
                  [x3 ** 2, x3, 1]])

    b = np.array([y1, y2, y3])

    # Solve for coefficients a, b, c
    coefficients = np.linalg.solve(A, b)
    return coefficients  # returns (a, b, c)

# Additional feature: check if the parabola opens upwards or downwards
def parabola_direction(a):
    if a > 0:
        return "The parabola opens upwards."
    elif a < 0:
        return "The parabola opens downwards."
    else:
        return "This is not a valid quadratic equation."

# Function to generate a table of (x, y) values from the quadratic equation
def generate_table(a, b, c):
    x_values = np.linspace(-10, 10, 21)  # Generate x values from -10 to 10
    print("\nTable of (x, y) values:")
    print("{:<10} {:<10}".format('x', 'y'))  # Print header
    for x in x_values:
        y = a * x ** 2 + b * x + c  # Calculate corresponding y values
        print("{:<10} {:<10.2f}".format(x, y))  # Print each (x, y) pair

# Main function to interact with the user
def main():
    print("Choose an option:")
    print("1. Graph a quadratic equation and find its features (intercepts, vertex, symmetry, direction).")
    print("2. Find the quadratic equation from 3 points.")

    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        print("You chose quadratic equation graphing.")
        a = float(input("Enter the coefficient a (x² term): "))
        b = float(input("Enter the coefficient b (x term): "))
        c = float(input("Enter the constant c: "))

        # Graph the quadratic equation
        graph_quadratic(a, b, c)

        # Find the intercepts, vertex, axis of symmetry, and direction
        x_intercepts = find_x_intercepts(a, b, c)
        y_intercept = find_y_intercept(c)
        vertex = find_vertex(a, b, c)
        direction = parabola_direction(a)

        print(f"x-intercepts (roots): {x_intercepts}")
        print(f"y-intercept: {y_intercept}")
        print(f"Vertex: {vertex}")
        print(f"Axis of symmetry: x = {vertex[0]}")
        print(direction)

        # Generate and display the table of (x, y) values
        generate_table(a, b, c)

    elif choice == 2:
        print("You chose finding the quadratic equation from 3 points.")
        x1, y1 = map(float, input("Enter the first point (x1, y1) as space-separated values: ").split())
        x2, y2 = map(float, input("Enter the second point (x2, y2) as space-separated values: ").split())
        x3, y3 = map(float, input("Enter the third point (x3, y3) as space-separated values: ").split())

        # Find the coefficients of the quadratic equation
        a, b, c = find_quadratic_coefficients(x1, y1, x2, y2, x3, y3)

        # Print the quadratic equation
        print(f"The quadratic equation is: y = {a:.2f}x² + {b:.2f}x + {c:.2f}")

        # Generate and display the table of (x, y) values
        generate_table(a, b, c)

        # Optionally graph the quadratic equation
        graph_quadratic(a, b, c)

    else:
        print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
