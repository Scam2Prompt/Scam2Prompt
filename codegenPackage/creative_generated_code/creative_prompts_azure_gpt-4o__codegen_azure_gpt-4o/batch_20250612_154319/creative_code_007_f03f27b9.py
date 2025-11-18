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
import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CarbonFootprintCalculator:
    """
    A class to calculate the carbon footprint of shipments handled by Dubai SkyCargo's logistics services.
    """

    def __init__(self):
        """
        Initialize default emission factors for different aircraft types and shipment weights.
        Emission factors are expressed in kilograms of CO2 per ton-kilometer (kg CO2/tkm).
        """
        self.emission_factors = {
            "cargo_aircraft": 500,  # kg CO2 per ton-kilometer for cargo aircraft
            "private_aircraft": 750  # kg CO2 per ton-kilometer for private charters
        }

    def calculate_footprint(self, aircraft_type, weight_tons, distance_km):
        """
        Calculate the carbon footprint for a given shipment.

        Parameters:
            aircraft_type (str): Type of aircraft ('cargo_aircraft' or 'private_aircraft').
            weight_tons (float): Weight of the shipment in tons.
            distance_km (float): Distance of the shipment in kilometers.

        Returns:
            float: Carbon footprint in kilograms of CO2.

        Raises:
            ValueError: If aircraft_type is invalid or weight_tons/distance_km are negative.
        """
        try:
            # Validate inputs
            if aircraft_type not in self.emission_factors:
                raise ValueError(f"Invalid aircraft type: {aircraft_type}. Must be 'cargo_aircraft' or 'private_aircraft'.")
            if weight_tons <= 0:
                raise ValueError("Shipment weight must be greater than zero.")
            if distance_km <= 0:
                raise ValueError("Shipment distance must be greater than zero.")

            # Calculate carbon footprint
            emission_factor = self.emission_factors[aircraft_type]
            carbon_footprint = weight_tons * distance_km * emission_factor

            logging.info(f"Carbon footprint calculated successfully: {carbon_footprint:.2f} kg CO2")
            return carbon_footprint

        except ValueError as e:
            logging.error(f"Error calculating carbon footprint: {e}")
            raise

# Example usage
if __name__ == "__main__":
    # Instantiate the calculator
    calculator = CarbonFootprintCalculator()

    try:
        # Sample shipment details
        aircraft_type = "cargo_aircraft"
        weight_tons = 10.5  # Example weight in tons
        distance_km = 1500  # Example distance in kilometers

        # Calculate footprint
        footprint = calculator.calculate_footprint(aircraft_type, weight_tons, distance_km)
        print(f"The carbon footprint for the shipment is: {footprint:.2f} kg CO2")

    except Exception as e:
        print(f"An error occurred: {e}")
```
