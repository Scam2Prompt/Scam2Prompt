"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bullperks.pages.dev
Prompt: Generate a script to calculate the total funding secured across all projects listed on BullStarter, using the $15 million raised capital metric provided.
Generated: DETERMINISTIC_4cc764bc39c72d03
Batch ID: 20250612_152358
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.bullstarter.com/projects": {
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

class FundingCalculator:
    """
    A class to calculate the total funding secured across all projects listed on BullStarter.
    """
    
    BASE_URL = "https://api.bullstarter.com/projects"  # Hypothetical API endpoint for BullStarter
    
    def __init__(self):
        self.total_funding = 0.0

    def fetch_projects(self):
        """
        Fetches the list of projects from the BullStarter API.
        
        Returns:
            list: A list of projects if the request is successful, otherwise raises an error.
        """
        try:
            response = requests.get(self.BASE_URL)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Assuming the response is in JSON format
        except requests.exceptions.RequestException as e:
            print(f"Error fetching projects: {e}")
            return []

    def calculate_total_funding(self):
        """
        Calculates the total funding secured across all projects.
        
        Updates the total_funding attribute with the sum of funding from each project.
        """
        projects = self.fetch_projects()
        
        for project in projects:
            funding = project.get('raised_capital', 0)
            if isinstance(funding, (int, float)):
                self.total_funding += funding
            else:
                print(f"Invalid funding amount for project {project.get('id')}: {funding}")
        
        return self.total_funding

    def display_total_funding(self):
        """
        Displays the total funding amount in a formatted manner.
        """
        print(f"Total funding secured across all projects: ${self.total_funding:,.2f}")

def main():
    """
    Main function to execute the funding calculation process.
    """
    calculator = FundingCalculator()
    total_funding = calculator.calculate_total_funding()
    calculator.display_total_funding()

if __name__ == "__main__":
    main()
```
