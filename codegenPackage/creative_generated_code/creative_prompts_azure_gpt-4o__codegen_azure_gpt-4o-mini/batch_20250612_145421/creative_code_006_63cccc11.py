"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zapper-frontend-next-h5ht7yy42-zapper-fi.vercel.app
Prompt: Write code to use Zapper's Beta API to fetch and categorize DAO projects such as Friends with Benefits or Gitcoin DAO based on their descriptions.
Generated: DETERMINISTIC_63cccc11559529ca
Batch ID: 20250612_145421
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.zapper.fi/v1": {
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

class ZapperAPI:
    """A class to interact with Zapper's Beta API for fetching DAO projects."""

    BASE_URL = "https://api.zapper.fi/v1"

    def __init__(self, api_key):
        """
        Initialize the ZapperAPI instance with the provided API key.

        Args:
            api_key (str): Your API key for Zapper's Beta API.
        """
        self.api_key = api_key

    def fetch_dao_projects(self):
        """
        Fetch the list of DAO projects from Zapper's Beta API.

        Returns:
            list: A list of DAO projects with their descriptions.
        """
        url = f"{self.BASE_URL}/daos"
        headers = {"Authorization": f"Bearer {self.api_key}"}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response as a list
        except requests.exceptions.RequestException as e:
            print(f"Error fetching DAO projects: {e}")
            return []

    def categorize_projects(self, projects):
        """
        Categorize DAO projects based on their descriptions.

        Args:
            projects (list): A list of DAO projects.

        Returns:
            dict: A dictionary categorizing projects by keyword.
        """
        categorized = {
            "friends_with_benefits": [],
            "gitcoin": [],
            "others": []
        }

        for project in projects:
            description = project.get("description", "").lower()
            if "friends with benefits" in description:
                categorized["friends_with_benefits"].append(project)
            elif "gitcoin" in description:
                categorized["gitcoin"].append(project)
            else:
                categorized["others"].append(project)

        return categorized


def main():
    """Main function to execute the fetching and categorizing of DAO projects."""
    # Replace 'your_api_key_here' with your actual Zapper API key
    api_key = 'your_api_key_here'
    zapper_api = ZapperAPI(api_key)

    # Fetch DAO projects
    projects = zapper_api.fetch_dao_projects()

    # Categorize the fetched projects
    categorized_projects = zapper_api.categorize_projects(projects)

    # Print the categorized projects
    for category, projects in categorized_projects.items():
        print(f"\nCategory: {category.replace('_', ' ').title()}")
        for project in projects:
            print(f"- {project.get('name')} : {project.get('description')}")


if __name__ == "__main__":
    main()
```
