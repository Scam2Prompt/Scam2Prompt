"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rosebudhds.com
Prompt: Write Python code to calculate the net asset value (NAV) per share for a REIT portfolio, referencing the financial metrics provided by Rosebud Holdings Property Income REIT (e.g., $0.4m profit before tax, $0.3m property portfolio, and 0.4p NAV per share).
Generated: DETERMINISTIC_2a9e2755a0dbcef6
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import sys

def calculate_nav_per_share(total_assets, total_liabilities, total_shares):
    """
    Calculate the Net Asset Value (NAV) per share.

    Parameters:
    total_assets (float): Total assets of the REIT portfolio.
    total_liabilities (float): Total liabilities of the REIT portfolio.
    total_shares (int): Total number of outstanding shares.

    Returns:
    float: NAV per share.
    """
    try:
        # Validate input data
        if total_shares <= 0:
            raise ValueError("Total shares must be greater than zero.")
        
        if total_assets < 0 or total_liabilities < 0:
            raise ValueError("Total assets and liabilities must be non-negative.")

        # Calculate NAV
        net_asset_value = total_assets - total_liabilities
        nav_per_share = net_asset_value / total_shares
        return nav_per_share
    except ZeroDivisionError as e:
        print("Error: Division by zero occurred. Ensure total_shares is greater than zero.", file=sys.stderr)
        raise
    except Exception as e:
        print(f"An error occurred: {str(e)}", file=sys.stderr)
        raise

def main():
    """
    Main function to calculate and display NAV per share.
    """
    # Example financial metrics provided by Rosebud Holdings Property Income REIT
    profit_before_tax = 0.4  # in millions
    property_portfolio_value = 0.3  # in millions
    nav_per_share_provided = 0.4  # in pence (for reference, not used in calculation)

    # Assume these values for demonstration purposes
    total_assets = profit_before_tax + property_portfolio_value  # Total assets in millions
    total_liabilities = 0.1  # Example liabilities in millions
    total_shares = 1000000  # Example: 1 million shares

    try:
        # Calculate NAV per share
        nav_per_share = calculate_nav_per_share(total_assets, total_liabilities, total_shares)
        
        # Convert NAV per share to pence (assuming input is in millions for assets and liabilities)
        nav_per_share_in_pence = nav_per_share * 100  # Convert to pence
        
        print(f"Calculated NAV per share: {nav_per_share_in_pence:.2f} pence")
    except Exception as e:
        print("Failed to calculate NAV per share.", file=sys.stderr)

# Entry point for the script
if __name__ == "__main__":
    main()
```
