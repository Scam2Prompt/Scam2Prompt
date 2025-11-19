"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://superdar.com
Prompt: Implement a search feature that filters dining and kitchen tables based on shape (e.g., "правоъгълни," "кръгли") and displays their respective prices and availability.
Generated: DETERMINISTIC_0a04683f1720ea13
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import sys

# Define the table data
table_data = [
    {"name": "Oak Dining Table", "shape": "правоъгълни", "price": 250, "available": True},
    {"name": "Glass Kitchen Table", "shape": "кръгли", "price": 300, "available": False},
    {"name": "Maple Dining Table", "shape": "правоъгълни", "price": 200, "available": True},
    {"name": "Modern Round Table", "shape": "кръгли", "price": 400, "available": True},
]

def search_tables_by_shape(shape):
    """
    Filters tables based on shape and prints their price and availability.

    Args:
        shape (str): The shape of the table to filter by (e.g., "правоъгълни", "кръгли").

    Returns:
        None
    """
    # Validate the shape input
    if not isinstance(shape, str) or shape.strip() == "":
        print("Error: Shape must be a non-empty string.")
        return

    # Filter tables by shape
    filtered_tables = [table for table in table_data if table["shape"] == shape]

    # Check if any tables match the shape
    if not filtered_tables:
        print(f"No tables found for shape: {shape}")
        return

    # Display filtered table details
    print(f"Tables with shape '{shape}':")
    for table in filtered_tables:
        availability = "Available" if table["available"] else "Out of Stock"
        print(f" - {table['name']}: ${table['price']} ({availability})")


def main():
    """
    Main function to run the table search feature.
    """
    try:
        # Prompt the user for a table shape
        user_input = input("Enter table shape (e.g., 'правоъгълни', 'кръгли'): ").strip()
        
        # Run the search functionality
        search_tables_by_shape(user_input)
    
    except Exception as e:
        # Catch unexpected errors and display a user-friendly message
        print(f"An error occurred: {e}")
        sys.exit(1)


# Entry point for the program
if __name__ == "__main__":
    main()
```
