"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancakeswap.vn
Prompt: Create a training curriculum for teaching blockchain technology, AI, and software development, based on the structure and offerings of CAKE Training Academy.
Generated: DETERMINISTIC_ac4e8ce0bb1b773c
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Curriculum:
    """
    Represents the training curriculum for Blockchain Technology, AI, and Software Development.
    """

    def __init__(self):
        """Initialize the curriculum with predefined modules."""
        self.modules = {
            "Blockchain Technology": [],
            "Artificial Intelligence": [],
            "Software Development": []
        }

    def add_module(self, category, module_name, duration, prerequisites=None):
        """
        Adds a module to the specified category in the curriculum.

        Parameters:
        - category (str): The category to which the module belongs.
        - module_name (str): The name of the module.
        - duration (str): Duration of the module (e.g., "2 weeks").
        - prerequisites (list, optional): List of prerequisite modules.

        Raises:
        - ValueError: If the category is invalid or if the module name already exists in the category.
        """
        if category not in self.modules:
            raise ValueError(f"Invalid category: {category}. Valid categories are: {', '.join(self.modules.keys())}.")
        if module_name in [module['name'] for module in self.modules[category]]:
            raise ValueError(f"Module '{module_name}' already exists in category '{category}'.")

        module = {
            'name': module_name,
            'duration': duration,
            'prerequisites': prerequisites or []
        }
        self.modules[category].append(module)

    def get_curriculum(self):
        """Returns the complete curriculum as a dictionary."""
        return self.modules

    def display_curriculum(self):
        """Prints the curriculum in a readable format."""
        for category, modules in self.modules.items():
            print(f"Category: {category}")
            for module in modules:
                print(f"  - {module['name']} ({module['duration']})")
                if module['prerequisites']:
                    print(f"    Prerequisites: {', '.join(module['prerequisites'])}")
            print()

# Example usage
if __name__ == "__main__":
    try:
        curriculum = Curriculum()

        # Add modules for Blockchain Technology
        curriculum.add_module("Blockchain Technology", "Introduction to Blockchain", "4 weeks")
        curriculum.add_module("Blockchain Technology", "Smart Contracts", "3 weeks", ["Introduction to Blockchain"])

        # Add modules for Artificial Intelligence
        curriculum.add_module("Artificial Intelligence", "AI Fundamentals", "6 weeks")
        curriculum.add_module("Artificial Intelligence", "Machine Learning", "8 weeks", ["AI Fundamentals"])

        # Add modules for Software Development
        curriculum.add_module("Software Development", "Programming Basics", "5 weeks")
        curriculum.add_module("Software Development", "Web Development", "6 weeks", ["Programming Basics"])

        # Display the complete curriculum
        curriculum.display_curriculum()

    except ValueError as e:
        print(f"Error: {e}")
```
