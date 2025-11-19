"""
Generated Code Metadata:
========================
Original URL: https://bouncebit.site
Prompt: Develop a script to calculate hosting plan costs and recommend the best plan for a domain using Hostinger's hosting options.
Generated: DETERMINISTIC_eae7a3af0697bfeb
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# hosting_plan_recommender.py

class HostingPlan:
    def __init__(self, name, price, storage, bandwidth, domains):
        """
        Initialize a hosting plan.

        Args:
            name (str): Plan name.
            price (float): Plan price per month.
            storage (int): Plan storage in GB.
            bandwidth (int): Plan bandwidth in GB.
            domains (int): Number of domains allowed.
        """
        self.name = name
        self.price = price
        self.storage = storage
        self.bandwidth = bandwidth
        self.domains = domains

class HostingPlanRecommender:
    def __init__(self):
        """
        Initialize the hosting plan recommender with Hostinger's hosting options.
        """
        self.plans = [
            HostingPlan("Single Web Hosting", 1.99, 50, 100, 1),
            HostingPlan("Premium Web Hosting", 4.99, 100, 200, 100),
            HostingPlan("Business Web Hosting", 7.99, 200, 500, 100),
        ]

    def calculate_cost(self, plan_name):
        """
        Calculate the cost of a hosting plan.

        Args:
            plan_name (str): Name of the plan.

        Returns:
            float: Plan price per month.

        Raises:
            ValueError: If the plan is not found.
        """
        for plan in self.plans:
            if plan.name == plan_name:
                return plan.price
        raise ValueError("Plan not found")

    def recommend_plan(self, required_storage, required_bandwidth, required_domains):
        """
        Recommend the best hosting plan based on the requirements.

        Args:
            required_storage (int): Required storage in GB.
            required_bandwidth (int): Required bandwidth in GB.
            required_domains (int): Required number of domains.

        Returns:
            HostingPlan: Recommended hosting plan.

        Raises:
            ValueError: If no plan meets the requirements.
        """
        recommended_plan = None
        min_price = float('inf')
        for plan in self.plans:
            if plan.storage >= required_storage and plan.bandwidth >= required_bandwidth and plan.domains >= required_domains:
                if plan.price < min_price:
                    min_price = plan.price
                    recommended_plan = plan
        if recommended_plan is None:
            raise ValueError("No plan meets the requirements")
        return recommended_plan

def main():
    try:
        recommender = HostingPlanRecommender()
        print("Available plans:")
        for plan in recommender.plans:
            print(f"{plan.name}: ${plan.price} - Storage: {plan.storage} GB, Bandwidth: {plan.bandwidth} GB, Domains: {plan.domains}")

        required_storage = int(input("Enter required storage in GB: "))
        required_bandwidth = int(input("Enter required bandwidth in GB: "))
        required_domains = int(input("Enter required number of domains: "))

        recommended_plan = recommender.recommend_plan(required_storage, required_bandwidth, required_domains)
        print(f"Recommended plan: {recommended_plan.name}")
        print(f"Cost: ${recommended_plan.price}")
        print(f"Storage: {recommended_plan.storage} GB")
        print(f"Bandwidth: {recommended_plan.bandwidth} GB")
        print(f"Domains: {recommended_plan.domains}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
