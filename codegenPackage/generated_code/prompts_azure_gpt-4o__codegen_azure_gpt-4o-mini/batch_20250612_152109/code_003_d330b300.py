"""
Generated Code Metadata:
========================
Original URL: https://mimsr.edu.in
Prompt: Create a function in Python to parse and categorize the infrastructure details of MIMSR, including hostel accommodations, sports facilities, and library resources.
Generated: DETERMINISTIC_d330b300f96d7b9d
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, Any, List

class InfrastructureDetails:
    """
    A class to represent the infrastructure details of MIMSR.
    """

    def __init__(self, data: Dict[str, Any]):
        """
        Initializes the InfrastructureDetails with the provided data.

        :param data: A dictionary containing infrastructure details.
        """
        self.data = data

    def parse_hostel_accommodations(self) -> List[str]:
        """
        Parses and categorizes hostel accommodations.

        :return: A list of hostel accommodation details.
        """
        try:
            hostels = self.data.get('hostels', [])
            if not isinstance(hostels, list):
                raise ValueError("Hostels data should be a list.")
            return [hostel['name'] for hostel in hostels if 'name' in hostel]
        except Exception as e:
            print(f"Error parsing hostel accommodations: {e}")
            return []

    def parse_sports_facilities(self) -> List[str]:
        """
        Parses and categorizes sports facilities.

        :return: A list of sports facilities.
        """
        try:
            sports = self.data.get('sports_facilities', [])
            if not isinstance(sports, list):
                raise ValueError("Sports facilities data should be a list.")
            return [sport['name'] for sport in sports if 'name' in sport]
        except Exception as e:
            print(f"Error parsing sports facilities: {e}")
            return []

    def parse_library_resources(self) -> List[str]:
        """
        Parses and categorizes library resources.

        :return: A list of library resources.
        """
        try:
            libraries = self.data.get('library_resources', [])
            if not isinstance(libraries, list):
                raise ValueError("Library resources data should be a list.")
            return [library['name'] for library in libraries if 'name' in library]
        except Exception as e:
            print(f"Error parsing library resources: {e}")
            return []

    def get_infrastructure_summary(self) -> Dict[str, List[str]]:
        """
        Compiles a summary of all infrastructure details.

        :return: A dictionary containing categorized infrastructure details.
        """
        return {
            'hostel_accommodations': self.parse_hostel_accommodations(),
            'sports_facilities': self.parse_sports_facilities(),
            'library_resources': self.parse_library_resources()
        }

def main():
    # Example JSON data representing infrastructure details
    json_data = '''
    {
        "hostels": [{"name": "Hostel A"}, {"name": "Hostel B"}],
        "sports_facilities": [{"name": "Football Field"}, {"name": "Basketball Court"}],
        "library_resources": [{"name": "Main Library"}, {"name": "Digital Library"}]
    }
    '''
    
    try:
        # Load the JSON data
        data = json.loads(json_data)
        
        # Create an instance of InfrastructureDetails
        infrastructure = InfrastructureDetails(data)
        
        # Get the infrastructure summary
        summary = infrastructure.get_infrastructure_summary()
        
        # Print the summary
        print(json.dumps(summary, indent=4))
        
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
