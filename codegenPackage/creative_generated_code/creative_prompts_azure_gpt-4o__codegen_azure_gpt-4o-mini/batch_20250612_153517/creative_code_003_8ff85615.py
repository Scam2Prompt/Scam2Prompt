"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plus.endeavorschools.com
Prompt: Write a script in Python to categorize and display extracurricular programs (e.g., STEM, Tot Hop, Art) based on the descriptions provided on the Endeavor Schools Plus website.
Generated: DETERMINISTIC_8ff85615bb877da1
Batch ID: 20250612_153517
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/api/programs": {
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

class ProgramCategorizer:
    """
    A class to categorize and display extracurricular programs based on their descriptions.
    """

    def __init__(self, url):
        """
        Initializes the ProgramCategorizer with the URL of the programs.

        Args:
            url (str): The URL to fetch the programs data from.
        """
        self.url = url
        self.programs = []

    def fetch_programs(self):
        """
        Fetches the extracurricular programs data from the provided URL.

        Raises:
            Exception: If the request to fetch data fails.
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an error for bad responses
            self.programs = response.json()  # Assuming the response is in JSON format
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching data: {e}")

    def categorize_programs(self):
        """
        Categorizes programs into various categories based on their descriptions.

        Returns:
            dict: A dictionary with categories as keys and lists of program names as values.
        """
        categories = {
            "STEM": [],
            "Arts": [],
            "Sports": [],
            "Dance": [],
            "Other": []
        }

        for program in self.programs:
            description = program.get("description", "").lower()
            name = program.get("name", "Unnamed Program")

            if "science" in description or "technology" in description or "engineering" in description or "math" in description:
                categories["STEM"].append(name)
            elif "art" in description or "craft" in description:
                categories["Arts"].append(name)
            elif "soccer" in description or "basketball" in description or "sports" in description:
                categories["Sports"].append(name)
            elif "dance" in description:
                categories["Dance"].append(name)
            else:
                categories["Other"].append(name)

        return categories

    def display_programs(self, categorized_programs):
        """
        Displays the categorized programs in a readable format.

        Args:
            categorized_programs (dict): The categorized programs to display.
        """
        for category, programs in categorized_programs.items():
            print(f"{category} Programs:")
            if programs:
                for program in programs:
                    print(f" - {program}")
            else:
                print(" - None")
            print("")  # Blank line for better readability

def main():
    """
    Main function to execute the program categorization.
    """
    url = "https://example.com/api/programs"  # Replace with the actual URL
    categorizer = ProgramCategorizer(url)

    try:
        categorizer.fetch_programs()
        categorized_programs = categorizer.categorize_programs()
        categorizer.display_programs(categorized_programs)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
