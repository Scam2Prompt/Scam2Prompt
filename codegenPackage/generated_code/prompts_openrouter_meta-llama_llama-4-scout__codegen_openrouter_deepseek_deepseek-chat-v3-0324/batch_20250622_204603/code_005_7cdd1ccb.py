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
def find_gcf(a, b):
    """
    Calculate the greatest common factor (GCF) of two numbers using the Euclidean algorithm.
    
    Args:
        a (int): First number.
        b (int): Second number.
    
    Returns:
        int: The greatest common factor of a and b.
    
    Raises:
        ValueError: If either a or b is not a positive integer.
    """
    # Validate input
    if not isinstance(a, int) or not isinstance(b, int) or a <= 0 or b <= 0:
        raise ValueError("Both numbers must be positive integers")
    
    # Ensure a is the larger number
    if a < b:
        a, b = b, a
    
    # Euclidean algorithm
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    try:
        num1 = 3675
        num2 = 882
        gcf = find_gcf(num1, num2)
        print(f"The GCF of {num1} and {num2} is {gcf}")
    except ValueError as e:
        print(f"Error: {e}")
```
