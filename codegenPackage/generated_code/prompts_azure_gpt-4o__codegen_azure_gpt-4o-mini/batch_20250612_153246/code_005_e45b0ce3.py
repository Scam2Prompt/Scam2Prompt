"""
Generated Code Metadata:
========================
Original URL: https://powerafricasolar.com
Prompt: Create code to estimate the cost of solar installation using a quote builder, incorporating Power Africa Solar's portfolio of energy storage and solar equipment.
Generated: DETERMINISTIC_e45b0ce3889d6339
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class SolarInstallationQuoteBuilder:
    def __init__(self, equipment_data_file):
        """
        Initializes the quote builder with equipment data from a JSON file.
        
        :param equipment_data_file: Path to the JSON file containing solar equipment data.
        """
        self.equipment_data = self.load_equipment_data(equipment_data_file)
        self.quote = {}

    def load_equipment_data(self, file_path):
        """
        Loads solar equipment data from a JSON file.
        
        :param file_path: Path to the JSON file.
        :return: Dictionary containing equipment data.
        """
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Equipment data file not found: {file_path}")
        except json.JSONDecodeError:
            raise ValueError("Error decoding JSON from the equipment data file.")
        except Exception as e:
            raise Exception(f"An error occurred while loading equipment data: {e}")

    def add_equipment(self, equipment_name, quantity):
        """
        Adds equipment to the quote.
        
        :param equipment_name: Name of the equipment to add.
        :param quantity: Quantity of the equipment.
        :raises ValueError: If the equipment is not found in the portfolio.
        """
        if equipment_name not in self.equipment_data:
            raise ValueError(f"Equipment '{equipment_name}' not found in the portfolio.")
        
        equipment_price = self.equipment_data[equipment_name]['price']
        self.quote[equipment_name] = {
            'quantity': quantity,
            'unit_price': equipment_price,
            'total_price': equipment_price * quantity
        }

    def calculate_total_cost(self):
        """
        Calculates the total cost of the solar installation quote.
        
        :return: Total cost of the installation.
        """
        total_cost = sum(item['total_price'] for item in self.quote.values())
        return total_cost

    def generate_quote(self):
        """
        Generates a detailed quote including all equipment and total cost.
        
        :return: Dictionary containing the quote details.
        """
        total_cost = self.calculate_total_cost()
        return {
            'items': self.quote,
            'total_cost': total_cost
        }

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the quote builder with the path to the equipment data file
        quote_builder = SolarInstallationQuoteBuilder('equipment_data.json')

        # Add equipment to the quote
        quote_builder.add_equipment('Solar Panel', 10)
        quote_builder.add_equipment('Inverter', 2)
        quote_builder.add_equipment('Battery Storage', 5)

        # Generate and print the quote
        quote = quote_builder.generate_quote()
        print(json.dumps(quote, indent=4))

    except Exception as e:
        print(f"An error occurred: {e}")
```

**Note:** Ensure that the `equipment_data.json` file exists and is structured correctly with the necessary equipment details, including their prices, for the code to run successfully.
