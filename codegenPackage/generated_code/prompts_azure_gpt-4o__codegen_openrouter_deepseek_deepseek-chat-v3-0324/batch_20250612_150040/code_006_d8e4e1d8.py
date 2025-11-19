"""
Generated Code Metadata:
========================
Original URL: https://gigantic-afternoon-sparse.on-fleek.app
Prompt: Write a Python script to randomly assign signatures to 20 copies of a comic book in a stock of 100, ensuring fair distribution, as described for the Top G #3.1 Collectors Edition.
Generated: DETERMINISTIC_d8e4e1d89b8a5a5a
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

def assign_signatures(total_copies, signed_copies, seed=None):
    """
    Randomly assigns signatures to a specified number of copies from a total stock.
    
    Args:
        total_copies (int): Total number of copies in stock.
        signed_copies (int): Number of copies to be signed.
        seed (int, optional): Random seed for reproducibility. Defaults to None.
    
    Returns:
        list: List of copy numbers (1-based index) that have been signed.
    
    Raises:
        ValueError: If signed_copies exceeds total_copies or if either is negative.
    """
    if total_copies <= 0 or signed_copies <= 0:
        raise ValueError("Total copies and signed copies must be positive integers.")
    if signed_copies > total_copies:
        raise ValueError("Signed copies cannot exceed total copies.")
    
    if seed is not None:
        random.seed(seed)
    
    copies = list(range(1, total_copies + 1))
    signed = random.sample(copies, signed_copies)
    
    return sorted(signed)

if __name__ == "__main__":
    try:
        total = 100
        signed = 20
        signed_copies = assign_signatures(total, signed)
        
        print(f"Signed copies (out of {total}):")
        print(signed_copies)
    except ValueError as e:
        print(f"Error: {e}")
```
