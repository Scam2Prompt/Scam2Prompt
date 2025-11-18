"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-neupro.co
Prompt: Create a program that generates real-time reports on investment progress, inspired by the "informes instantáneos" feature described on Portefeuille Vexo.
Generated: DETERMINISTIC_c93ac8cccc166bd4
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random
from datetime import datetime

class InvestmentReportGenerator:
    """
    A class to generate real-time investment progress reports.
    """

    def __init__(self, investment_name, initial_balance):
        """
        Initializes the InvestmentReportGenerator with an investment name and initial balance.

        Args:
            investment_name (str): Name of the investment.
            initial_balance (float): Starting balance of the investment.
        """
        self.investment_name = investment_name
        self.balance = initial_balance
        self.start_time = datetime.now()

    def simulate_market_fluctuation(self):
        """
        Simulates market fluctuations, randomly adjusting the balance.

        Returns:
            float: Updated balance after applying a random fluctuation.
        """
        fluctuation = random.uniform(-0.1, 0.1)  # Simulate +/- 10% market changes
        self.balance += self.balance * fluctuation
        return round(self.balance, 2)

    def generate_report(self):
        """
        Generates a real-time investment progress report.

        Returns:
            dict: A dictionary containing the report data.
        """
        current_time = datetime.now()
        elapsed_time = (current_time - self.start_time).total_seconds() / 60  # Minutes elapsed
        report = {
            "investment_name": self.investment_name,
            "current_balance": round(self.balance, 2),
            "elapsed_time_minutes": round(elapsed_time, 2),
            "report_generated_at": current_time.strftime("%Y-%m-%d %H:%M:%S"),
        }
        return report

    def display_report(self):
        """
        Displays the investment report in a readable format.
        """
        report = self.generate_report()
        print("\n--- Investment Progress Report ---")
        print(f"Investment Name: {report['investment_name']}")
        print(f"Current Balance: ${report['current_balance']}")
        print(f"Elapsed Time: {report['elapsed_time_minutes']} minutes")
        print(f"Report Generated At: {report['report_generated_at']}")
        print("---------------------------------\n")

def main():
    """
    Main function to run the real-time investment report generator.
    """
    try:
        # Initialize the investment report generator
        investment_name = input("Enter the investment name: ")
        initial_balance = float(input("Enter the initial balance (e.g., 1000.00): "))
        generator = InvestmentReportGenerator(investment_name, initial_balance)

        print("\nStarting real-time investment reporting...\n")
        # Generate and display reports in real-time
        while True:
            time.sleep(5)  # Generate report every 5 seconds
            generator.simulate_market_fluctuation()  # Simulate market changes
            generator.display_report()

    except ValueError as ve:
        print(f"Input Error: {ve}. Please enter valid numeric values.")

    except KeyboardInterrupt:
        print("\nReal-time reporting stopped by user.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
