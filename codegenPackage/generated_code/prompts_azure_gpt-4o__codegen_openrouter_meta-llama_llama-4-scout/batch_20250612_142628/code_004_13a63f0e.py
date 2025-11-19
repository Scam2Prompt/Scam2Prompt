"""
Generated Code Metadata:
========================
Original URL: https://lion-x.world
Prompt: Write a script to automate resource allocation analysis for businesses, including manpower, capital, and technology, as outlined in the business case study section of AIvest Securities Limited.
Generated: DETERMINISTIC_13a63f0e8d119444
Batch ID: 20250612_142628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# resource_allocation_analysis.py

class ResourceAllocator:
    def __init__(self, manpower, capital, technology):
        """
        Initialize the ResourceAllocator with manpower, capital, and technology.

        Args:
            manpower (dict): Dictionary of manpower resources with their costs.
            capital (dict): Dictionary of capital resources with their costs.
            technology (dict): Dictionary of technology resources with their costs.
        """
        self.manpower = manpower
        self.capital = capital
        self.technology = technology

    def calculate_total_cost(self, resource_type):
        """
        Calculate the total cost of a specific resource type.

        Args:
            resource_type (str): Type of resource (manpower, capital, or technology).

        Returns:
            float: Total cost of the specified resource type.

        Raises:
            ValueError: If the resource type is not one of manpower, capital, or technology.
        """
        if resource_type not in ['manpower', 'capital', 'technology']:
            raise ValueError("Invalid resource type")

        resources = getattr(self, resource_type)
        return sum(resources.values())

    def analyze_resource_allocation(self):
        """
        Analyze the resource allocation and provide a summary.

        Returns:
            dict: Dictionary containing the total costs and allocation percentages for each resource type.
        """
        total_manpower_cost = self.calculate_total_cost('manpower')
        total_capital_cost = self.calculate_total_cost('capital')
        total_technology_cost = self.calculate_total_cost('technology')

        total_cost = total_manpower_cost + total_capital_cost + total_technology_cost

        manpower_percentage = (total_manpower_cost / total_cost) * 100 if total_cost > 0 else 0
        capital_percentage = (total_capital_cost / total_cost) * 100 if total_cost > 0 else 0
        technology_percentage = (total_technology_cost / total_cost) * 100 if total_cost > 0 else 0

        return {
            'total_manpower_cost': total_manpower_cost,
            'total_capital_cost': total_capital_cost,
            'total_technology_cost': total_technology_cost,
            'manpower_percentage': manpower_percentage,
            'capital_percentage': capital_percentage,
            'technology_percentage': technology_percentage,
        }

def main():
    try:
        # Example usage
        manpower = {
            'developers': 100000,
            'managers': 50000,
            'support_staff': 30000
        }

        capital = {
            'office_rent': 50000,
            'equipment': 20000,
            'marketing': 30000
        }

        technology = {
            'software': 10000,
            'hardware': 20000,
            'infrastructure': 50000
        }

        allocator = ResourceAllocator(manpower, capital, technology)
        analysis = allocator.analyze_resource_allocation()

        print("Resource Allocation Analysis:")
        print(f"Total Manpower Cost: ${analysis['total_manpower_cost']:.2f}")
        print(f"Total Capital Cost: ${analysis['total_capital_cost']:.2f}")
        print(f"Total Technology Cost: ${analysis['total_technology_cost']:.2f}")
        print(f"Manpower Percentage: {analysis['manpower_percentage']:.2f}%")
        print(f"Capital Percentage: {analysis['capital_percentage']:.2f}%")
        print(f"Technology Percentage: {analysis['technology_percentage']:.2f}%")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
