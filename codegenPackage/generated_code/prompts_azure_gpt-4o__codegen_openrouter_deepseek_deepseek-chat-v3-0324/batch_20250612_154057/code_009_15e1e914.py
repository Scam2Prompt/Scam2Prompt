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
def tower_of_hanoi(n, source, target, auxiliary):
    """
    Solves the Tower of Hanoi problem recursively for n disks.
    
    Args:
        n (int): Number of disks to move.
        source (str): Name of the source peg.
        target (str): Name of the target peg.
        auxiliary (str): Name of the auxiliary peg.
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n-1, auxiliary, target, source)


def main():
    """
    Main function to get user input and solve the Tower of Hanoi problem.
    """
    print("Tower of Hanoi Solver")
    print("---------------------")
    
    while True:
        try:
            num_disks = int(input("Enter the number of disks (positive integer): "))
            if num_disks <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    
    print("\nSolution Steps:")
    tower_of_hanoi(num_disks, 'A', 'C', 'B')


if __name__ == "__main__":
    main()
```
