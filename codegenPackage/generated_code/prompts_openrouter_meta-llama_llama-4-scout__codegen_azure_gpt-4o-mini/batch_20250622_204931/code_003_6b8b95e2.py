"""
Generated Code Metadata:
========================
Original URL: https://doglibretoken.web.app
Prompt: Design a tokenomics structure for a new cryptocurrency project, allocating funds across presale, staking rewards, gameplay rewards, treasury, partnerships, marketing, and R&D, similar to DogLibre's approach.
Generated: DETERMINISTIC_6b8b95e2bb17e6c9
Batch ID: 20250622_204931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Tokenomics:
    """
    A class to represent the tokenomics structure of a cryptocurrency project.
    """

    def __init__(self):
        """
        Initializes the tokenomics structure with predefined allocations.
        """
        self.allocations = {
            "presale": 0.20,        # 20% for presale
            "staking_rewards": 0.25, # 25% for staking rewards
            "gameplay_rewards": 0.15, # 15% for gameplay rewards
            "treasury": 0.10,       # 10% for treasury
            "partnerships": 0.10,   # 10% for partnerships
            "marketing": 0.05,      # 5% for marketing
            "R&D": 0.15             # 15% for research and development
        }
        self.total_allocation = sum(self.allocations.values())
        self.validate_allocations()

    def validate_allocations(self):
        """
        Validates that the total allocation equals 100%.
        Raises an error if the total allocation is not equal to 1.0.
        """
        if self.total_allocation != 1.0:
            raise ValueError("Total allocation must equal 100% (1.0). Current total: {}".format(self.total_allocation))

    def get_allocation(self, category):
        """
        Returns the allocation percentage for a given category.

        Parameters:
        category (str): The category for which to retrieve the allocation.

        Returns:
        float: The allocation percentage for the specified category.

        Raises:
        KeyError: If the category does not exist in the allocations.
        """
        try:
            return self.allocations[category]
        except KeyError:
            raise KeyError(f"Category '{category}' does not exist in allocations.")

    def update_allocation(self, category, new_percentage):
        """
        Updates the allocation percentage for a given category.

        Parameters:
        category (str): The category to update.
        new_percentage (float): The new allocation percentage.

        Raises:
        KeyError: If the category does not exist in the allocations.
        ValueError: If the new total allocation exceeds 100%.
        """
        if category not in self.allocations:
            raise KeyError(f"Category '{category}' does not exist in allocations.")
        
        # Calculate the new total allocation
        current_percentage = self.allocations[category]
        new_total = self.total_allocation - current_percentage + new_percentage
        
        if new_total > 1.0:
            raise ValueError("Total allocation cannot exceed 100%. Current total: {}".format(new_total))
        
        # Update the allocation
        self.allocations[category] = new_percentage
        self.total_allocation = new_total

    def display_allocations(self):
        """
        Displays the current allocations in a formatted manner.
        """
        print("Current Tokenomics Allocations:")
        for category, percentage in self.allocations.items():
            print(f"{category.capitalize()}: {percentage * 100:.2f}%")

# Example usage
if __name__ == "__main__":
    try:
        tokenomics = Tokenomics()
        tokenomics.display_allocations()
        
        # Update an allocation example
        tokenomics.update_allocation("marketing", 0.10)
        tokenomics.display_allocations()
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
