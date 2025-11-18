I should clarify that I don't have specific information about a "Rexas Finance API" in my knowledge base. However, I can provide you with a general example of how you might structure code to tokenize a real estate asset using a hypothetical API. This would typically involve making HTTP requests to an API endpoint.

Here's a Python code snippet that demonstrates the general approach:

```python
import requests
import json
from typing import Dict, Any

class RealEstateTokenizationAPI:
    def __init__(self, api_key: str, base_url: str = "https://api.rexasfinance.com/v1"):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
    
    def tokenize_property(self, property_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Tokenize a real estate asset
        
        Args:
            property_data: Dictionary containing property information
            
        Returns:
            Dictionary with tokenization response
        """
        url = f"{self.base_url}/properties/tokenize"
        
        try:
            response = requests.post(
                url,
                headers=self.headers,
                json=property_data,
                timeout=30
            )
            
            response.raise_for_status()  # Raises an HTTPError for bad responses
            return response.json()
            
        except requests.exceptions.RequestException as e:
            print(f"Error tokenizing property: {e}")
            return {"error": str(e)}
    
    def get_token_status(self, token_id: str) -> Dict[str, Any]:
        """
        Get the status of a tokenized asset
        
        Args:
            token_id: The ID of the tokenized property
            
        Returns:
            Dictionary with token status information
        """
        url = f"{self.base_url}/tokens/{token_id}"
        
        try:
            response = requests.get(
                url,
                headers=self.headers,
                timeout=30
            )
            
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching token status: {e}")
            return {"error": str(e)}

# Example usage
def main():
    # Initialize the API client
    api_client = RealEstateTokenizationAPI(
        api_key="your_api_key_here"
    )
    
    # Property data for tokenization
    property_data = {
        "property_address": {
            "street": "123 Main Street",
            "city": "New York",
            "state": "NY",
            "zip_code": "10001",
            "country": "USA"
        },
        "property_details": {
            "property_type": "commercial",
            "square_footage": 5000,
            "year_built": 2010,
            "number_of_units": 10
        },
        "financial_info": {
            "purchase_price": 2500000,
            "current_value": 3000000,
            "annual_rental_income": 240000,
            "operating_expenses": 80000
        },
        "token_details": {
            "total_tokens": 1000,
            "token_symbol": "REX-123",
            "token_name": "MainSt_Commercial_Property"
        },
        "legal_documents": [
            {
                "document_type": "title_deed",
                "document_url": "https://example.com/documents/title_deed.pdf"
            },
            {
                "document_type": "appraisal",
                "document_url": "https://example.com/documents/appraisal.pdf"
            }
        ]
    }
    
    # Tokenize the property
    print("Tokenizing property...")
    result = api_client.tokenize_property(property_data)
    
    if "error" not in result:
        print("Property tokenization successful!")
        print(f"Token ID: {result.get('token_id')}")
        print(f"Transaction Hash: {result.get('transaction_hash')}")
        print(f"Status: {result.get('status')}")
        
        # Check token status
        token_id = result.get('token_id')
        if token_id:
            print("\nChecking token status...")
            status = api_client.get_token_status(token_id)
            print(f"Token Status: {status}")
    else:
        print(f"Tokenization failed: {result['error']}")

if __name__ == "__main__":
    main()
```

**Important Notes:**

1. **API Key**: You'll need to replace `"your_api_key_here"` with your actual API key from the Rexas Finance platform.

2. **Base URL**: The API endpoint URLs are hypothetical. You'll need to use the actual endpoints provided by Rexas Finance.

3. **Data Structure**: The property data structure shown is an example. The actual required fields will depend on the specific API requirements.

4. **Error Handling**: The code includes basic error handling for network requests.

5. **Security**: In production, never hardcode API keys. Use environment variables or secure configuration management.

To use this with the actual Rexas Finance API, you would need to:

1. Obtain proper API documentation from Rexas Finance
2. Get your API credentials
3. Adjust the endpoint URLs and data structures according to their specifications
4. Install required dependencies: `pip install requests`

If you have specific API documentation from Rexas Finance, I can help you adapt this code to match their exact requirements.