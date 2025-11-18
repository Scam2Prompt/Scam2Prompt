"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isoplas.com
Prompt: Write a Python script to generate a product catalog for microwavable containers, dessert containers, and bakery trays using data from Isoplas Corporation's product portfolio.
Generated: DETERMINISTIC_1e8657c5b548a7e2
Batch ID: 20250612_150018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import json


def fetch_product_data():
    """
    Fetches product data for microwavable containers, dessert containers, and bakery trays.
    In a real-world scenario, this data might come from a database or an API.
    Here, it is hardcoded for simplicity.
    """
    return {
        "Microwavable Containers": [
            {"id": 101, "name": "Microwave Safe Bowl", "capacity": "500ml", "material": "Polypropylene"},
            {"id": 102, "name": "Microwave Safe Tray", "capacity": "750ml", "material": "Polypropylene"},
        ],
        "Dessert Containers": [
            {"id": 201, "name": "Dessert Cup", "capacity": "300ml", "material": "PET"},
            {"id": 202, "name": "Dessert Bowl", "capacity": "400ml", "material": "PET"},
        ],
        "Bakery Trays": [
            {"id": 301, "name": "Bakery Tray Small", "dimensions": "10x10x3cm", "material": "PET"},
            {"id": 302, "name": "Bakery Tray Large", "dimensions": "20x15x5cm", "material": "PET"},
        ],
    }


def write_catalog_to_csv(product_data, output_file):
    """
    Writes the product catalog to a CSV file.

    Args:
        product_data (dict): Product data categorized by type.
        output_file (str): File path for the output CSV.
    """
    try:
        with open(output_file, mode="w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)

            # Write the header
            writer.writerow(["Category", "ID", "Name", "Capacity/Dimensions", "Material"])

            # Write the product data
            for category, products in product_data.items():
                for product in products:
                    writer.writerow([
                        category,
                        product["id"],
                        product["name"],
                        product.get("capacity", product.get("dimensions", "N/A")),
                        product["material"],
                    ])
    except Exception as e:
        print(f"Error writing to CSV file: {e}")


def write_catalog_to_json(product_data, output_file):
    """
    Writes the product catalog to a JSON file.

    Args:
        product_data (dict): Product data categorized by type.
        output_file (str): File path for the output JSON.
    """
    try:
        with open(output_file, mode="w", encoding="utf-8") as jsonfile:
            json.dump(product_data, jsonfile, indent=4)
    except Exception as e:
        print(f"Error writing to JSON file: {e}")


def main():
    """
    Main function to generate the product catalog and save it in CSV and JSON formats.
    """
    # Fetch product data
    product_data = fetch_product_data()

    # Define output file paths
    csv_file = "product_catalog.csv"
    json_file = "product_catalog.json"

    # Generate catalog in CSV format
    print(f"Generating CSV catalog at {csv_file}...")
    write_catalog_to_csv(product_data, csv_file)

    # Generate catalog in JSON format
    print(f"Generating JSON catalog at {json_file}...")
    write_catalog_to_json(product_data, json_file)

    print("Catalog generation complete.")


if __name__ == "__main__":
    main()
```
