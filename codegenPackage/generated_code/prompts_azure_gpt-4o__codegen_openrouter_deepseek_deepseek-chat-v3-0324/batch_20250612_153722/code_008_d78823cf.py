"""
Generated Code Metadata:
========================
Original URL: https://pengwu.io
Prompt: Write a script to calculate and display the token distribution percentages for PENGWU's tokenomics, including presale, liquidity, staking rewards, and team allocations.
Generated: DETERMINISTIC_d78823cf00ab628c
Batch ID: 20250612_153722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
PENGWU Tokenomics Calculator

This script calculates and displays the token distribution percentages
for PENGWU's tokenomics, including presale, liquidity, staking rewards,
and team allocations.
"""

def calculate_token_distribution(total_supply, allocations):
    """
    Calculate token distribution based on allocation percentages.
    
    Args:
        total_supply (int): Total token supply
        allocations (dict): Dictionary of allocation names and percentages
        
    Returns:
        dict: Dictionary with allocation names and token amounts
    """
    distribution = {}
    for name, percentage in allocations.items():
        distribution[name] = int(total_supply * (percentage / 100))
    return distribution

def display_distribution(total_supply, distribution):
    """
    Display the token distribution in a formatted table.
    
    Args:
        total_supply (int): Total token supply
        distribution (dict): Dictionary with allocation names and token amounts
    """
    print("\nPENGWU Token Distribution")
    print("=" * 30)
    print(f"Total Supply: {total_supply:,} PENGWU\n")
    
    print("{:<20} {:<15} {:<10}".format("Category", "Tokens", "Percentage"))
    print("-" * 45)
    
    for category, tokens in distribution.items():
        percentage = (tokens / total_supply) * 100
        print("{:<20} {:<15,} {:<10.2f}%".format(
            category, tokens, percentage
        ))
    
    # Verify total matches
    calculated_total = sum(distribution.values())
    if calculated_total != total_supply:
        print("\nWarning: Distribution total doesn't match supply!")
        print(f"Calculated: {calculated_total:,} vs Supply: {total_supply:,}")

def main():
    try:
        # Tokenomics parameters
        TOTAL_SUPPLY = 1_000_000_000  # 1 billion tokens
        
        # Allocation percentages
        ALLOCATIONS = {
            "Presale": 30,
            "Liquidity": 25,
            "Staking Rewards": 20,
            "Team": 15,
            "Advisors": 5,
            "Marketing": 3,
            "Development Fund": 2
        }
        
        # Calculate distribution
        distribution = calculate_token_distribution(TOTAL_SUPPLY, ALLOCATIONS)
        
        # Display results
        display_distribution(TOTAL_SUPPLY, distribution)
        
    except Exception as e:
        print(f"Error calculating token distribution: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
```
