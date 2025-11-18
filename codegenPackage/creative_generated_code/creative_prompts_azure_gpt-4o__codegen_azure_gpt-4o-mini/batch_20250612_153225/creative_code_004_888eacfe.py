"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medpointye.com
Prompt: Write a script to simulate a search feature for ELISA kits, allowing users to filter by keywords such as "Anti CCP" or "ANA," inspired by the sorting functionality on MedPointYE.
Generated: DETERMINISTIC_888eacfe2a0e2452
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class ElisaKit:
    """Class representing an ELISA kit with associated attributes."""
    def __init__(self, name, keywords):
        self.name = name
        self.keywords = keywords

    def __repr__(self):
        return f"ElisaKit(name='{self.name}', keywords={self.keywords})"


class ElisaKitSearch:
    """Class to handle searching and filtering of ELISA kits."""
    def __init__(self):
        self.kits = []

    def load_kits(self, kit_data):
        """Load ELISA kits from JSON data.

        Args:
            kit_data (str): JSON string containing kit information.
        """
        try:
            data = json.loads(kit_data)
            for item in data:
                self.kits.append(ElisaKit(name=item["name"], keywords=item.get("keywords", [])))
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
        except KeyError as e:
            print(f"Missing expected key: {e}")

    def search_kits(self, keyword):
        """Search for ELISA kits that match the provided keyword.

        Args:
            keyword (str): The keyword to search for.

        Returns:
            list: A list of matching ElisaKit objects.
        """
        keyword_lower = keyword.lower()
        matches = [kit for kit in self.kits if keyword_lower in (k.lower() for k in kit.keywords)]
        return matches

    def display_results(self, results):
        """Display the search results in a user-friendly format.

        Args:
            results (list): List of matching ElisaKit objects.
        """
        if not results:
            print("No kits found matching the search criteria.")
            return
        
        print("Matching ELISA Kits:")
        for kit in results:
            print(f"- {kit.name} (Keywords: {', '.join(kit.keywords)})")


def main():
    """Main function to run the ELISA kit search feature."""
    kit_data_json = '''
    [
        {"name": "Anti CCP ELISA Kit", "keywords": ["Anti CCP", "Rheumatoid Arthritis"]},
        {"name": "ANA ELISA Kit", "keywords": ["ANA", "Autoimmune Disease"]},
        {"name": "Vitamin D ELISA Kit", "keywords": ["Vitamin D", "Bone Health"]}
    ]
    '''

    search_feature = ElisaKitSearch()
    search_feature.load_kits(kit_data_json)

    # Example search keywords
    search_keyword = input("Enter a keyword to search for ELISA kits: ")
    results = search_feature.search_kits(search_keyword)
    search_feature.display_results(results)


if __name__ == "__main__":
    main()
```
