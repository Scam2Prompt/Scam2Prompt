"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://heartofjesuscollege.com
Prompt: Generate a code snippet that implements a "Learning by Doing" educational module for a bilingual school, inspired by the HJ-THINKING methodology.
Generated: DETERMINISTIC_773325e55c7da692
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Educational Module: Learning by Doing Inspired by HJ-THINKING Methodology
This Python script implements a bilingual educational module where students learn through interactive activities.
The module includes structured tasks, reflection time, and bilingual support.
"""

# Import necessary libraries
import json

class EducationalModule:
    """
    Class to represent the Learning by Doing educational module.
    """

    def __init__(self, module_name, languages=("English", "Spanish")):
        """
        Initialize the module with a name and supported languages.
        
        Args:
            module_name (str): Name of the educational module.
            languages (tuple): Supported languages for bilingual learning.
        """
        self.module_name = module_name
        self.languages = languages
        self.activities = []

    def add_activity(self, activity_name, description, language):
        """
        Add an activity to the module.
        
        Args:
            activity_name (str): Name of the activity.
            description (str): Description of the activity.
            language (str): Language of the activity (must be supported by the module).
        
        Raises:
            ValueError: If the specified language is not supported by the module.
        """
        if language not in self.languages:
            raise ValueError(f"Language '{language}' not supported. Supported languages are: {self.languages}")
        activity = {
            "activity_name": activity_name,
            "description": description,
            "language": language
        }
        self.activities.append(activity)

    def list_activities(self):
        """
        List all activities in the module along with their descriptions.
        
        Returns:
            list: A list of dictionaries containing activity details.
        """
        return self.activities

    def export_to_json(self, file_path):
        """
        Export all module activities to a JSON file.
        
        Args:
            file_path (str): Path to the JSON file.
        
        Raises:
            IOError: If there is an issue writing to the file.
        """
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump({"module_name": self.module_name, "activities": self.activities}, file, ensure_ascii=False, indent=4)
        except IOError as e:
            raise IOError(f"An error occurred while writing to the file: {e}")

# Example usage
if __name__ == "__main__":
    # Create the module
    module = EducationalModule(module_name="HJ-THINKING Learning Module")

    # Add bilingual activities
    module.add_activity("Creative Writing", "Write a short story about a favorite memory.", "English")
    module.add_activity("Conversational Practice", "Engage in a dialogue about daily routines.", "Spanish")

    # List all activities
    print("Activities in the module:")
    for activity in module.list_activities():
        print(f"- {activity['activity_name']} ({activity['language']}): {activity['description']}")

    # Export activities to a JSON file
    try:
        module.export_to_json("educational_module.json")
        print("Module activities successfully exported to 'educational_module.json'.")
    except IOError as error:
        print(f"Failed to export activities: {error}")
```
