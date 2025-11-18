"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binqutab.ae
Prompt: Create a program to simulate multi-modal transport logistics, including air and sea freight, inspired by Bin Qutab Logistics' proven experience in handling large-scale projects.
Generated: DETERMINISTIC_960384e447f999ae
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import json

class TransportMode:
    """
    Base class for transport modes. Defines the interface for transport classes.
    """
    def __init__(self, mode_name):
        self.mode_name = mode_name

    def calculate_cost(self, distance, weight):
        """
        Calculates the cost for transportation.
        Must be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses must implement calculate_cost method.")

class AirFreight(TransportMode):
    """
    Class for Air Freight transport.
    """
    def __init__(self):
        super().__init__('Air Freight')

    def calculate_cost(self, distance, weight):
        # Air Freight cost calculation: base cost + cost per km + cost per kg
        base_cost = 500  # Fixed base cost
        cost_per_km = 0.5  # Cost per kilometer
        cost_per_kg = 2.0  # Cost per kilogram
        return base_cost + (distance * cost_per_km) + (weight * cost_per_kg)


class SeaFreight(TransportMode):
    """
    Class for Sea Freight transport.
    """
    def __init__(self):
        super().__init__('Sea Freight')

    def calculate_cost(self, distance, weight):
        # Sea Freight cost calculation: base cost + cost per km + cost per kg
        base_cost = 300  # Fixed base cost
        cost_per_km = 0.2  # Cost per kilometer
        cost_per_kg = 0.5  # Cost per kilogram
        return base_cost + (distance * cost_per_km) + (weight * cost_per_kg)


class LogisticsSimulator:
    """
    Main class for simulating multi-modal transport logistics.
    """
    def __init__(self):
        self.available_modes = {
            'air': AirFreight(),
            'sea': SeaFreight()
        }

    def simulate_transport(self, mode, distance, weight):
        """
        Simulate transport using the given mode, distance, and weight.

        Args:
            mode (str): 'air' or 'sea'
            distance (float): Distance in kilometers.
            weight (float): Weight in kilograms.

        Returns:
            dict: Summary of the simulation results.
        """
        if mode not in self.available_modes:
            raise ValueError(f"Invalid transport mode: {mode}")

        transport_mode = self.available_modes[mode]
        cost = transport_mode.calculate_cost(distance, weight)
        result = {
            'mode': transport_mode.mode_name,
            'distance': distance,
            'weight': weight,
            'cost': round(cost, 2)
        }
        return result

    def simulate_random_scenario(self):
        """
        Simulates logistics for a random scenario.

        Returns:
            dict: Summary of the simulation.
        """
        mode = random.choice(list(self.available_modes.keys()))
        distance = random.uniform(100, 5000)  # Random distance between 100 and 5000 km
        weight = random.uniform(50, 1000)  # Random weight between 50 and 1000 kg
        return self.simulate_transport(mode, distance, weight)


def main():
    """
    Main function to run the logistics simulation based on user input.
    """
    simulator = LogisticsSimulator()

    print("Welcome to the Multi-modal Transport Logistics Simulator!")
    print("Available Modes: Air Freight ('air'), Sea Freight ('sea')")

    try:
        mode = input("Enter transport mode (air/sea): ").strip().lower()
        distance = float(input("Enter transport distance (km): ").strip())
        weight = float(input("Enter cargo weight (kg): ").strip())

        # Run simulation with user input
        result = simulator.simulate_transport(mode, distance, weight)
        print("\nSimulation Result:")
        print(json.dumps(result, indent=4))

        # Run a random simulation scenario
        print("\nRandom Scenario Simulation:")
        random_result = simulator.simulate_random_scenario()
        print(json.dumps(random_result, indent=4))

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
