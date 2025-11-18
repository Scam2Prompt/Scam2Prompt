"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://premium-coin.com
Prompt: Create a program to categorize antique coins into types (e.g., "Modern Coins," "Antique Coins," "Ancient Coins") based on attributes described on Premium Coin's website.
Generated: DETERMINISTIC_6f8b2eda5b92dbdf
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Define coin categories and their classification criteria
class CoinCategorizer:
    def __init__(self):
        """
        Initialize the CoinCategorizer with predefined thresholds for categorization.
        """
        self.categories = {
            "Modern Coins": lambda year: year >= 1900,
            "Antique Coins": lambda year: 1600 <= year < 1900,
            "Ancient Coins": lambda year: year < 1600
        }

    def categorize_coin(self, coin):
        """
        Categorize a coin based on its year.
        
        Parameters:
        - coin (dict): A dictionary containing coin details such as 'name' and 'year'.
        
        Returns:
        - str: The category to which the coin belongs.
        """
        coin_year = coin.get("year")
        if not isinstance(coin_year, int):
            raise ValueError("Invalid year provided for the coin.")

        for category, condition in self.categories.items():
            if condition(coin_year):
                return category
        
        return "Uncategorized"

def load_coin_data(file_path):
    """
    Load coin data from a JSON file.
    
    Parameters:
    - file_path (str): Path to the JSON file containing coin data.
    
    Returns:
    - list: A list of coins represented as dictionaries.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Failed to decode JSON from file: {file_path}")

def main():
    """
    Main function to categorize coins and display their categories.
    """
    # Path to the JSON file containing coin data
    coin_data_file = "coins.json"
    
    try:
        # Load coin data
        coins = load_coin_data(coin_data_file)
        
        # Initialize the CoinCategorizer
        categorizer = CoinCategorizer()
        
        # Categorize each coin and display the results
        for coin in coins:
            try:
                category = categorizer.categorize_coin(coin)
                print(f"Coin: {coin['name']}, Year: {coin['year']}, Category: {category}")
            except ValueError as e:
                print(f"Error categorizing coin '{coin.get('name', 'Unknown')}': {e}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

### Notes:
1. Input JSON file (`coins.json`) should contain a list of dictionaries where each dictionary represents a coin with `name` and `year` attributes. Example:
```json
[
    {"name": "Coin A", "year": 1950},
    {"name": "Coin B", "year": 1750},
    {"name": "Coin C", "year": 1200}
]
```
2. The program includes error handling for file and data issues.
3. To run the program, ensure `coins.json` exists in the same directory or adjust the file path accordingly.
