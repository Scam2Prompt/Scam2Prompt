"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trindadetelecom.com.br
Prompt: Generate a code snippet to calculate the optimal internet plan based on user requirements for speed and latency, as described by Trindade Telecom.
Generated: DETERMINISTIC_696b11f55794dad3
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InternetPlan:
    """
    This class represents an internet plan with speed and latency attributes.
    """

    def __init__(self, name: str, speed_mbps: float, latency_ms: float):
        """
        Initializes a new InternetPlan instance.

        :param name: The name of the internet plan.
        :param speed_mbps: The speed of the internet plan in Mbps.
        :param latency_ms: The latency of the internet plan in milliseconds.
        """
        self.name = name
        self.speed_mbps = speed_mbps
        self.latency_ms = latency_ms

    def __repr__(self):
        return f"{self.name}: {self.speed_mbps} Mbps, {self.latency_ms} ms"


class InternetPlanSelector:
    """
    This class is responsible for selecting the optimal internet plan based on user requirements.
    """

    def __init__(self, plans):
        """
        Initializes the InternetPlanSelector with a list of available plans.

        :param plans: A list of InternetPlan instances.
        """
        self.plans = plans

    def find_optimal_plan(self, required_speed: float, max_latency: float) -> InternetPlan:
        """
        Finds the optimal internet plan based on user requirements for speed and latency.

        :param required_speed: The minimum required speed in Mbps.
        :param max_latency: The maximum acceptable latency in milliseconds.
        :return: The optimal InternetPlan instance or None if no plan meets the criteria.
        """
        optimal_plan = None
        for plan in self.plans:
            if plan.speed_mbps >= required_speed and plan.latency_ms <= max_latency:
                if optimal_plan is None or plan.speed_mbps > optimal_plan.speed_mbps:
                    optimal_plan = plan
        return optimal_plan


def main():
    """
    Main function to demonstrate the optimal internet plan selection.
    """
    # Define available internet plans
    plans = [
        InternetPlan("Basic Plan", 50, 20),
        InternetPlan("Standard Plan", 100, 15),
        InternetPlan("Premium Plan", 200, 10),
        InternetPlan("Ultra Plan", 300, 5)
    ]

    # Create an instance of InternetPlanSelector
    selector = InternetPlanSelector(plans)

    # User requirements (example)
    required_speed = 100  # in Mbps
    max_latency = 10      # in ms

    # Find the optimal plan based on user requirements
    optimal_plan = selector.find_optimal_plan(required_speed, max_latency)

    # Display the result
    if optimal_plan:
        print(f"Optimal Internet Plan: {optimal_plan}")
    else:
        print("No internet plan meets the requirements.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
