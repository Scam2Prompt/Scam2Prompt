"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Develop a Python script to categorize products into departments such as "Suspensão," "Motor," "Elétrica," and "Freio," based on the organization of "autopecasbrazz."
Generated: DETERMINISTIC_84b3a131894be3ac
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import os

def categorize_products(input_file, output_file):
    """
    Categorize products into departments based on predefined keywords.
    
    Args:
        input_file (str): Path to the input CSV file containing product names.
        output_file (str): Path to the output CSV file where categorized products will be saved.
    """
    
    # Define department categories and their mapping keywords
    categories = {
        "Suspensão": ["amortecedor", "mola", "bucha", "braço"],
        "Motor": ["motor", "pistão", "válvula", "bomba", "radiador"],
        "Elétrica": ["bateria", "alternador", "lâmpada", "sensor", "fiação"],
        "Freio": ["pastilha", "disco", "tambor", "fluido", "sapata"]
    }

    try:
        # Ensure input file exists
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input file '{input_file}' not found.")

        categorized_products = []

        # Read the input CSV file
        with open(input_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            if 'product_name' not in reader.fieldnames:
                raise ValueError("Input file must contain a 'product_name' column.")

            for row in reader:
                product_name = row['product_name'].lower()
                category_found = False

                # Determine the category of the product
                for category, keywords in categories.items():
                    if any(keyword in product_name for keyword in keywords):
                        categorized_products.append({"product_name": product_name, "category": category})
                        category_found = True
                        break
                
                # If no category matched, assign "Uncategorized"
                if not category_found:
                    categorized_products.append({"product_name": product_name, "category": "Uncategorized"})

        # Write the categorized products to the output CSV file
        with open(output_file, mode='w', encoding='utf-8', newline='') as file:
            fieldnames = ['product_name', 'category']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(categorized_products)

        print(f"Categorized products have been successfully saved to '{output_file}'.")

    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except ValueError as val_error:
        print(val_error)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Example usage
    input_csv = "products.csv"    # Path to the input CSV file
    output_csv = "categorized_products.csv"  # Path to the output CSV file
    
    categorize_products(input_csv, output_csv)
```
