"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dubaiskycargo.com
Prompt: Provide code to calculate the carbon footprint of shipments handled by Dubai SkyCargo's logistics services, including private and cargo aircraft charters.
Generated: DETERMINISTIC_f03f27b9c075135b
Batch ID: 20250612_154319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class CarbonFootprintCalculator:
    """
    A class to calculate the carbon footprint of shipments handled by Dubai SkyCargo's logistics services.
    
    Attributes:
        aircraft_data (pd.DataFrame): DataFrame containing aircraft types and their emissions factors.
    """
    
    def __init__(self, aircraft_data: pd.DataFrame):
        """
        Initializes the CarbonFootprintCalculator with aircraft emissions data.
        
        Args:
            aircraft_data (pd.DataFrame): DataFrame containing aircraft types and their respective emissions factors.
        """
        self.aircraft_data = aircraft_data

    def calculate_footprint(self, shipment_weight: float, aircraft_type: str, distance: float) -> float:
        """
        Calculate the carbon footprint of a shipment.
        
        Args:
            shipment_weight (float): The weight of the shipment in kilograms.
            aircraft_type (str): The type of aircraft used for the shipment.
            distance (float): The distance traveled in kilometers.
        
        Returns:
            float: The carbon footprint in kilograms of CO2 emitted.
        
        Raises:
            ValueError: If the aircraft type is not found in the aircraft data or if inputs are invalid.
        """
        # Validate inputs
        if shipment_weight <= 0 or distance <= 0:
            raise ValueError("Shipment weight and distance must be greater than zero.")
        
        # Check if aircraft type is in the emissions data
        if aircraft_type not in self.aircraft_data['aircraft_type'].values:
            raise ValueError(f"Aircraft type '{aircraft_type}' not found in emissions data.")

        # Get the emissions factor for the specified aircraft type
        emissions_factor = self.aircraft_data.loc[self.aircraft_data['aircraft_type'] == aircraft_type, 'emissions_factor'].values[0]

        # Calculate carbon footprint
        carbon_footprint = shipment_weight * distance * emissions_factor

        return carbon_footprint

def main():
    # Sample aircraft emissions data
    aircraft_data = pd.DataFrame({
        'aircraft_type': ['Boeing 747', 'Airbus A380', 'Boeing 737'],
        'emissions_factor': [0.115, 0.1, 0.154]  # kg CO2 per kg cargo per km
    })

    # Create a calculator instance
    calculator = CarbonFootprintCalculator(aircraft_data)

    # Example shipment data
    shipment_weight = 1000  # kg
    aircraft_type = 'Boeing 747'
    distance = 2000  # km

    try:
        # Calculate the carbon footprint
        footprint = calculator.calculate_footprint(shipment_weight, aircraft_type, distance)
        print(f"Carbon Footprint for shipment: {footprint:.2f} kg CO2")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
