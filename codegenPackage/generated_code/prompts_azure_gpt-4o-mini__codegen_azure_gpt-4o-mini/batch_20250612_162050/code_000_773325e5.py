"""
Generated Code Metadata:
========================
Original URL: https://heartofjesuscollege.com
Prompt: Generate a code snippet that implements a "Learning by Doing" educational module for a bilingual school, inspired by the HJ-THINKING methodology.
Generated: DETERMINISTIC_773325e55c7da692
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class LearningByDoingModule:
    """
    A class to implement a 'Learning by Doing' educational module for a bilingual school,
    inspired by the HJ-THINKING methodology.
    """

    def __init__(self, language='English'):
        """
        Initializes the LearningByDoingModule with a specified language.

        :param language: The language of instruction (default is 'English').
        """
        self.language = language
        self.activities = []
        self.current_activity_index = 0

    def add_activity(self, activity):
        """
        Adds a new activity to the module.

        :param activity: A dictionary containing activity details.
        :raises ValueError: If the activity does not contain required keys.
        """
        required_keys = ['title', 'description', 'instructions']
        if not all(key in activity for key in required_keys):
            raise ValueError(f"Activity must contain keys: {required_keys}")

        self.activities.append(activity)

    def get_current_activity(self):
        """
        Retrieves the current activity based on the current index.

        :return: A dictionary containing the current activity details.
        :raises IndexError: If there are no activities added.
        """
        if not self.activities:
            raise IndexError("No activities available. Please add an activity.")
        
        return self.activities[self.current_activity_index]

    def next_activity(self):
        """
        Moves to the next activity in the module.

        :raises IndexError: If there are no more activities to navigate to.
        """
        if self.current_activity_index + 1 >= len(self.activities):
            raise IndexError("No more activities available.")
        
        self.current_activity_index += 1

    def reset_activities(self):
        """
        Resets the activity index to the first activity.
        """
        self.current_activity_index = 0

    def display_activity(self):
        """
        Displays the current activity in the specified language.
        """
        try:
            activity = self.get_current_activity()
            print(f"Title: {activity['title']}")
            print(f"Description: {activity['description']}")
            print(f"Instructions: {activity['instructions']}")
        except (IndexError, ValueError) as e:
            print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    module = LearningByDoingModule(language='Spanish')

    # Adding activities
    try:
        module.add_activity({
            'title': 'Construir un puente',
            'description': 'Usar materiales reciclados para construir un puente.',
            'instructions': 'Usa cinta adhesiva, palitos de helado y tu creatividad.'
        })

        module.add_activity({
            'title': 'Experimento de volcán',
            'description': 'Crear un volcán en erupción usando bicarbonato de sodio.',
            'instructions': 'Mezcla bicarbonato de sodio y vinagre para ver la erupción.'
        })

        # Displaying activities
        module.display_activity()  # Display first activity
        module.next_activity()      # Move to next activity
        module.display_activity()  # Display second activity

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
