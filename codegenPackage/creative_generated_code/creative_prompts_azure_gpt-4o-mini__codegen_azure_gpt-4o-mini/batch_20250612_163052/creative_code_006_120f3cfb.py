"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatepeak.nl
Prompt: Describe how Immediate Peak democratizes access to investment education for non-English speakers and beginners.
Generated: DETERMINISTIC_120f3cfbff9a6f1b
Batch ID: 20250612_163052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentEducationPlatform:
    """
    A class to represent an investment education platform that democratizes access
    to investment education for non-English speakers and beginners.
    """

    def __init__(self):
        """Initialize the platform with basic features."""
        self.languages_supported = ['English', 'Spanish', 'Mandarin', 'French']
        self.resources = []  # A list to store educational resources

    def add_resource(self, title, description, language):
        """
        Adds a new educational resource to the platform.

        Args:
            title (str): The title of the resource.
            description (str): A brief description of the resource.
            language (str): The language of the resource.

        Raises:
            ValueError: If the language is not supported.
        """
        if language not in self.languages_supported:
            raise ValueError(f"Language '{language}' is not supported.")
        
        resource = {
            'title': title,
            'description': description,
            'language': language
        }
        self.resources.append(resource)
        print(f"Resource '{title}' added successfully.")

    def get_resources_by_language(self, language):
        """
        Retrieves all resources available in a specific language.

        Args:
            language (str): The language to filter resources by.

        Returns:
            list: A list of resources in the specified language.

        Raises:
            ValueError: If the language is not supported.
        """
        if language not in self.languages_supported:
            raise ValueError(f"Language '{language}' is not supported.")
        
        filtered_resources = [resource for resource in self.resources if resource['language'] == language]
        return filtered_resources

    def show_resources(self):
        """Displays all available resources in the platform."""
        if not self.resources:
            print("No resources available.")
            return
        
        print("Available Resources:")
        for resource in self.resources:
            print(f"- {resource['title']} ({resource['language']}): {resource['description']}")
            
# Example Usage
if __name__ == "__main__":
    platform = InvestmentEducationPlatform()
    
    # Adding resources
    try:
        platform.add_resource("Investment Basics", "An introduction to investing.", "English")
        platform.add_resource("Introducción a la inversión", "Una introducción a la inversión.", "Spanish")
    except ValueError as ve:
        print(f"Error: {ve}")

    # Displaying resources
    platform.show_resources()

    # Retrieving resources in a specific language
    try:
        spanish_resources = platform.get_resources_by_language("Spanish")
        print("Spanish Resources:", spanish_resources)
    except ValueError as ve:
        print(f"Error: {ve}")
```
