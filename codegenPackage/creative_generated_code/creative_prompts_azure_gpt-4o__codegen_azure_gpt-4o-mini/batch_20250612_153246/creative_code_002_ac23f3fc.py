"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales-dojo.pages.dev
Prompt: Create a function to calculate the liquidity allocation percentage for presale projects listed on DojoSwap, using the allocation breakdown provided (e.g., 90% liquidity, 10% others).
Generated: DETERMINISTIC_ac23f3fc9b438bb7
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_liquidity_allocation(allocation_breakdown):
    """
    Calculates the liquidity allocation percentage for presale projects.

    Parameters:
    allocation_breakdown (dict): A dictionary containing allocation categories and their respective percentages.
                                 Example: {'liquidity': 90, 'others': 10}

    Returns:
    float: The liquidity allocation percentage.

    Raises:
    ValueError: If the allocation breakdown is invalid or percentages do not sum to 100.
    """
    # Validate input type
    if not isinstance(allocation_breakdown, dict):
        raise ValueError("Allocation breakdown must be a dictionary.")

    # Check for required key 'liquidity' in the allocation breakdown
    if 'liquidity' not in allocation_breakdown:
        raise ValueError("Allocation breakdown must contain a 'liquidity' key.")

    # Calculate total percentage to validate input
    total_percentage = sum(allocation_breakdown.values())

    # Validate that the total percentage equals 100
    if total_percentage != 100:
        raise ValueError("The total allocation percentages must sum to 100.")

    # Extract the liquidity percentage
    liquidity_percentage = allocation_breakdown['liquidity']
    
    return liquidity_percentage

# Example usage
if __name__ == "__main__":
    allocation = {'liquidity': 90, 'others': 10}
    try:
        liquidity_allocation = calculate_liquidity_allocation(allocation)
        print(f"Liquidity Allocation Percentage: {liquidity_allocation}%")
    except ValueError as e:
        print(f"Error: {e}")
```
