"""
Generated Code Metadata:
========================
Original URL: https://rosebudhds.com
Prompt: Write Python code to calculate the net asset value (NAV) per share for a REIT portfolio, referencing the financial metrics provided by Rosebud Holdings Property Income REIT (e.g., $0.4m profit before tax, $0.3m property portfolio, and 0.4p NAV per share).
Generated: DETERMINISTIC_2a9e2755a0dbcef6
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_nav_per_share(total_assets, total_liabilities, number_of_shares):
    """
    Calculate the Net Asset Value (NAV) per share for a REIT portfolio.
    
    Parameters:
    total_assets (float): Total value of all assets in the portfolio (in millions)
    total_liabilities (float): Total value of all liabilities (in millions)
    number_of_shares (int): Total number of outstanding shares
    
    Returns:
    float: NAV per share in pence (p)
    
    Raises:
    ValueError: If number_of_shares is zero or negative
    """
    if number_of_shares <= 0:
        raise ValueError("Number of shares must be positive")
    
    net_assets = total_assets - total_liabilities
    nav_per_share = (net_assets * 100) / number_of_shares  # Convert to pence
    
    return nav_per_share

# Example usage with Rosebud Holdings Property Income REIT metrics
if __name__ == "__main__":
    try:
        # Example values (in £m except shares which are count)
        total_assets = 0.3  # £0.3m property portfolio
        total_liabilities = 0.0  # Assuming no liabilities for this example
        number_of_shares = 100  # Assuming 100 shares outstanding
        
        nav = calculate_nav_per_share(total_assets, total_liabilities, number_of_shares)
        print(f"NAV per share: {nav:.1f}p")
        
    except ValueError as e:
        print(f"Error calculating NAV: {e}")
```
