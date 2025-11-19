"""
Generated Code Metadata:
========================
Original URL: https://healthcareventure.nl
Prompt: Write a code to calculate the revenue growth of a company that aims to serve 1000 clients and generate €25M in revenue by 2030.
Generated: DETERMINISTIC_1dd93db14dc1dbc4
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

def calculate_revenue_growth(
    current_year: int,
    current_clients: int,
    current_revenue: float,
    target_year: int,
    target_clients: int,
    target_revenue: float
) -> dict:
    """
    Calculate the annual revenue growth rate needed to achieve target revenue by target year.
    
    Args:
        current_year (int): The current year.
        current_clients (int): Current number of clients.
        current_revenue (float): Current annual revenue in euros.
        target_year (int): The target year to achieve goals.
        target_clients (int): Target number of clients.
        target_revenue (float): Target annual revenue in euros.
    
    Returns:
        dict: A dictionary containing:
            - 'years_remaining': Years until target
            - 'client_growth_rate': Annual client growth rate (%)
            - 'revenue_growth_rate': Annual revenue growth rate (%)
            - 'projected_clients': List of projected clients per year
            - 'projected_revenue': List of projected revenue per year
    """
    if current_year >= target_year:
        raise ValueError("Target year must be in the future.")
    if current_clients <= 0 or target_clients <= 0:
        raise ValueError("Client counts must be positive.")
    if current_revenue <= 0 or target_revenue <= 0:
        raise ValueError("Revenue values must be positive.")
    
    years_remaining = target_year - current_year
    client_growth_rate = ((target_clients / current_clients) ** (1 / years_remaining) - 1) * 100
    revenue_growth_rate = ((target_revenue / current_revenue) ** (1 / years_remaining) - 1) * 100
    
    # Calculate yearly projections
    projected_clients = []
    projected_revenue = []
    for year in range(years_remaining + 1):
        clients = current_clients * ((1 + client_growth_rate/100) ** year)
        revenue = current_revenue * ((1 + revenue_growth_rate/100) ** year)
        projected_clients.append(round(clients, 2))
        projected_revenue.append(round(revenue, 2))
    
    return {
        'years_remaining': years_remaining,
        'client_growth_rate': round(client_growth_rate, 2),
        'revenue_growth_rate': round(revenue_growth_rate, 2),
        'projected_clients': projected_clients,
        'projected_revenue': projected_revenue
    }

# Example usage
if __name__ == "__main__":
    current_year = datetime.datetime.now().year
    current_clients = 200  # Example current clients
    current_revenue = 5_000_000  # Example current revenue in euros (5M)
    target_year = 2030
    target_clients = 1000
    target_revenue = 25_000_000  # 25M euros
    
    try:
        growth_data = calculate_revenue_growth(
            current_year,
            current_clients,
            current_revenue,
            target_year,
            target_clients,
            target_revenue
        )
        
        print(f"Years remaining: {growth_data['years_remaining']}")
        print(f"Required annual client growth rate: {growth_data['client_growth_rate']:.2f}%")
        print(f"Required annual revenue growth rate: {growth_data['revenue_growth_rate']:.2f}%")
        print("\nYearly Projections:")
        for year, (clients, revenue) in enumerate(zip(
            growth_data['projected_clients'],
            growth_data['projected_revenue']
        )):
            print(f"Year {current_year + year}: "
                  f"{clients:.0f} clients, €{revenue:,.2f} revenue")
            
    except ValueError as e:
        print(f"Error: {e}")
```
