"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gala-games-official-k.blogspot.com
Prompt: Write Python code to recommend a computer configuration based on user requirements (e.g., gaming or office use) using specifications similar to those listed for Londritech computers, such as processor type, memory size, and graphics card.
Generated: DETERMINISTIC_8807f66a2df60c2e
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ComputerConfiguration:
    """A class to represent a computer configuration based on user requirements."""

    def __init__(self, usage_type):
        """Initializes the ComputerConfiguration with a usage type.

        Args:
            usage_type (str): The type of usage ('gaming' or 'office').
        """
        self.usage_type = usage_type.lower()
        self.configuration = {}

    def recommend_configuration(self):
        """Recommends a computer configuration based on the usage type."""
        if self.usage_type == 'gaming':
            self.configuration = {
                'Processor': 'Intel Core i7 or AMD Ryzen 7',
                'Memory': '16 GB DDR4 RAM',
                'Graphics Card': 'NVIDIA GeForce RTX 3060 or AMD Radeon RX 6700 XT',
                'Storage': '1 TB SSD + 2 TB HDD',
                'Power Supply': '650W 80+ Gold',
                'Cooling': 'Liquid Cooling System'
            }
        elif self.usage_type == 'office':
            self.configuration = {
                'Processor': 'Intel Core i5 or AMD Ryzen 5',
                'Memory': '8 GB DDR4 RAM',
                'Graphics Card': 'Integrated Graphics',
                'Storage': '512 GB SSD',
                'Power Supply': '500W 80+ Bronze',
                'Cooling': 'Air Cooling'
            }
        else:
            raise ValueError(f"Unsupported usage type: '{self.usage_type}'. Please choose 'gaming' or 'office'.")

    def display_configuration(self):
        """Displays the recommended computer configuration."""
        if not self.configuration:
            raise RuntimeError("Configuration not recommended. Please call 'recommend_configuration()' first.")
        
        print("Recommended Computer Configuration:")
        for component, spec in self.configuration.items():
            print(f"{component}: {spec}")

def main():
    """Main function to run the configuration recommendation."""
    try:
        usage_type = input("Enter usage type (gaming/office): ")
        config = ComputerConfiguration(usage_type)
        config.recommend_configuration()
        config.display_configuration()
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except RuntimeError as re:
        print(f"RuntimeError: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
