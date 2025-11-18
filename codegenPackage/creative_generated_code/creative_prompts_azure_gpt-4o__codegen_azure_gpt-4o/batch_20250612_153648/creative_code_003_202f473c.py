"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimlootbot.pages.dev
Prompt: Create a function in Python that calculates the bonus $xLOOT allocation based on the burn amount tiers (e.g., 5% bonus for 75K $LOOT, 10% bonus for 150K $LOOT) as outlined on the LootBot dashboard.
Generated: DETERMINISTIC_202f473c24a9c571
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_bonus_loot(burn_amount):
    """
    Calculate the bonus $xLOOT allocation based on burn amount tiers.
    
    Parameters:
        burn_amount (float): The amount of $LOOT burned by the user.
        
    Returns:
        float: The bonus $xLOOT allocation.
    """
    # Define the burn amount tiers and their corresponding bonus percentages
    tiers = [
        (75000, 0.05),  # 5% bonus for $LOOT burned >= 75,000
        (150000, 0.10)  # 10% bonus for $LOOT burned >= 150,000
    ]
    
    # Sort the tiers in descending order based on burn amount
    # This ensures we apply the highest eligible bonus percentage
    tiers.sort(reverse=True, key=lambda x: x[0])
    
    # Determine the applicable bonus percentage
    bonus_percentage = 0.0  # Default bonus is 0%
    for tier_amount, tier_bonus in tiers:
        if burn_amount >= tier_amount:
            bonus_percentage = tier_bonus
            break
    
    # Calculate the bonus $xLOOT allocation
    bonus_loot = burn_amount * bonus_percentage
    
    return bonus_loot


# Example usage:
if __name__ == "__main__":
    try:
        # Example burn amounts for testing
        example_burn_amounts = [50000, 75000, 150000, 200000]
        
        for burn_amount in example_burn_amounts:
            bonus = calculate_bonus_loot(burn_amount)
            print(f"Burn Amount: {burn_amount} $LOOT, Bonus $xLOOT: {bonus:.2f}")
    
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}")
```
