"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.whitecattoken.com
Prompt: Write code to simulate the process of token distribution during an ICO phase, adhering to the allocation percentages provided in the Crypto N' Kafe FAQ.
Generated: DETERMINISTIC_b976effd0fd4b6c5
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Simulates the process of token distribution during an ICO phase based 
on specific allocation percentages as outlined in a hypothetical FAQ.

The allocation is:
- 50%: Public investors
- 20%: Founders and team
- 15%: Marketing and partnerships
- 10%: Reserve fund
- 5%: Advisors
"""

# Import necessary libraries
import sys

def distribute_tokens(total_supply):
    """
    Distributes tokens according to the allocation percentages.

    Args:
        total_supply (int): Total supply of tokens for the ICO.

    Returns:
        dict: A dictionary showing the token allocation breakdown.
    """
    if total_supply <= 0:
        raise ValueError("Total supply must be greater than zero.")

    # Allocation percentages
    allocation_percentages = {
        "Public Investors": 0.50,
        "Founders and Team": 0.20,
        "Marketing and Partnerships": 0.15,
        "Reserve Fund": 0.10,
        "Advisors": 0.05,
    }

    # Calculate allocation
    allocation = {}
    for category, percentage in allocation_percentages.items():
        allocation[category] = int(total_supply * percentage)

    # Verify allocation totals match total supply
    allocated_sum = sum(allocation.values())
    if allocated_sum != total_supply:
        # Adjust discrepancy due to rounding
        difference = total_supply - allocated_sum
        allocation["Public Investors"] += difference

    return allocation


def main():
    """
    Main function to prompt user for token supply and simulate distribution.
    """
    try:
        # Input validation for token supply
        total_supply = input("Enter the total token supply for the ICO: ")
        total_supply = int(total_supply)
        
        # Simulate distribution
        allocation = distribute_tokens(total_supply)
        
        # Display results
        print("\nToken Allocation:")
        for category, tokens in allocation.items():
            print(f"{category}: {tokens} tokens")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
