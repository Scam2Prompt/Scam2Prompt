"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://investmentbrokertransactions.com
Prompt: Write code for a system that assists startups in negotiations with angel investors, including generating detailed feedback and financial consultation reports, as outlined by Investment Brokers.
Generated: DETERMINISTIC_b9cfca19856cd2a3
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Sure! Below is a Python implementation for the requested system.

```python
import json
from datetime import datetime

class InvestmentBroker:
    """
    Class representing an Investment Broker that assists startups with 
    negotiations and generates financial consultation reports.
    """

    def __init__(self, broker_name: str):
        """
        Initializes the InvestmentBroker instance.

        Args:
            broker_name (str): Name of the broker.
        """
        self.broker_name = broker_name
        self.startup_data = []

    def add_startup_data(self, startup_name: str, annual_revenue: float, funding_requested: float, equity_offered: float):
        """
        Adds startup data for financial consultation.

        Args:
            startup_name (str): Name of the startup.
            annual_revenue (float): Annual revenue of the startup (in USD).
            funding_requested (float): Amount of funding requested (in USD).
            equity_offered (float): Equity offered to investors (as a percentage).
        """
        try:
            if not (0 < equity_offered <= 100):
                raise ValueError("Equity offered must be between 0 and 100 (exclusive).")
            if annual_revenue < 0 or funding_requested < 0:
                raise ValueError("Annual revenue and funding requested must be non-negative.")
            
            startup_entry = {
                "name": startup_name,
                "annual_revenue": annual_revenue,
                "funding_requested": funding_requested,
                "equity_offered": equity_offered,
                "feedback": None,
                "report_generated": False
            }
            self.startup_data.append(startup_entry)
        except ValueError as e:
            print(f"Error adding startup data: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def generate_feedback(self, startup_name: str) -> str:
        """
        Generates negotiation feedback for a specified startup.

        Args:
            startup_name (str): Name of the startup.

        Returns:
            str: Feedback for the startup.
        """
        for startup in self.startup_data:
            if startup["name"] == startup_name:
                # Basic feedback generation logic
                if startup["annual_revenue"] < 100000:
                    feedback = f"{startup_name} should focus on increasing revenue before seeking funding."
                elif startup["equity_offered"] > 20:
                    feedback = f"{startup_name} is offering too much equity. Consider lowering it to attract better investors."
                else:
                    feedback = f"{startup_name}'s proposal looks promising. Proceed with negotiations."

                startup["feedback"] = feedback
                return feedback
        
        return f"Startup '{startup_name}' not found in the system."

    def generate_consultation_report(self, startup_name: str) -> str:
        """
        Generates a detailed financial consultation report for a specified startup.

        Args:
            startup_name (str): Name of the startup.

        Returns:
            str: Path to the generated report file.
        """
        for startup in self.startup_data:
            if startup["name"] == startup_name:
                try:
                    report_data = {
                        "Broker Name": self.broker_name,
                        "Startup Name": startup["name"],
                        "Annual Revenue": startup["annual_revenue"],
                        "Funding Requested": startup["funding_requested"],
                        "Equity Offered": startup["equity_offered"],
                        "Feedback": startup["feedback"],
                        "Report Generated At": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    }
                    report_path = f"{startup_name.replace(' ', '_')}_consultation_report.json"
                    with open(report_path, "w") as report_file:
                        json.dump(report_data, report_file, indent=4)
                    startup["report_generated"] = True
                    return report_path
                except Exception as e:
                    print(f"Error generating report: {e}")
                    return None
        
        return f"Startup '{startup_name}' not found in the system."

    def get_startup_data(self) -> list:
        """
        Returns all stored startup data.

        Returns:
            list: List of startup data.
        """
        return self.startup_data


if __name__ == "__main__":
    # Example usage
    broker = InvestmentBroker("Smith Investment Group")
    
    # Adding startup data
    broker.add_startup_data("Tech Innovators", 500000, 250000, 15)
    broker.add_startup_data("Green Energy Co", 75000, 100000, 25)  # Feedback will suggest lowering equity
    broker.add_startup_data("EduTech Startups", -50000, 50000, 10)  # Error: Negative revenue

    # Generating feedback and consultation reports
    print(broker.generate_feedback("Tech Innovators"))
    print(broker.generate_feedback("Green Energy Co"))

    report = broker.generate_consultation_report("Tech Innovators")
    if report:
        print(f"Consultation report generated at: {report}")

    print(json.dumps(broker.get_startup_data(), indent=4))
```

### Features:
1. Proper error handling for invalid inputs.
2. JSON-based report generation for scalability.
3. Feedback generation based on simple business logic.

### To run:
Save the code in a `.py` file and execute it using Python. Adjust startup names and parameters as needed for testing.
