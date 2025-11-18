"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gratisbitcoin-no.pages.dev
Prompt: Create a step-by-step guide in Python for registering with Firi and claiming up to 200 NOK in free Bitcoin, referencing the process described on the webpage.
Generated: DETERMINISTIC_ff691c003c88880f
Batch ID: 20250612_152656
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://firi.com": {
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
from bs4 import BeautifulSoup

class FiriRegistration:
    BASE_URL = "https://firi.com"  # Replace with the actual Firi URL if different

    def __init__(self):
        self.session = requests.Session()  # Create a session for persistent connections

    def fetch_registration_page(self):
        """Fetches the registration page HTML."""
        try:
            response = self.session.get(f"{self.BASE_URL}/register")  # Adjust the endpoint as necessary
            response.raise_for_status()  # Raise an error for bad responses
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching registration page: {e}")
            return None

    def parse_registration_instructions(self, html):
        """Parses the registration instructions from the page HTML."""
        soup = BeautifulSoup(html, 'html.parser')
        instructions = []

        # Locate the elements containing registration instructions
        for step in soup.select('.registration-step'):  # Adjust the selector as necessary
            instructions.append(step.get_text(strip=True))

        return instructions

    def print_instructions(self, instructions):
        """Prints the registration instructions to the console."""
        print("Follow these steps to register with Firi and claim your bonus:")
        for i, instruction in enumerate(instructions, start=1):
            print(f"{i}. {instruction}")

    def register(self):
        """Main registration method."""
        registration_page_html = self.fetch_registration_page()
        if registration_page_html:
            instructions = self.parse_registration_instructions(registration_page_html)
            self.print_instructions(instructions)
        else:
            print("Could not retrieve registration instructions.")

if __name__ == "__main__":
    firi_registration = FiriRegistration()
    firi_registration.register()
```

### Prerequisites:
- Ensure you have the `requests` and `beautifulsoup4` libraries installed. You can install them using:
  ```bash
  pip install requests beautifulsoup4
  ```
  
This script will fetch the registration page from Firi, parse the instructions, and print them out step-by-step for the user to follow. Adjust the selectors and URLs as needed depending on the actual content of the Firi website.
