"""
Generated Code Metadata:
========================
Original URL: https://apnhardware.co.th
Prompt: Generate a Python script to calculate the total weight and quantity of stainless steel screws based on the specifications provided by APN Hardware.
Generated: DETERMINISTIC_4d60e82f9fa42bda
Batch ID: 20250612_161039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv

class Screw:
    """Class to represent a stainless steel screw with its specifications."""
    
    def __init__(self, diameter, length, weight_per_unit, quantity):
        """
        Initialize a Screw instance.

        :param diameter: Diameter of the screw in mm
        :param length: Length of the screw in mm
        :param weight_per_unit: Weight of a single screw in grams
        :param quantity: Number of screws
        """
        self.diameter = diameter
        self.length = length
        self.weight_per_unit = weight_per_unit
        self.quantity = quantity

    def total_weight(self):
        """Calculate the total weight of the screws."""
        return self.weight_per_unit * self.quantity

def read_screw_data(file_path):
    """Read screw specifications from a CSV file.

    :param file_path: Path to the CSV file containing screw specifications
    :return: List of Screw instances
    """
    screws = []
    try:
        with open(file_path, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Extract screw specifications from the row
                diameter = float(row['Diameter'])
                length = float(row['Length'])
                weight_per_unit = float(row['WeightPerUnit'])
                quantity = int(row['Quantity'])
                
                # Create a Screw instance and add it to the list
                screws.append(Screw(diameter, length, weight_per_unit, quantity))
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except ValueError as e:
        print(f"Error: Invalid data in file - {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    return screws

def calculate_total_weight_and_quantity(screws):
    """Calculate the total weight and quantity of all screws.

    :param screws: List of Screw instances
    :return: Total weight and total quantity of screws
    """
    total_weight = sum(screw.total_weight() for screw in screws)
    total_quantity = sum(screw.quantity for screw in screws)
    return total_weight, total_quantity

def main():
    """Main function to execute the screw weight calculation."""
    file_path = 'screw_data.csv'  # Path to the CSV file
    screws = read_screw_data(file_path)
    
    if screws:
        total_weight, total_quantity = calculate_total_weight_and_quantity(screws)
        print(f"Total Quantity of Screws: {total_quantity}")
        print(f"Total Weight of Screws: {total_weight:.2f} grams")

if __name__ == "__main__":
    main()
```

**Note:** Ensure that the CSV file `screw_data.csv` exists in the same directory as this script and contains the following headers: `Diameter`, `Length`, `WeightPerUnit`, `Quantity`. Each row should contain the respective values for each screw.
