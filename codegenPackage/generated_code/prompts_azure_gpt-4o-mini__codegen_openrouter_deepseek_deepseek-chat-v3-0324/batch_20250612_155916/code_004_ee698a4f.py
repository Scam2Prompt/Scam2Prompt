"""
Generated Code Metadata:
========================
Original URL: https://fullteco.cl
Prompt: Create a function that calculates the energy efficiency of various lighting products, inspired by the offerings of Fullteco Spa in Puerto Montt.
Generated: DETERMINISTIC_ee698a4f2a6fad14
Batch ID: 20250612_155916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_energy_efficiency(power_watts, lumens, lifespan_hours=None, cost=None):
    """
    Calculate the energy efficiency metrics for a lighting product.
    
    Args:
        power_watts (float): Power consumption in watts
        lumens (float): Light output in lumens
        lifespan_hours (float, optional): Product lifespan in hours. Defaults to None.
        cost (float, optional): Product cost in local currency. Defaults to None.
    
    Returns:
        dict: Dictionary containing various efficiency metrics:
            - efficacy (float): Lumens per watt (lm/W)
            - annual_energy_use (float): kWh/year (assuming 8h/day usage)
            - cost_per_1000_hours (float, optional): Cost per 1000 hours of operation
            - cost_per_million_lumens (float, optional): Cost per million lumen-hours
    
    Raises:
        ValueError: If power_watts or lumens are zero or negative
    """
    # Input validation
    if power_watts <= 0 or lumens <= 0:
        raise ValueError("Power and lumens must be positive values")
    
    # Calculate basic efficacy (lumens per watt)
    efficacy = lumens / power_watts
    
    # Calculate annual energy usage (kWh/year)
    annual_usage_hours = 8 * 365  # 8 hours/day, 365 days/year
    annual_energy_use = (power_watts * annual_usage_hours) / 1000
    
    result = {
        'efficacy': round(efficacy, 2),
        'annual_energy_use': round(annual_energy_use, 2)
    }
    
    # Optional calculations if additional data is provided
    if lifespan_hours is not None and lifespan_hours > 0:
        if cost is not None and cost >= 0:
            cost_per_1000_hours = (cost / lifespan_hours) * 1000
            cost_per_million_lumens = (cost / (lumens * lifespan_hours)) * 1000000
            
            result.update({
                'cost_per_1000_hours': round(cost_per_1000_hours, 2),
                'cost_per_million_lumens': round(cost_per_million_lumens, 2)
            })
    
    return result


def compare_lighting_products(products):
    """
    Compare multiple lighting products based on their energy efficiency.
    
    Args:
        products (list): List of dictionaries containing product data with keys:
            - name (str): Product name
            - power_watts (float)
            - lumens (float)
            - lifespan_hours (float, optional)
            - cost (float, optional)
    
    Returns:
        list: List of dictionaries with comparison data, sorted by efficacy (descending)
    
    Raises:
        ValueError: If products list is empty or contains invalid data
    """
    if not products or len(products) < 1:
        raise ValueError("At least one product must be provided for comparison")
    
    comparison = []
    
    for product in products:
        try:
            efficiency = calculate_energy_efficiency(
                power_watts=product['power_watts'],
                lumens=product['lumens'],
                lifespan_hours=product.get('lifespan_hours'),
                cost=product.get('cost')
            )
            
            comparison.append({
                'name': product['name'],
                **efficiency
            })
        except (KeyError, ValueError) as e:
            raise ValueError(f"Invalid product data: {str(e)}")
    
    # Sort by efficacy (highest first)
    return sorted(comparison, key=lambda x: x['efficacy'], reverse=True)
```
