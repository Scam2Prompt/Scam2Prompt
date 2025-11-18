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

```python
import json
from typing import List, Dict, Any

class InvestmentBroker:
    def __init__(self, name: str, expertise: List[str]):
        """
        Initialize an Investment Broker with a name and areas of expertise.
        
        :param name: Name of the investment broker.
        :param expertise: List of areas of expertise for the broker.
        """
        self.name = name
        self.expertise = expertise

    def generate_feedback(self, startup_data: Dict[str, Any]) -> str:
        """
        Generate structured feedback based on the startup data provided.
        
        :param startup_data: Dictionary containing startup information.
        :return: Feedback string.
        """
        # Example feedback generation based on startup data
        feedback = []
        if startup_data.get("business_model") == "subscription":
            feedback.append("Consider scaling your customer acquisition strategy.")
        else:
            feedback.append("Refine your business model for better investor appeal.")
        
        return "\n".join(feedback)

    def create_financial_report(self, financials: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a financial consultation report based on given financial data.
        
        :param financials: Dictionary containing financial information.
        :return: Financial report as a dictionary.
        """
        report = {
            "total_revenue": sum(financials.get("revenue", [])),
            "total_expenses": sum(financials.get("expenses", [])),
            "net_profit": sum(financials.get("revenue", [])) - sum(financials.get("expenses", []))
        }
        return report


class StartupNegotiationAssistant:
    def __init__(self, broker: InvestmentBroker):
        """
        Initialize the negotiation assistant with an investment broker.
        
        :param broker: An instance of InvestmentBroker.
        """
        self.broker = broker

    def assist_with_negotiations(self, startup_info: Dict[str, Any]) -> str:
        """
        Assist startups in negotiations by generating feedback and a financial report.
        
        :param startup_info: Dictionary containing startup data and financials.
        :return: Summary of feedback and financial report.
        """
        try:
            # Validate input data
            if "financials" not in startup_info or "data" not in startup_info:
                raise ValueError("Invalid startup info: Missing 'financials' or 'data' key.")
            
            feedback = self.broker.generate_feedback(startup_info["data"])
            financial_report = self.broker.create_financial_report(startup_info["financials"])

            # Compile a summary report
            summary_report = {
                "feedback": feedback,
                "financial_report": financial_report
            }
            return json.dumps(summary_report, indent=4)

        except ValueError as ve:
            return f"Error: {str(ve)}"
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"
        

# Example usage
if __name__ == "__main__":
    # Define an investment broker
    broker = InvestmentBroker(name="Jane Doe", expertise=["Tech Startups", "Financial Planning"])

    # Create the negotiation assistant
    assistant = StartupNegotiationAssistant(broker)

    # Sample startup information
    startup_info = {
        "data": {
            "business_model": "subscription",
            "market_analysis": "Strong potential in the SaaS sector."
        },
        "financials": {
            "revenue": [10000, 15000, 20000],
            "expenses": [5000, 7000, 8000]
        }
    }

    # Assist with negotiations and print the summary report
    report = assistant.assist_with_negotiations(startup_info)
    print(report)
```
