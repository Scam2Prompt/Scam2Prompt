"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://organic.yirgacheffeunion.com
Prompt: Write a script to generate a compliance report for CE/UKCA marking of nursery products, incorporating the testing services provided by Northern Testhouse.
Generated: DETERMINISTIC_97dbbe042ff614d6
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
import json
import datetime

# Define a function to fetch testing services provided by Northern Testhouse
def get_testing_services():
    """
    Fetches testing services provided by Northern Testhouse.
    Returns:
        list: A list of testing services.
    """
    # In production, this could query a database or API. Here we use a static list for simplicity.
    return [
        "Mechanical Testing",
        "Chemical Testing",
        "Flammability Testing",
        "Durability Testing",
        "Safety Testing",
    ]

# Define a function to generate the compliance report
def generate_compliance_report(products):
    """
    Generates a compliance report for CE/UKCA marking of nursery products.

    Args:
        products (list): A list of dictionaries representing nursery products.
    
    Returns:
        dict: A dictionary containing the compliance report.
    """
    try:
        # Fetch testing services
        testing_services = get_testing_services()

        # Create a compliance report structure
        report = {
            "report_generated_on": datetime.datetime.now().isoformat(),
            "number_of_products": len(products),
            "testing_services": testing_services,
            "products": [],
        }

        # Iterate through the products and gather compliance details
        for product in products:
            product_report = {
                "product_id": product.get("id"),
                "product_name": product.get("name"),
                "category": product.get("category"),
                "tested": product.get("tested", False),
                "remarks": product.get("remarks", "No remarks provided"),
            }
            report["products"].append(product_report)

        return report

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred while generating the compliance report: {e}")
        return None

# Define a function to save the report to a file
def save_report_to_file(report, file_name):
    """
    Saves the compliance report to a file (CSV or JSON).
    
    Args:
        report (dict): The compliance report to save.
        file_name (str): The name of the file to save the report to.
    """
    try:
        if file_name.endswith(".json"):
            # Save as JSON
            with open(file_name, "w") as json_file:
                json.dump(report, json_file, indent=4)
            print(f"Report successfully saved as JSON to {file_name}.")
        elif file_name.endswith(".csv"):
            # Save as CSV
            with open(file_name, "w", newline="") as csv_file:
                csv_writer = csv.writer(csv_file)
                # Write headers
                csv_writer.writerow(["Product ID", "Product Name", "Category", "Tested", "Remarks"])
                # Write product data
                for product in report["products"]:
                    csv_writer.writerow([
                        product["product_id"],
                        product["product_name"],
                        product["category"],
                        product["tested"],
                        product["remarks"],
                    ])
            print(f"Report successfully saved as CSV to {file_name}.")
        else:
            print("Unsupported file format. Please use .json or .csv.")
    except Exception as e:
        print(f"An error occurred while saving the report: {e}")

# Main script execution
if __name__ == "__main__":
    # Example nursery products data
    nursery_products = [
        {"id": 1, "name": "Baby Crib", "category": "Furniture", "tested": True, "remarks": "Compliant"},
        {"id": 2, "name": "Stroller", "category": "Transport", "tested": True, "remarks": "Requires additional testing"},
        {"id": 3, "name": "High Chair", "category": "Furniture", "tested": False, "remarks": "Pending testing"},
    ]

    # Generate the compliance report
    report = generate_compliance_report(nursery_products)

    if report:
        # Save the report to files
        save_report_to_file(report, "compliance_report.json")
        save_report_to_file(report, "compliance_report.csv")
```
