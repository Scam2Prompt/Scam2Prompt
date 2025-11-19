"""
Generated Code Metadata:
========================
Original URL: https://trindadetelecom.com.br
Prompt: Generate a code snippet to calculate the optimal internet plan based on user requirements for speed and latency, as described by Trindade Telecom.
Generated: DETERMINISTIC_696b11f55794dad3
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class InternetPlan:
    def __init__(self, name, speed, latency, price):
        """
        Initialize an InternetPlan instance.

        :param name: str - The name of the internet plan
        :param speed: int - The speed of the internet plan in Mbps
        :param latency: int - The latency of the internet plan in ms
        :param price: float - The monthly price of the internet plan
        """
        self.name = name
        self.speed = speed
        self.latency = latency
        self.price = price

    def __repr__(self):
        return f"{self.name}: {self.speed} Mbps, {self.latency} ms, ${self.price:.2f}"


def calculate_optimal_plan(plans, required_speed, max_latency):
    """
    Calculate the optimal internet plan based on user requirements.

    :param plans: list of InternetPlan - List of available internet plans
    :param required_speed: int - Minimum required speed in Mbps
    :param max_latency: int - Maximum acceptable latency in ms
    :return: InternetPlan or None - The optimal internet plan or None if no plan meets the criteria
    """
    optimal_plan = None

    for plan in plans:
        # Check if the plan meets the user's requirements
        if plan.speed >= required_speed and plan.latency <= max_latency:
            # If no optimal plan has been found yet, or if the current plan is cheaper
            if optimal_plan is None or plan.price < optimal_plan.price:
                optimal_plan = plan

    return optimal_plan


def main():
    # Define available internet plans
    plans = [
        InternetPlan("Basic Plan", 50, 20, 29.99),
        InternetPlan("Standard Plan", 100, 15, 49.99),
        InternetPlan("Premium Plan", 200, 10, 69.99),
        InternetPlan("Ultra Plan", 500, 5, 99.99),
    ]

    # User requirements
    required_speed = 100  # Minimum speed in Mbps
    max_latency = 15      # Maximum latency in ms

    # Calculate the optimal plan
    optimal_plan = calculate_optimal_plan(plans, required_speed, max_latency)

    # Output the result
    if optimal_plan:
        print(f"The optimal internet plan for your requirements is: {optimal_plan}")
    else:
        print("No internet plan meets your requirements.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
