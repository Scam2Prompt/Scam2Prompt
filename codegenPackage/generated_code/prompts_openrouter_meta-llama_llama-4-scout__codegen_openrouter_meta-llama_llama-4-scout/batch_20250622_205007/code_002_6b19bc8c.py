"""
Generated Code Metadata:
========================
Original URL: https://binance5000.epizy.com
Prompt: Recommend a suitable web hosting plan from iFastNet for a small business website with moderate traffic, and explain the included features such as unlimited disk space and bandwidth.
Generated: DETERMINISTIC_6b19bc8cb3ebb34d
Batch ID: 20250622_205007
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# iFastNet Web Hosting Plan Recommender

class WebHostingPlan:
    def __init__(self, name, disk_space, bandwidth, price):
        """
        Initialize a WebHostingPlan object.

        Args:
            name (str): Plan name
            disk_space (str): Disk space offered
            bandwidth (str): Bandwidth offered
            price (float): Plan price
        """
        self.name = name
        self.disk_space = disk_space
        self.bandwidth = bandwidth
        self.price = price

class iFastNetWebHosting:
    def __init__(self):
        """
        Initialize an iFastNetWebHosting object.
        """
        self.plans = [
            WebHostingPlan("Basic", "unlimited", "unlimited", 5.99),
            WebHostingPlan("Premium", "unlimited", "unlimited", 9.99),
            WebHostingPlan("Business", "unlimited", "unlimited", 14.99),
        ]

    def recommend_plan(self, traffic_level):
        """
        Recommend a suitable web hosting plan based on traffic level.

        Args:
            traffic_level (str): Traffic level (low, moderate, high)

        Returns:
            WebHostingPlan: Recommended plan
        """
        if traffic_level == "low":
            return self.plans[0]
        elif traffic_level == "moderate":
            return self.plans[1]
        elif traffic_level == "high":
            return self.plans[2]
        else:
            raise ValueError("Invalid traffic level")

    def display_plan_features(self, plan):
        """
        Display features of a web hosting plan.

        Args:
            plan (WebHostingPlan): Plan to display features for
        """
        print(f"Plan Name: {plan.name}")
        print(f"Disk Space: {plan.disk_space}")
        print(f"Bandwidth: {plan.bandwidth}")
        print(f"Price: ${plan.price:.2f}")

def main():
    try:
        hosting = iFastNetWebHosting()
        traffic_level = "moderate"
        recommended_plan = hosting.recommend_plan(traffic_level)
        print(f"Recommended plan for {traffic_level} traffic: ")
        hosting.display_plan_features(recommended_plan)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
