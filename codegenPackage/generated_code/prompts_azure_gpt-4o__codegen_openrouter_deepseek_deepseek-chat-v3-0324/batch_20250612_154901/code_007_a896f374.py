"""
Generated Code Metadata:
========================
Original URL: https://hurmanblirrikxvcu.firebaseapp.com
Prompt: Develop a Python program to convert historical daily exchange rates between USD and EUR, using provided maximum and minimum values for specific dates.
Generated: DETERMINISTIC_a896f3744726381b
Batch ID: 20250612_154901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
from datetime import datetime
from typing import Dict, List, Tuple

def load_exchange_rates(file_path: str) -> Dict[str, Tuple[float, float]]:
    """
    Load exchange rates from a CSV file with date, min, and max values.
    
    Args:
        file_path: Path to the CSV file containing exchange rate data.
        
    Returns:
        A dictionary with dates as keys and tuples of (min_rate, max_rate) as values.
        
    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file is malformed.
    """
    exchange_rates = {}
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    date = row['date']
                    min_rate = float(row['min'])
                    max_rate = float(row['max'])
                    exchange_rates[date] = (min_rate, max_rate)
                except (KeyError, ValueError) as e:
                    raise ValueError(f"Malformed data in row: {row}. Error: {str(e)}")
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    
    return exchange_rates

def convert_amount(
    amount: float,
    date: str,
    exchange_rates: Dict[str, Tuple[float, float]],
    use_max: bool = True
) -> float:
    """
    Convert an amount between USD and EUR using historical exchange rates.
    
    Args:
        amount: The amount to convert.
        date: The date of the exchange rate in 'YYYY-MM-DD' format.
        exchange_rates: Dictionary of exchange rates.
        use_max: If True, use the max rate; otherwise use the min rate.
        
    Returns:
        The converted amount.
        
    Raises:
        ValueError: If the date is not found or invalid.
    """
    try:
        rates = exchange_rates[date]
    except KeyError:
        raise ValueError(f"No exchange rate data available for date: {date}")
    
    rate = rates[1] if use_max else rates[0]
    return amount * rate

def validate_date(date_str: str) -> bool:
    """
    Validate that a date string is in 'YYYY-MM-DD' format.
    
    Args:
        date_str: Date string to validate.
        
    Returns:
        True if valid, False otherwise.
    """
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def main():
    """
    Main function to demonstrate the conversion functionality.
    """
    try:
        # Load exchange rates from a CSV file (example path)
        exchange_rates = load_exchange_rates('exchange_rates.csv')
        
        # Example conversion
        amount = 100.0
        date = '2023-01-15'
        
        if not validate_date(date):
            print("Invalid date format. Please use 'YYYY-MM-DD'.")
            return
        
        converted_amount_max = convert_amount(amount, date, exchange_rates, use_max=True)
        converted_amount_min = convert_amount(amount, date, exchange_rates, use_max=False)
        
        print(f"On {date}:")
        print(f"100 USD -> EUR (using max rate): {converted_amount_max:.2f}")
        print(f"100 USD -> EUR (using min rate): {converted_amount_min:.2f}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
