"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kalinski-energia.pl
Prompt: Develop a Python program to assist in energy market operations, referencing the professional experience of Jacek Kaliński.
Generated: DETERMINISTIC_bc8144e3041c4f7d
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Energy Market Operations Assistant Program
Author: Inspired by Jacek Kaliński's professional experience
Description:
This program assists in energy market operations by calculating metrics such as total energy demand, 
average price per unit energy, and suggesting optimal energy allocation strategies based on market data.
"""

import csv
import statistics


class EnergyMarketOperations:
    """
    A class to encapsulate operations for energy market calculations.
    """

    def __init__(self, data_file: str):
        """
        Initializes the EnergyMarketOperations instance.

        :param data_file: Path to the CSV file containing energy market data.
        """
        self.data_file = data_file
        self.market_data = []  # List to store market data

    def load_data(self):
        """
        Load energy market data from a CSV file.

        The file should contain columns:
        - 'Region': Region name
        - 'EnergyDemand': Energy demand in MWh
        - 'PricePerUnit': Price per unit energy in USD
        """
        try:
            with open(self.data_file, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Convert numerical fields to appropriate types
                    row['EnergyDemand'] = float(row['EnergyDemand'])
                    row['PricePerUnit'] = float(row['PricePerUnit'])
                    self.market_data.append(row)
        except FileNotFoundError:
            raise FileNotFoundError(f"The file '{self.data_file}' was not found.")
        except ValueError as e:
            raise ValueError(f"Error parsing file: {e}")
        except Exception as e:
            raise Exception(f"An unexpected error occurred: {e}")

    def calculate_total_demand(self) -> float:
        """
        Calculate the total energy demand from all regions.

        :return: Total energy demand in MWh.
        """
        return sum(entry['EnergyDemand'] for entry in self.market_data)

    def calculate_average_price(self) -> float:
        """
        Calculate the average price per unit of energy across all regions.

        :return: Average price per unit energy in USD.
        """
        prices = [entry['PricePerUnit'] for entry in self.market_data]
        return statistics.mean(prices)

    def suggest_optimal_allocation(self) -> dict:
        """
        Suggest optimal allocation strategies based on energy demand and price.

        The suggestion is based on regions sorted by price per unit (ascending).

        :return: Dictionary suggesting the order of regions for energy allocation.
        """
        sorted_data = sorted(self.market_data, key=lambda x: x['PricePerUnit'])
        suggestions = {entry['Region']: entry for entry in sorted_data}
        return suggestions

    def display_summary(self):
        """
        Display a summary of the energy market data and calculated metrics.
        """
        print("Energy Market Summary:")
        print(f"Total Energy Demand: {self.calculate_total_demand():.2f} MWh")
        print(f"Average Price Per Unit: ${self.calculate_average_price():.2f}")
        print("Optimal Allocation Suggestions:")
        suggestions = self.suggest_optimal_allocation()
        for region, data in suggestions.items():
            print(f"  - Region: {region}, Energy Demand: {data['EnergyDemand']:.2f} MWh, Price: ${data['PricePerUnit']:.2f}")


def main():
    """
    Main function to execute the program.
    """
    print("Welcome to the Energy Market Operations Assistant Program.")
    input_file = input("Please enter the path to the market data CSV file: ")

    try:
        # Initialize the class with the provided file
        energy_market = EnergyMarketOperations(data_file=input_file)

        # Load and process the data
        energy_market.load_data()

        # Display the summary
        energy_market.display_summary()
    except Exception as e:
        # Handle any errors gracefully
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
