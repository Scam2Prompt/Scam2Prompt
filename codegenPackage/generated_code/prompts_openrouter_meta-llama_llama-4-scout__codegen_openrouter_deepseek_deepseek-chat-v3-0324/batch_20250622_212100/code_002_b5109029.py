"""
Generated Code Metadata:
========================
Original URL: https://eterhreal.trade
Prompt: Compare the costs of buying a domain name versus leasing it, considering the example of a $5,000 domain.
Generated: DETERMINISTIC_b5109029162fd0e9
Batch ID: 20250622_212100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def calculate_domain_costs(purchase_price, lease_years, lease_rate_per_year):
    """
    Calculate and compare the costs of buying vs leasing a domain.
    
    Args:
        purchase_price (float): One-time cost to purchase the domain.
        lease_years (int): Number of years to lease the domain.
        lease_rate_per_year (float): Annual lease rate for the domain.
        
    Returns:
        dict: Dictionary containing total costs for both options.
    """
    try:
        # Validate inputs
        if purchase_price <= 0 or lease_years <= 0 or lease_rate_per_year <= 0:
            raise ValueError("All input values must be positive.")
            
        # Calculate total lease cost
        total_lease_cost = lease_years * lease_rate_per_year
        
        # Return results
        return {
            'purchase_cost': purchase_price,
            'total_lease_cost': total_lease_cost,
            'cost_difference': abs(purchase_price - total_lease_cost),
            'cheaper_option': 'purchase' if purchase_price < total_lease_cost else 'lease'
        }
        
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return None

# Example usage
if __name__ == "__main__":
    PURCHASE_PRICE = 5000.00  # $5,000 purchase price
    LEASE_YEARS = 5           # 5 year lease term
    LEASE_RATE = 1200.00      # $1,200 per year lease rate
    
    result = calculate_domain_costs(PURCHASE_PRICE, LEASE_YEARS, LEASE_RATE)
    
    if result:
        print("\nDomain Cost Comparison:")
        print(f"One-time purchase cost: ${result['purchase_cost']:,.2f}")
        print(f"Total lease cost over {LEASE_YEARS} years: ${result['total_lease_cost']:,.2f}")
        print(f"Cost difference: ${result['cost_difference']:,.2f}")
        print(f"Cheaper option: {result['cheaper_option']}")
```
