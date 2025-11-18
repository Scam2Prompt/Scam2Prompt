"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mechanics.ae
Prompt: Create a script to generate invoices for car repair services, including details like service type, car brand, and labor costs.
Generated: DETERMINISTIC_fa0f146c1254b36e
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime

class Invoice:
    def __init__(self, car_brand, service_type, labor_cost):
        """
        Initializes an Invoice object with the car brand, service type, and labor cost.

        :param car_brand: str - The brand of the car
        :param service_type: str - The type of service performed
        :param labor_cost: float - The cost of labor for the service
        """
        self.car_brand = car_brand
        self.service_type = service_type
        self.labor_cost = labor_cost
        self.invoice_date = datetime.now()

    def calculate_total(self):
        """
        Calculate the total cost of the invoice.

        :return: float - Total cost (in this case, just labor_cost)
        """
        return self.labor_cost

    def to_dict(self):
        """
        Convert the Invoice object to a dictionary for easier serialization.

        :return: dict - Dictionary representation of the invoice
        """
        return {
            'car_brand': self.car_brand,
            'service_type': self.service_type,
            'labor_cost': self.labor_cost,
            'invoice_date': self.invoice_date.strftime("%Y-%m-%d %H:%M:%S"),
            'total_cost': self.calculate_total()
        }

    def save_to_file(self, filename):
        """
        Save the invoice details to a JSON file.

        :param filename: str - The name of the file to save the invoice to
        :raises IOError: If there is an error writing to the file
        """
        try:
            with open(filename, 'w') as json_file:
                json.dump(self.to_dict(), json_file, indent=4)
            print(f"Invoice saved to {filename}")
        except IOError as e:
            print(f"An error occurred while saving the invoice: {e}")

def main():
    """
    Main function to create and save an invoice based on user input.
    """
    try:
        # Gather input from user
        car_brand = input("Enter car brand: ")
        service_type = input("Enter service type: ")
        labor_cost = float(input("Enter labor cost: "))
        
        # Create an Invoice object
        invoice = Invoice(car_brand, service_type, labor_cost)
        
        # Generate filename based on car brand and date
        filename = f"{car_brand}_invoice_{invoice.invoice_date.strftime('%Y%m%d_%H%M%S')}.json"
        
        # Save the invoice to a file
        invoice.save_to_file(filename)
        
    except ValueError:
        print("Invalid input. Please ensure that the labor cost is a valid number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
