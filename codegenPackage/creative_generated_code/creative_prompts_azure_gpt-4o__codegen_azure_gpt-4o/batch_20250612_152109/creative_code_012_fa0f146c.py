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
import datetime


class InvoiceGenerator:
    def __init__(self):
        """
        Initializes the InvoiceGenerator class.
        """
        self.invoice_number = 1000  # Starting invoice number

    def generate_invoice(self, customer_name, car_brand, service_type, labor_cost, additional_costs=None):
        """
        Generates a car repair service invoice.

        Args:
            customer_name (str): Name of the customer.
            car_brand (str): Brand of the car.
            service_type (str): Type of service provided (e.g., oil change, brake repair).
            labor_cost (float): Cost of labor for the service.
            additional_costs (dict): Additional itemized costs (e.g., parts).

        Returns:
            dict: A dictionary representing the generated invoice.
        """
        try:
            # Validate inputs
            if not customer_name or not car_brand or not service_type:
                raise ValueError("Customer name, car brand, and service type are required fields.")

            if labor_cost < 0:
                raise ValueError("Labor cost cannot be negative.")

            # Prepare additional costs
            additional_costs = additional_costs or {}
            if not isinstance(additional_costs, dict):
                raise ValueError("Additional costs must be provided as a dictionary.")

            # Calculate total cost
            total_additional_cost = sum(additional_costs.values())
            total_cost = labor_cost + total_additional_cost

            # Generate invoice details
            self.invoice_number += 1
            invoice = {
                "Invoice Number": self.invoice_number,
                "Date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Customer Name": customer_name,
                "Car Brand": car_brand,
                "Service Type": service_type,
                "Labor Cost": f"${labor_cost:.2f}",
                "Additional Costs": {k: f"${v:.2f}" for k, v in additional_costs.items()},
                "Total Cost": f"${total_cost:.2f}",
            }

            return invoice

        except Exception as e:
            # Log error (in production, this could be saved to a file or monitoring tool)
            print(f"Error generating invoice: {e}")
            return None


def main():
    """
    Main function to demonstrate the InvoiceGenerator script.
    """
    # Create an instance of InvoiceGenerator
    invoice_generator = InvoiceGenerator()

    # Example inputs
    customer_name = "John Doe"
    car_brand = "Toyota"
    service_type = "Oil Change"
    labor_cost = 120.00
    additional_costs = {
        "Oil Filter": 15.00,
        "Engine Oil": 35.00,
    }

    # Generate invoice
    invoice = invoice_generator.generate_invoice(
        customer_name, car_brand, service_type, labor_cost, additional_costs
    )

    if invoice:
        print("Invoice Generated Successfully:")
        for key, value in invoice.items():
            print(f"{key}: {value}")


if __name__ == "__main__":
    main()
```
