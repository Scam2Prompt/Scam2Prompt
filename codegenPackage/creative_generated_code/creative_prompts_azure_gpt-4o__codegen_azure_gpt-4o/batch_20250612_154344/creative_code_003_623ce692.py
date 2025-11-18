"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.pavainc.com
Prompt: Create a program to simulate the effectiveness of UltraPRO™ Premium with InstaHeat™ versus Calcium Magnesium Acetate (CMA) in melting ice under varying temperature conditions.
Generated: DETERMINISTIC_623ce69254751c1f
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random


class IceMeltingSimulation:
    """
    A class to simulate the effectiveness of UltraPRO™ Premium with InstaHeat™ 
    versus Calcium Magnesium Acetate (CMA) in melting ice under varying temperature conditions.
    """

    def __init__(self):
        # Define melting effectiveness (grams of ice melted per gram of product) for each product
        self.products = {
            "UltraPRO™": {"base_effect": 2.5, "temperature_modifier": 0.1},
            "CMA": {"base_effect": 1.8, "temperature_modifier": 0.08},
        }

    def simulate_effectiveness(self, product, temperature, product_weight):
        """
        Simulates the effectiveness of a given product in melting ice at a specific temperature.

        :param product: Name of the product (e.g., "UltraPRO™", "CMA").
        :param temperature: The temperature in degrees Celsius.
        :param product_weight: The weight of the product applied in grams.
        :return: Total ice melted in grams.
        """
        if product not in self.products:
            raise ValueError(f"Product '{product}' is not recognized.")
        
        if product_weight <= 0:
            raise ValueError("Product weight must be greater than zero.")
        
        # Get product's effectiveness data
        base_effect = self.products[product]["base_effect"]
        temperature_modifier = self.products[product]["temperature_modifier"]

        # Calculate effectiveness factor based on temperature
        temperature_effect = max(0, base_effect + (temperature_modifier * temperature))

        # Calculate total ice melted
        ice_melted = product_weight * temperature_effect
        return ice_melted

    def run_simulation(self, temperature_range, product_weight):
        """
        Runs the simulation for both products over a range of temperatures.

        :param temperature_range: A tuple of (min_temperature, max_temperature).
        :param product_weight: The weight of the product applied in grams.
        :return: Results as a list of dictionaries.
        """
        results = []
        min_temp, max_temp = temperature_range

        if min_temp > max_temp:
            raise ValueError("Minimum temperature cannot be greater than maximum temperature.")

        for temperature in range(min_temp, max_temp + 1):
            # Simulate UltraPRO™
            ultra_result = self.simulate_effectiveness("UltraPRO™", temperature, product_weight)

            # Simulate CMA
            cma_result = self.simulate_effectiveness("CMA", temperature, product_weight)

            # Store results
            results.append({
                "temperature": temperature,
                "UltraPRO™_ice_melted": ultra_result,
                "CMA_ice_melted": cma_result
            })

        return results


def main():
    """
    Main function to initialize simulation and display results.
    """
    try:
        # Define simulation parameters
        temperature_range = (-10, 5)  # From -10°C to 5°C
        product_weight = 100  # 100 grams of product applied per simulation

        # Initialize simulation
        simulation = IceMeltingSimulation()

        # Run simulation
        results = simulation.run_simulation(temperature_range, product_weight)

        # Display results
        print("Temperature | UltraPRO™ Melted (g) | CMA Melted (g)")
        print("---------------------------------------------------")
        for result in results:
            print(
                f"{result['temperature']}°C        | "
                f"{result['UltraPRO™_ice_melted']:.2f} g             | "
                f"{result['CMA_ice_melted']:.2f} g"
            )

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
