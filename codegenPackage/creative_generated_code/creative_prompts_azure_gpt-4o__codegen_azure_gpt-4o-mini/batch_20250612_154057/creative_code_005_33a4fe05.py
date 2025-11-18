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
class TowerOfHanoi:
    def __init__(self, disks):
        """
        Initializes the Tower of Hanoi puzzle with a specified number of disks.

        :param disks: Number of disks in the puzzle.
        """
        if disks < 1:
            raise ValueError("The number of disks must be at least 1.")
        self.disks = disks
        self.source = 'A'  # Starting peg
        self.target = 'C'  # Target peg
        self.auxiliary = 'B'  # Auxiliary peg

    def solve(self):
        """
        Solves the Tower of Hanoi puzzle and prints the steps to move the disks.
        """
        self._move_disks(self.disks, self.source, self.target, self.auxiliary)

    def _move_disks(self, n, source, target, auxiliary):
        """
        Recursive method to move disks between pegs.

        :param n: Number of disks to move.
        :param source: The peg from which to move disks.
        :param target: The peg to which disks are to be moved.
        :param auxiliary: The peg used as an auxiliary storage.
        """
        if n == 1:
            print(f"Move disk 1 from {source} to {target}")
            return
        
        # Move n-1 disks from source to auxiliary, so they are out of the way
        self._move_disks(n - 1, source, auxiliary, target)
        
        # Move the nth disk from source to target
        print(f"Move disk {n} from {source} to {target}")

        # Move the n-1 disks that we left on auxiliary to target
        self._move_disks(n - 1, auxiliary, target, source)


if __name__ == "__main__":
    try:
        number_of_disks = int(input("Enter the number of disks: "))
        hanoi = TowerOfHanoi(number_of_disks)
        hanoi.solve()
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
