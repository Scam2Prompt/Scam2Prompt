"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://haseebbaig.me
Prompt: Write a Python script for automating e-commerce order processing and report generation, as outlined in the Enorness e-commerce solutions.
Generated: DETERMINISTIC_b25b07d156934aff
Batch ID: 20250612_153314
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
import logging
from datetime import datetime

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("order_processing.log"),
        logging.StreamHandler()
    ]
)

# Constants
ORDERS_FILE = 'orders.json'  # JSON file containing order data
PROCESSED_FILE = 'processed_orders.csv'  # CSV file to save processed orders
REPORT_FILE = 'order_report.txt'  # Text file for summary report

def load_orders(file_path):
    """
    Load order data from a JSON file.
    :param file_path: Path to the JSON file.
    :return: List of orders.
    """
    try:
        with open(file_path, 'r') as file:
            orders = json.load(file)
        logging.info(f"Loaded {len(orders)} orders from {file_path}.")
        return orders
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return []
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON: {e}")
        return []

def process_orders(orders):
    """
    Process orders and prepare for CSV export.
    :param orders: List of orders.
    :return: List of processed order dictionaries.
    """
    processed_orders = []
    for order in orders:
        try:
            # Extract necessary fields and compute values (e.g., total price)
            order_id = order['order_id']
            customer_name = order['customer_name']
            products = order['products']  # List of products
            total_price = sum(product['price'] * product['quantity'] for product in products)
            
            processed_orders.append({
                'Order ID': order_id,
                'Customer Name': customer_name,
                'Total Price': round(total_price, 2),
                'Order Date': order.get('order_date', 'N/A'),
            })
        except KeyError as e:
            logging.error(f"Missing field in order data: {e}")
            continue
    logging.info(f"Processed {len(processed_orders)} orders.")
    return processed_orders

def save_processed_orders(file_path, processed_orders):
    """
    Save processed orders to a CSV file.
    :param file_path: Path to the CSV file.
    :param processed_orders: List of processed order dictionaries.
    """
    try:
        with open(file_path, 'w', newline='') as csvfile:
            fieldnames = ['Order ID', 'Customer Name', 'Total Price', 'Order Date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(processed_orders)
        logging.info(f"Processed orders saved to {file_path}.")
    except Exception as e:
        logging.error(f"Error saving processed orders: {e}")

def generate_report(file_path, processed_orders):
    """
    Generate a summary report and save to a text file.
    :param file_path: Path to the text file.
    :param processed_orders: List of processed order dictionaries.
    """
    try:
        total_orders = len(processed_orders)
        total_revenue = sum(order['Total Price'] for order in processed_orders)
        average_order_value = round(total_revenue / total_orders, 2) if total_orders > 0 else 0
        
        report_lines = [
            f"Order Processing Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"Total Orders Processed: {total_orders}",
            f"Total Revenue: ${total_revenue:.2f}",
            f"Average Order Value: ${average_order_value:.2f}",
        ]
        
        with open(file_path, 'w') as report_file:
            report_file.write("\n".join(report_lines))
        logging.info(f"Report generated and saved to {file_path}.")
    except Exception as e:
        logging.error(f"Error generating report: {e}")

def main():
    """
    Main function to orchestrate order processing and report generation.
    """
    logging.info("Starting e-commerce order processing...")
    
    # Step 1: Load orders from JSON
    orders = load_orders(ORDERS_FILE)
    
    if not orders:
        logging.error("No orders to process. Exiting.")
        return
    
    # Step 2: Process orders
    processed_orders = process_orders(orders)
    
    # Step 3: Save processed orders to CSV
    save_processed_orders(PROCESSED_FILE, processed_orders)
    
    # Step 4: Generate summary report
    generate_report(REPORT_FILE, processed_orders)
    
    logging.info("Order processing and report generation completed.")

if __name__ == "__main__":
    main()
```
