"""
Task 1: Simple Calculator
Performs addition, subtraction, multiplication, and division.
Includes input validation and division-by-zero handling.
"""

def get_number(prompt):
    """Read a valid number from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    print("=== Simple Calculator ===")
    print("Operations: +  -  *  /")

    first_number = get_number("Enter the first number: ")
    operator = input("Enter an operation (+, -, *, /): ").strip()
    second_number = get_number("Enter the second number: ")

    try:
        if operator == "+":
            result = first_number + second_number
        elif operator == "-":
            result = first_number - second_number
        elif operator == "*":
            result = first_number * second_number
        elif operator == "/":
            # Division by zero is not allowed.
            result = first_number / second_number
        else:
            print("Invalid operation. Please choose +, -, *, or /.")
            return

        print(f"Result: {result:g}")
    except ZeroDivisionError:
        print("Error: You cannot divide by zero.")


if __name__ == "__main__":
    main()