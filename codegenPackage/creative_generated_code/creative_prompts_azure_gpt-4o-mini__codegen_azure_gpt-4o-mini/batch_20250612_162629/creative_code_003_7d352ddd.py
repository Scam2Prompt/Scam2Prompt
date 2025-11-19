"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://battle-barkers.com
Prompt: Create a Python script that evaluates the risk tolerance of an investor based on their financial goals and investment history.
Generated: DETERMINISTIC_7d352ddd0fb82c32
Batch ID: 20250612_162629
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class Investor:
    def __init__(self, name, age, investment_history, financial_goals):
        """
        Initializes an Investor instance.

        :param name: str - The name of the investor.
        :param age: int - The age of the investor.
        :param investment_history: list - A list of past investments.
        :param financial_goals: dict - A dictionary with financial goals and their priorities.
        """
        self.name = name
        self.age = age
        self.investment_history = investment_history
        self.financial_goals = financial_goals

    def evaluate_risk_tolerance(self):
        """
        Evaluates the risk tolerance of the investor based on their age, investment history, and financial goals.

        :return: str - A risk tolerance level (Low, Medium, High).
        """
        risk_score = 0

        # Age consideration for risk tolerance
        if self.age < 30:
            risk_score += 2  # Younger investors can typically handle more risk
        elif self.age < 50:
            risk_score += 1  # Moderate risk tolerance
        else:
            risk_score -= 1  # Older investors tend to be more conservative

        # Evaluating investment history
        for investment in self.investment_history:
            if investment['performance'] > 0:
                risk_score += 1  # Positive performance increases risk tolerance
            else:
                risk_score -= 1  # Negative performance decreases risk tolerance

        # Evaluating financial goals
        for goal, priority in self.financial_goals.items():
            if priority == 'high':
                risk_score += 1  # High-priority goals can justify higher risk
            elif priority == 'low':
                risk_score -= 1  # Low-priority goals suggest caution

        # Determine risk tolerance level based on risk score
        if risk_score < -1:
            return 'Low'
        elif risk_score == -1 or risk_score == 0:
            return 'Medium'
        else:
            return 'High'


def load_investor_data(file_path):
    """
    Loads investor data from a JSON file.

    :param file_path: str - The path to the JSON file containing investor data.
    :return: Investor - An instance of the Investor class.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return Investor(**data)
    except FileNotFoundError:
        raise FileNotFoundError("The specified file was not found.")
    except json.JSONDecodeError:
        raise ValueError("Error decoding JSON from the file.")
    except TypeError as e:
        raise ValueError("Invalid data format: {}".format(e))


def main():
    """
    Main function to execute the script.
    """
    try:
        investor = load_investor_data('investor_data.json')
        risk_tolerance = investor.evaluate_risk_tolerance()
        print(f"{investor.name}, your risk tolerance is: {risk_tolerance}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

This script assumes you have a JSON file named `investor_data.json` with the following structure:

```json
{
    "name": "John Doe",
    "age": 35,
    "investment_history": [
        {"investment": "Stock A", "performance": 10},
        {"investment": "Bond B", "performance": -5}
    ],
    "financial_goals": {
        "retirement": "high",
        "vacation": "low"
    }
}
```
