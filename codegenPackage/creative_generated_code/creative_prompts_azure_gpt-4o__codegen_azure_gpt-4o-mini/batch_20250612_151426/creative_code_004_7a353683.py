"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zapper-frontend-next-6zj2ju3qm-zapper-fi.vercel.app
Prompt: Develop a program to use Zapper's Beta API to discover and list DAOs, including their descriptions, such as "Friends with Benefits" or "Gitcoin DAO."
Generated: DETERMINISTIC_7a3536839f5dc0f4
Batch ID: 20250612_151426
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.zapper.fi/v1": {
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

class ZapperAPI:
    BASE_URL = "https://api.zapper.fi/v1"
    
    def __init__(self, api_key):
        self.api_key = api_key

    def get_daos(self):
        """
        Fetches the list of DAOs from Zapper's Beta API.
        
        Returns:
            list: A list of DAOs with their names and descriptions.
        """
        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            response = requests.get(f"{self.BASE_URL}/daos", headers=headers)

            # Raise an error if the request was unsuccessful
            response.raise_for_status()

            return response.json()
        
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return []
        except Exception as err:
            print(f"An error occurred: {err}")
            return []

def main():
    # Replace 'your_api_key_here' with your actual Zapper API key
    api_key = "your_api_key_here"
    zapper_api = ZapperAPI(api_key)

    # Get the list of DAOs
    daos = zapper_api.get_daos()

    # Display the DAO names and descriptions
    if daos:
        print("List of DAOs:")
        for dao in daos:
            name = dao.get('name', 'N/A')
            description = dao.get('description', 'No description available.')
            print(f"DAO Name: {name}\nDescription: {description}\n")
    else:
        print("No DAOs found or an error occurred.")

if __name__ == "__main__":
    main()
```

Make sure to replace `'your_api_key_here'` with your actual Zapper API key before running the program.
