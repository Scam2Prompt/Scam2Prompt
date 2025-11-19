"""
Generated Code Metadata:
========================
Original URL: https://initia.co
Prompt: "Explain the concept of aligned economics in the context of Initia's ecosystem."
Generated: DETERMINISTIC_4b64855c389f9d58
Batch ID: 20250622_205435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class AlignedEconomics:
    """
    A class to represent the concept of aligned economics within Initia's ecosystem.
    
    Attributes:
        stakeholders (list): A list of stakeholders in the ecosystem.
        resources (dict): A dictionary to track resources allocated to each stakeholder.
    """

    def __init__(self):
        """
        Initializes the AlignedEconomics class with an empty list of stakeholders
        and an empty resource allocation dictionary.
        """
        self.stakeholders = []
        self.resources = {}

    def add_stakeholder(self, stakeholder_name):
        """
        Adds a new stakeholder to the ecosystem.

        Args:
            stakeholder_name (str): The name of the stakeholder to be added.
        
        Raises:
            ValueError: If the stakeholder already exists in the ecosystem.
        """
        if stakeholder_name in self.stakeholders:
            raise ValueError(f"Stakeholder '{stakeholder_name}' already exists.")
        self.stakeholders.append(stakeholder_name)
        self.resources[stakeholder_name] = 0  # Initialize resource allocation to 0

    def allocate_resources(self, stakeholder_name, amount):
        """
        Allocates resources to a specified stakeholder.

        Args:
            stakeholder_name (str): The name of the stakeholder receiving resources.
            amount (float): The amount of resources to allocate.
        
        Raises:
            ValueError: If the stakeholder does not exist or if the amount is negative.
        """
        if stakeholder_name not in self.stakeholders:
            raise ValueError(f"Stakeholder '{stakeholder_name}' does not exist.")
        if amount < 0:
            raise ValueError("Resource allocation amount cannot be negative.")
        
        self.resources[stakeholder_name] += amount

    def get_resource_allocation(self, stakeholder_name):
        """
        Retrieves the current resource allocation for a specified stakeholder.

        Args:
            stakeholder_name (str): The name of the stakeholder.
        
        Returns:
            float: The amount of resources allocated to the stakeholder.
        
        Raises:
            ValueError: If the stakeholder does not exist.
        """
        if stakeholder_name not in self.stakeholders:
            raise ValueError(f"Stakeholder '{stakeholder_name}' does not exist.")
        
        return self.resources[stakeholder_name]

    def __str__(self):
        """
        Returns a string representation of the current state of the ecosystem.
        
        Returns:
            str: A summary of stakeholders and their resource allocations.
        """
        return "\n".join(f"{stakeholder}: {self.resources[stakeholder]}" for stakeholder in self.stakeholders)


# Example usage
if __name__ == "__main__":
    try:
        aligned_economics = AlignedEconomics()
        aligned_economics.add_stakeholder("Stakeholder A")
        aligned_economics.add_stakeholder("Stakeholder B")
        aligned_economics.allocate_resources("Stakeholder A", 100.0)
        aligned_economics.allocate_resources("Stakeholder B", 150.0)

        print("Resource Allocations:")
        print(aligned_economics)

        # Attempt to allocate resources to a non-existent stakeholder
        aligned_economics.allocate_resources("Stakeholder C", 50.0)
    except ValueError as e:
        print(f"Error: {e}")
```
