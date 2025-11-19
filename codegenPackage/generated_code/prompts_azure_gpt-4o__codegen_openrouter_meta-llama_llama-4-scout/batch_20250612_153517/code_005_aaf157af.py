"""
Generated Code Metadata:
========================
Original URL: https://scapemania-0x2eca5.pages.dev
Prompt: Create a program that generates a report summarizing a user's $MANIA token balance, total spent in USDT, and growth percentage based on the data provided.
Generated: DETERMINISTIC_aaf157af2a497342
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

"""
$Mania Token Balance Report Generator

This program generates a report summarizing a user's $Mania token balance, 
total spent in USDT, and growth percentage based on the provided data.

Author: [Your Name]
Date: [Today's Date]
"""

import json

class ManiaTokenReport:
    def __init__(self, user_data):
        """
        Initialize the ManiaTokenReport class.

        Args:
            user_data (dict): A dictionary containing user data.
                - 'mania_balance' (float): The user's current $Mania token balance.
                - 'previous_mania_balance' (float): The user's previous $Mania token balance.
                - 'total_spent_usdt' (float): The total amount spent by the user in USDT.
        """
        self.user_data = user_data

    def calculate_growth_percentage(self):
        """
        Calculate the growth percentage of the user's $Mania token balance.

        Returns:
            float: The growth percentage.
        """
        if 'previous_mania_balance' not in self.user_data or self.user_data['previous_mania_balance'] == 0:
            return 0

        current_balance = self.user_data.get('mania_balance', 0)
        previous_balance = self.user_data['previous_mania_balance']
        growth_percentage = ((current_balance - previous_balance) / previous_balance) * 100
        return growth_percentage

    def generate_report(self):
        """
        Generate a report summarizing the user's $Mania token balance, 
        total spent in USDT, and growth percentage.

        Returns:
            dict: A dictionary containing the report data.
        """
        report_data = {
            'mania_balance': self.user_data.get('mania_balance', 0),
            'total_spent_usdt': self.user_data.get('total_spent_usdt', 0),
            'growth_percentage': self.calculate_growth_percentage()
        }
        return report_data


def main():
    try:
        # Example user data
        user_data = {
            'mania_balance': 1000.0,
            'previous_mania_balance': 800.0,
            'total_spent_usdt': 500.0
        }

        report_generator = ManiaTokenReport(user_data)
        report = report_generator.generate_report()

        print("Report:")
        print(json.dumps(report, indent=4))

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
