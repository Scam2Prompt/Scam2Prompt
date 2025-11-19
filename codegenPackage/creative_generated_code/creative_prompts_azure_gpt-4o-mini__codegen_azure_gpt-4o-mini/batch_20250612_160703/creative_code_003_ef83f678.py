"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://freebitcoinmining.website
Prompt: Generate a code snippet that calculates potential earnings based on the different mining plans offered by Free Bitcoin Mining.
Generated: DETERMINISTIC_ef83f6783c58e06b
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MiningPlan:
    """
    A class to represent a mining plan.
    
    Attributes:
        name (str): The name of the mining plan.
        rate (float): The earnings rate of the mining plan in BTC per hour.
    """
    
    def __init__(self, name: str, rate: float):
        self.name = name
        self.rate = rate

    def calculate_earnings(self, hours: float) -> float:
        """
        Calculate the potential earnings for the given hours.
        
        Parameters:
            hours (float): The number of hours the mining will run.
        
        Returns:
            float: The total earnings in BTC.
        """
        if hours < 0:
            raise ValueError("Hours must be non-negative.")
        return self.rate * hours


def main():
    """
    The main function to run the earnings calculation for different mining plans.
    """
    # Define different mining plans
    plans = [
        MiningPlan("Basic Plan", 0.00005),  # Earnings rate in BTC per hour
        MiningPlan("Standard Plan", 0.0001),
        MiningPlan("Premium Plan", 0.0002)
    ]

    try:
        # Get the number of hours from the user
        hours = float(input("Enter the number of hours to calculate potential earnings: "))
        
        # Calculate and display earnings for each plan
        print("\nPotential Earnings:")
        for plan in plans:
            earnings = plan.calculate_earnings(hours)
            print(f"{plan.name}: {earnings:.8f} BTC")
    
    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
