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
def tower_of_hanoi(n, from_rod, to_rod, aux_rod):
    """
    Solves the Tower of Hanoi problem.

    Args:
        n (int): Number of disks.
        from_rod (str): Name of the rod where disks are initially located.
        to_rod (str): Name of the rod where disks need to be moved.
        aux_rod (str): Name of the auxiliary rod.

    Raises:
        ValueError: If the number of disks is not a positive integer.

    Returns:
        None
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Number of disks must be a positive integer.")

    _tower_of_hanoi_recursive(n, from_rod, to_rod, aux_rod)


def _tower_of_hanoi_recursive(n, from_rod, to_rod, aux_rod):
    """
    Recursive helper function for solving the Tower of Hanoi problem.

    Args:
        n (int): Number of disks.
        from_rod (str): Name of the rod where disks are initially located.
        to_rod (str): Name of the rod where disks need to be moved.
        aux_rod (str): Name of the auxiliary rod.

    Returns:
        None
    """
    if n == 1:
        # Base case: move one disk
        print(f"Move disk 1 from rod {from_rod} to rod {to_rod}")
        return

    # Move n - 1 disks from from_rod to aux_rod
    _tower_of_hanoi_recursive(n - 1, from_rod, aux_rod, to_rod)

    # Move the nth disk from from_rod to to_rod
    print(f"Move disk {n} from rod {from_rod} to rod {to_rod}")

    # Move the n - 1 disks that we left on aux_rod to to_rod
    _tower_of_hanoi_recursive(n - 1, aux_rod, to_rod, from_rod)


def main():
    try:
        num_disks = int(input("Enter the number of disks: "))
        tower_of_hanoi(num_disks, 'A', 'C', 'B')
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
