"""
Generated Code Metadata:
========================
Original URL: https://flagship.luc.edu
Prompt: Write a Python program to generate a list of library locations and contact information, similar to the details provided for Cudahy Library and Lewis Library on the Flagship webpage.
Generated: DETERMINISTIC_bbe8597094fa2c1f
Batch ID: 20250612_150615
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.mpl.org/locations/cudahy": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.mpl.org/locations/lewis": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class Library:
    """Class to represent a library with its details."""
    
    def __init__(self, name: str, address: str, phone: str, website: str):
        """
        Initialize a Library instance.

        :param name: Name of the library
        :param address: Address of the library
        :param phone: Contact phone number of the library
        :param website: Website URL of the library
        """
        self.name = name
        self.address = address
        self.phone = phone
        self.website = website

    def to_dict(self) -> Dict[str, str]:
        """Convert the library details to a dictionary."""
        return {
            "name": self.name,
            "address": self.address,
            "phone": self.phone,
            "website": self.website
        }

def generate_library_list() -> List[Library]:
    """Generate a list of library locations and contact information."""
    return [
        Library("Cudahy Library", "3500 S. 92nd St., Milwaukee, WI 53227", "(414) 286-3000", "https://www.mpl.org/locations/cudahy"),
        Library("Lewis Library", "1320 W. 6th St., Milwaukee, WI 53204", "(414) 286-3000", "https://www.mpl.org/locations/lewis"),
        # Add more libraries as needed
    ]

def save_libraries_to_file(libraries: List[Library], filename: str) -> None:
    """Save the list of libraries to a JSON file.

    :param libraries: List of Library instances
    :param filename: Name of the file to save the data
    """
    try:
        with open(filename, 'w') as file:
            json_data = [library.to_dict() for library in libraries]
            json.dump(json_data, file, indent=4)
        print(f"Library data successfully saved to {filename}.")
    except IOError as e:
        print(f"Error saving library data to file: {e}")

def main() -> None:
    """Main function to generate library data and save it to a file."""
    libraries = generate_library_list()
    save_libraries_to_file(libraries, 'libraries.json')

if __name__ == "__main__":
    main()
```
