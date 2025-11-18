"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-crest.com
Prompt: Write Python code to simulate asset allocation strategies for beginners, incorporating stocks, bonds, and real estate, as described on Immediate Crest V2.
Generated: DETERMINISTIC_fc99abf63bf35d78
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

def simulate_asset_allocation(initial_investment, years, risk_profile):
    """
    Simulates asset allocation across stocks, bonds, and real estate based on a user's risk profile.
    
    Parameters:
    - initial_investment (int | float): The initial amount of investment.
    - years (int): Number of years to simulate.
    - risk_profile (str): Risk tolerance level ('low', 'medium', or 'high').
    
    Returns:
    - dict: Simulated portfolio values after the specified number of years.
    """
    
    # Define allocation percentages based on risk profile
    allocation = {
        'low': {'stocks': 0.30, 'bonds': 0.50, 'real_estate': 0.20},
        'medium': {'stocks': 0.50, 'bonds': 0.30, 'real_estate': 0.20},
        'high': {'stocks': 0.70, 'bonds': 0.10, 'real_estate': 0.20}
    }
    
    if risk_profile not in allocation:
        raise ValueError("Invalid risk profile. Choose from 'low', 'medium', or 'high'.")
    
    # Historical average yearly returns for assets (approximation)
    asset_returns = {
        'stocks': (0.07, 0.15),        # Avg return: 7%, Std Dev: 15%
        'bonds': (0.03, 0.05),         # Avg return: 3%, Std Dev: 5%
        'real_estate': (0.05, 0.10)    # Avg return: 5%, Std Dev: 10%
    }
    
    # Portfolio allocation percentages
    allocation_percentages = allocation[risk_profile]
    
    # Initialize portfolio values for each asset
    portfolio = {asset: initial_investment * percent for asset, percent in allocation_percentages.items()}
    
    # Simulate growth over the specified number of years
    for year in range(1, years + 1):
        for asset in portfolio.keys():
            avg_return, std_dev = asset_returns[asset]
            # Simulate yearly returns using a normal distribution
            yearly_return = random.gauss(avg_return, std_dev)
            portfolio[asset] += portfolio[asset] * yearly_return
    
    # Calculate total portfolio value
    total_value = sum(portfolio.values())
    
    # Add total value to the portfolio for reporting
    portfolio['total'] = total_value
    
    return portfolio


if __name__ == "__main__":
    try:
        # User-defined parameters
        initial_investment = 10000  # Example: $10,000
        years = 10                  # Example: 10 years
        risk_profile = 'medium'     # Example: 'medium' risk tolerance
        
        # Simulate asset allocation
        results = simulate_asset_allocation(initial_investment, years, risk_profile)
        
        # Display results
        print(f"Simulated portfolio after {years} years:")
        for asset, value in results.items():
            print(f"  {asset.capitalize()}: ${value:,.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
