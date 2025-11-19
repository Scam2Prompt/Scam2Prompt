"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-token.pages.dev
Prompt: Create a Python script to calculate potential returns for DOGE20 tokens based on presale prices and projected token price increases, as shown in the site's returns calculator.
Generated: DETERMINISTIC_64cd976bf5f85c3c
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_returns(
    initial_investment: float,
    presale_price: float,
    projected_price: float,
    vesting_period: int = 12,
    vesting_cliff: int = 3,
    vesting_unlock_percent: float = 8.33
) -> dict:
    """
    Calculate potential returns for DOGE20 tokens based on presale and projected prices.
    
    Args:
        initial_investment (float): Amount invested in USD
        presale_price (float): Price per token during presale in USD
        projected_price (float): Expected future price per token in USD
        vesting_period (int): Total vesting period in months (default: 12)
        vesting_cliff (int): Cliff period in months before vesting starts (default: 3)
        vesting_unlock_percent (float): Percentage of tokens unlocked each month after cliff (default: 8.33)
    
    Returns:
        dict: Dictionary containing calculated returns and vesting schedule
    """
    
    try:
        # Validate inputs
        if any(arg <= 0 for arg in [initial_investment, presale_price, projected_price]):
            raise ValueError("Investment amounts and prices must be positive")
        if vesting_period <= 0 or vesting_cliff < 0:
            raise ValueError("Vesting period and cliff must be positive values")
        if vesting_unlock_percent <= 0 or vesting_unlock_percent > 100:
            raise ValueError("Vesting unlock percentage must be between 0 and 100")
        
        # Calculate initial token amount
        tokens_purchased = initial_investment / presale_price
        
        # Calculate potential value at projected price
        potential_value = tokens_purchased * projected_price
        
        # Calculate ROI
        roi = ((potential_value - initial_investment) / initial_investment) * 100
        
        # Generate vesting schedule
        vesting_schedule = []
        total_unlocked = 0.0
        
        for month in range(1, vesting_period + 1):
            if month <= vesting_cliff:
                unlocked = 0.0
            else:
                unlocked = min(
                    tokens_purchased * (vesting_unlock_percent / 100),
                    tokens_purchased - total_unlocked
                )
            
            total_unlocked += unlocked
            value_unlocked = unlocked * projected_price
            vesting_schedule.append({
                'month': month,
                'tokens_unlocked': unlocked,
                'value_unlocked': value_unlocked,
                'cumulative_tokens': total_unlocked,
                'cumulative_value': total_unlocked * projected_price
            })
        
        return {
            'initial_investment': initial_investment,
            'tokens_purchased': tokens_purchased,
            'potential_value': potential_value,
            'roi_percent': roi,
            'vesting_schedule': vesting_schedule,
            'presale_price': presale_price,
            'projected_price': projected_price
        }
        
    except Exception as e:
        raise ValueError(f"Error calculating returns: {str(e)}")

def format_currency(value: float) -> str:
    """Format a numeric value as USD currency string."""
    return f"${value:,.2f}"

def display_results(results: dict):
    """Display the calculation results in a user-friendly format."""
    try:
        print("\nDOGE20 Investment Returns Calculator")
        print("=" * 40)
        print(f"Initial Investment: {format_currency(results['initial_investment'])}")
        print(f"Presale Price: {format_currency(results['presale_price'])} per token")
        print(f"Projected Price: {format_currency(results['projected_price'])} per token")
        print(f"\nTokens Purchased: {results['tokens_purchased']:,.2f}")
        print(f"Potential Value: {format_currency(results['potential_value'])}")
        print(f"ROI: {results['roi_percent']:,.2f}%")
        
        print("\nVesting Schedule:")
        print("-" * 40)
        print("Month | Tokens Unlocked | Value Unlocked | Cumulative Tokens | Cumulative Value")
        print("-" * 40)
        
        for month in results['vesting_schedule']:
            print(
                f"{month['month']:5} | "
                f"{month['tokens_unlocked']:15,.2f} | "
                f"{format_currency(month['value_unlocked']):15} | "
                f"{month['cumulative_tokens']:17,.2f} | "
                f"{format_currency(month['cumulative_value'])}"
            )
            
    except Exception as e:
        print(f"Error displaying results: {str(e)}")

def main():
    """Main function to run the calculator interactively."""
    print("DOGE20 Returns Calculator")
    print("=" * 40)
    
    try:
        initial_investment = float(input("Enter initial investment (USD): "))
        presale_price = float(input("Enter presale price per token (USD): "))
        projected_price = float(input("Enter projected future price per token (USD): "))
        
        # Optional advanced inputs
        try:
            vesting_period = int(input("Enter vesting period in months (default 12): ") or 12)
            vesting_cliff = int(input("Enter vesting cliff in months (default 3): ") or 3)
            vesting_unlock = float(input("Enter monthly vesting unlock % (default 8.33): ") or 8.33)
        except ValueError:
            print("Using default vesting parameters")
            vesting_period = 12
            vesting_cliff = 3
            vesting_unlock = 8.33
        
        results = calculate_returns(
            initial_investment,
            presale_price,
            projected_price,
            vesting_period,
            vesting_cliff,
            vesting_unlock
        )
        
        display_results(results)
        
    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
