"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://projectdeksa.pages.dev
Prompt: Provide a code example for generating historical MASA coin data in a virtual economy simulation, using JavaScript or Python, as part of Project DEKSA's virtual kingdom.
Generated: DETERMINISTIC_3d7c45d2b966f9dc
Batch ID: 20250612_145625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from datetime import datetime, timedelta
import json

class MASACoinDataGenerator:
    def __init__(self, start_date, end_date, initial_supply, daily_mint_rate):
        """
        Initialize the MASACoinDataGenerator.

        :param start_date: The start date for the historical data.
        :param end_date: The end date for the historical data.
        :param initial_supply: The initial supply of MASA coins.
        :param daily_mint_rate: The daily mint rate of new MASA coins.
        """
        self.start_date = start_date
        self.end_date = end_date
        self.initial_supply = initial_supply
        self.daily_mint_rate = daily_mint_rate
        self.data = []

    def generate_data(self):
        """
        Generate historical MASA coin data over the specified date range.
        """
        current_date = self.start_date
        total_supply = self.initial_supply

        # Generate data for each day in the range
        while current_date <= self.end_date:
            minted_today = random.randint(0, self.daily_mint_rate)
            total_supply += minted_today

            # Create a record for the current date
            record = {
                "date": current_date.strftime("%Y-%m-%d"),
                "minted": minted_today,
                "total_supply": total_supply
            }
            self.data.append(record)

            current_date += timedelta(days=1)

    def save_to_json(self, filename):
        """
        Save the generated data to a JSON file.

        :param filename: The name of the file to save the data.
        """
        try:
            with open(filename, 'w') as json_file:
                json.dump(self.data, json_file, indent=4)
            print(f"Data successfully saved to {filename}")
        except IOError as e:
            print(f"Error saving data to {filename}: {e}")

def main():
    # Define parameters for the MASA coin data generation
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2023, 10, 1)
    initial_supply = 1000  # Initial supply of MASA coins
    daily_mint_rate = 50   # Max coins minted per day

    # Create an instance of the data generator
    masa_coin_generator = MASACoinDataGenerator(start_date, end_date, initial_supply, daily_mint_rate)
    
    # Generate the historical data
    masa_coin_generator.generate_data()

    # Save the data to a JSON file
    masa_coin_generator.save_to_json("masa_coin_data.json")

if __name__ == "__main__":
    main()
```
