"""
Generated Code Metadata:
========================
Original URL: https://masitsolutions.net
Prompt: "Provide an example of a technical support outsourcing agreement for a company with a global presence."
Generated: DETERMINISTIC_218fa1aafd1e0351
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Technical Support Outsourcing Agreement Generator

This script generates a sample technical support outsourcing agreement for a company with a global presence.
The agreement is structured as a JSON object for easy integration into systems or further processing.
"""

import json
from datetime import datetime

def generate_agreement(company_name, service_provider_name, start_date, end_date, services, contact_info):
    """
    Generates a technical support outsourcing agreement.

    Args:
        company_name (str): Name of the company outsourcing technical support.
        service_provider_name (str): Name of the service provider.
        start_date (str): Start date of the agreement in YYYY-MM-DD format.
        end_date (str): End date of the agreement in YYYY-MM-DD format.
        services (list): List of services to be provided.
        contact_info (dict): Contact information for both parties.

    Returns:
        dict: A structured agreement as a dictionary.
    """
    try:
        # Validate date format
        datetime.strptime(start_date, "%Y-%m-%d")
        datetime.strptime(end_date, "%Y-%m-%d")
        
        # Validate services list
        if not isinstance(services, list) or not all(isinstance(service, str) for service in services):
            raise ValueError("Services must be a list of strings.")
        
        # Validate contact info
        if not isinstance(contact_info, dict) or "company" not in contact_info or "provider" not in contact_info:
            raise ValueError("Contact info must be a dictionary with 'company' and 'provider' keys.")
        
        # Create agreement structure
        agreement = {
            "agreement_title": "Technical Support Outsourcing Agreement",
            "company_name": company_name,
            "service_provider_name": service_provider_name,
            "start_date": start_date,
            "end_date": end_date,
            "services": services,
            "contact_info": contact_info,
            "terms_and_conditions": {
                "confidentiality": "Both parties agree to maintain confidentiality of sensitive information.",
                "payment_terms": "Payment will be made on a monthly basis as per the agreed rates.",
                "termination_clause": "Either party may terminate the agreement with a 30-day written notice.",
                "liability": "The service provider is liable for damages caused by negligence up to the agreed limit."
            },
            "global_support": {
                "availability": "24/7 support across all time zones.",
                "languages_supported": ["English", "Spanish", "French", "German", "Mandarin"]
            }
        }
        
        return agreement
    
    except ValueError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def save_agreement_to_file(agreement, file_name):
    """
    Saves the agreement to a JSON file.

    Args:
        agreement (dict): The agreement to save.
        file_name (str): Name of the file to save the agreement to.

    Returns:
        bool: True if the file was saved successfully, False otherwise.
    """
    try:
        with open(file_name, "w") as file:
            json.dump(agreement, file, indent=4)
        print(f"Agreement saved to {file_name}")
        return True
    except Exception as e:
        print(f"Failed to save agreement: {e}")
        return False

# Example usage
if __name__ == "__main__":
    company_name = "GlobalTech Inc."
    service_provider_name = "SupportPro Solutions"
    start_date = "2023-01-01"
    end_date = "2025-12-31"
    services = ["Help Desk Support", "Network Monitoring", "Incident Management"]
    contact_info = {
        "company": {
            "name": "GlobalTech Inc.",
            "email": "contact@globaltech.com",
            "phone": "+1-800-555-1234"
        },
        "provider": {
            "name": "SupportPro Solutions",
            "email": "support@supportpro.com",
            "phone": "+1-800-555-5678"
        }
    }
    
    agreement = generate_agreement(company_name, service_provider_name, start_date, end_date, services, contact_info)
    
    if agreement:
        save_agreement_to_file(agreement, "technical_support_agreement.json")
```
