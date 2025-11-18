"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trindadetelecom.com.br
Prompt: Write a function to calculate the cost-benefit ratio of internet plans, factoring in speed (Mbps), latency, and installation features, as described on Trindade Telecom's site.
Generated: DETERMINISTIC_646fae2dcab3a3c2
Batch ID: 20250612_153225
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
    A class to represent an Internet plan and calculate its cost-benefit ratio.
    """

    def __init__(self, name, cost_per_month, speed_mbps, latency_ms, installation_fee):
        """
        Initializes the InternetPlan instance.

        :param name: Name of the internet plan.
        :param cost_per_month: Monthly cost of the plan in dollars.
        :param speed_mbps: Speed of the internet plan in Mbps.
        :param latency_ms: Latency of the internet plan in milliseconds.
        :param installation_fee: One-time installation fee in dollars.
        """
        self.name = name
        self.cost_per_month = cost_per_month
        self.speed_mbps = speed_mbps
        self.latency_ms = latency_ms
        self.installation_fee = installation_fee

    def calculate_cost_benefit_ratio(self):
        """
        Calculates the cost-benefit ratio of the internet plan.

        :return: Cost-benefit ratio as a float.
        :raises ValueError: If any of the inputs are invalid (e.g., negative values).
        """
        if self.cost_per_month < 0 or self.speed_mbps <= 0 or self.latency_ms < 0 or self.installation_fee < 0:
            raise ValueError("Cost, speed, latency, and installation fee must be non-negative.")

        # Calculate the total cost over one year including the installation fee
        total_cost = (self.cost_per_month * 12) + self.installation_fee

        # Using speed and latency to calculate benefit
        benefit_score = self.speed_mbps / (self.latency_ms + 1)  # Adding 1 to avoid division by zero

        # Calculate cost-benefit ratio
        cost_benefit_ratio = benefit_score / total_cost
        return cost_benefit_ratio

    def __str__(self):
        """
        Returns a string representation of the InternetPlan instance.

        :return: A formatted string with plan details.
        """
        return f"Internet Plan: {self.name}, Cost: ${self.cost_per_month}/month, Speed: {self.speed_mbps} Mbps, " \
               f"Latency: {self.latency_ms} ms, Installation Fee: ${self.installation_fee}"


# Example usage:
if __name__ == "__main__":
    try:
        plan1 = InternetPlan(name="Basic Plan", cost_per_month=50, speed_mbps=100, latency_ms=20, installation_fee=100)
        print(plan1)
        ratio = plan1.calculate_cost_benefit_ratio()
        print(f"Cost-benefit ratio: {ratio:.6f}")

    except ValueError as e:
        print(f"Error: {e}")
```
