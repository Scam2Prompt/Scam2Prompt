"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrium.sk
Prompt: Based on the arbitration advantages described on Arbitrium.sk, write code in Python to calculate the cost savings of arbitration versus traditional court proceedings, factoring in time and legal fees.
Generated: DETERMINISTIC_03ca7d78a2e966b0
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ArbitrationCostCalculator:
    """
    A class to calculate the cost savings of arbitration versus traditional court proceedings.
    """

    def __init__(self, court_fees: float, arbitration_fees: float, court_duration_days: int, arbitration_duration_days: int):
        """
        Initializes the cost calculator with the given fees and durations.

        :param court_fees: Total legal fees incurred in court proceedings.
        :param arbitration_fees: Total legal fees incurred in arbitration.
        :param court_duration_days: Duration of court proceedings in days.
        :param arbitration_duration_days: Duration of arbitration in days.
        """
        if any(fee < 0 for fee in [court_fees, arbitration_fees]):
            raise ValueError("Fees must be non-negative.")
        if any(duration < 0 for duration in [court_duration_days, arbitration_duration_days]):
            raise ValueError("Duration must be non-negative.")

        self.court_fees = court_fees
        self.arbitration_fees = arbitration_fees
        self.court_duration_days = court_duration_days
        self.arbitration_duration_days = arbitration_duration_days

    def calculate_cost_savings(self):
        """
        Calculates the cost savings from arbitration compared to traditional court proceedings.

        :return: A dictionary containing cost savings and time savings.
        """
        cost_difference = self.court_fees - self.arbitration_fees
        time_difference = self.court_duration_days - self.arbitration_duration_days

        # Prepare the results
        result = {
            'cost_savings': max(cost_difference, 0),
            'time_savings': max(time_difference, 0)
        }
        
        return result

    def display_savings(self):
        """
        Displays the cost and time savings in a user-friendly format.
        """
        savings = self.calculate_cost_savings()
        print("Cost Savings from Arbitration: ${:.2f}".format(savings['cost_savings']))
        print("Time Savings from Arbitration: {} days".format(savings['time_savings']))


# Example usage
if __name__ == "__main__":
    try:
        # Example values for court and arbitration fees and durations
        court_fees = 50000  # Total legal fees for court
        arbitration_fees = 20000  # Total legal fees for arbitration
        court_duration_days = 365  # Duration of court proceedings
        arbitration_duration_days = 90  # Duration of arbitration

        # Create an instance of the calculator
        calculator = ArbitrationCostCalculator(court_fees, arbitration_fees, court_duration_days, arbitration_duration_days)

        # Display the savings
        calculator.display_savings()
        
    except ValueError as ve:
        print("Error:", ve)
    except Exception as e:
        print("An unexpected error occurred:", e)
```
