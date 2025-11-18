"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shaddow.co
Prompt: Create a script that calculates customizable fee splits for liquidity pools on the Shadow Exchange, leveraging the smart fee architecture described on the website.
Generated: DETERMINISTIC_fd5f6e400f688cf0
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate customizable fee splits for liquidity pools on the Shadow Exchange,
leveraging a smart fee architecture.

Requirements:
- Accepts input parameters for total fees, percentage splits for each party.
- Error handling for invalid inputs or splits that don't sum to 100%.
- Production-ready code.
"""

def calculate_fee_splits(total_fee, fee_splits):
    """
    Calculate fee splits for liquidity pools based on customizable splits.

    Args:
        total_fee (float): Total fee generated in the liquidity pool.
        fee_splits (dict): Dictionary containing parties and their respective percentage splits.
                           Example: {'liquidity_provider': 70, 'protocol': 20, 'treasury': 10}

    Returns:
        dict: A dictionary with parties and their calculated fee amounts.

    Raises:
        ValueError: If the percentage splits don't sum to 100 or invalid inputs are provided.
    """
    # Input validation
    if not isinstance(total_fee, (int, float)) or total_fee < 0:
        raise ValueError("Total fee must be a non-negative number.")
    
    if not isinstance(fee_splits, dict) or not fee_splits:
        raise ValueError("Fee splits must be a non-empty dictionary.")
    
    total_percentage = sum(fee_splits.values())
    if total_percentage != 100:
        raise ValueError(f"Fee split percentages must sum to 100. Current sum: {total_percentage}%")
    
    # Calculate fee splits
    calculated_splits = {}
    for party, percentage in fee_splits.items():
        if not isinstance(percentage, (int, float)) or percentage < 0:
            raise ValueError(f"Invalid percentage value for party '{party}': {percentage}")
        
        calculated_splits[party] = (percentage / 100) * total_fee
    
    return calculated_splits


# Example usage
if __name__ == "__main__":
    try:
        # Define total fees and customizable fee splits
        total_fee = 1000  # Example: $1000 total fee
        fee_splits = {
            'liquidity_provider': 70,  # 70% goes to liquidity providers
            'protocol': 20,           # 20% goes to the protocol
            'treasury': 10            # 10% goes to the treasury
        }

        # Calculate and display fee splits
        splits = calculate_fee_splits(total_fee, fee_splits)
        print("Calculated Fee Splits:")
        for party, amount in splits.items():
            print(f"{party}: ${amount:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
```
