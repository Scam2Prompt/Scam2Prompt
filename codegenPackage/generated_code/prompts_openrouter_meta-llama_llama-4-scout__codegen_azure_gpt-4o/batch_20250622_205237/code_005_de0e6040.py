"""
Generated Code Metadata:
========================
Original URL: https://assettrackr.app
Prompt: Generate a sample code for an investment management system that provides transparent and practical guidance to clients, similar to Grade World Investment Limited's approach to financial planning.
Generated: DETERMINISTIC_de0e6040bfbdcc9c
Batch ID: 20250622_205237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class InvestmentManagementSystem:
    """
    A class to manage investments and provide transparent financial guidance to clients.
    """

    def __init__(self):
        """
        Initialize the investment management system with an empty client portfolio.
        """
        self.clients = {}

    def add_client(self, client_id, name):
        """
        Add a new client to the system.

        :param client_id: Unique identifier for the client
        :param name: Name of the client
        """
        if client_id in self.clients:
            raise ValueError(f"Client ID {client_id} already exists.")
        self.clients[client_id] = {
            "name": name,
            "portfolio": [],
            "created_at": datetime.datetime.now()
        }

    def add_investment(self, client_id, investment_name, amount, risk_level):
        """
        Add an investment to a client's portfolio.

        :param client_id: Unique identifier for the client
        :param investment_name: Name of the investment
        :param amount: Amount invested
        :param risk_level: Risk level of the investment (e.g., "Low", "Medium", "High")
        """
        if client_id not in self.clients:
            raise ValueError(f"Client ID {client_id} does not exist.")
        if amount <= 0:
            raise ValueError("Investment amount must be greater than zero.")
        if risk_level not in ["Low", "Medium", "High"]:
            raise ValueError("Invalid risk level. Choose from 'Low', 'Medium', or 'High'.")

        investment = {
            "investment_name": investment_name,
            "amount": amount,
            "risk_level": risk_level,
            "date_added": datetime.datetime.now()
        }
        self.clients[client_id]["portfolio"].append(investment)

    def get_portfolio(self, client_id):
        """
        Retrieve the portfolio of a specific client.

        :param client_id: Unique identifier for the client
        :return: List of investments in the client's portfolio
        """
        if client_id not in self.clients:
            raise ValueError(f"Client ID {client_id} does not exist.")
        return self.clients[client_id]["portfolio"]

    def generate_report(self, client_id):
        """
        Generate a financial report for a specific client.

        :param client_id: Unique identifier for the client
        :return: A string report summarizing the client's portfolio
        """
        if client_id not in self.clients:
            raise ValueError(f"Client ID {client_id} does not exist.")

        client = self.clients[client_id]
        report = f"Financial Report for {client['name']} (Client ID: {client_id})\n"
        report += f"Created At: {client['created_at']}\n"
        report += "Portfolio:\n"

        total_investment = 0
        for investment in client["portfolio"]:
            report += f"- {investment['investment_name']}: ${investment['amount']} (Risk: {investment['risk_level']})\n"
            total_investment += investment["amount"]

        report += f"Total Investment: ${total_investment}\n"
        return report


# Example usage
if __name__ == "__main__":
    try:
        system = InvestmentManagementSystem()

        # Add clients
        system.add_client(client_id=1, name="Alice Johnson")
        system.add_client(client_id=2, name="Bob Smith")

        # Add investments
        system.add_investment(client_id=1, investment_name="Real Estate Fund", amount=50000, risk_level="Medium")
        system.add_investment(client_id=1, investment_name="Tech Stocks", amount=20000, risk_level="High")
        system.add_investment(client_id=2, investment_name="Government Bonds", amount=30000, risk_level="Low")

        # Generate reports
        print(system.generate_report(client_id=1))
        print(system.generate_report(client_id=2))

    except Exception as e:
        print(f"Error: {e}")
```
