"""
Generated Code Metadata:
========================
Original URL: https://ac-world-galagames.blogspot.com
Prompt: Write a Python script to categorize vintage toys into different types, such as "Ambulância", "Animal", "Arvore", etc.
Generated: DETERMINISTIC_c0532e9b0f3803fa
Batch ID: 20250622_212855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import os

def categorize_toys(input_file, output_file):
    """
    Categorizes vintage toys into different types based on their names.

    Args:
        input_file (str): Path to the input CSV file containing toy data.
        output_file (str): Path to the output CSV file to save categorized toy data.

    Raises:
        FileNotFoundError: If the input file does not exist.
        Exception: For any other unexpected errors during processing.
    """
    # Define toy categories based on keywords
    categories = {
        "Ambulância": ["ambulância", "ambulance"],
        "Animal": ["animal", "dog", "cat", "lion", "tiger", "bear"],
        "Arvore": ["arvore", "tree", "oak", "pine"],
        # Add more categories and keywords as needed
    }

    try:
        # Check if the input file exists
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input file '{input_file}' not found.")

        categorized_toys = []

        # Read the input CSV file
        with open(input_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                toy_name = row.get("name", "").lower()  # Get toy name and convert to lowercase
                toy_category = "Unknown"  # Default category

                # Determine the category based on keywords
                for category, keywords in categories.items():
                    if any(keyword in toy_name for keyword in keywords):
                        toy_category = category
                        break

                # Append categorized toy data
                categorized_toys.append({
                    "name": row.get("name", ""),
                    "category": toy_category
                })

        # Write the categorized toys to the output CSV file
        with open(output_file, mode='w', encoding='utf-8', newline='') as file:
            fieldnames = ["name", "category"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(categorized_toys)

        print(f"Categorized toys have been saved to '{output_file}'.")

    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Example usage
    input_csv = "vintage_toys.csv"  # Input file containing toy data
    output_csv = "categorized_toys.csv"  # Output file to save categorized toy data

    categorize_toys(input_csv, output_csv)
```
