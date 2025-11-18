"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simho.in
Prompt: Write Python code to automate the process of collecting and organizing contact information from HR service providers, referencing the structure of the contact details provided on the SIMHO website.
Generated: DETERMINISTIC_55411b8d44f068f9
Batch ID: 20250612_153246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.simho.org/contact": {
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
import csv
import os

# Constants for the target URL and output file
TARGET_URL = 'https://www.simho.org/contact'
OUTPUT_FILE = 'hr_service_providers_contacts.csv'

def fetch_contact_information(url):
    """
    Fetch contact information from the specified URL.
    
    Args:
        url (str): The URL to scrape contact information from.

    Returns:
        list: A list of dictionaries containing contact details.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        contacts = []

        # Assuming the contact details are in a specific HTML structure
        # Modify the selectors according to the actual structure of the website
        for contact in soup.select('.contact-card'):
            name = contact.select_one('.name').get_text(strip=True)
            email = contact.select_one('.email').get_text(strip=True)
            phone = contact.select_one('.phone').get_text(strip=True)
            organization = contact.select_one('.organization').get_text(strip=True)

            # Append the contact information to the list
            contacts.append({
                'Name': name,
                'Email': email,
                'Phone': phone,
                'Organization': organization
            })
        
        return contacts
    
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

def save_contacts_to_csv(contacts, filename):
    """
    Save the list of contacts to a CSV file.
    
    Args:
        contacts (list): A list of dictionaries containing contact details.
        filename (str): The name of the output CSV file.
    """
    try:
        # Check if contacts list is empty
        if not contacts:
            print("No contacts to save.")
            return
        
        # Define CSV field names
        fieldnames = contacts[0].keys()
        
        with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()  # Write the header
            writer.writerows(contacts)  # Write the contact data
        
        print(f"Contacts saved to {filename}")
    
    except IOError as e:
        print(f"Error writing to file: {e}")

def main():
    """
    Main function to orchestrate the fetching and saving of contact information.
    """
    contacts = fetch_contact_information(TARGET_URL)
    save_contacts_to_csv(contacts, OUTPUT_FILE)

if __name__ == '__main__':
    main()
```
