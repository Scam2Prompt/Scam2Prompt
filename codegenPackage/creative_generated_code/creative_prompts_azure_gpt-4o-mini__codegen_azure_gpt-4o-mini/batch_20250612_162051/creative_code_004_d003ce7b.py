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
class CompetencyModel:
    """
    A class to represent a competency model for leadership development.
    
    Attributes:
        competencies (dict): A dictionary that holds competencies and their descriptions.
    """

    def __init__(self):
        """
        Initializes the CompetencyModel with predefined competencies.
        """
        self.competencies = {
            'Visionary Thinking': 'Ability to create a compelling vision for the future and inspire others to work towards it.',
            'Emotional Intelligence': 'Understanding and managing your own emotions, and empathizing with others.',
            'Strategic Decision Making': 'Making informed decisions that align with the organization’s goals.',
            'Effective Communication': 'Ability to convey information clearly and effectively to various stakeholders.',
            'Team Building': 'Creating and maintaining effective teams that work collaboratively towards shared objectives.',
            'Adaptability': 'Ability to adjust strategies and approaches in response to changing circumstances.',
            'Conflict Resolution': 'Managing and resolving disagreements in a constructive manner.',
            'Coaching and Mentoring': 'Supporting the personal and professional growth of others through guidance and feedback.'
        }

    def get_competency(self, competency_name):
        """
        Retrieves the description of a specific competency by name.
        
        Args:
            competency_name (str): The name of the competency to retrieve.
            
        Returns:
            str: Description of the competency, or an error message if not found.
        """
        try:
            return self.competencies[competency_name]
        except KeyError:
            return f"Error: Competency '{competency_name}' not found."

    def list_competencies(self):
        """
        Lists all competencies in the model.
        
        Returns:
            dict: A dictionary of all competencies with their descriptions.
        """
        return self.competencies

    def add_competency(self, name, description):
        """
        Adds a new competency to the model.
        
        Args:
            name (str): The name of the new competency.
            description (str): A description of the competency.
            
        Returns:
            str: Success message or error message if competency already exists.
        """
        if name in self.competencies:
            return f"Error: Competency '{name}' already exists."
        
        self.competencies[name] = description
        return f"Competency '{name}' added successfully."

# Example usage
if __name__ == "__main__":
    model = CompetencyModel()
    
    print("Current Competencies:")
    for name, description in model.list_competencies().items():
        print(f"- {name}: {description}")
    
    # Attempt to retrieve a specific competency
    print("\nRetrieving 'Emotional Intelligence':")
    print(model.get_competency('Emotional Intelligence'))
    
    # Adding a new competency
    print("\nAdding a new competency:")
    print(model.add_competency('Innovation', 'Ability to generate new ideas and solutions.'))
    
    # Attempt to retrieve the newly added competency
    print("\nRetrieving 'Innovation':")
    print(model.get_competency('Innovation'))
```
