"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.somosfortic.es
Prompt: Write a program to simulate the environmental impact of using Fortic's concrete beams versus traditional wood beams in construction projects.
Generated: DETERMINISTIC_c56c00a233cdf70c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class Beam:
    """
    A class to represent a construction beam and calculate its environmental impact.
    """
    def __init__(self, material: str, production_emission: float, lifespan_years: int):
        """
        Initialize a construction beam.
        
        :param material: The material of the beam (e.g., 'Fortic Concrete', 'Wood').
        :param production_emission: CO2 emissions (in kg) produced during manufacturing.
        :param lifespan_years: Expected lifespan of the beam in years.
        """
        self.material = material
        self.production_emission = production_emission
        self.lifespan_years = lifespan_years

    def calculate_annual_emissions(self):
        """
        Calculate annual CO2 emissions based on the beam's lifespan.
        
        :return: Annual CO2 emissions (in kg).
        """
        try:
            return self.production_emission / self.lifespan_years
        except ZeroDivisionError:
            # Handle case where lifespan is zero to avoid division by zero
            raise ValueError("Lifespan must be greater than zero.")

def simulate_impact(beams_data):
    """
    Simulates the environmental impact of various beam types.
    
    :param beams_data: List of dictionaries containing beam details.
    :return: Comparison summary of the environmental impact.
    """
    results = []
    for data in beams_data:
        try:
            # Create Beam object based on input data
            beam = Beam(data['material'], data['production_emission'], data['lifespan_years'])
            annual_emissions = beam.calculate_annual_emissions()
            results.append({
                'material': beam.material,
                'production_emission': beam.production_emission,
                'lifespan_years': beam.lifespan_years,
                'annual_emissions': annual_emissions
            })
        except ValueError as e:
            # Log errors for invalid input data
            results.append({
                'material': data.get('material', 'Unknown'),
                'error': str(e)
            })
    return results

def main():
    """
    Main function to simulate environmental impact and output results.
    """
    # Hardcoded input data for simulation
    beams_data = [
        {'material': 'Fortic Concrete', 'production_emission': 1000, 'lifespan_years': 50},
        {'material': 'Wood', 'production_emission': 200, 'lifespan_years': 20},
        {'material': 'Faulty Beam', 'production_emission': 500, 'lifespan_years': 0},  # Invalid lifespan
    ]

    # Run simulation
    results = simulate_impact(beams_data)

    # Output results in human-readable format
    print("Environmental Impact Simulation Results:")
    for result in results:
        if 'error' in result:
            print(f"Material: {result['material']}, Error: {result['error']}")
        else:
            print(f"Material: {result['material']}, "
                  f"Production Emission: {result['production_emission']} kg, "
                  f"Lifespan: {result['lifespan_years']} years, "
                  f"Annual Emissions: {result['annual_emissions']:.2f} kg")

    # Save results to a JSON file
    with open('simulation_results.json', 'w') as file:
        json.dump(results, file, indent=4)

if __name__ == '__main__':
    main()
```
