"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://propsfundedtrader.com
Prompt: Write Python code to automate the calculation of a 10% monthly ROI for a $100,000 funded trading account, factoring in profit splits of 30% for the service provider, 10% for the prop firm, and 60% for the account owner.
Generated: DETERMINISTIC_c3a298f85045cbf1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to calculate monthly ROI and profit splits for a funded trading account

# Constants
INITIAL_ACCOUNT_BALANCE = 100000  # Initial funded trading account balance in USD
MONTHLY_ROI_PERCENTAGE = 10       # Monthly ROI percentage
SERVICE_PROVIDER_SPLIT = 0.30     # Profit split for the service provider
PROP_FIRM_SPLIT = 0.10            # Profit split for the prop firm
ACCOUNT_OWNER_SPLIT = 0.60        # Profit split for the account owner

def calculate_monthly_roi(account_balance, roi_percentage):
    """
    Calculate the monthly ROI for the account balance.

    Parameters:
        account_balance (float): The current account balance.
        roi_percentage (float): ROI percentage to calculate.

    Returns:
        float: ROI amount for the month.
    """
    return account_balance * (roi_percentage / 100)

def calculate_profit_splits(total_roi, service_split, prop_split, owner_split):
    """
    Calculate profit splits for service provider, prop firm, and account owner.

    Parameters:
        total_roi (float): Total ROI calculated for the month.
        service_split (float): Percentage for the service provider.
        prop_split (float): Percentage for the prop firm.
        owner_split (float): Percentage for the account owner.

    Returns:
        dict: Dictionary containing the profit splits.
    """
    return {
        "service_provider": total_roi * service_split,
        "prop_firm": total_roi * prop_split,
        "account_owner": total_roi * owner_split
    }

def main():
    """
    Main function to automate ROI calculation and profit splits.
    """
    try:
        # Step 1: Calculate Monthly ROI
        monthly_roi = calculate_monthly_roi(INITIAL_ACCOUNT_BALANCE, MONTHLY_ROI_PERCENTAGE)

        # Step 2: Calculate Profit Splits
        profit_splits = calculate_profit_splits(
            monthly_roi,
            SERVICE_PROVIDER_SPLIT,
            PROP_FIRM_SPLIT,
            ACCOUNT_OWNER_SPLIT
        )

        # Step 3: Display the results
        print(f"Initial Account Balance: ${INITIAL_ACCOUNT_BALANCE:,.2f}")
        print(f"Monthly ROI (%): {MONTHLY_ROI_PERCENTAGE}%")
        print(f"Monthly ROI Amount: ${monthly_roi:,.2f}\n")
        
        print("Profit Splits:")
        print(f"  Service Provider: ${profit_splits['service_provider']:,.2f}")
        print(f"  Prop Firm:        ${profit_splits['prop_firm']:,.2f}")
        print(f"  Account Owner:    ${profit_splits['account_owner']:,.2f}")

    except Exception as e:
        # Proper error handling in case of unexpected issues
        print(f"An error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
