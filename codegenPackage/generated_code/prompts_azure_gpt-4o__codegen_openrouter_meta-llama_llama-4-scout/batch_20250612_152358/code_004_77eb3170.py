"""
Generated Code Metadata:
========================
Original URL: https://sus.weebly.com
Prompt: Develop a Python script to simulate the financing model of SUS, where resources are allocated from federal, state, and municipal levels based on population needs and healthcare service demands.
Generated: DETERMINISTIC_77eb317002545983
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# sus_financing_model.py

class SUSFinancingModel:
    """
    Simulates the financing model of SUS (Sistema Único de Saúde), 
    allocating resources from federal, state, and municipal levels 
    based on population needs and healthcare service demands.
    """

    def __init__(self, population, federal_funding, state_funding, municipal_funding):
        """
        Initializes the SUS financing model.

        Args:
        - population (int): The population to be served.
        - federal_funding (float): The federal funding available.
        - state_funding (float): The state funding available.
        - municipal_funding (float): The municipal funding available.
        """
        self.population = population
        self.federal_funding = federal_funding
        self.state_funding = state_funding
        self.municipal_funding = municipal_funding

    def calculate_healthcare_demand(self, population_needs):
        """
        Calculates the healthcare demand based on population needs.

        Args:
        - population_needs (dict): A dictionary containing population needs.

        Returns:
        - float: The total healthcare demand.
        """
        # Assuming population needs are represented as a dictionary with 
        # 'primary_care', 'secondary_care', and 'tertiary_care' as keys
        demand = 0
        for need, value in population_needs.items():
            demand += value
        return demand

    def allocate_federal_resources(self, healthcare_demand):
        """
        Allocates federal resources based on healthcare demand.

        Args:
        - healthcare_demand (float): The total healthcare demand.

        Returns:
        - float: The allocated federal resources.
        """
        # Assuming federal resources are allocated based on a fixed rate
        federal_allocation_rate = 0.4
        return min(self.federal_funding, healthcare_demand * federal_allocation_rate)

    def allocate_state_resources(self, healthcare_demand, federal_allocation):
        """
        Allocates state resources based on healthcare demand and federal allocation.

        Args:
        - healthcare_demand (float): The total healthcare demand.
        - federal_allocation (float): The allocated federal resources.

        Returns:
        - float: The allocated state resources.
        """
        # Assuming state resources are allocated based on a fixed rate
        state_allocation_rate = 0.3
        return min(self.state_funding, (healthcare_demand - federal_allocation) * state_allocation_rate)

    def allocate_municipal_resources(self, healthcare_demand, federal_allocation, state_allocation):
        """
        Allocates municipal resources based on healthcare demand, 
        federal allocation, and state allocation.

        Args:
        - healthcare_demand (float): The total healthcare demand.
        - federal_allocation (float): The allocated federal resources.
        - state_allocation (float): The allocated state resources.

        Returns:
        - float: The allocated municipal resources.
        """
        # Assuming municipal resources are allocated based on a fixed rate
        municipal_allocation_rate = 0.3
        return min(self.municipal_funding, (healthcare_demand - federal_allocation - state_allocation) * municipal_allocation_rate)

    def simulate_financing_model(self, population_needs):
        """
        Simulates the SUS financing model.

        Args:
        - population_needs (dict): A dictionary containing population needs.

        Returns:
        - dict: A dictionary containing the allocated resources.
        """
        healthcare_demand = self.calculate_healthcare_demand(population_needs)
        federal_allocation = self.allocate_federal_resources(healthcare_demand)
        state_allocation = self.allocate_state_resources(healthcare_demand, federal_allocation)
        municipal_allocation = self.allocate_municipal_resources(healthcare_demand, federal_allocation, state_allocation)

        return {
            'federal_allocation': federal_allocation,
            'state_allocation': state_allocation,
            'municipal_allocation': municipal_allocation,
            'total_allocation': federal_allocation + state_allocation + municipal_allocation
        }


def main():
    try:
        population = 1000000
        federal_funding = 1000000.0
        state_funding = 800000.0
        municipal_funding = 600000.0
        population_needs = {
            'primary_care': 50000,
            'secondary_care': 30000,
            'tertiary_care': 20000
        }

        sus_model = SUSFinancingModel(population, federal_funding, state_funding, municipal_funding)
        allocated_resources = sus_model.simulate_financing_model(population_needs)

        print("Allocated Resources:")
        for resource, allocation in allocated_resources.items():
            print(f"{resource.capitalize().replace('_', ' ')}: R${allocation:.2f}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
