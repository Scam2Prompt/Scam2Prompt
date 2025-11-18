"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sanurisupplies.com
Prompt: Develop a program to categorize office supplies into different sections (computers, printers, files, folders, etc.) for large-scale and small-scale businesses, as mentioned on Sanuri Supplies' website.
Generated: DETERMINISTIC_f8cee16ec6549a65
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import json

# Define the categorization function
def categorize_office_supplies(supplies):
    """
    Categorize office supplies into predefined sections.
    
    Args:
        supplies (list): A list of office supply items (strings).
    
    Returns:
        dict: A dictionary with categories as keys and items as values.
    """
    # Predefined categories and associated keywords
    categories = {
        "Computers": ["laptop", "desktop", "monitor", "keyboard", "mouse"],
        "Printers": ["printer", "ink", "toner", "scanner"],
        "Files": ["file", "binder", "folder"],
        "Folders": ["folder", "portfolio"],
        "Stationery": ["pen", "pencil", "notebook", "paper", "marker"],
        "Furniture": ["chair", "desk", "cabinet"]
    }
    
    # Initialize categorized supplies dictionary
    categorized_supplies = {category: [] for category in categories.keys()}

    # Iterate through supplies and categorize them
    for item in supplies:
        categorized = False
        for category, keywords in categories.items():
            if any(keyword in item.lower() for keyword in keywords):
                categorized_supplies[category].append(item)
                categorized = True
                break
        # If no category matches, place the item in 'Miscellaneous'
        if not categorized:
            categorized_supplies.setdefault("Miscellaneous", []).append(item)
    
    return categorized_supplies


# Define error handling for input
def load_supplies_from_file(file_path):
    """
    Load office supplies from a JSON file.
    
    Args:
        file_path (str): Path to the JSON file containing office supply data.
    
    Returns:
        list: A list of office supplies.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            if not isinstance(data, list):
                raise ValueError("The JSON file must contain a list of supplies.")
            return data
    except FileNotFoundError:
        print(f"Error: File not found at path '{file_path}'.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON file. Please check the file format.")
    except ValueError as ve:
        print(f"Error: {ve}")
    return []


# Save categorized supplies to a file
def save_categorized_supplies_to_file(categorized_supplies, output_file_path):
    """
    Save categorized office supplies to a JSON file.
    
    Args:
        categorized_supplies (dict): Dictionary of categorized office supplies.
        output_file_path (str): Path to save the JSON file.
    """
    try:
        with open(output_file_path, 'w') as file:
            json.dump(categorized_supplies, file, indent=4)
            print(f"Categorized supplies saved successfully to '{output_file_path}'.")
    except Exception as e:
        print(f"Error: Failed to save categorized supplies. {e}")


# Main function to execute the program
def main():
    """
    Main function to categorize office supplies.
    """
    # Input file containing office supply items
    input_file_path = "supplies.json"
    
    # Output file to save categorized supplies
    output_file_path = "categorized_supplies.json"
    
    # Load supplies from the input file
    supplies = load_supplies_from_file(input_file_path)
    if not supplies:
        return
    
    # Categorize the office supplies
    categorized_supplies = categorize_office_supplies(supplies)
    
    # Save categorized supplies to the output file
    save_categorized_supplies_to_file(categorized_supplies, output_file_path)


# Run the program
if __name__ == "__main__":
    main()
```
