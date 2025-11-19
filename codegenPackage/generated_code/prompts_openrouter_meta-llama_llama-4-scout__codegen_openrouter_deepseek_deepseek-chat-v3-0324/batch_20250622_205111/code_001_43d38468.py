"""
Generated Code Metadata:
========================
Original URL: https://tokenfi-teal.vercel.app
Prompt: Compare the APY for staking TOKEN tokens on Ethereum versus BNB Chain for a 1-year duration, using the provided rates (≈ 24.24%* for Ethereum and ≈ 19.55%* for BNB Chain).
Generated: DETERMINISTIC_43d384684f4baf64
Batch ID: 20250622_205111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_apy_comparison(initial_investment: float, eth_apy: float, bnb_apy: float, duration_years: float = 1.0) -> dict:
    """
    Calculate and compare the APY returns for staking on Ethereum vs BNB Chain.
    
    Args:
        initial_investment (float): Initial investment amount in TOKEN tokens
        eth_apy (float): APY percentage for Ethereum (e.g., 24.24)
        bnb_apy (float): APY percentage for BNB Chain (e.g., 19.55)
        duration_years (float): Duration in years (default: 1.0)
    
    Returns:
        dict: Dictionary containing calculated returns and comparison data
    """
    try:
        # Validate inputs
        if initial_investment <= 0:
            raise ValueError("Initial investment must be positive")
        if eth_apy <= 0 or bnb_apy <= 0:
            raise ValueError("APY rates must be positive")
        if duration_years <= 0:
            raise ValueError("Duration must be positive")
        
        # Calculate returns
        eth_return = initial_investment * (1 + eth_apy/100) ** duration_years
        bnb_return = initial_investment * (1 + bnb_apy/100) ** duration_years
        
        # Calculate difference
        difference = eth_return - bnb_return
        percentage_diff = (difference / bnb_return) * 100
        
        return {
            'initial_investment': initial_investment,
            'duration_years': duration_years,
            'ethereum': {
                'apy': eth_apy,
                'final_amount': eth_return,
                'profit': eth_return - initial_investment
            },
            'bnb_chain': {
                'apy': bnb_apy,
                'final_amount': bnb_return,
                'profit': bnb_return - initial_investment
            },
            'comparison': {
                'absolute_difference': difference,
                'percentage_difference': percentage_diff,
                'better_chain': 'Ethereum' if difference > 0 else 'BNB Chain'
            }
        }
        
    except ValueError as ve:
        return {'error': str(ve)}
    except Exception as e:
        return {'error': f"An unexpected error occurred: {str(e)}"}

# Example usage
if __name__ == "__main__":
    # Input parameters
    initial_amount = 1000.0  # Example: 1000 TOKEN tokens
    eth_rate = 24.24
    bnb_rate = 19.55
    duration = 1.0  # 1 year
    
    # Calculate and print results
    result = calculate_apy_comparison(initial_amount, eth_rate, bnb_rate, duration)
    
    if 'error' in result:
        print(f"Error: {result['error']}")
    else:
        print(f"APY Comparison for {initial_amount} TOKEN over {duration} year(s):")
        print(f"Ethereum ({result['ethereum']['apy']}% APY):")
        print(f"  Final Amount: {result['ethereum']['final_amount']:.2f} TOKEN")
        print(f"  Profit: {result['ethereum']['profit']:.2f} TOKEN")
        print(f"BNB Chain ({result['bnb_chain']['apy']}% APY):")
        print(f"  Final Amount: {result['bnb_chain']['final_amount']:.2f} TOKEN")
        print(f"  Profit: {result['bnb_chain']['profit']:.2f} TOKEN")
        print("\nComparison:")
        print(f"Ethereum yields {result['comparison']['absolute_difference']:.2f} TOKEN more")
        print(f"which is {result['comparison']['percentage_difference']:.2f}% higher")
        print(f"Better choice: {result['comparison']['better_chain']}")
```
