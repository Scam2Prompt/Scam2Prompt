"""
Generated Code Metadata:
========================
Original URL: https://earnm-io.web.app
Prompt: "Design a loyalty program using EARN'M's ecosystem, targeting an average user redemption rate of 11.2 codes, and calculate the potential earnings and savings."
Generated: DETERMINISTIC_196be4d4e299698f
Batch ID: 20250622_212723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# loyalty_program.py

class LoyaltyProgram:
    """
    A class representing the EARN'M loyalty program.

    Attributes:
    ----------
    redemption_rate : float
        The average user redemption rate.
    earn_rate : float
        The rate at which users earn points.
    save_rate : float
        The rate at which users save points.

    Methods:
    -------
    calculate_earnings(points):
        Calculates the potential earnings based on points earned.
    calculate_savings(points):
        Calculates the potential savings based on points saved.
    """

    def __init__(self, redemption_rate=11.2, earn_rate=1.0, save_rate=0.5):
        """
        Initializes the LoyaltyProgram class.

        Parameters:
        ----------
        redemption_rate : float, optional
            The average user redemption rate (default is 11.2).
        earn_rate : float, optional
            The rate at which users earn points (default is 1.0).
        save_rate : float, optional
            The rate at which users save points (default is 0.5).
        """
        self.redemption_rate = redemption_rate
        self.earn_rate = earn_rate
        self.save_rate = save_rate

    def calculate_earnings(self, points):
        """
        Calculates the potential earnings based on points earned.

        Parameters:
        ----------
        points : int
            The number of points earned.

        Returns:
        -------
        float
            The potential earnings.
        """
        try:
            if points < 0:
                raise ValueError("Points cannot be negative.")
            earnings = points * self.earn_rate * (self.redemption_rate / 100)
            return earnings
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None

    def calculate_savings(self, points):
        """
        Calculates the potential savings based on points saved.

        Parameters:
        ----------
        points : int
            The number of points saved.

        Returns:
        -------
        float
            The potential savings.
        """
        try:
            if points < 0:
                raise ValueError("Points cannot be negative.")
            savings = points * self.save_rate * (self.redemption_rate / 100)
            return savings
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None


def main():
    loyalty_program = LoyaltyProgram()

    # Example usage:
    points_earned = 1000
    points_saved = 500

    earnings = loyalty_program.calculate_earnings(points_earned)
    savings = loyalty_program.calculate_savings(points_saved)

    print(f"Potential earnings: ${earnings:.2f}")
    print(f"Potential savings: ${savings:.2f}")


if __name__ == "__main__":
    main()
```
