"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opcsas.com
Prompt: Develop a script to calculate the cost of transporting liquid cargo across various cities in Colombia, taking into account OPC S.A.S.'s coverage and fleet capabilities.
Generated: DETERMINISTIC_d4967d6d84e8e782
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class CargoTransportCostCalculator:
    """
    A class to calculate the cost of transporting liquid cargo across various cities based on
    OPC S.A.S. coverage and fleet capabilities.
    """

    def __init__(self):
        # Initialize cities and fleet details
        self.coverage = {
            "Bogotá": {"distance_km": 500, "cost_per_km": 1500},
            "Medellín": {"distance_km": 400, "cost_per_km": 1400},
            "Cali": {"distance_km": 600, "cost_per_km": 1600},
            "Barranquilla": {"distance_km": 1000, "cost_per_km": 1800},
            "Cartagena": {"distance_km": 900, "cost_per_km": 1700}
        }
        self.fleet = {
            "small_tanker": {"capacity_liters": 10000, "base_cost": 50000},
            "medium_tanker": {"capacity_liters": 25000, "base_cost": 120000},
            "large_tanker": {"capacity_liters": 50000, "base_cost": 200000}
        }

    def calculate_transport_cost(self, city, cargo_volume_liters, tanker_type):
        """
        Calculate the transport cost for a given city, cargo volume, and tanker type.

        :param city: The destination city.
        :param cargo_volume_liters: Total cargo volume in liters.
        :param tanker_type: Type of tanker (small_tanker, medium_tanker, large_tanker).
        :return: Total transport cost or error message.
        """
        try:
            # Validate inputs
            if city not in self.coverage:
                raise ValueError(f"City '{city}' is not covered by OPC S.A.S.")
            if tanker_type not in self.fleet:
                raise ValueError(f"Tanker type '{tanker_type}' is not available in the fleet.")
            if cargo_volume_liters <= 0:
                raise ValueError("Cargo volume must be greater than zero.")
            
            # Fetch city and tanker details
            city_info = self.coverage[city]
            tanker_info = self.fleet[tanker_type]
            
            # Validate tanker capacity
            if cargo_volume_liters > tanker_info["capacity_liters"]:
                raise ValueError(f"Cargo volume exceeds the capacity of the chosen tanker ({tanker_info['capacity_liters']} liters).")
            
            # Calculate cost
            distance_cost = city_info["distance_km"] * city_info["cost_per_km"]
            total_cost = distance_cost + tanker_info["base_cost"]
            
            return {
                "city": city,
                "tanker_type": tanker_type,
                "cargo_volume_liters": cargo_volume_liters,
                "distance_cost": distance_cost,
                "base_tanker_cost": tanker_info["base_cost"],
                "total_transport_cost": total_cost
            }
        
        except ValueError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": f"An unexpected error occurred: {str(e)}"}

if __name__ == "__main__":
    # Example usage
    calculator = CargoTransportCostCalculator()
    
    # Input parameters
    city = "Bogotá"
    cargo_volume_liters = 8000
    tanker_type = "small_tanker"
    
    # Calculate transport cost
    result = calculator.calculate_transport_cost(city, cargo_volume_liters, tanker_type)
    
    # Output result
    print(json.dumps(result, indent=4))
```
