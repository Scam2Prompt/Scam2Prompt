"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cartoansurperu.com
Prompt: Write a program to generate a report comparing the resistance levels of different corrugated cardboard products, such as "Cartón Corrugado 1.64mts x 210gr" and "Cartón Corrugado 1.23mts x 110gr," based on their attributes from Cartonerías Andinas del Sur.
Generated: DETERMINISTIC_0429d505d0d0b25a
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program to generate a report comparing resistance levels of corrugated cardboard products.
Author: [Your Name]
Date: [Today’s Date]
Description: The program reads corrugated cardboard data, calculates resistance levels,
and generates a comparison report. Designed for Cartonerías Andinas del Sur.
"""

import csv
import os

# Constants
INPUT_FILE = "cardboard_data.csv"  # Input file containing cardboard product data
OUTPUT_FILE = "cardboard_resistance_report.txt"  # Output file for the generated report

# Function to calculate resistance level
def calculate_resistance(weight: float, area: float) -> float:
    """
    Calculate the resistance level of a cardboard product based on weight and area.
    
    Formula: Resistance = (Weight * Area) / 1000
    
    Args:
        weight (float): Weight of the cardboard in grams.
        area (float): Area of the cardboard in square meters.
        
    Returns:
        float: Calculated resistance level.
    """
    try:
        resistance = (weight * area) / 1000
        return round(resistance, 2)
    except Exception as e:
        raise ValueError(f"Error calculating resistance: {e}")

# Function to parse product data
def parse_product_data(file_path: str) -> list:
    """
    Read and parse product data from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing cardboard data.
        
    Returns:
        list: List of dictionaries containing product data.
    """
    products = []
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    product = {
                        "name": row["Name"],
                        "weight": float(row["Weight"]),
                        "width": float(row["Width"]),
                        "height": float(row["Height"]),
                    }
                    product["area"] = product["width"] * product["height"]
                    product["resistance"] = calculate_resistance(product["weight"], product["area"])
                    products.append(product)
                except KeyError as ke:
                    print(f"Missing key in row: {ke}")
                except ValueError as ve:
                    print(f"Invalid data in row: {ve}")
        return products
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except Exception as e:
        raise Exception(f"Error reading file: {e}")

# Function to generate a report
def generate_report(products: list, output_path: str) -> None:
    """
    Generate a comparison report for cardboard products.

    Args:
        products (list): List of product data dictionaries.
        output_path (str): Path to the output file for the report.
    """
    try:
        with open(output_path, mode="w", encoding="utf-8") as file:
            file.write("Cardboard Resistance Report\n")
            file.write("=" * 30 + "\n")
            for product in products:
                file.write(f"Name: {product['name']}\n")
                file.write(f"Weight: {product['weight']} grams\n")
                file.write(f"Area: {product['area']} square meters\n")
                file.write(f"Resistance: {product['resistance']} units\n")
                file.write("-" * 30 + "\n")
        print(f"Report successfully generated: {output_path}")
    except Exception as e:
        raise Exception(f"Error writing report: {e}")

# Main function
def main():
    """
    Main function to execute the program workflow.
    """
    try:
        # Check if input file exists
        if not os.path.exists(INPUT_FILE):
            raise FileNotFoundError(f"Input file not found: {INPUT_FILE}")

        # Parse product data from the input file
        products = parse_product_data(INPUT_FILE)

        # Generate the report
        generate_report(products, OUTPUT_FILE)

    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point of the program
if __name__ == "__main__":
    main()
```

### Notes
1. Ensure the `cardboard_data.csv` file exists and contains data in the following format:
   ```
   Name,Weight,Width,Height
   Cartón Corrugado 1.64mts x 210gr,210,1.64,1.00
   Cartón Corrugado 1.23mts x 110gr,110,1.23,1.00
   ```
2. Adjust the file paths (`INPUT_FILE` and `OUTPUT_FILE`) as necessary.
3. Additional logging or error-handling mechanisms can be added to suit specific production needs.
