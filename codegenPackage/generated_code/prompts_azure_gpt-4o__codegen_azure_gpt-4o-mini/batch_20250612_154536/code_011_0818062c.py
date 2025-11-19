"""
Generated Code Metadata:
========================
Original URL: https://airlinesmanagebooking.com
Prompt: Create a Python script to check refund eligibility for canceled flights based on the refund policies for Emirates and Qatar Airways, as outlined on Airlines Manage Booking.
Generated: DETERMINISTIC_0818062cc2e4d823
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests

class FlightRefundChecker:
    """
    A class to check refund eligibility for canceled flights based on airline policies.
    """

    def __init__(self, airline):
        """
        Initializes the FlightRefundChecker with the specified airline.

        :param airline: The airline for which to check refund eligibility ('Emirates' or 'Qatar Airways').
        """
        self.airline = airline
        self.refund_policy = self.get_refund_policy()

    def get_refund_policy(self):
        """
        Retrieves the refund policy for the specified airline.

        :return: A dictionary containing refund eligibility criteria.
        """
        policies = {
            'Emirates': {
                'cancellation': True,
                'refund': True,
                'conditions': 'Refunds are available for canceled flights if requested within 24 hours.'
            },
            'Qatar Airways': {
                'cancellation': True,
                'refund': False,
                'conditions': 'Refunds are not available for canceled flights unless specified otherwise.'
            }
        }
        return policies.get(self.airline, None)

    def check_refund_eligibility(self):
        """
        Checks if a refund is eligible based on the airline's policy.

        :return: A string indicating refund eligibility.
        """
        if self.refund_policy is None:
            return f"Error: No refund policy found for {self.airline}."

        if self.refund_policy['cancellation']:
            if self.refund_policy['refund']:
                return f"Refund is eligible for {self.airline}. {self.refund_policy['conditions']}"
            else:
                return f"Refund is not eligible for {self.airline}. {self.refund_policy['conditions']}"
        else:
            return f"Cancellation is not allowed for {self.airline}."

def main():
    """
    Main function to execute the refund eligibility check.
    """
    airlines = ['Emirates', 'Qatar Airways']
    
    for airline in airlines:
        checker = FlightRefundChecker(airline)
        eligibility = checker.check_refund_eligibility()
        print(eligibility)

if __name__ == "__main__":
    main()
```
