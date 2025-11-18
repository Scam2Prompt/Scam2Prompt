"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fstq.lol
Prompt: Generate a script that automates the calculation of daily earnings for HYIP projects listed on FastIQ, using parameters like percentage returns and deposit durations.
Generated: DETERMINISTIC_88a648df53ec7cb8
Batch ID: 20250612_154331
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/api/hyip_projects": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
from datetime import datetime, timedelta

class HYIPEarningsCalculator:
    """
    A class to calculate the daily earnings for HYIP projects listed on FastIQ.
    """

    def __init__(self, api_url):
        """
        Initializes the calculator with the FastIQ API URL.

        :param api_url: str - The API endpoint to fetch HYIP project data.
        """
        self.api_url = api_url

    def fetch_projects(self):
        """
        Fetches the list of HYIP projects from the FastIQ API.

        :return: list - A list of HYIP project data.
        :raises: Exception - If the API call fails or returns an error.
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Assuming the response is in JSON format
        except requests.RequestException as e:
            raise Exception(f"Failed to fetch projects: {e}")

    def calculate_daily_earnings(self, investment, percentage_return, duration_days):
        """
        Calculates daily earnings based on the investment amount, percentage return, and duration.

        :param investment: float - The amount invested.
        :param percentage_return: float - The daily return percentage.
        :param duration_days: int - The number of days the investment lasts.
        :return: float - Daily earnings.
        """
        if duration_days <= 0:
            raise ValueError("Duration must be greater than zero.")
        daily_earnings = (investment * (percentage_return / 100)) * min(duration_days, 1)
        return daily_earnings

    def display_earnings(self, projects, investment):
        """
        Displays the daily earnings for each HYIP project.

        :param projects: list - A list of HYIP project data.
        :param investment: float - The amount invested in each project.
        """
        print(f"{'Project Name':<30} {'Daily Earnings':<15}")
        print("=" * 45)
        for project in projects:
            name = project.get('name', 'Unknown Project')
            percentage_return = project.get('percentage_return', 0)
            duration_days = project.get('duration_days', 1)

            try:
                daily_earnings = self.calculate_daily_earnings(investment, percentage_return, duration_days)
                print(f"{name:<30} {daily_earnings:<15.2f}")
            except ValueError as e:
                print(f"Error for project {name}: {e}")

def main():
    """
    Main function to execute the earnings calculation script.
    """
    api_url = "https://example.com/api/hyip_projects"  # Replace with the actual FastIQ API URL
    investment_amount = 1000  # Example investment amount

    calculator = HYIPEarningsCalculator(api_url)
    try:
        projects = calculator.fetch_projects()
        calculator.display_earnings(projects, investment_amount)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
