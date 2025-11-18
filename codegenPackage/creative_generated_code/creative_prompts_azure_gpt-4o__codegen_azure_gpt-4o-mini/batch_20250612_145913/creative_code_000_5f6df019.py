"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tc-harsewinkel.de
Prompt: Write a Python script to automate membership registration for a tennis club using the "easyVerein" API, ensuring the username format follows the convention "nachname_vorname" in lowercase.
Generated: DETERMINISTIC_5f6df0197dce1c7e
Batch ID: 20250612_145913
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.easyverein.de": {
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

class TennisClubMembership:
    """Class to handle membership registration for a tennis club using the easyVerein API."""
    
    def __init__(self, api_url):
        """
        Initializes the TennisClubMembership instance.
        
        Args:
            api_url (str): The base URL for the easyVerein API.
        """
        self.api_url = api_url

    def format_username(self, last_name, first_name):
        """
        Formats the username according to the convention 'nachname_vorname' in lowercase.
        
        Args:
            last_name (str): The last name of the member.
            first_name (str): The first name of the member.
        
        Returns:
            str: The formatted username.
        """
        return f"{last_name.lower()}_{first_name.lower()}"

    def register_member(self, last_name, first_name, email):
        """
        Registers a new member with the provided details.
        
        Args:
            last_name (str): The last name of the member.
            first_name (str): The first name of the member.
            email (str): The email address of the member.
        
        Raises:
            ValueError: If the email is invalid or the member registration fails.
        """
        username = self.format_username(last_name, first_name)
        payload = {
            "username": username,
            "email": email,
            "first_name": first_name,
            "last_name": last_name
        }

        try:
            response = requests.post(f"{self.api_url}/register", json=payload)
            response.raise_for_status()  # Raises an error for bad responses (4xx or 5xx)
        except requests.exceptions.RequestException as e:
            raise ValueError(f"Failed to register member: {e}")

        # Handle successful registration
        return response.json()

def main():
    """Main function to execute the membership registration."""
    api_url = "https://api.easyverein.de"  # Replace with the actual API URL
    last_name = input("Enter last name: ")
    first_name = input("Enter first name: ")
    email = input("Enter email: ")

    membership_handler = TennisClubMembership(api_url)

    try:
        member_details = membership_handler.register_member(last_name, first_name, email)
        print("Member registered successfully:", member_details)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
```
