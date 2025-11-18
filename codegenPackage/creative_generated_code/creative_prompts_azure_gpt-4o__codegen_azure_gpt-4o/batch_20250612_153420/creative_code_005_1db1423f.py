"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ihsh.edu.bd
Prompt: Write a function to extract contact details, including phone numbers and email addresses, from the Ideal High School's "Contact Us" section.
Generated: DETERMINISTIC_1db1423f84080072
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from bs4 import BeautifulSoup

def extract_contact_details(html_content):
    """
    Extracts contact details (phone numbers and email addresses) from the HTML content 
    of a webpage's 'Contact Us' section.

    Parameters:
        html_content (str): The HTML content of the webpage.

    Returns:
        dict: A dictionary containing extracted phone numbers and email addresses.
    """
    try:
        # Validate input
        if not isinstance(html_content, str):
            raise ValueError("html_content must be a string containing valid HTML.")

        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Initialize patterns for extracting phone numbers and email addresses
        phone_pattern = r'\+?[0-9\s\-\(\)]{7,15}'
        email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

        # Extract text content from the Contact Us section
        contact_section = soup.find('section', {'id': 'contact-us'})  # Assuming section ID is 'contact-us'
        if not contact_section:
            raise ValueError("No 'Contact Us' section found in the provided HTML.")

        contact_text = contact_section.get_text()  # Get all text within the section

        # Extract phone numbers and email addresses using regular expressions
        phone_numbers = re.findall(phone_pattern, contact_text)
        emails = re.findall(email_pattern, contact_text)

        # Remove duplicates and clean up results
        phone_numbers = list(set(phone_numbers))
        emails = list(set(emails))

        # Return results as a dictionary
        return {
            'phone_numbers': phone_numbers,
            'emails': emails
        }

    except Exception as e:
        # Log or handle errors appropriately; re-raise for now
        raise RuntimeError(f"An error occurred while extracting contact details: {e}")

# Example usage:
# html_content = "<html>...</html>"  # Replace with actual HTML content
# contact_details = extract_contact_details(html_content)
# print(contact_details)
```
