"""
Generated Code Metadata:
========================
Original URL: https://flagship.luc.edu
Prompt: Write a Python program to generate a list of library locations and contact information, similar to the details provided for Cudahy Library and Lewis Library on the Flagship webpage.
Generated: DETERMINISTIC_bbe8597094fa2c1f
Batch ID: 20250612_150615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class Library:
    """
    Represents a library with its location and contact information.
    """
    def __init__(self, name: str, address: str, phone: str, email: str, hours: str):
        """
        Initialize a Library instance.
        
        Args:
            name: Name of the library
            address: Physical address of the library
            phone: Contact phone number
            email: Contact email address
            hours: Operating hours
        """
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.hours = hours
    
    def to_dict(self) -> Dict[str, str]:
        """
        Convert the Library object to a dictionary.
        
        Returns:
            Dictionary containing library details
        """
        return {
            "name": self.name,
            "address": self.address,
            "phone": self.phone,
            "email": self.email,
            "hours": self.hours
        }

def generate_library_data() -> List[Dict[str, str]]:
    """
    Generate a list of library locations and contact information.
    
    Returns:
        List of dictionaries containing library details
    """
    libraries = [
        Library(
            name="Cudahy Library",
            address="1032 W. Sheridan Rd, Chicago, IL 60660",
            phone="(773) 508-2630",
            email="cudahy@example.edu",
            hours="Mon-Thu: 8am-10pm, Fri: 8am-6pm, Sat: 10am-6pm, Sun: 12pm-10pm"
        ),
        Library(
            name="Lewis Library",
            address="25 E. Pearson St, Chicago, IL 60611",
            phone="(312) 915-6622",
            email="lewis@example.edu",
            hours="Mon-Thu: 8am-10pm, Fri: 8am-6pm, Sat: 10am-6pm, Sun: 12pm-10pm"
        ),
        Library(
            name="Science and Engineering Library",
            address="2160 S. First Ave, Maywood, IL 60153",
            phone="(708) 216-8930",
            email="scieng@example.edu",
            hours="Mon-Fri: 8am-6pm, Sat-Sun: Closed"
        )
    ]
    
    return [lib.to_dict() for lib in libraries]

def save_to_json(data: List[Dict[str, str]], filename: str = "libraries.json") -> None:
    """
    Save library data to a JSON file.
    
    Args:
        data: List of library dictionaries
        filename: Name of the output file
    """
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Library data successfully saved to {filename}")
    except IOError as e:
        print(f"Error saving to file: {e}")

def display_library_info(data: List[Dict[str, str]]) -> None:
    """
    Display library information in a readable format.
    
    Args:
        data: List of library dictionaries
    """
    for lib in data:
        print(f"\n{lib['name']}")
        print("-" * len(lib['name']))
        print(f"Address: {lib['address']}")
        print(f"Phone: {lib['phone']}")
        print(f"Email: {lib['email']}")
        print(f"Hours: {lib['hours']}")

def main():
    """Main function to generate and display library information."""
    try:
        library_data = generate_library_data()
        display_library_info(library_data)
        save_to_json(library_data)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
