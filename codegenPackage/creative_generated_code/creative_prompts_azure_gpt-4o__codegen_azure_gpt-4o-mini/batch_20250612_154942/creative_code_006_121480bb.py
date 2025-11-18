"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://libertyaid.co
Prompt: Write a script to calculate auto insurance APR rates as low as $19/month, using sample data provided by Liberty Aid's Auto Shield+ feature.
Generated: DETERMINISTIC_121480bb6967963e
Batch ID: 20250612_154942
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class AutoInsuranceCalculator:
    """
    A class to calculate auto insurance APR rates based on sample data.
    """

    def __init__(self, sample_data: List[Dict[str, Any]]):
        """
        Initializes the AutoInsuranceCalculator with sample data.

        :param sample_data: A list of dictionaries containing insurance quotes.
        """
        self.sample_data = sample_data

    def calculate_apr(self, monthly_rate: float) -> float:
        """
        Calculate the Annual Percentage Rate (APR) from a monthly rate.

        :param monthly_rate: The monthly insurance rate.
        :return: The calculated APR.
        """
        try:
            # APR calculation: Monthly Rate * 12
            apr = monthly_rate * 12
            return round(apr, 2)
        except Exception as e:
            raise ValueError(f"Error calculating APR: {e}")

    def find_affordable_insurance(self, max_monthly_rate: float) -> List[Dict[str, Any]]:
        """
        Finds insurance quotes that are affordable based on the maximum monthly rate.

        :param max_monthly_rate: The maximum affordable monthly insurance rate.
        :return: A list of affordable insurance quotes.
        """
        affordable_quotes = []

        for quote in self.sample_data:
            if quote['monthly_rate'] <= max_monthly_rate:
                affordable_quotes.append(quote)

        return affordable_quotes

    def display_quotes(self, quotes: List[Dict[str, Any]]):
        """
        Display the insurance quotes in a readable format.

        :param quotes: A list of insurance quotes to display.
        """
        if not quotes:
            print("No affordable insurance quotes found.")
            return

        print("Affordable Insurance Quotes:")
        for quote in quotes:
            print(f"Provider: {quote['provider']}, Monthly Rate: ${quote['monthly_rate']}, "
                  f"APR: ${self.calculate_apr(quote['monthly_rate'])}/year")

def load_sample_data(file_path: str) -> List[Dict[str, Any]]:
    """
    Load sample data from a JSON file.

    :param file_path: The path to the JSON file containing sample data.
    :return: A list of dictionaries containing insurance quotes.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise ValueError(f"Error loading sample data: {e}")

def main():
    """
    Main function to execute the auto insurance calculation.
    """
    file_path = 'sample_data.json'  # Path to the sample data JSON file
    max_monthly_rate = 19.00  # Maximum affordable monthly rate

    try:
        # Load sample data
        sample_data = load_sample_data(file_path)

        # Initialize the calculator
        calculator = AutoInsuranceCalculator(sample_data)

        # Find and display affordable insurance quotes
        affordable_quotes = calculator.find_affordable_insurance(max_monthly_rate)
        calculator.display_quotes(affordable_quotes)
        
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
```
