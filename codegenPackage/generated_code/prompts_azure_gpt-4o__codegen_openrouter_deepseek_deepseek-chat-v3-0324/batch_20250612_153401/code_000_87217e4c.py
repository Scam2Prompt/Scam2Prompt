"""
Generated Code Metadata:
========================
Original URL: https://libointeriors.net
Prompt: Write Python code to calculate the cost of installing raised access flooring in a data center, using specifications for calcium sulphate panels and accessories like panel lifters and airflow panels.
Generated: DETERMINISTIC_87217e4c6552ca2a
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This module calculates the cost of installing raised access flooring in a data center.
It supports calcium sulphate panels and accessories like panel lifters and airflow panels.
"""

class RaisedFloorCostCalculator:
    """
    A class to calculate the total cost of raised access flooring installation.
    """
    
    def __init__(self):
        """
        Initialize the calculator with default prices and specifications.
        """
        # Base prices (per square meter)
        self.panel_price = 150.00  # Calcium sulphate panel price per m²
        self.pedestal_price = 12.00  # Price per pedestal
        self.stringer_price = 8.00  # Price per meter of stringer
        
        # Accessory prices
        self.panel_lifter_price = 250.00  # Price per panel lifter
        self.airflow_panel_price = 200.00  # Price per airflow panel
        
        # Installation rates
        self.installation_rate = 35.00  # Installation cost per m²
        
        # Default specifications
        self.panel_size = 0.6  # Panel size in meters (assuming 600x600mm)
        self.pedestals_per_panel = 4  # Number of pedestals per panel
        self.stringers_per_panel = 2  # Meters of stringer per panel
    
    def calculate_materials(self, area):
        """
        Calculate the required materials for the given floor area.
        
        Args:
            area (float): Total floor area in square meters.
            
        Returns:
            dict: Dictionary containing quantities of materials needed.
        """
        if area <= 0:
            raise ValueError("Area must be a positive number.")
            
        panels = area / (self.panel_size ** 2)
        pedestals = panels * self.pedestals_per_panel
        stringers = panels * self.stringers_per_panel
        
        return {
            'panels': round(panels),
            'pedestals': round(pedestals),
            'stringers': round(stringers, 1)
        }
    
    def calculate_cost(self, area, panel_lifters=0, airflow_panels=0):
        """
        Calculate the total cost for the raised floor installation.
        
        Args:
            area (float): Total floor area in square meters.
            panel_lifters (int): Number of panel lifters needed.
            airflow_panels (int): Number of airflow panels needed.
            
        Returns:
            dict: Dictionary containing cost breakdown and total.
        """
        try:
            materials = self.calculate_materials(area)
            
            # Material costs
            panel_cost = materials['panels'] * (self.panel_size ** 2) * self.panel_price
            pedestal_cost = materials['pedestals'] * self.pedestal_price
            stringer_cost = materials['stringers'] * self.stringer_price
            
            # Accessory costs
            lifter_cost = panel_lifters * self.panel_lifter_price
            airflow_cost = airflow_panels * self.airflow_panel_price
            
            # Installation cost
            installation_cost = area * self.installation_rate
            
            # Total cost
            total_cost = (
                panel_cost + pedestal_cost + stringer_cost +
                lifter_cost + airflow_cost + installation_cost
            )
            
            return {
                'materials': {
                    'panels': round(panel_cost, 2),
                    'pedestals': round(pedestal_cost, 2),
                    'stringers': round(stringer_cost, 2),
                    'panel_lifters': round(lifter_cost, 2),
                    'airflow_panels': round(airflow_cost, 2)
                },
                'installation': round(installation_cost, 2),
                'total': round(total_cost, 2)
            }
            
        except ValueError as e:
            return {'error': str(e)}
    
    def update_prices(self, **kwargs):
        """
        Update the pricing parameters.
        
        Args:
            **kwargs: Key-value pairs of parameters to update.
                     Valid keys: panel_price, pedestal_price, stringer_price,
                                panel_lifter_price, airflow_panel_price,
                                installation_rate
        """
        valid_keys = {
            'panel_price', 'pedestal_price', 'stringer_price',
            'panel_lifter_price', 'airflow_panel_price',
            'installation_rate'
        }
        
        for key, value in kwargs.items():
            if key in valid_keys:
                setattr(self, key, value)
            else:
                raise ValueError(f"Invalid price parameter: {key}")


# Example usage
if __name__ == "__main__":
    calculator = RaisedFloorCostCalculator()
    
    # Calculate for a 100m² data center with 2 panel lifters and 5 airflow panels
    result = calculator.calculate_cost(100, panel_lifters=2, airflow_panels=5)
    
    print("Cost Breakdown:")
    print(f"Materials: {result['materials']}")
    print(f"Installation: ${result['installation']}")
    print(f"Total Cost: ${result['total']}")
```
