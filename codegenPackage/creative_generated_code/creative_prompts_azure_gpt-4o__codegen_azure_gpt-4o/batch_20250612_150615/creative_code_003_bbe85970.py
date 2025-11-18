"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flagship.luc.edu
Prompt: Write a Python program to generate a list of library locations and contact information, similar to the details provided for Cudahy Library and Lewis Library on the Flagship webpage.
Generated: DETERMINISTIC_bbe8597094fa2c1f
Batch ID: 20250612_150615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def main():
    """
    Main function to generate a list of libraries with their locations and contact information.
    The data is printed in a JSON format for easy readability.
    """
    # List of libraries with details
    libraries = [
        {
            "name": "Cudahy Library",
            "address": "1032 W. Sheridan Rd, Chicago, IL 60660",
            "phone": "(773) 508-2632",
            "email": "cudahylibrary@university.edu",
            "hours": "Mon-Fri: 8am - 10pm, Sat-Sun: 10am - 6pm"
        },
        {
            "name": "Lewis Library",
            "address": "25 E. Pearson St, Chicago, IL 60611",
            "phone": "(312) 915-6622",
            "email": "lewislibrary@university.edu",
            "hours": "Mon-Fri: 9am - 9pm, Sat: 10am - 5pm, Sun: Closed"
        }
    ]

    try:
        # Convert the list of libraries to a JSON string with indentation for readability
        library_json = json.dumps(libraries, indent=4)
        
        # Print the formatted JSON string
        print("Library Information:")
        print(library_json)
    except Exception as e:
        # Handle any unexpected exceptions
        print(f"An error occurred while generating library data: {e}")


if __name__ == "__main__":
    # Entry point of the program
    main()
```
