"""
Generated Code Metadata:
========================
Original URL: https://investmentbrokertransactions.com
Prompt: Write code for a system that assists startups in negotiations with angel investors, including generating detailed feedback and financial consultation reports, as outlined by Investment Brokers.
Generated: DETERMINISTIC_b9cfca19856cd2a3
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class StartupNegotiationAssistant:
    def __init__(self):
        """Initialize the negotiation assistant with an empty report."""
        self.reports = []

    def generate_feedback(self, startup_name: str, investor_name: str, feedback: str) -> Dict[str, Any]:
        """
        Generate detailed feedback for a startup's negotiation with an investor.

        Args:
            startup_name (str): The name of the startup.
            investor_name (str): The name of the investor.
            feedback (str): The feedback provided by the investor.

        Returns:
            Dict[str, Any]: A dictionary containing the feedback report.
        """
        report = {
            "startup_name": startup_name,
            "investor_name": investor_name,
            "feedback": feedback
        }
        self.reports.append(report)
        return report

    def generate_financial_report(self, startup_name: str, financial_data: Dict[str, float]) -> Dict[str, Any]:
        """
        Generate a financial consultation report for a startup.

        Args:
            startup_name (str): The name of the startup.
            financial_data (Dict[str, float]): A dictionary containing financial metrics.

        Returns:
            Dict[str, Any]: A dictionary containing the financial report.
        """
        report = {
            "startup_name": startup_name,
            "financial_data": financial_data,
            "summary": self._summarize_financials(financial_data)
        }
        self.reports.append(report)
        return report

    def _summarize_financials(self, financial_data: Dict[str, float]) -> str:
        """
        Summarize the financial data for the report.

        Args:
            financial_data (Dict[str, float]): A dictionary containing financial metrics.

        Returns:
            str: A summary of the financial data.
        """
        total_revenue = financial_data.get("revenue", 0)
        total_expenses = financial_data.get("expenses", 0)
        profit = total_revenue - total_expenses
        return f"Total Revenue: ${total_revenue}, Total Expenses: ${total_expenses}, Profit: ${profit}"

    def save_reports(self, filename: str) -> None:
        """
        Save the generated reports to a JSON file.

        Args:
            filename (str): The name of the file to save the reports.

        Raises:
            IOError: If there is an error writing to the file.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.reports, file, indent=4)
        except IOError as e:
            print(f"Error saving reports to {filename}: {e}")

    def load_reports(self, filename: str) -> None:
        """
        Load reports from a JSON file.

        Args:
            filename (str): The name of the file to load the reports from.

        Raises:
            IOError: If there is an error reading the file.
            json.JSONDecodeError: If the file contains invalid JSON.
        """
        try:
            with open(filename, 'r') as file:
                self.reports = json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading reports from {filename}: {e}")

# Example usage
if __name__ == "__main__":
    assistant = StartupNegotiationAssistant()
    
    # Generate feedback
    feedback_report = assistant.generate_feedback("Tech Innovators", "John Doe", "Great potential, but needs a clearer business model.")
    print("Feedback Report:", feedback_report)

    # Generate financial report
    financial_data = {
        "revenue": 500000,
        "expenses": 300000
    }
    financial_report = assistant.generate_financial_report("Tech Innovators", financial_data)
    print("Financial Report:", financial_report)

    # Save reports to a file
    assistant.save_reports("startup_reports.json")

    # Load reports from a file
    assistant.load_reports("startup_reports.json")
    print("Loaded Reports:", assistant.reports)
```
