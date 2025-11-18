"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sadadeng.com
Prompt: Write code to simulate the allocation of resources (e.g., staff and equipment) for construction projects based on the types of projects described on Sadad Engineering's website.
Generated: DETERMINISTIC_c51dd4c0fae8c22e
Batch ID: 20250612_152326
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import List, Dict, Union

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ResourceAllocator:
    """
    Class to simulate the allocation of resources for construction projects.
    """
    def __init__(self):
        # Initialize available resources
        self.staff = {
            "engineer": 10,
            "technician": 20,
            "laborer": 50
        }
        self.equipment = {
            "crane": 2,
            "excavator": 4,
            "truck": 10
        }
        logging.info("ResourceAllocator initialized with staff and equipment.")

    def allocate_resources(self, project_type: str) -> Union[Dict[str, int], str]:
        """
        Allocate resources based on the type of project.
        Args:
            project_type (str): The type of construction project.
        Returns:
            Union[Dict[str, int], str]: Allocated resources or an error message.
        """
        # Define resource requirements for different project types
        project_requirements = {
            "residential": {"engineer": 2, "technician": 5, "laborer": 10, "crane": 0, "excavator": 1, "truck": 2},
            "commercial": {"engineer": 3, "technician": 8, "laborer": 15, "crane": 1, "excavator": 2, "truck": 4},
            "industrial": {"engineer": 5, "technician": 10, "laborer": 20, "crane": 2, "excavator": 3, "truck": 6}
        }

        if project_type not in project_requirements:
            logging.error(f"Invalid project type: {project_type}")
            return f"Error: Invalid project type '{project_type}'."

        required_resources = project_requirements[project_type]

        allocated_resources = {}
        for resource, required_amount in required_resources.items():
            if resource in self.staff:
                if self.staff[resource] >= required_amount:
                    self.staff[resource] -= required_amount
                    allocated_resources[resource] = required_amount
                else:
                    logging.warning(f"Insufficient staff for {resource}. Required: {required_amount}, Available: {self.staff[resource]}")
                    return f"Error: Insufficient staff for {resource}."
            elif resource in self.equipment:
                if self.equipment[resource] >= required_amount:
                    self.equipment[resource] -= required_amount
                    allocated_resources[resource] = required_amount
                else:
                    logging.warning(f"Insufficient equipment for {resource}. Required: {required_amount}, Available: {self.equipment[resource]}")
                    return f"Error: Insufficient equipment for {resource}."
            else:
                logging.error(f"Unknown resource type: {resource}")
                return f"Error: Unknown resource type '{resource}'."

        logging.info(f"Resources allocated successfully for project type '{project_type}': {allocated_resources}")
        return allocated_resources

    def reset_resources(self):
        """
        Reset resources to their initial state.
        """
        self.staff = {
            "engineer": 10,
            "technician": 20,
            "laborer": 50
        }
        self.equipment = {
            "crane": 2,
            "excavator": 4,
            "truck": 10
        }
        logging.info("Resources reset to initial state.")

if __name__ == "__main__":
    # Example usage of the ResourceAllocator class
    allocator = ResourceAllocator()

    # Simulate allocation for a residential project
    result = allocator.allocate_resources("residential")
    print(result)

    # Simulate allocation for an industrial project
    result = allocator.allocate_resources("industrial")
    print(result)

    # Reset resources to their initial state
    allocator.reset_resources()
    print("Resources have been reset.")
```
