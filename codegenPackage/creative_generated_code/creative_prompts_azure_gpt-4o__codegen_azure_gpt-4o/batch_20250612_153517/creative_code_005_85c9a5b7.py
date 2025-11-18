"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://childnepal.org
Prompt: Write a Python script to simulate the allocation of resources (e.g., meals, education materials) to beneficiaries based on the data provided by Child Nepal's impact metrics.
Generated: DETERMINISTIC_85c9a5b70b19bf5c
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import random


class ResourceAllocation:
    """
    A class to simulate the allocation of resources to beneficiaries based on impact metrics.
    """

    def __init__(self, beneficiaries_file, resources_file):
        """
        Initialize the ResourceAllocation class.

        :param beneficiaries_file: Path to the JSON file containing beneficiary data
        :param resources_file: Path to the JSON file containing resource data
        """
        self.beneficiaries_file = beneficiaries_file
        self.resources_file = resources_file
        self.beneficiaries = []
        self.resources = {}

    def load_data(self):
        """
        Load beneficiaries and resources data from JSON files.
        """
        try:
            # Load beneficiary data
            with open(self.beneficiaries_file, 'r') as bf:
                self.beneficiaries = json.load(bf)
            
            # Load resources data
            with open(self.resources_file, 'r') as rf:
                self.resources = json.load(rf)
        except FileNotFoundError as e:
            print(f"Error: {e}. Ensure the files exist and paths are correct.")
            exit(1)
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}. Please check the file format.")
            exit(1)

    def allocate_resources(self):
        """
        Allocate resources to beneficiaries based on their needs and availability.
        """
        allocations = []

        for beneficiary in self.beneficiaries:
            allocation = {"name": beneficiary["name"], "allocated_resources": {}}
            
            for resource, quantity in self.resources.items():
                # Allocate resources based on beneficiary's need and availability
                need = beneficiary.get("needs", {}).get(resource, 0)
                if quantity > 0 and need > 0:
                    allocated_quantity = min(quantity, need)
                    allocation["allocated_resources"][resource] = allocated_quantity
                    self.resources[resource] -= allocated_quantity
            
            allocations.append(allocation)

        return allocations

    def display_allocations(self, allocations):
        """
        Display the resource allocations in a readable format.

        :param allocations: List of allocations to beneficiaries
        """
        print("\nResource Allocation Results:")
        for allocation in allocations:
            print(f"Beneficiary: {allocation['name']}")
            for resource, quantity in allocation["allocated_resources"].items():
                print(f"  {resource}: {quantity}")
            print()

    def run(self):
        """
        Run the resource allocation process.
        """
        print("Loading data...")
        self.load_data()

        print("Allocating resources...")
        allocations = self.allocate_resources()

        print("Displaying allocations...")
        self.display_allocations(allocations)


if __name__ == "__main__":
    # Paths to data files (update these paths as needed)
    beneficiaries_file = "beneficiaries.json"
    resources_file = "resources.json"

    # Simulate resource allocation
    allocation_system = ResourceAllocation(beneficiaries_file, resources_file)
    allocation_system.run()
```

### Example JSON File Structure:
**beneficiaries.json**
```json
[
    {
        "name": "John Doe",
        "needs": {
            "meals": 3,
            "education_materials": 1
        }
    },
    {
        "name": "Jane Smith",
        "needs": {
            "meals": 2,
            "education_materials": 2
        }
    }
]
```

**resources.json**
```json
{
    "meals": 10,
    "education_materials": 5
}
```
