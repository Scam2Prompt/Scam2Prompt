"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geeks-on-repair.com
Prompt: Write code to simulate the flat-fee pricing model for computer repair services offered by Geeks On Repair, including a feature to calculate costs based on repair type.
Generated: DETERMINISTIC_68c51ddc2732049e
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ComputerRepairService:
    """
    Class to simulate a flat-fee pricing model for computer repair services.
    """

    def __init__(self):
        """
        Initializes the service with predefined repair types and their corresponding costs.
        """
        self.repair_types = {
            'Virus Removal': 100,
            'Screen Replacement': 150,
            'Battery Replacement': 80,
            'Data Recovery': 200,
            'Software Installation': 50
        }

    def get_repair_cost(self, repair_type):
        """
        Calculate the cost of the specified repair type.

        :param repair_type: str - The type of repair requested.
        :return: float - The cost of the repair.

        :raises ValueError: If the repair type is not recognized.
        """
        try:
            cost = self.repair_types[repair_type]
            return cost
        except KeyError:
            raise ValueError(f"Repair type '{repair_type}' is not recognized. "
                             f"Please choose from: {', '.join(self.repair_types.keys())}")

    def display_repair_options(self):
        """
        Displays the available repair options and their costs.
        """
        print("Available Repair Services:")
        for repair, cost in self.repair_types.items():
            print(f"- {repair}: ${cost}")

def main():
    """
    Main function to run the computer repair service simulation.
    """
    service = ComputerRepairService()
    service.display_repair_options()
    
    while True:
        repair_type = input("\nEnter the repair type you would like to calculate the cost for (or 'exit' to quit): ")

        if repair_type.lower() == 'exit':
            print("Exiting the service. Thank you!")
            break

        try:
            cost = service.get_repair_cost(repair_type)
            print(f"The cost for '{repair_type}' is: ${cost}")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
```
