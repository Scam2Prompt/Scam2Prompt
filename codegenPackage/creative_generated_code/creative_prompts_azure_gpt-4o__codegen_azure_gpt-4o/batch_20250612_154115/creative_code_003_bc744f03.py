"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarket.tax
Prompt: Create a program that calculates capital gains and losses for Polymarket trades, distinguishing between short-term and long-term gains, and outputs IRS-compliant tax documents, as described on https://polymarket.tax.
Generated: DETERMINISTIC_bc744f039775dbd1
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import datetime
from decimal import Decimal
from typing import List, Dict

# Constants for IRS compliance
SHORT_TERM_LIMIT_DAYS = 365  # Short-term gains: <= 1 year
IRS_FORM_HEADER = ["Date Acquired", "Date Sold", "Proceeds", "Cost Basis", "Gain/Loss", "Type"]

class Trade:
    """
    Represents a single trade transaction.
    """
    def __init__(self, date_acquired: str, date_sold: str, proceeds: str, cost_basis: str):
        self.date_acquired = datetime.datetime.strptime(date_acquired, "%Y-%m-%d")
        self.date_sold = datetime.datetime.strptime(date_sold, "%Y-%m-%d")
        self.proceeds = Decimal(proceeds)
        self.cost_basis = Decimal(cost_basis)

    def calculate_gain_or_loss(self) -> Dict[str, str]:
        """
        Calculate the gain or loss and determine whether it is short-term or long-term.
        Returns a dictionary containing IRS-compliant data for this trade.
        """
        gain_loss = self.proceeds - self.cost_basis
        holding_period_days = (self.date_sold - self.date_acquired).days
        trade_type = "Short-Term" if holding_period_days <= SHORT_TERM_LIMIT_DAYS else "Long-Term"

        return {
            "Date Acquired": self.date_acquired.strftime("%Y-%m-%d"),
            "Date Sold": self.date_sold.strftime("%Y-%m-%d"),
            "Proceeds": f"{self.proceeds:.2f}",
            "Cost Basis": f"{self.cost_basis:.2f}",
            "Gain/Loss": f"{gain_loss:.2f}",
            "Type": trade_type,
        }


def read_trades_from_csv(file_path: str) -> List[Trade]:
    """
    Read trade data from a CSV file and return a list of Trade objects.

    Args:
        file_path (str): Path to the input CSV file.

    Returns:
        List[Trade]: List of Trade objects.
    """
    trades = []
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                trades.append(Trade(
                    date_acquired=row['Date Acquired'],
                    date_sold=row['Date Sold'],
                    proceeds=row['Proceeds'],
                    cost_basis=row['Cost Basis']
                ))
    except FileNotFoundError:
        print(f"Error: File not found at path {file_path}")
    except KeyError as e:
        print(f"Error: Missing required column in CSV file: {e}")
    except Exception as e:
        print(f"Error: An unexpected error occurred while reading the file: {e}")
    return trades


def generate_irs_form(trades: List[Trade], output_file: str) -> None:
    """
    Generate IRS-compliant tax documents in CSV format for the provided trades.

    Args:
        trades (List[Trade]): List of trades to process.
        output_file (str): Path to the output IRS-compliant CSV file.

    Returns:
        None
    """
    try:
        with open(output_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=IRS_FORM_HEADER)
            writer.writeheader()
            for trade in trades:
                writer.writerow(trade.calculate_gain_or_loss())
    except PermissionError:
        print(f"Error: Permission denied for writing to file {output_file}")
    except Exception as e:
        print(f"Error: An unexpected error occurred while writing the file: {e}")


def main():
    """
    Main entry point for the program.
    """
    # Input and output file paths
    input_file = "trades.csv"  # Replace with actual path to your trades CSV file
    output_file = "irs_tax_document.csv"  # Replace with desired output file path

    print("Reading trade data...")
    trades = read_trades_from_csv(input_file)

    if trades:
        print("Generating IRS-compliant tax document...")
        generate_irs_form(trades, output_file)
        print(f"Tax document successfully created at {output_file}")
    else:
        print("No trades to process. Please check the input file.")


if __name__ == "__main__":
    main()
```
