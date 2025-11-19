"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wemix-shoebill.pages.dev
Prompt: Generate a script to calculate the net APY and borrow limit for a user on the Shoebill Finance platform.
Generated: DETERMINISTIC_cd390ba1261babe8
Batch ID: 20250612_161042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def calculate_net_apy_and_borrow_limit(user_data):
    """
    Function to calculate net APY and borrow limit for a user on Shoebill Finance platform.

    Parameters:
        user_data (dict): User data containing information about assets, liabilities, and rates.

    Returns:
        dict: A dictionary containing net APY and borrow limit.
    """
    try:
        # Validate input data
        if not isinstance(user_data, dict):
            raise ValueError("Input user_data must be a dictionary.")

        # Extract required data
        assets = user_data.get("assets", [])
        liabilities = user_data.get("liabilities", [])
        
        # Validate extracted data
        if not isinstance(assets, list) or not isinstance(liabilities, list):
            raise ValueError("Assets and liabilities must be lists.")
        
        net_apy = 0.0
        total_borrow_limit = 0.0

        # Calculate net APY from assets
        for asset in assets:
            # Validate asset data
            if not all(k in asset for k in ("value", "apy", "collateral_factor")):
                raise ValueError(f"Asset data is missing required fields: {asset}")
            try:
                asset_value = float(asset["value"])
                asset_apy = float(asset["apy"])
                collateral_factor = float(asset["collateral_factor"])
            except ValueError:
                raise ValueError(f"Invalid numeric values in asset data: {asset}")
            
            net_apy += asset_value * (asset_apy / 100)
            total_borrow_limit += asset_value * (collateral_factor / 100)

        # Subtract liabilities' APY
        for liability in liabilities:
            # Validate liability data
            if not all(k in liability for k in ("value", "apy")):
                raise ValueError(f"Liability data is missing required fields: {liability}")
            try:
                liability_value = float(liability["value"])
                liability_apy = float(liability["apy"])
            except ValueError:
                raise ValueError(f"Invalid numeric values in liability data: {liability}")
            
            net_apy -= liability_value * (liability_apy / 100)

        # Return results in a structured format
        return {
            "net_apy": net_apy,
            "borrow_limit": total_borrow_limit
        }
    except Exception as e:
        # Log and propagate errors
        print(f"Error calculating net APY and borrow limit: {e}")
        raise

# Example usage
if __name__ == "__main__":
    # Example user data
    user_data = {
        "assets": [
            {"value": 1000, "apy": 5, "collateral_factor": 50},
            {"value": 2000, "apy": 3, "collateral_factor": 60}
        ],
        "liabilities": [
            {"value": 500, "apy": 7},
            {"value": 300, "apy": 6}
        ]
    }

    try:
        # Calculate net APY and borrow limit
        results = calculate_net_apy_and_borrow_limit(user_data)
        # Output results
        print(json.dumps(results, indent=4))
    except Exception as e:
        print(f"Failed to calculate: {e}")
```
