"""
Generated Code Metadata:
========================
Original URL: https://uagra.com.ua
Prompt: Develop a simple code snippet to calculate potential winnings on Parimatch, taking into account their odds and betting limits.
Generated: DETERMINISTIC_d68845b81fd96153
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def calculate_winnings(odds: float, stake: float, max_limit: float = 10000.0) -> float:
    """
    Calculate potential winnings based on odds and stake, considering betting limits.
    
    Args:
        odds (float): The odds provided by Parimatch (must be >= 1.0)
        stake (float): The amount bet (must be > 0 and <= max_limit)
        max_limit (float): Maximum allowed stake (default: 10000.0)
    
    Returns:
        float: Potential winnings (stake * odds)
    
    Raises:
        ValueError: If odds or stake are invalid
    """
    if not isinstance(odds, (int, float)) or odds < 1.0:
        raise ValueError("Odds must be a number >= 1.0")
    
    if not isinstance(stake, (int, float)) or stake <= 0:
        raise ValueError("Stake must be a positive number")
    
    if stake > max_limit:
        raise ValueError(f"Stake exceeds maximum limit of {max_limit}")
    
    return stake * odds

def main():
    """Main function to demonstrate the calculation."""
    try:
        # Get user input
        odds = float(input("Enter the odds: "))
        stake = float(input("Enter your stake: "))
        
        # Calculate and display winnings
        winnings = calculate_winnings(odds, stake)
        print(f"Potential winnings: {winnings:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
