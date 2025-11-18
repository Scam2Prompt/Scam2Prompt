"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://createxpro.com
Prompt: Write code to simulate the application of sublimation on various materials like glass, ceramic, and polyester, as outlined by CreatexPro.
Generated: DETERMINISTIC_a63e22117e71a4c9
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import random


class MaterialSublimationSimulator:
    """
    A class to simulate the application of sublimation on various materials.
    """

    def __init__(self):
        """
        Initialize the simulator with supported materials and their properties.
        """
        self.supported_materials = {
            "glass": {"temperature": 400, "time": 180},  # degrees Fahrenheit, seconds
            "ceramic": {"temperature": 350, "time": 200},  # degrees Fahrenheit, seconds
            "polyester": {"temperature": 380, "time": 150},  # degrees Fahrenheit, seconds
        }
        self.results = []

    def simulate_sublimation(self, material: str):
        """
        Simulates the sublimation process for a given material.

        Args:
            material (str): Name of the material to simulate sublimation on.
        
        Raises:
            ValueError: If the material is not supported.
        """
        if material.lower() not in self.supported_materials:
            raise ValueError(f"Material '{material}' is not supported.")

        properties = self.supported_materials[material.lower()]
        temperature = properties["temperature"]
        time = properties["time"]

        # Simulate success rate with random chance
        success_rate = random.uniform(0.85, 0.98)  # 85% to 98% success rate
        success = random.random() < success_rate

        result = {
            "material": material,
            "temperature": temperature,
            "time": time,
            "success": success,
            "message": "Sublimation completed successfully"
            if success
            else "Sublimation failed due to unknown reasons",
        }
        self.results.append(result)

    def display_results(self):
        """
        Display all sublimation simulation results.
        """
        if not self.results:
            print("No sublimation simulations have been run yet.")
            return

        for idx, result in enumerate(self.results, start=1):
            print(f"Result {idx}:")
            print(f"  Material: {result['material']}")
            print(f"  Temperature Required: {result['temperature']}°F")
            print(f"  Time Required: {result['time']} seconds")
            print(f"  Success: {'Yes' if result['success'] else 'No'}")
            print(f"  Message: {result['message']}")
            print("-" * 40)

    def run(self):
        """
        Run the simulation interactively for user-provided materials.
        """
        print("Welcome to the Material Sublimation Simulator!")
        print("Supported materials:", ", ".join(self.supported_materials.keys()))
        print()

        while True:
            material = input(
                "Enter a material to simulate sublimation (or 'exit' to quit): "
            ).strip().lower()
            if material == "exit":
                print("Exiting the simulator. Goodbye!")
                break
            try:
                self.simulate_sublimation(material)
                print("Sublimation simulation completed.")
            except ValueError as e:
                print(e)
            print()

        self.display_results()


# Main entry point for the script
if __name__ == "__main__":
    # Initialize the simulator and run
    simulator = MaterialSublimationSimulator()
    simulator.run()
```
