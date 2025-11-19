"""
Generated Code Metadata:
========================
Original URL: https://propsfundedtrader.com
Prompt: Write Python code to automate the calculation of a 10% monthly ROI for a $100,000 funded trading account, factoring in profit splits of 30% for the service provider, 10% for the prop firm, and 60% for the account owner.
Generated: DETERMINISTIC_c3a298f85045cbf1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_monthly_roi(
    initial_capital: float,
    monthly_roi_percentage: float,
    profit_split_provider: float,
    profit_split_firm: float,
    profit_split_owner: float,
    months: int
) -> dict:
    """
    Calculate the monthly ROI for a funded trading account, factoring in profit splits.

    Args:
        initial_capital (float): Initial capital in the account.
        monthly_roi_percentage (float): Expected monthly ROI as a percentage.
        profit_split_provider (float): Profit split for the service provider (as a decimal).
        profit_split_firm (float): Profit split for the prop firm (as a decimal).
        profit_split_owner (float): Profit split for the account owner (as a decimal).
        months (int): Number of months to calculate.

    Returns:
        dict: A dictionary containing monthly balances and profit distributions.
    """
    
    # Validate input parameters
    if not all(isinstance(arg, (int, float)) for arg in [
        initial_capital, monthly_roi_percentage,
        profit_split_provider, profit_split_firm, profit_split_owner
    ]):
        raise ValueError("All numerical parameters must be integers or floats.")
    
    if not isinstance(months, int) or months <= 0:
        raise ValueError("Months must be a positive integer.")
    
    if not (0 <= monthly_roi_percentage <= 100):
        raise ValueError("Monthly ROI percentage must be between 0 and 100.")
    
    total_split = profit_split_provider + profit_split_firm + profit_split_owner
    if not (0.99 <= total_split <= 1.01):  # Allow for minor floating point rounding
        raise ValueError("Profit splits must sum to 1 (100%).")
    
    # Initialize results
    results = {
        'initial_capital': initial_capital,
        'monthly_roi_percentage': monthly_roi_percentage,
        'profit_splits': {
            'provider': profit_split_provider,
            'firm': profit_split_firm,
            'owner': profit_split_owner
        },
        'months': []
    }
    
    current_balance = initial_capital
    
    for month in range(1, months + 1):
        # Calculate monthly profit
        monthly_profit = current_balance * (monthly_roi_percentage / 100)
        
        # Calculate profit distributions
        provider_share = monthly_profit * profit_split_provider
        firm_share = monthly_profit * profit_split_firm
        owner_share = monthly_profit * profit_split_owner
        
        # Update balance (owner's share is reinvested)
        current_balance += owner_share
        
        # Record monthly results
        results['months'].append({
            'month': month,
            'starting_balance': current_balance - owner_share,
            'monthly_profit': monthly_profit,
            'profit_distribution': {
                'provider': provider_share,
                'firm': firm_share,
                'owner': owner_share
            },
            'ending_balance': current_balance
        })
    
    return results


def format_results(results: dict) -> None:
    """
    Format and print the ROI calculation results in a human-readable way.
    
    Args:
        results (dict): The results dictionary from calculate_monthly_roi.
    """
    print(f"\nInitial Capital: ${results['initial_capital']:,.2f}")
    print(f"Monthly ROI: {results['monthly_roi_percentage']}%")
    print("Profit Splits:")
    print(f"  - Service Provider: {results['profit_splits']['provider']*100:.0f}%")
    print(f"  - Prop Firm: {results['profit_splits']['firm']*100:.0f}%")
    print(f"  - Account Owner: {results['profit_splits']['owner']*100:.0f}%")
    print("\nMonthly Breakdown:")
    
    for month_data in results['months']:
        print(f"\nMonth {month_data['month']}:")
        print(f"  Starting Balance: ${month_data['starting_balance']:,.2f}")
        print(f"  Monthly Profit: ${month_data['monthly_profit']:,.2f}")
        print("  Profit Distribution:")
        print(f"    - Provider: ${month_data['profit_distribution']['provider']:,.2f}")
        print(f"    - Firm: ${month_data['profit_distribution']['firm']:,.2f}")
        print(f"    - Owner: ${month_data['profit_distribution']['owner']:,.2f}")
        print(f"  Ending Balance: ${month_data['ending_balance']:,.2f}")


if __name__ == "__main__":
    try:
        # Configuration
        INITIAL_CAPITAL = 100000.00
        MONTHLY_ROI = 10.0  # 10%
        PROFIT_SPLIT_PROVIDER = 0.30  # 30%
        PROFIT_SPLIT_FIRM = 0.10  # 10%
        PROFIT_SPLIT_OWNER = 0.60  # 60%
        MONTHS = 12  # 1 year
        
        # Calculate ROI
        roi_results = calculate_monthly_roi(
            initial_capital=INITIAL_CAPITAL,
            monthly_roi_percentage=MONTHLY_ROI,
            profit_split_provider=PROFIT_SPLIT_PROVIDER,
            profit_split_firm=PROFIT_SPLIT_FIRM,
            profit_split_owner=PROFIT_SPLIT_OWNER,
            months=MONTHS
        )
        
        # Display results
        format_results(roi_results)
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
