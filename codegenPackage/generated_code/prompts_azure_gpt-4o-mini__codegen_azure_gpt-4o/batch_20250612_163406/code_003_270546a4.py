"""
Generated Code Metadata:
========================
Original URL: https://ac-world-galagames.blogspot.com
Prompt: Create a function that organizes toy data from the blog into a structured format, highlighting unique toys like "Caminhão Guincho" and "Caixa de Música."
Generated: DETERMINISTIC_270546a4e2ec93c4
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

def organize_toy_data(toy_data):
    """
    Organizes toy data into a structured format, highlighting unique toys.

    Args:
        toy_data (list): A list of dictionaries containing toy information.

    Returns:
        dict: A structured dictionary with organized toy data.
    """
    try:
        # Initialize the structured format
        structured_data = {
            "unique_toys": [],
            "all_toys": []
        }

        # Define the unique toys to highlight
        unique_toy_names = {"Caminhão Guincho", "Caixa de Música"}

        # Process each toy in the input data
        for toy in toy_data:
            # Validate toy data structure
            if not isinstance(toy, dict) or "name" not in toy:
                raise ValueError("Invalid toy data format. Each toy must be a dictionary with a 'name' key.")

            # Add toy to the list of all toys
            structured_data["all_toys"].append(toy)

            # Highlight unique toys
            if toy["name"] in unique_toy_names:
                structured_data["unique_toys"].append(toy)

        return structured_data

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred while organizing toy data: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Sample toy data
    toy_data = [
        {"name": "Caminhão Guincho", "price": 50.0, "category": "Vehicles"},
        {"name": "Caixa de Música", "price": 30.0, "category": "Music"},
        {"name": "Boneca", "price": 20.0, "category": "Dolls"},
        {"name": "Carrinho de Controle Remoto", "price": 100.0, "category": "Vehicles"}
    ]

    # Organize the toy data
    organized_data = organize_toy_data(toy_data)

    # Print the structured data in JSON format for better readability
    if organized_data:
        print(json.dumps(organized_data, indent=4, ensure_ascii=False))
```
