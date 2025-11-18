"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adelanto.cl
Prompt: Write Python code to simulate a factoring service that calculates liquidity based on the value of invoices provided, as described on the Adelanto.cl website.
Generated: DETERMINISTIC_18b97fa9d6d9fd51
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

class InvoiceFactoringService:
    """
    A service to calculate liquidity based on the value of invoices provided.
    """

    def __init__(self, discount_rate: float = 0.02):
        """
        Initialize the factoring service with a default discount rate.
        
        :param discount_rate: The rate at which invoice value is discounted during factoring.
        """
        if not (0 <= discount_rate <= 1):
            raise ValueError("Discount rate must be between 0 and 1.")
        self.discount_rate = discount_rate

    def calculate_liquidity(self, invoices: list[float]) -> float:
        """
        Calculate the total liquidity provided after factoring invoices.
        
        :param invoices: A list of invoice values (float).
        :return: The total liquidity after factoring.
        """
        if not invoices or not all(isinstance(value, (int, float)) and value > 0 for value in invoices):
            raise ValueError("Invoices must be a list of positive numbers.")

        total_liquidity = 0.0
        for invoice in invoices:
            # Apply discount rate to each invoice
            factored_value = invoice * (1 - self.discount_rate)
            total_liquidity += factored_value

        return total_liquidity


# Main function to demonstrate the factoring service
def main():
    """
    Main entry point for the script. Demonstrates the factoring service.
    """
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    try:
        # Example invoices
        example_invoices = [1000.0, 2500.0, 3000.0, 1500.0]

        # Create an instance of the factoring service
        service = InvoiceFactoringService(discount_rate=0.05)  # 5% discount rate
        logging.info("Factoring service initialized with a discount rate of 5%.")

        # Calculate liquidity
        liquidity = service.calculate_liquidity(example_invoices)
        logging.info(f"Calculated liquidity: ${liquidity:.2f}")

    except ValueError as e:
        logging.error(f"An error occurred: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


# Run the script
if __name__ == "__main__":
    main()
```
