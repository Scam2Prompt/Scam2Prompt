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
    Solve the Tower of Hanoi problem.

    Parameters:
    n (int): The number of disks.
    source (str): The name of the source rod.
    target (str): The name of the target rod.
    auxiliary (str): The name of the auxiliary rod.
    """
    # Base case: If there's only one disk, move it from source to target
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return

    # Move n-1 disks from source to auxiliary, using target as a temporary rod
    tower_of_hanoi(n - 1, source, auxiliary, target)

    # Move the nth disk from source to target
    print(f"Move disk {n} from {source} to {target}")

    # Move the n-1 disks from auxiliary to target, using source as a temporary rod
    tower_of_hanoi(n - 1, auxiliary, target, source)

def main():
    """
    Main function to execute the Tower of Hanoi simulation.
    """
    try:
        # Number of disks
        num_disks = 3
        
        # Start the Tower of Hanoi simulation
        print(f"Solving Tower of Hanoi for {num_disks} disks:")
        tower_of_hanoi(num_disks, 'A', 'C', 'B')
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
