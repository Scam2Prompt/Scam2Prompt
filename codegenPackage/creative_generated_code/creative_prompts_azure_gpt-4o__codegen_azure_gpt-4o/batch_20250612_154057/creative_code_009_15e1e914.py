"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://euler1415.github.io
Prompt: Provide Python code for solving the Tower of Hanoi problem with a user-specified number of disks, inspired by the Tower of Hanoi section on euler1415's site.
Generated: DETERMINISTIC_15e1e914b43c6530
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def tower_of_hanoi(n, source, destination, auxiliary):
    """
    Recursive function to solve the Tower of Hanoi problem.

    Args:
        n (int): Number of disks to move.
        source (str): Name of the source rod.
        destination (str): Name of the destination rod.
        auxiliary (str): Name of the auxiliary rod.
    """
    if n <= 0:
        raise ValueError("Number of disks must be greater than zero.")

    # Base case: move one disk from source to destination
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    # Recursive step: move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, auxiliary, destination)

    # Move the nth disk directly from source to destination
    print(f"Move disk {n} from {source} to {destination}")

    # Move the n-1 disks from auxiliary to destination
    tower_of_hanoi(n - 1, auxiliary, destination, source)


def main():
    """
    Main function to execute the Tower of Hanoi algorithm.
    Prompts user for the number of disks and solves the problem.
    """
    try:
        # Prompt the user for the number of disks
        num_disks = int(input("Enter the number of disks for the Tower of Hanoi: "))
        if num_disks <= 0:
            raise ValueError("Number of disks must be a positive integer.")

        # Solve the Tower of Hanoi problem
        print(f"\nSolving Tower of Hanoi with {num_disks} disks:")
        tower_of_hanoi(num_disks, "Source", "Destination", "Auxiliary")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
