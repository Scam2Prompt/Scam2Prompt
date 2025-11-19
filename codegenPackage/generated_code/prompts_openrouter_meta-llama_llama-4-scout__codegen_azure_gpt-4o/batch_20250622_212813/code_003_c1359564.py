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
def tower_of_hanoi(n, source, target, auxiliary):
    """
    Solves the Tower of Hanoi problem recursively.

    Parameters:
    n (int): Number of disks to move.
    source (str): The name of the source rod.
    target (str): The name of the target rod.
    auxiliary (str): The name of the auxiliary rod.

    Returns:
    None
    """
    # Base case: If there's only one disk, move it directly from source to target
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return

    # Step 1: Move n-1 disks from source to auxiliary using target as a helper
    tower_of_hanoi(n - 1, source, auxiliary, target)

    # Step 2: Move the nth disk from source to target
    print(f"Move disk {n} from {source} to {target}")

    # Step 3: Move the n-1 disks from auxiliary to target using source as a helper
    tower_of_hanoi(n - 1, auxiliary, target, source)


def main():
    """
    Main function to execute the Tower of Hanoi simulation.
    """
    try:
        # Number of disks
        num_disks = int(input("Enter the number of disks: "))
        if num_disks <= 0:
            raise ValueError("Number of disks must be a positive integer.")

        print(f"\nSteps to solve Tower of Hanoi with {num_disks} disks:")
        tower_of_hanoi(num_disks, "Source", "Target", "Auxiliary")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
