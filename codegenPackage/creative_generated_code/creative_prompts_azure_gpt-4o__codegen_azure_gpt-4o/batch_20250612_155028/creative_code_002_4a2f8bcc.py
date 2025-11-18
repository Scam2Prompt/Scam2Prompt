"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stelllar.org
Prompt: Generate a script to calculate on-time delivery rates for shipments using Stelllar Logistics' performance metrics (e.g., 99.4% on-time delivery rate).
Generated: DETERMINISTIC_4a2f8bcc823a1375
Batch ID: 20250612_155028
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import sys


def calculate_on_time_delivery_rate(shipments):
    """
    Calculate the on-time delivery rate based on shipment data.

    Args:
        shipments (list of dict): A list of dictionaries containing shipment data.
                                  Each dictionary must have a 'delivered_on_time' key
                                  with a boolean value.

    Returns:
        float: The on-time delivery rate as a percentage.
    """
    if not shipments:
        raise ValueError("Shipment list is empty. Cannot calculate delivery rate.")

    total_shipments = len(shipments)
    on_time_deliveries = sum(1 for shipment in shipments if shipment.get('delivered_on_time', False))

    return (on_time_deliveries / total_shipments) * 100


def read_shipment_data(file_path):
    """
    Read shipment data from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing shipment data.

    Returns:
        list of dict: A list of dictionaries containing shipment data.
    """
    shipments = []
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert 'delivered_on_time' field to boolean if present
                if 'delivered_on_time' in row:
                    row['delivered_on_time'] = row['delivered_on_time'].strip().lower() == 'true'
                shipments.append(row)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except Exception as e:
        raise Exception(f"Error reading file: {e}")

    return shipments


def main():
    """
    Main function to calculate and display the on-time delivery rate.
    """
    try:
        # File path to the shipment data CSV file (adjust as needed)
        file_path = 'shipment_data.csv'

        # Read shipment data from the file
        shipments = read_shipment_data(file_path)

        # Calculate the on-time delivery rate
        on_time_rate = calculate_on_time_delivery_rate(shipments)

        # Display the result
        print(f"On-Time Delivery Rate: {on_time_rate:.2f}%")

    except ValueError as ve:
        print(f"Error: {ve}")
    except FileNotFoundError as fnfe:
        print(f"Error: {fnfe}")
    except Exception as e:
        print(f"Error: {e}")


# Entry point of the script
if __name__ == "__main__":
    main()
```
