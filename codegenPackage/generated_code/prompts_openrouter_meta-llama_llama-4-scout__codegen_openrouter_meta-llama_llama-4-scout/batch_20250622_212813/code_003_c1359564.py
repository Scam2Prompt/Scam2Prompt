"""
Generated Code Metadata:
========================
Original URL: https://euler1415.github.io
Prompt: Generate a Python code snippet to simulate the Tower of Hanoi problem.
Generated: DETERMINISTIC_c1359564072910af
Batch ID: 20250622_212813
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
        ValueError: If n is not a positive integer.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    if n == 1:
        # Base case: move one disk
        print(f"Move disk 1 from rod {from_rod} to rod {to_rod}")
        return

    # Move n - 1 disks from from_rod to aux_rod
    tower_of_hanoi(n - 1, from_rod, aux_rod, to_rod)

    # Move the nth disk from from_rod to to_rod
    print(f"Move disk {n} from rod {from_rod} to rod {to_rod}")

    # Move the n - 1 disks that we left on aux_rod to to_rod
    tower_of_hanoi(n - 1, aux_rod, to_rod, from_rod)


def main():
    try:
        n = int(input("Enter the number of disks: "))
        tower_of_hanoi(n, 'A', 'C', 'B')
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
