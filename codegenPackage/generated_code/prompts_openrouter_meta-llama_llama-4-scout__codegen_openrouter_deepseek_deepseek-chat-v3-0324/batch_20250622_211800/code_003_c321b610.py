"""
Generated Code Metadata:
========================
Original URL: https://zkstacks.in
Prompt: How can I implement a simple lottery number generator inspired by dear lottery today using Python?
Generated: DETERMINISTIC_c321b6107e1eef8e
Batch ID: 20250622_211800
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import argparse
from typing import List

def generate_lottery_numbers(pool_size: int = 49, numbers_to_pick: int = 6) -> List[int]:
    """
    Generates unique lottery numbers within a specified range.
    
    Args:
        pool_size: The upper bound of the number range (inclusive)
        numbers_to_pick: How many numbers to select
        
    Returns:
        List of sorted unique random numbers
    """
    if numbers_to_pick > pool_size:
        raise ValueError("Cannot pick more numbers than available in the pool")
    
    numbers = list(range(1, pool_size + 1))
    selected = random.sample(numbers, numbers_to_pick)
    selected.sort()
    return selected

def main():
    parser = argparse.ArgumentParser(description="Lottery Number Generator")
    parser.add_argument(
        "--pool", 
        type=int, 
        default=49,
        help="Upper bound of number range (default: 49)"
    )
    parser.add_argument(
        "--pick", 
        type=int, 
        default=6,
        help="How many numbers to pick (default: 6)"
    )
    parser.add_argument(
        "--sets", 
        type=int, 
        default=1,
        help="How many sets of numbers to generate (default: 1)"
    )
    
    args = parser.parse_args()
    
    try:
        for i in range(args.sets):
            numbers = generate_lottery_numbers(args.pool, args.pick)
            print(f"Set {i + 1}: {numbers}")
    except ValueError as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == "__main__":
    main()
```
