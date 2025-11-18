"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thoinayadv.com
Prompt: Write a Python script to automate bulk order processing for electroforming signs and custom metallic stickers, including Nickel Metal and Stainless Steel options.
Generated: DETERMINISTIC_de932676c86b0383
Batch ID: 20250612_153224
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
import datetime

# Define constants for allowed materials
ALLOWED_MATERIALS = {"Nickel Metal", "Stainless Steel"}
OUTPUT_DIRECTORY = "processed_orders"

# Function to validate the order data
def validate_order(order):
    """
    Validate the order data.
    :param order: Dictionary with order details
    :return: Tuple (bool, str) -> (IsValid, ErrorMessage)
    """
    if "customer_name" not in order or not order["customer_name"].strip():
        return False, "Customer name is missing or empty."
    if "material" not in order or order["material"] not in ALLOWED_MATERIALS:
        return False, f"Invalid material specified. Allowed materials are: {', '.join(ALLOWED_MATERIALS)}."
    if "quantity" not in order or not order["quantity"].isdigit() or int(order["quantity"]) <= 0:
        return False, "Quantity must be a positive integer."
    return True, ""

# Function to process a single order
def process_order(order):
    """
    Process a single order.
    :param order: Dictionary containing order details
    :return: None
    """
    try:
        # Create output directory if it doesn't exist
        os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)

        # Generate order processing file
        filename = f"{order['customer_name'].replace(' ', '_')}_{order['material']}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
        filepath = os.path.join(OUTPUT_DIRECTORY, filename)

        with open(filepath, "w") as file:
            file.write("Order Summary:\n")
            file.write(f"Customer Name: {order['customer_name']}\n")
            file.write(f"Material: {order['material']}\n")
            file.write(f"Quantity: {order['quantity']}\n")
            file.write(f"Order Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        print(f"Order processed successfully. Output file: {filepath}")
    
    except Exception as e:
        print(f"Error processing order for {order['customer_name']}: {str(e)}")

# Function to process bulk orders from a CSV file
def process_bulk_orders(input_csv):
    """
    Process bulk orders from an input CSV file.
    :param input_csv: Path to the input CSV file
    :return: None
    """
    try:
        # Open and read the CSV file
        with open(input_csv, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                # Validate order data
                is_valid, error_message = validate_order(row)
                if not is_valid:
                    print(f"Skipping order due to validation error: {error_message}")
                    continue
                
                # Process the order
                process_order(row)
    
    except FileNotFoundError:
        print(f"Error: Input file '{input_csv}' not found.")
    except Exception as e:
        print(f"Error processing bulk orders: {str(e)}")

# Main function to execute the script
def main():
    """
    Main function to execute the script.
    :return: None
    """
    input_csv = input("Enter the path to the bulk orders CSV file: ").strip()
    process_bulk_orders(input_csv)

if __name__ == "__main__":
    main()
```
