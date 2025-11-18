"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bipzy-frontend-master-5ot8k5vwq-bipzy1.vercel.app
Prompt: Write a script to interact with Bipzy's launchpad API to retrieve details about upcoming token sales, including project names, funding goals, and supported blockchains like Ethereum, Binance Smart Chain, Polygon, and Arbitrum.
Generated: DETERMINISTIC_1d2234da3c056970
Batch ID: 20250612_153606
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.bipzy.com/v1": {
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

# Constants
BASE_URL = "https://api.bipzy.com/v1"  # Replace with the actual Bipzy API base URL
ENDPOINT_UPCOMING_SALES = "/launchpad/upcoming-sales"  # Replace with the actual endpoint if different
SUPPORTED_BLOCKCHAINS = ["Ethereum", "Binance Smart Chain", "Polygon", "Arbitrum"]

def fetch_upcoming_token_sales():
    """
    Fetch details of upcoming token sales from Bipzy's launchpad API.
    
    Returns:
        list: A list of dictionaries containing token sale details (project name, funding goal, and supported blockchains).
    """
    url = f"{BASE_URL}{ENDPOINT_UPCOMING_SALES}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        data = response.json()

        # Validate response structure
        if not isinstance(data, list):
            raise ValueError("Unexpected response format: Expected a list of sales data.")

        # Filter and format token sale details
        upcoming_sales = []
        for sale in data:
            project_name = sale.get("projectName", "Unknown Project")  # Default to "Unknown Project" if key is missing
            funding_goal = sale.get("fundingGoal", "Unknown Goal")  # Default to "Unknown Goal" if key is missing
            supported_blockchains = sale.get("supportedBlockchains", [])

            # Filter supported blockchains to include only those in SUPPORTED_BLOCKCHAINS
            filtered_blockchains = [bc for bc in supported_blockchains if bc in SUPPORTED_BLOCKCHAINS]

            upcoming_sales.append({
                "projectName": project_name,
                "fundingGoal": funding_goal,
                "supportedBlockchains": filtered_blockchains
            })
        return upcoming_sales

    except requests.exceptions.RequestException as e:
        # Handle networking errors
        print(f"Error fetching data from API: {e}")
        return []
    except ValueError as ve:
        # Handle unexpected data formats
        print(f"Error processing API response: {ve}")
        return []

def main():
    """
    Main function to retrieve and display upcoming token sale details.
    """
    print("Fetching details of upcoming token sales...")
    sales = fetch_upcoming_token_sales()

    if not sales:
        print("No upcoming token sales found or an error occurred.")
        return

    # Display token sale details
    print("\nUpcoming Token Sales:")
    for i, sale in enumerate(sales, 1):
        print(f"\nSale #{i}:")
        print(f"  Project Name: {sale['projectName']}")
        print(f"  Funding Goal: {sale['fundingGoal']}")
        print(f"  Supported Blockchains: {', '.join(sale['supportedBlockchains']) if sale['supportedBlockchains'] else 'None'}")

if __name__ == "__main__":
    main()
```

**Note:** Ensure the `BASE_URL` and `ENDPOINT_UPCOMING_SALES` constants match the actual Bipzy API documentation, as the details provided are placeholders. You may need an API key or other authentication mechanisms depending on the API's requirements.
