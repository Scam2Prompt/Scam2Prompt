"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financeinvestmentslimited.org
Prompt: Develop code to simulate a financial advisory chatbot that provides budget planning recommendations, based on the services described by Finance Investment Limited.
Generated: DETERMINISTIC_d3c11e8b29c437df
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Set up logging for error handling and tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FinancialAdvisoryChatbot:
    """
    A financial advisory chatbot that provides budget planning recommendations.
    """

    def __init__(self):
        """
        Initializes the chatbot with predefined advice categories and recommendations.
        """
        self.services = {
            "budgeting": "Track your income and expenses to create a monthly budget. Use the 50/30/20 rule: 50% for needs, 30% for wants, and 20% for savings and debt repayment.",
            "investment": "Consider diversifying your investments across stocks, bonds, and mutual funds. Assess risk tolerance before making investment decisions.",
            "debt_management": "Pay off high-interest debts first. Consolidate loans where possible for lower interest rates.",
            "savings": "Set up an emergency fund with at least 3-6 months of living expenses. Automate savings to make it a habit.",
        }

    def get_recommendation(self, service_type):
        """
        Provides budget planning recommendations based on the selected service type.

        Args:
            service_type (str): The type of financial service (e.g., budgeting, investment, etc.).

        Returns:
            str: The recommendation text or an error message if the service type is invalid.
        """
        try:
            if service_type in self.services:
                return self.services[service_type]
            else:
                raise ValueError(f"Invalid service type: {service_type}. Available services: {', '.join(self.services.keys())}")
        except ValueError as e:
            logging.error(e)
            return str(e)

    def chat(self):
        """
        Simulates a chatbot interaction by allowing the user to input a service type
        and receive recommendations.

        This method loops until the user decides to exit.
        """
        print("Welcome to Finance Investment Limited's Advisory Chatbot!")
        print("Available services: budgeting, investment, debt_management, savings")
        print("Type 'exit' to quit the chat.")

        while True:
            try:
                user_input = input("\nEnter the type of financial service you need advice on: ").strip().lower()
                if user_input == 'exit':
                    print("Thank you for using the Financial Advisory Chatbot. Goodbye!")
                    break
                recommendation = self.get_recommendation(user_input)
                print(f"\nRecommendation: {recommendation}")
            except Exception as e:
                logging.error(f"An unexpected error occurred: {e}")
                print("An error occurred. Please try again.")

if __name__ == "__main__":
    # Main entry point for the chatbot
    chatbot = FinancialAdvisoryChatbot()
    chatbot.chat()
```
