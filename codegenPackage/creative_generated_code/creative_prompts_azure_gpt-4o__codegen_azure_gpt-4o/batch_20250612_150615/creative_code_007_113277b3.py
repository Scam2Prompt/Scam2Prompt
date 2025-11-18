"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://currency-connect.com
Prompt: Write code to generate a report showing the savings achieved by using a specialized currency exchange service for legal transactions compared to traditional banking methods.
Generated: DETERMINISTIC_113277b389793ab5
Batch ID: 20250612_150615
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

class CurrencyExchangeService:
    """
    A class to simulate a specialized currency exchange service.
    """
    def __init__(self, service_rate):
        """
        Initialize with a specific exchange rate for the specialized service.
        :param service_rate: The rate charged by the specialized service (as a percentage of the transaction amount).
        """
        self.service_rate = service_rate

    def calculate_cost(self, amount):
        """
        Calculate the cost of exchange for a given transaction amount using the specialized service.
        :param amount: Transaction amount.
        :return: Cost of exchange for this transaction.
        """
        return amount * (self.service_rate / 100)


class TraditionalBank:
    """
    A class to simulate a traditional banking method for currency exchange.
    """
    def __init__(self, bank_rate):
        """
        Initialize with a specific exchange rate for the bank.
        :param bank_rate: The rate charged by the bank (as a percentage of the transaction amount).
        """
        self.bank_rate = bank_rate

    def calculate_cost(self, amount):
        """
        Calculate the cost of exchange for a given transaction amount using the bank.
        :param amount: Transaction amount.
        :return: Cost of exchange for this transaction.
        """
        return amount * (self.bank_rate / 100)


def generate_report(transactions, service, bank, output_file):
    """
    Generate a report showing the savings achieved by using the specialized currency exchange service.
    :param transactions: A list of transaction amounts.
    :param service: An instance of CurrencyExchangeService.
    :param bank: An instance of TraditionalBank.
    :param output_file: Path to the output CSV file for the report.
    :return: None
    """
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    try:
        with open(output_file, mode='w', newline='') as file:
            writer = csv.writer(file)

            # Write header row
            writer.writerow(["Transaction Amount", "Bank Cost", "Service Cost", "Savings"])

            # Process each transaction
            for amount in transactions:
                bank_cost = bank.calculate_cost(amount)
                service_cost = service.calculate_cost(amount)
                savings = bank_cost - service_cost

                # Write transaction data
                writer.writerow([amount, round(bank_cost, 2), round(service_cost, 2), round(savings, 2)])

    except IOError as e:
        print(f"Error while writing the report: {e}")


if __name__ == "__main__":
    # Sample data
    transactions = [1000, 2500, 5000, 10000, 20000]  # Transaction amounts in USD

    # Initialize services
    specialized_service = CurrencyExchangeService(service_rate=1.5)  # Specialized service with 1.5% rate
    traditional_bank = TraditionalBank(bank_rate=3.0)  # Traditional bank with 3.0% rate

    # Generate and save report
    report_file = "reports/savings_report.csv"  # Output file path
    generate_report(transactions, specialized_service, traditional_bank, report_file)

    print(f"Report generated successfully and saved to {report_file}")
```
