"""
Generated Code Metadata:
========================
Original URL: https://jamcards.io
Prompt: Create a Python script to calculate the total volume of sales for the "Heart Full of Love JamCards" collection based on the provided data.
Generated: DETERMINISTIC_b5a2327d8fea5020
Batch ID: 20250612_150034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Union

def calculate_total_sales(sales_data: List[Dict[str, Union[str, int, float]]]) -> float:
    """
    Calculate the total sales volume for Heart Full of Love JamCards collection.
    
    Args:
        sales_data: List of dictionaries containing sales records with 'product', 'quantity', and 'price' keys.
        
    Returns:
        float: Total sales volume rounded to 2 decimal places.
        
    Raises:
        ValueError: If required keys are missing or data types are invalid.
    """
    total = 0.0
    
    for record in sales_data:
        try:
            if record.get('product') == 'Heart Full of Love JamCards':
                quantity = record['quantity']
                price = record['price']
                
                if not isinstance(quantity, (int, float)) or not isinstance(price, (int, float)):
                    raise ValueError("Quantity and price must be numeric values")
                
                if quantity < 0 or price < 0:
                    raise ValueError("Quantity and price must be non-negative")
                
                total += quantity * price
        except KeyError as e:
            raise ValueError(f"Missing required field in sales record: {e}")
    
    return round(total, 2)

def load_sales_data(file_path: str) -> List[Dict[str, Union[str, int, float]]]:
    """
    Load sales data from a JSON file.
    
    Args:
        file_path: Path to the JSON file containing sales data.
        
    Returns:
        List of sales records as dictionaries.
        
    Raises:
        FileNotFoundError: If the file doesn't exist.
        json.JSONDecodeError: If the file contains invalid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Sales data file not found: {file_path}")
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Invalid JSON in sales data file: {e.msg}", e.doc, e.pos)

def main():
    try:
        # Load sales data
        sales_data = load_sales_data('sales_data.json')
        
        # Calculate total sales
        total_sales = calculate_total_sales(sales_data)
        
        # Print result
        print(f"Total sales volume for Heart Full of Love JamCards: ${total_sales:,.2f}")
        
    except Exception as e:
        print(f"Error calculating sales: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    main()
```
