"""
Generated Code Metadata:
========================
Original URL: https://euler1415.github.io
Prompt: Provide Python code for solving the Tower of Hanoi problem with a user-specified number of disks, inspired by the Tower of Hanoi section on euler1415's site.
Generated: DETERMINISTIC_15e1e914b43c6530
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def tower_of_hanoi(n, source='A', target='C', auxiliary='B'):
    """
    Solve the Tower of Hanoi problem.

    Parameters:
    n (int): The number of disks.
    source (str): The name of the source peg.
    target (str): The name of the target peg.
    auxiliary (str): The name of the auxiliary peg.
    """
    # Validate input
    if not isinstance(n, int) or n < 1:
        raise ValueError("Number of disks must be a positive integer.")

    # Base case: only one disk to move
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return

    # Move n-1 disks from source to auxiliary, using target as a temporary peg
    tower_of_hanoi(n - 1, source, auxiliary, target)

    # Move the nth disk from source to target
    print(f"Move disk {n} from {source} to {target}")

    # Move the n-1 disks from auxiliary to target, using source as a temporary peg
    tower_of_hanoi(n - 1, auxiliary, target, source)

if __name__ == "__main__":
    try:
        # User input for the number of disks
        num_disks = int(input("Enter the number of disks: "))
        tower_of_hanoi(num_disks)
    except ValueError as e:
        print(f"Error: {e}")
```
