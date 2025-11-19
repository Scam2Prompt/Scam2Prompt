"""
Generated Code Metadata:
========================
Original URL: https://orlandoplasmacenters.com
Prompt: Generate a Python script to calculate the total earnings for a donor based on the compensation structure of $100-$200 per donation at Orlando Plasma Centers.
Generated: DETERMINISTIC_9ef0562148b3b61c
Batch ID: 20250622_211932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_total_earnings(donations):
    """
    Calculate the total earnings for a donor based on the compensation structure.
    
    Args:
        donations (list of int): List of donation amounts (between $100 and $200).
        
    Returns:
        float: Total earnings rounded to 2 decimal places.
        
    Raises:
        ValueError: If any donation amount is outside the valid range ($100-$200).
    """
    MIN_COMPENSATION = 100
    MAX_COMPENSATION = 200
    
    total = 0.0
    
    for amount in donations:
        if not MIN_COMPENSATION <= amount <= MAX_COMPENSATION:
            raise ValueError(
                f"Invalid donation amount: ${amount}. "
                f"Amount must be between ${MIN_COMPENSATION} and ${MAX_COMPENSATION}."
            )
        total += amount
    
    return round(total, 2)


def main():
    """Main function to demonstrate the earnings calculation."""
    try:
        # Example usage
        donations = [100, 150, 200, 175]
        total_earnings = calculate_total_earnings(donations)
        print(f"Total earnings: ${total_earnings:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
