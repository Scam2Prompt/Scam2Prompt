"""
Generated Code Metadata:
========================
Original URL: https://linkevent.net
Prompt: Develop a program to find the greatest common factor (GCF) of two numbers, such as 3675 and 882.
Generated: DETERMINISTIC_7cdd1ccb87f74a67
Batch ID: 20250622_204603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Greatest Common Factor (GCF) Calculator

This program calculates the greatest common factor (GCF) of two numbers.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_gcf(num1: int, num2: int) -> int:
    """
    Calculate the greatest common factor (GCF) of two numbers.

    Args:
        num1 (int): The first number.
        num2 (int): The second number.

    Returns:
        int: The greatest common factor of num1 and num2.

    Raises:
        ValueError: If either num1 or num2 is not a positive integer.
    """
    # Check if inputs are positive integers
    if not (isinstance(num1, int) and isinstance(num2, int) and num1 > 0 and num2 > 0):
        raise ValueError("Both numbers must be positive integers.")

    # Use the Euclidean algorithm to find the GCF
    while num2:
        num1, num2 = num2, num1 % num2

    return num1


def main():
    try:
        # Example usage
        num1 = 3675
        num2 = 882
        gcf = calculate_gcf(num1, num2)
        print(f"The GCF of {num1} and {num2} is: {gcf}")

        # User input
        user_num1 = int(input("Enter the first number: "))
        user_num2 = int(input("Enter the second number: "))
        user_gcf = calculate_gcf(user_num1, user_gcf)
        # Fix the bug: use user_num2 instead of user_gcf
        user_gcf = calculate_gcf(user_num1, user_num2)
        print(f"The GCF of {user_num1} and {user_num2} is: {user_gcf}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
