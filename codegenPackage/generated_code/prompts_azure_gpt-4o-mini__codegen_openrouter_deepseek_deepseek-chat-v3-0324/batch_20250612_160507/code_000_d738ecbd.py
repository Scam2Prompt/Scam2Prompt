"""
Generated Code Metadata:
========================
Original URL: https://hubexperts.ch
Prompt: Generate a Python script that automates the process of creating a company in Switzerland, including steps for domiciliation and appointing an administrator, as described by Hub Experts.
Generated: DETERMINISTIC_d738ecbd5072408a
Batch ID: 20250612_160507
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.hubexperts.com/v1": {
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
import requests
import json
from typing import Dict, Optional, Union
from datetime import datetime

class SwissCompanyCreator:
    """
    A class to automate the process of creating a company in Switzerland,
    including domiciliation and appointing an administrator.
    """
    
    def __init__(self, api_key: str, base_url: str = "https://api.hubexperts.com/v1"):
        """
        Initialize the SwissCompanyCreator with API credentials.
        
        Args:
            api_key (str): API key for Hub Experts service
            base_url (str, optional): Base URL for the API. Defaults to Hub Experts production URL.
        """
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
    def _make_request(self, method: str, endpoint: str, data: Optional[Dict] = None) -> Union[Dict, None]:
        """
        Internal method to make API requests with error handling.
        
        Args:
            method (str): HTTP method (GET, POST, PUT, DELETE)
            endpoint (str): API endpoint
            data (Optional[Dict]): Request payload
            
        Returns:
            Union[Dict, None]: Response data or None if request failed
            
        Raises:
            ValueError: If the request fails
        """
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.request(method, url, headers=self.headers, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            raise ValueError(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as err:
            raise ValueError(f"Request error occurred: {err}")
        except json.JSONDecodeError as json_err:
            raise ValueError(f"JSON decode error: {json_err}")
    
    def check_company_name_availability(self, company_name: str) -> bool:
        """
        Check if a company name is available in Switzerland.
        
        Args:
            company_name (str): Desired company name
            
        Returns:
            bool: True if name is available, False otherwise
        """
        endpoint = f"company/check-name?name={company_name}"
        response = self._make_request("GET", endpoint)
        return response.get("available", False)
    
    def create_legal_entity(self, company_data: Dict) -> Dict:
        """
        Create a new legal entity in Switzerland.
        
        Args:
            company_data (Dict): Company details including:
                - name (str): Company name
                - legal_form (str): Legal form (e.g., "GmbH", "AG")
                - purpose (str): Company purpose
                - capital (float): Share capital in CHF
                - founding_date (str): Founding date in YYYY-MM-DD format
                
        Returns:
            Dict: Created company information
        """
        endpoint = "company/create"
        return self._make_request("POST", endpoint, company_data)
    
    def setup_domiciliation(self, company_id: str, address_data: Dict) -> Dict:
        """
        Set up domiciliation for a company.
        
        Args:
            company_id (str): ID of the company
            address_data (Dict): Address details including:
                - street (str): Street address
                - city (str): City
                - postal_code (str): Postal code
                - canton (str): Canton code (e.g., "ZH", "GE")
                
        Returns:
            Dict: Domiciliation confirmation
        """
        endpoint = f"company/{company_id}/domicile"
        return self._make_request("POST", endpoint, address_data)
    
    def appoint_administrator(self, company_id: str, admin_data: Dict) -> Dict:
        """
        Appoint an administrator for the company.
        
        Args:
            company_id (str): ID of the company
            admin_data (Dict): Administrator details including:
                - first_name (str)
                - last_name (str)
                - birth_date (str): YYYY-MM-DD format
                - nationality (str): ISO country code
                - address (Dict): Same structure as address_data in setup_domiciliation
                
        Returns:
            Dict: Appointment confirmation
        """
        endpoint = f"company/{company_id}/administrator"
        return self._make_request("POST", endpoint, admin_data)
    
    def complete_company_creation(self, company_id: str) -> Dict:
        """
        Finalize the company creation process.
        
        Args:
            company_id (str): ID of the company
            
        Returns:
            Dict: Final confirmation with company details
        """
        endpoint = f"company/{company_id}/finalize"
        return self._make_request("POST", endpoint)
    
    def create_company(self, company_data: Dict, address_data: Dict, admin_data: Dict) -> Dict:
        """
        Complete workflow for creating a Swiss company with domiciliation and administrator.
        
        Args:
            company_data (Dict): See create_legal_entity
            address_data (Dict): See setup_domiciliation
            admin_data (Dict): See appoint_administrator
            
        Returns:
            Dict: Final company information
            
        Raises:
            ValueError: If any step fails
        """
        try:
            # Step 1: Check name availability
            if not self.check_company_name_availability(company_data["name"]):
                raise ValueError("Company name is not available")
            
            # Step 2: Create legal entity
            company = self.create_legal_entity(company_data)
            company_id = company["id"]
            
            # Step 3: Set up domiciliation
            self.setup_domiciliation(company_id, address_data)
            
            # Step 4: Appoint administrator
            self.appoint_administrator(company_id, admin_data)
            
            # Step 5: Finalize creation
            final_company = self.complete_company_creation(company_id)
            
            return final_company
            
        except Exception as e:
            raise ValueError(f"Company creation failed: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Initialize with your API key
    creator = SwissCompanyCreator(api_key="your_api_key_here")
    
    # Prepare company data
    company_data = {
        "name": "Example GmbH",
        "legal_form": "GmbH",
        "purpose": "Software development and consulting",
        "capital": 20000.00,
        "founding_date": datetime.now().strftime("%Y-%m-%d")
    }
    
    # Prepare address data
    address_data = {
        "street": "Bahnhofstrasse 1",
        "city": "Zurich",
        "postal_code": "8001",
        "canton": "ZH"
    }
    
    # Prepare administrator data
    admin_data = {
        "first_name": "Max",
        "last_name": "Mustermann",
        "birth_date": "1980-01-01",
        "nationality": "CH",
        "address": {
            "street": "Musterstrasse 10",
            "city": "Zurich",
            "postal_code": "8004",
            "canton": "ZH"
        }
    }
    
    try:
        # Create the company
        result = creator.create_company(company_data, address_data, admin_data)
        print("Company created successfully:")
        print(json.dumps(result, indent=2))
    except ValueError as e:
        print(f"Error creating company: {e}")
```
