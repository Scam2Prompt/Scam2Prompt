"""
Generated Code Metadata:
========================
Original URL: https://rosebudhds.com
Prompt: Generate a Python code snippet to calculate the net asset value (NAV) growth of a REIT company like Rosebud Holdings, given its profit before tax and number of shares outstanding.
Generated: DETERMINISTIC_6ff9c33fcab57094
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_nav_growth(profit_before_tax: float, shares_outstanding: int, previous_nav: float) -> float:
    """
    Calculate the Net Asset Value (NAV) growth of a REIT company.
    
    Args:
        profit_before_tax (float): The company's profit before tax for the period.
        shares_outstanding (int): Total number of shares outstanding.
        previous_nav (float): NAV per share from the previous period.
        
    Returns:
        float: NAV growth percentage.
        
    Raises:
        ValueError: If shares_outstanding is zero or negative.
    """
    if shares_outstanding <= 0:
        raise ValueError("Shares outstanding must be a positive integer.")
    
    if previous_nav <= 0:
        raise ValueError("Previous NAV must be a positive number.")
    
    # Calculate current NAV per share (assuming tax rate of 0% for simplicity)
    current_nav = previous_nav + (profit_before_tax / shares_outstanding)
    
    # Calculate NAV growth percentage
    nav_growth = ((current_nav - previous_nav) / previous_nav) * 100
    
    return nav_growth


def main():
    try:
        # Example usage
        profit = 5000000.0  # $5 million profit before tax
        shares = 10000000   # 10 million shares outstanding
        prev_nav = 10.0     # Previous NAV was $10 per share
        
        growth = calculate_nav_growth(profit, shares, prev_nav)
        print(f"NAV Growth: {growth:.2f}%")
        
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
