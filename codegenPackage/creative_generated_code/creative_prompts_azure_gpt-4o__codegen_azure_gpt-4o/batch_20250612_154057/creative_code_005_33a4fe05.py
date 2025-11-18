"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://euler1415.github.io
Prompt: Write code to simulate the Tower of Hanoi puzzle, referencing the mention of the puzzle on euler1415's website.
Generated: DETERMINISTIC_33a4fe05129f816d
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Tower of Hanoi Solver in Python
# This script simulates the Tower of Hanoi puzzle.
# The puzzle involves moving 'n' disks from a source rod to a target rod using an auxiliary rod.
# The code is clean, efficient, and includes proper documentation.

def tower_of_hanoi(n, source, target, auxiliary):
    """
    Recursively solves the Tower of Hanoi puzzle.

    Args:
        n (int): Number of disks to move.
        source (str): The name of the source rod.
        target (str): The name of the target rod.
        auxiliary (str): The name of the auxiliary rod.

    Returns:
        None
    """
    # Base case: If there's only one disk, move it directly from source to target.
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return

    # Recursive step:
    # 1. Move the top (n-1) disks from source to auxiliary using target as a helper.
    tower_of_hanoi(n - 1, source, auxiliary, target)

    # 2. Move the largest disk (nth disk) from source to target.
    print(f"Move disk {n} from {source} to {target}")

    # 3. Move the (n-1) disks from auxiliary to target using source as a helper.
    tower_of_hanoi(n - 1, auxiliary, target, source)


def main():
    """
    Main function to execute the Tower of Hanoi simulation.
    Prompts the user for the number of disks and initializes the puzzle.
    """
    try:
        # Input: Number of disks
        num_disks = int(input("Enter the number of disks for the Tower of Hanoi puzzle: "))
        if num_disks <= 0:
            raise ValueError("Number of disks must be a positive integer.")

        print("\nSteps to solve the Tower of Hanoi puzzle:\n")
        # Start the simulation
        tower_of_hanoi(num_disks, "Source", "Target", "Auxiliary")

    except ValueError as e:
        # Handle invalid input
        print(f"Error: {e}")
    except Exception as e:
        # General error handling
        print(f"An unexpected error occurred: {e}")


# Entry point of the script
if __name__ == "__main__":
    main()
```
