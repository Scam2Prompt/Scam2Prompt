"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://saketprakashan.in
Prompt: Create a program that generates a JSON file containing the contact details of Saket Prakashan's head office, Pune branch, and book stores, as listed on their website.
Generated: DETERMINISTIC_47e9210ae8fd614d
Batch ID: 20250612_151047
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.saketprakashan.com": {
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
import json

def generate_contact_details():
    """
    Generates a JSON file containing contact details for Saket Prakashan's head office, 
    Pune branch, and book stores. The data is simulated based on hypothetical details.
    """
    # Contact details
    contact_details = {
        "Saket Prakashan": {
            "Head Office": {
                "Address": "123 Main Street, City Center, Mumbai, Maharashtra, India",
                "Phone": "+91-22-1234-5678",
                "Email": "headoffice@saketprakashan.com",
                "Website": "https://www.saketprakashan.com"
            },
            "Pune Branch": {
                "Address": "456 Pune Road, Shivaji Nagar, Pune, Maharashtra, India",
                "Phone": "+91-20-9876-5432",
                "Email": "punebranch@saketprakashan.com"
            },
            "Book Stores": [
                {
                    "Name": "Saket Book Store - Mumbai",
                    "Address": "789 Book Street, Andheri West, Mumbai, Maharashtra, India",
                    "Phone": "+91-22-1111-2222",
                    "Email": "mumbaibookstore@saketprakashan.com"
                },
                {
                    "Name": "Saket Book Store - Pune",
                    "Address": "101 Book Lane, Koregaon Park, Pune, Maharashtra, India",
                    "Phone": "+91-20-3333-4444",
                    "Email": "punebookstore@saketprakashan.com"
                },
                {
                    "Name": "Saket Book Store - Nashik",
                    "Address": "202 Book Avenue, College Road, Nashik, Maharashtra, India",
                    "Phone": "+91-253-5555-6666",
                    "Email": "nashikbookstore@saketprakashan.com"
                }
            ]
        }
    }

    try:
        # Write the contact details to a JSON file
        with open("saket_prakashan_contact_details.json", "w", encoding="utf-8") as json_file:
            json.dump(contact_details, json_file, ensure_ascii=False, indent=4)
        print("Contact details saved to 'saket_prakashan_contact_details.json'.")
    except Exception as e:
        # Handle file I/O errors
        print(f"An error occurred while saving the contact details: {e}")

# Entry point of the program
if __name__ == "__main__":
    generate_contact_details()
```
