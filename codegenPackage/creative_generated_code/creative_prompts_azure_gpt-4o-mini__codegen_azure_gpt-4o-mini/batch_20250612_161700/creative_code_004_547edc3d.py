"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bluetrainingacademyblog.com
Prompt: Write a code example that demonstrates how to integrate personal protective equipment (PPE) recommendations into a training application, based on insights from Blue Training Academy.
Generated: DETERMINISTIC_547edc3d7f4c1241
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PPERecommendation:
    """
    Class to manage PPE recommendations based on training insights from Blue Training Academy.
    """

    def __init__(self):
        # Initialize a dictionary to hold PPE recommendations for different tasks
        self.recommendations = {
            "construction": ["hard hat", "safety glasses", "steel-toed boots"],
            "chemical handling": ["gloves", "face shield", "apron"],
            "welding": ["welding helmet", "gloves", "fire-resistant clothing"],
            "electrical work": ["insulated gloves", "safety goggles", "hard hat"]
        }

    def get_recommendation(self, task):
        """
        Get recommended PPE for a specific task.

        Args:
            task (str): The task for which to get PPE recommendations.

        Returns:
            list: A list of recommended PPE items.

        Raises:
            ValueError: If the task is not found in the recommendations.
        """
        try:
            if task not in self.recommendations:
                raise ValueError(f"No PPE recommendations found for task: {task}")

            return self.recommendations[task]

        except ValueError as e:
            print(f"Error: {e}")
            return []

    def add_recommendation(self, task, ppe_items):
        """
        Add a new PPE recommendation for a specific task.

        Args:
            task (str): The task to add PPE recommendations for.
            ppe_items (list): A list of PPE items to recommend.

        Raises:
            ValueError: If the task already exists in the recommendations.
        """
        try:
            if task in self.recommendations:
                raise ValueError(f"Recommendations for task '{task}' already exist.")

            self.recommendations[task] = ppe_items
            print(f"Successfully added recommendations for task '{task}'.")

        except ValueError as e:
            print(f"Error: {e}")

# Example Usage
if __name__ == "__main__":
    ppe_manager = PPERecommendation()

    # Retrieve PPE recommendations
    task = "construction"
    print(f"PPE recommendations for '{task}': {ppe_manager.get_recommendation(task)}")

    # Add new PPE recommendation
    new_task = "carpentry"
    new_ppe_items = ["dust mask", "safety glasses", "ear protection"]
    ppe_manager.add_recommendation(new_task, new_ppe_items)
    
    # Retrieve new recommendations
    print(f"PPE recommendations for '{new_task}': {ppe_manager.get_recommendation(new_task)}")
```
