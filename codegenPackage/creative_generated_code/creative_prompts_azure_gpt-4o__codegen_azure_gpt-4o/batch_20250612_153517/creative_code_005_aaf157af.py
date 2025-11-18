"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scapemania-0x2eca5.pages.dev
Prompt: Create a program that generates a report summarizing a user's $MANIA token balance, total spent in USDT, and growth percentage based on the data provided.
Generated: DETERMINISTIC_aaf157af2a497342
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class TokenReportGenerator:
    """
    A class to generate a report summarizing a user's $MANIA token balance,
    total spent in USDT, and growth percentage.
    """

    def __init__(self, user_data):
        """
        Initializes the report generator with user data.
        
        :param user_data: Dictionary containing token balance, total spent, and current token price.
        """
        self.user_data = user_data

    def calculate_growth_percentage(self):
        """
        Calculates the growth percentage based on the user's total spent in USDT
        and the current value of their $MANIA token holdings.

        :return: Growth percentage as a float.
        """
        try:
            # Ensure necessary keys are present
            if 'total_spent_usdt' not in self.user_data or 'current_token_price_usdt' not in self.user_data or 'token_balance' not in self.user_data:
                raise KeyError("User data must include 'total_spent_usdt', 'current_token_price_usdt', and 'token_balance'.")

            total_spent = self.user_data['total_spent_usdt']
            current_token_price = self.user_data['current_token_price_usdt']
            token_balance = self.user_data['token_balance']

            # Calculate the current value of the tokens
            current_value = token_balance * current_token_price

            # Formula: ((Current Value - Total Spent) / Total Spent) * 100
            growth_percentage = ((current_value - total_spent) / total_spent) * 100
            return growth_percentage
        except KeyError as e:
            raise Exception(f"Missing required user data: {e}")
        except ZeroDivisionError:
            raise Exception("Total spent cannot be zero.")
        except Exception as e:
            raise Exception(f"An error occurred while calculating growth percentage: {e}")

    def generate_report(self):
        """
        Generates a summary report for the user.

        :return: A dictionary containing the report data.
        """
        try:
            # Calculate growth percentage
            growth_percentage = self.calculate_growth_percentage()

            # Generate the report
            report = {
                "token_balance": self.user_data['token_balance'],
                "total_spent_usdt": self.user_data['total_spent_usdt'],
                "growth_percentage": round(growth_percentage, 2)
            }
            return report
        except Exception as e:
            return {"error": str(e)}

# Example usage:
if __name__ == "__main__":
    # Sample user data
    user_data = {
        "token_balance": 1000,  # Number of $MANIA tokens the user owns
        "total_spent_usdt": 500,  # Total spent in USDT
        "current_token_price_usdt": 0.8  # Current price of a single $MANIA token in USDT
    }

    # Initialize the report generator
    report_generator = TokenReportGenerator(user_data)

    # Generate the report
    report = report_generator.generate_report()

    # Print the report in JSON format
    print(json.dumps(report, indent=4))
```
