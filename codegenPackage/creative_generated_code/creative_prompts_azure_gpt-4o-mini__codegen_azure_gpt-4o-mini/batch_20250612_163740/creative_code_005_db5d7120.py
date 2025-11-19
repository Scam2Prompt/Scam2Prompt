"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tcs-campaigns.com
Prompt: Create a guided development prompt using the pre-built prompt library from TCS AI Catapult Forward for a new software project.
Generated: DETERMINISTIC_db5d71208c374e3c
Batch ID: 20250612_163740
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.tcsai.catapultforward.com/prompts": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests

class GuidedDevelopment:
    """
    A class to facilitate guided development prompts using TCS AI Catapult Forward's pre-built prompt library.
    """

    BASE_URL = "https://api.tcsai.catapultforward.com/prompts"

    def __init__(self, project_name: str):
        """
        Initializes the GuidedDevelopment with a project name.

        Args:
            project_name (str): The name of the software project for which prompts will be generated.
        """
        self.project_name = project_name

    def fetch_prompts(self):
        """
        Fetches the guided development prompts for the specified project.

        Returns:
            list: A list of prompts related to the project.

        Raises:
            Exception: If there is an error fetching prompts from the API.
        """
        try:
            response = requests.get(f"{self.BASE_URL}?project_name={self.project_name}")

            # Raise an exception for HTTP errors
            response.raise_for_status()

            # Return the JSON response containing prompts
            return response.json().get("prompts", [])

        except requests.RequestException as e:
            raise Exception(f"Error fetching prompts: {e}")

    def display_prompts(self):
        """
        Displays the fetched prompts in a user-friendly format.
        """
        try:
            prompts = self.fetch_prompts()
            if not prompts:
                print("No prompts found for the project.")
                return

            print(f"Guided Development Prompts for '{self.project_name}':\n")
            for idx, prompt in enumerate(prompts, start=1):
                print(f"{idx}. {prompt}")

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    project_name = "NewSoftwareProject"  # Replace with the actual project name
    guided_dev = GuidedDevelopment(project_name)
    guided_dev.display_prompts()
```
