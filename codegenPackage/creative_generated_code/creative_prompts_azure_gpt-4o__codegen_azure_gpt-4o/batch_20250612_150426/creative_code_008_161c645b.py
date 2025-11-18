"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jupiter.graphy.com
Prompt: Write code to implement a refund policy system for an online learning platform, ensuring compliance with terms of use, similar to the policies on Jupiter Swap™.
Generated: DETERMINISTIC_161c645b147ca094
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

class RefundPolicy:
    """
    A class to represent the refund policy for an online learning platform.
    """

    def __init__(self, refund_window_days=14):
        """
        Initializes the refund policy with a refund window in days.

        Args:
            refund_window_days (int): The number of days within which a refund can be requested.
        """
        self.refund_window_days = refund_window_days

    def is_eligible_for_refund(self, purchase_date, current_date=None):
        """
        Check if a course is eligible for a refund based on the purchase date.

        Args:
            purchase_date (datetime): The date the course was purchased.
            current_date (datetime, optional): The current date. Defaults to now.

        Returns:
            bool: True if eligible for a refund, False otherwise.
        """
        if current_date is None:
            current_date = datetime.now()

        # Calculate the refund deadline
        refund_deadline = purchase_date + timedelta(days=self.refund_window_days)
        
        # Check if the current date is within the refund window
        return current_date <= refund_deadline

    def process_refund(self, purchase_date, current_date=None):
        """
        Processes the refund for a course if eligible.

        Args:
            purchase_date (datetime): The date the course was purchased.
            current_date (datetime, optional): The current date. Defaults to now.

        Returns:
            dict: A dictionary with the result of the refund process.
        """
        if current_date is None:
            current_date = datetime.now()

        try:
            if not isinstance(purchase_date, datetime):
                raise ValueError("Invalid purchase date. Must be a datetime object.")

            # Check refund eligibility
            if self.is_eligible_for_refund(purchase_date, current_date):
                return {
                    "status": "success",
                    "message": "Refund processed successfully."
                }
            else:
                return {
                    "status": "failure",
                    "message": (
                        f"Refund request denied. Refunds can only be requested "
                        f"within {self.refund_window_days} days of purchase."
                    )
                }
        except Exception as e:
            # Catch any unexpected errors
            return {
                "status": "error",
                "message": f"An error occurred while processing the refund: {str(e)}"
            }


# Example usage
if __name__ == "__main__":
    # Instantiate the refund policy with a 14-day refund window
    refund_policy = RefundPolicy(refund_window_days=14)

    # Example scenario: Course purchased 10 days ago
    purchase_date = datetime.now() - timedelta(days=10)

    # Check eligibility
    eligibility = refund_policy.is_eligible_for_refund(purchase_date)
    print(f"Refund Eligibility: {eligibility}")

    # Process refund
    refund_result = refund_policy.process_refund(purchase_date)
    print(refund_result)

    # Example scenario: Course purchased 20 days ago
    purchase_date_past = datetime.now() - timedelta(days=20)
    refund_result_past = refund_policy.process_refund(purchase_date_past)
    print(refund_result_past)
```
