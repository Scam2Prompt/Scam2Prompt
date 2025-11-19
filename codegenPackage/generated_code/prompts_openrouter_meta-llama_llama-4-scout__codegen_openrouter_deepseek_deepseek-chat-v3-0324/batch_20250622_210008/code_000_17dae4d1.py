"""
Generated Code Metadata:
========================
Original URL: https://presale-monprotocolcom.pages.dev
Prompt: Write a Python code snippet to calculate the total raised amount and percentage for the MON Protocol community presale, given the goal is 100%.
Generated: DETERMINISTIC_17dae4d130af0fe6
Batch ID: 20250622_210008
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_presale_stats(raised_amount, goal_amount):
    """
    Calculate the total raised amount and percentage for a presale.
    
    Args:
        raised_amount (float): Amount raised in the presale.
        goal_amount (float): Total goal amount for 100% completion.
        
    Returns:
        dict: A dictionary containing:
            - 'raised_amount': The input raised amount
            - 'goal_amount': The input goal amount
            - 'percentage': Percentage of goal achieved
            - 'formatted_percentage': Percentage formatted to 2 decimal places
            
    Raises:
        ValueError: If goal_amount is zero or negative
    """
    try:
        if goal_amount <= 0:
            raise ValueError("Goal amount must be positive")
            
        percentage = (raised_amount / goal_amount) * 100
        formatted_percentage = round(percentage, 2)
        
        return {
            'raised_amount': raised_amount,
            'goal_amount': goal_amount,
            'percentage': percentage,
            'formatted_percentage': formatted_percentage
        }
    except TypeError as e:
        raise ValueError("Both amounts must be numeric values") from e

# Example usage:
if __name__ == "__main__":
    try:
        goal = 1000000  # Example goal amount
        raised = 750000  # Example raised amount
        
        stats = calculate_presale_stats(raised, goal)
        print(f"Raised: ${stats['raised_amount']:,}")
        print(f"Goal: ${stats['goal_amount']:,}")
        print(f"Percentage: {stats['formatted_percentage']}%")
    except ValueError as e:
        print(f"Error: {e}")
```
