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
def tower_of_hanoi(n, source='A', target='C', auxiliary='B', moves=None):
    """
    Solve the Tower of Hanoi problem using recursion.

    :param n: Number of disks
    :param source: The source peg
    :param target: The target peg
    :param auxiliary: The auxiliary peg
    :param moves: List to store the sequence of moves (for output)
    :return: List of moves for moving disks from source to target
    """
    if moves is None:
        moves = []  # Initialize moves list if not provided

    # Input validation
    if not isinstance(n, int) or n < 1:
        raise ValueError("Number of disks must be a positive integer.")

    # Base case: Move a single disk
    if n == 1:
        moves.append(f"Move disk 1 from {source} to {target}")
        return moves

    # Move n-1 disks from source to auxiliary peg
    tower_of_hanoi(n - 1, source, auxiliary, target, moves)
    
    # Move the nth disk from source to target peg
    moves.append(f"Move disk {n} from {source} to {target}")
    
    # Move the n-1 disks from auxiliary to target peg
    tower_of_hanoi(n - 1, auxiliary, target, source, moves)

    return moves

def main():
    """Main function to execute the Tower of Hanoi solution."""
    try:
        num_disks = int(input("Enter the number of disks: "))
        moves = tower_of_hanoi(num_disks)
        print("\nSequence of moves:")
        for move in moves:
            print(move)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
