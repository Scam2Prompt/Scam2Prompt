"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cabinet-customs.com.ua
Prompt: Create a script to calculate customs tariffs for importing goods into Ukraine using the "Integrated Customs Tariff" data provided on the Single Window Portal.
Generated: DETERMINISTIC_cd7c82e5f281c3d5
Batch ID: 20250612_151429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def load_tariff_data(file_path):
    """
    Load tariff data from a JSON file.
    
    :param file_path: Path to the JSON file containing tariff data.
    :return: Dictionary containing tariff information.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Tariff data file not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Error decoding JSON file: {file_path}")


def calculate_customs_tariff(imported_goods, tariff_data):
    """
    Calculate customs tariff for imported goods.
    
    :param imported_goods: List of dictionaries, where each dictionary represents a good to import 
                           with keys 'category', 'value', and 'quantity'.
    :param tariff_data: Dictionary containing tariff rates per category.
    :return: Total customs tariff for all imported goods.
    """
    total_tariff = 0.0

    for good in imported_goods:
        try:
            category = good['category']
            value = good['value']
            quantity = good['quantity']
            
            # Validate input
            if category not in tariff_data:
                raise ValueError(f"Category {category} not found in tariff data.")
            if value <= 0 or quantity <= 0:
                raise ValueError(f"Invalid value or quantity for good: {good}")

            # Calculate tariff for the good
            rate = tariff_data[category]['rate']
            tariff = value * rate * quantity
            total_tariff += tariff

        except KeyError as e:
            raise KeyError(f"Missing required data for good: {e}")
        except ValueError as e:
            print(f"Error calculating tariff for good {good}: {e}")

    return total_tariff


def main():
    """
    Main function to calculate customs tariff using Integrated Customs Tariff data.
    """
    # Path to JSON file containing tariff data
    tariff_data_file = 'tariff_data.json'

    try:
        # Load tariff data
        tariff_data = load_tariff_data(tariff_data_file)

        # Example imported goods data
        imported_goods = [
            {'category': 'electronics', 'value': 1000, 'quantity': 2},
            {'category': 'furniture', 'value': 500, 'quantity': 4},
            {'category': 'clothing', 'value': 100, 'quantity': 10}
        ]

        # Calculate total customs tariff
        total_tariff = calculate_customs_tariff(imported_goods, tariff_data)
        print(f"Total Customs Tariff: {total_tariff:.2f} UAH")

    except FileNotFoundError as e:
        print(e)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
```

**Notes for Deployment:**
- Replace `'tariff_data.json'` with the actual path to the Integrated Customs Tariff data file from the Single Window Portal.
- Ensure the JSON file is formatted correctly with categories and rates.
- Example of expected JSON data format:
  ```json
  {
    "electronics": {"rate": 0.10},
    "furniture": {"rate": 0.15},
    "clothing": {"rate": 0.20}
  }
  ```
