"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jamcards.io
Prompt: Create a Python script to calculate the total volume of sales for the "Heart Full of Love JamCards" collection based on the provided data.
Generated: DETERMINISTIC_b5a2327d8fea5020
Batch ID: 20250612_150034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def calculate_total_volume(sales_data, collection_name):
    """
    Calculate the total volume of sales for a specified collection.

    Parameters:
        sales_data (list): A list of sales records in dictionary format.
        collection_name (str): The name of the collection to filter and sum sales for.

    Returns:
        int: The total volume of sales for the specified collection.
    """
    try:
        # Filter sales data to include only records related to the specified collection
        filtered_sales = [sale for sale in sales_data if sale.get('collection') == collection_name]
        
        if not filtered_sales:
            raise ValueError(f"No sales found for the collection '{collection_name}'.")

        # Sum up the 'volume' field from filtered sales records
        total_volume = sum(sale.get('volume', 0) for sale in filtered_sales)

        return total_volume

    except ValueError as ve:
        print(f"Error: {ve}")
        return 0
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 0

def main():
    """
    Main function to execute the script.
    """
    # Example sales data (can be replaced with actual data from a file or API)
    sales_data = [
        {"collection": "Heart Full of Love JamCards", "volume": 100},
        {"collection": "Heart Full of Love JamCards", "volume": 150},
        {"collection": "Sunshine Greeting Cards", "volume": 200},
        {"collection": "Heart Full of Love JamCards", "volume": 50},
        {"collection": "Holiday Special Cards", "volume": 300}
    ]

    # Specify the collection name to calculate the total volume for
    collection_name = "Heart Full of Love JamCards"

    # Calculate and print the total volume of sales
    total_volume = calculate_total_volume(sales_data, collection_name)
    print(f"Total volume of sales for '{collection_name}': {total_volume}")

if __name__ == "__main__":
    main()
```
