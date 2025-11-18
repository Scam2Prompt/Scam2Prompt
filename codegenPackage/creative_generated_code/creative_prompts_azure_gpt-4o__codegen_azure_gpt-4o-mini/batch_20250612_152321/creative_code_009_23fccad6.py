"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xrp.promo
Prompt: Write code to compare hosting plans offered by Timeweb (e.g., virtual hosting vs. VDS/VPS) and recommend the best option based on specific requirements.
Generated: DETERMINISTIC_23fccad6ac302fce
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class HostingPlan:
    """A class representing a hosting plan offered by Timeweb."""

    def __init__(self, name, price, storage, ram, cpu_cores, bandwidth, type_):
        """
        Initialize a new HostingPlan instance.

        Args:
            name (str): Name of the hosting plan.
            price (float): Monthly price of the hosting plan.
            storage (int): Storage space in GB.
            ram (int): RAM in GB.
            cpu_cores (int): Number of CPU cores.
            bandwidth (int): Monthly bandwidth in GB.
            type_ (str): Type of hosting (e.g., 'virtual', 'VDS', 'VPS').
        """
        self.name = name
        self.price = price
        self.storage = storage
        self.ram = ram
        self.cpu_cores = cpu_cores
        self.bandwidth = bandwidth
        self.type_ = type_

    def __str__(self):
        """Return a string representation of the hosting plan."""
        return f"{self.name} ({self.type_}): ${self.price}/month, {self.storage}GB Storage, {self.ram}GB RAM, {self.cpu_cores} Cores, {self.bandwidth}GB Bandwidth"


def recommend_hosting_plan(requirements, plans):
    """
    Recommend the best hosting plan based on user requirements.

    Args:
        requirements (dict): A dictionary containing user requirements.
        plans (list): A list of HostingPlan instances to evaluate.

    Returns:
        HostingPlan: The recommended hosting plan based on requirements.
    """
    best_plan = None
    best_score = float('-inf')

    for plan in plans:
        score = (
            (plan.storage >= requirements['storage']) +
            (plan.ram >= requirements['ram']) +
            (plan.cpu_cores >= requirements['cpu_cores']) +
            (plan.bandwidth >= requirements['bandwidth'])
        )
        
        # Check if this plan is the best choice based on the score
        if score > best_score:
            best_score = score
            best_plan = plan

    # If no plan meets the requirements, raise an error
    if best_plan is None:
        raise ValueError("No hosting plan meets the specified requirements.")

    return best_plan


def main():
    """Main function to compare hosting plans and recommend one based on requirements."""
    # Define hosting plans available from Timeweb
    plans = [
        HostingPlan("Basic Virtual Hosting", 5.99, 50, 2, 1, 200, "virtual"),
        HostingPlan("Advanced Virtual Hosting", 10.99, 100, 4, 2, 500, "virtual"),
        HostingPlan("VDS Plan A", 29.99, 200, 8, 4, 1000, "VDS"),
        HostingPlan("VPS Plan B", 49.99, 400, 16, 8, 2000, "VPS"),
    ]

    # Define user requirements
    requirements = {
        'storage': 100,      # Required storage in GB
        'ram': 4,            # Required RAM in GB
        'cpu_cores': 2,      # Required number of CPU cores
        'bandwidth': 300      # Required bandwidth in GB
    }

    try:
        # Get the recommended hosting plan
        recommended_plan = recommend_hosting_plan(requirements, plans)
        print(f"Recommended Plan: {recommended_plan}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()
```
