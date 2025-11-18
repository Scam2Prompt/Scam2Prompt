"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zapper-frontend-next-h5ht7yy42-zapper-fi.vercel.app
Prompt: Develop a program that integrates with Zapper's Beta API to search for wallet profiles and display their associated NFTs, DAOs, and DeFi assets.
Generated: DETERMINISTIC_88602f0f85597767
Batch ID: 20250612_145421
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.zapper.xyz/v1": {
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

class ZapperAPIClient:
    """
    A client for interacting with Zapper's Beta API to fetch wallet profiles and their associated
    NFTs, DAOs, and DeFi assets.
    """
    
    BASE_URL = 'https://api.zapper.xyz/v1'
    API_KEY = 'your_api_key_here'  # Replace with your actual Zapper API key
    
    def __init__(self, api_key):
        """
        Initialize the client with the API key.
        :param api_key: Zapper API key for authentication.
        """
        self.api_key = api_key

    def get_wallet_profile(self, wallet_address):
        """
        Fetch wallet profile details including NFTs, DAOs, and DeFi assets.
        :param wallet_address: Ethereum wallet address to query.
        :return: Dictionary with wallet profile data or None if the request fails.
        """
        try:
            endpoint = f'{self.BASE_URL}/wallet/{wallet_address}/profile'
            headers = {'Authorization': f'Bearer {self.api_key}'}
            
            # Perform the API request
            response = requests.get(endpoint, headers=headers)
            
            # Raise an exception for HTTP errors
            response.raise_for_status()
            
            return response.json()  # Return the parsed JSON response
        
        except requests.exceptions.RequestException as e:
            # Log the error message and return None
            print(f"Error fetching wallet profile: {e}")
            return None

    def display_profile_data(self, profile_data):
        """
        Display wallet profile data in a readable format.
        :param profile_data: Dictionary containing wallet profile data.
        """
        if not profile_data:
            print("No profile data available.")
            return
        
        print("\n=== Wallet Profile ===")
        
        # Display NFTs
        print("\nNFTs:")
        for nft in profile_data.get('nfts', []):
            print(f"- {nft.get('name', 'Unknown NFT')} ({nft.get('contractAddress')})")
        
        # Display DAOs
        print("\nDAOs:")
        for dao in profile_data.get('daos', []):
            print(f"- {dao.get('name', 'Unknown DAO')} ({dao.get('address')})")
        
        # Display DeFi assets
        print("\nDeFi Assets:")
        for asset in profile_data.get('defiAssets', []):
            print(f"- {asset.get('name', 'Unknown Asset')} ({asset.get('type')})")
        
        print("\n======================")

def main():
    """
    Main function to interact with Zapper's API and display wallet profile data.
    """
    # Replace with your API key
    api_key = 'your_api_key_here'
    
    # Instantiate the Zapper API client
    zapper_client = ZapperAPIClient(api_key)
    
    # Prompt the user for a wallet address
    wallet_address = input("Enter the Ethereum wallet address: ").strip()
    
    # Fetch wallet profile data
    profile_data = zapper_client.get_wallet_profile(wallet_address)
    
    # Display the profile data
    zapper_client.display_profile_data(profile_data)

if __name__ == "__main__":
    main()
```
