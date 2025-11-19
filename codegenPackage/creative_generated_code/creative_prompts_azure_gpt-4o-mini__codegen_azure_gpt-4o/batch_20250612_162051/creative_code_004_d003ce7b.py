"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neshagroup.ir
Prompt: What are the key components of a competency model for leadership development as outlined by Nesha Group? Provide a code snippet that outlines a framework for this model.
Generated: DETERMINISTIC_d003ce7b663e773b
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# competency_model.py

class CompetencyModel:
    """
    A framework for defining key components of a competency model 
    for leadership development, as outlined by Nesha Group.
    """

    def __init__(self):
        """
        Initializes the competency model with predefined components.
        """
        self.components = {
            "Visionary Thinking": "Ability to articulate and inspire a clear vision.",
            "Emotional Intelligence": "Capacity to understand, manage, and influence emotions effectively.",
            "Decision-Making": "Skill in making informed and strategic decisions.",
            "Communication Skills": "Proficiency in conveying ideas and fostering collaboration.",
            "Adaptability": "Flexibility and resilience in navigating change.",
            "Team Building": "Ability to develop and lead high-performing teams.",
            "Ethical Leadership": "Commitment to integrity, accountability, and ethical decision-making."
        }

    def get_components(self):
        """
        Retrieves the key components of the competency model.

        Returns:
            dict: A dictionary of competency components and their descriptions.
        """
        return self.components

    def add_component(self, name, description):
        """
        Adds a new component to the competency model.

        Args:
            name (str): The name of the competency component.
            description (str): A brief description of the component.

        Raises:
            ValueError: If the name or description is empty.
        """
        if not name or not description:
            raise ValueError("Both name and description must be provided.")
        
        self.components[name] = description

    def remove_component(self, name):
        """
        Removes a component from the competency model.

        Args:
            name (str): The name of the component to be removed.

        Raises:
            KeyError: If the component with the given name does not exist.
        """
        if name not in self.components:
            raise KeyError(f"Component '{name}' does not exist.")
        
        del self.components[name]

    def display_model(self):
        """
        Displays the competency model in a readable format.
        """
        print("Leadership Development Competency Model (Nesha Group):")
        for name, description in self.components.items():
            print(f"- {name}: {description}")


# Example usage
if __name__ == "__main__":
    try:
        model = CompetencyModel()
        model.display_model()

        # Adding a new competency
        model.add_component("Strategic Thinking", "Ability to forecast and plan long-term goals.")
        print("\nUpdated Model:")
        model.display_model()

        # Removing an existing competency
        model.remove_component("Team Building")
        print("\nModel after removal:")
        model.display_model()

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
