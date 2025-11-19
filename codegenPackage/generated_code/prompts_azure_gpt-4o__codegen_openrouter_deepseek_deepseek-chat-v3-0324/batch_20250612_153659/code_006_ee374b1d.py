"""
Generated Code Metadata:
========================
Original URL: https://helio-rave3.web.app
Prompt: Demonstrate how to use Helio's platform to set up a presale with limited spots and free minting, as described in the Rave-3 PreSale example.
Generated: DETERMINISTIC_ee374b1dac53267f
Batch ID: 20250612_153659
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.hel.io/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/rave3-presale-image.png": {
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
from typing import Dict, Any, Optional

class HelioPresale:
    """
    A class to interact with Helio's platform for setting up a presale with limited spots and free minting.
    """
    
    def __init__(self, api_key: str, base_url: str = "https://api.hel.io/v1"):
        """
        Initialize the HelioPresale client.
        
        Args:
            api_key: Your Helio API key for authentication
            base_url: Base URL for Helio API (defaults to production)
        """
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    
    def create_presale(
        self,
        name: str,
        total_spots: int,
        start_time: str,
        end_time: str,
        collection_id: str,
        metadata: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Create a new presale with limited spots and free minting.
        
        Args:
            name: Name of the presale
            total_spots: Total number of spots available
            start_time: ISO 8601 formatted start time
            end_time: ISO 8601 formatted end time
            collection_id: ID of the collection for minting
            metadata: Optional additional metadata
            
        Returns:
            Response from Helio API
        """
        url = f"{self.base_url}/presales"
        payload = {
            "name": name,
            "type": "free_mint",
            "total_spots": total_spots,
            "start_time": start_time,
            "end_time": end_time,
            "collection_id": collection_id,
            "settings": {
                "allowlist_only": False,
                "max_per_wallet": 1
            }
        }
        
        if metadata:
            payload["metadata"] = metadata
            
        try:
            response = requests.post(url, json=payload, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to create presale: {str(e)}")
    
    def get_presale(self, presale_id: str) -> Dict[str, Any]:
        """
        Get details of a specific presale.
        
        Args:
            presale_id: ID of the presale to retrieve
            
        Returns:
            Presale details
        """
        url = f"{self.base_url}/presales/{presale_id}"
        
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to get presale: {str(e)}")
    
    def update_presale(
        self,
        presale_id: str,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Update a presale's properties.
        
        Args:
            presale_id: ID of the presale to update
            **kwargs: Fields to update (name, total_spots, etc.)
            
        Returns:
            Updated presale details
        """
        url = f"{self.base_url}/presales/{presale_id}"
        
        try:
            response = requests.patch(url, json=kwargs, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to update presale: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Initialize client
    helio = HelioPresale(api_key="your_api_key_here")
    
    # Create a presale similar to Rave-3 example
    presale = helio.create_presale(
        name="Rave-3 PreSale",
        total_spots=500,
        start_time="2023-12-01T00:00:00Z",
        end_time="2023-12-07T23:59:59Z",
        collection_id="coll_abc123xyz",
        metadata={
            "description": "Limited 500 spots free mint presale for Rave-3 collection",
            "image_url": "https://example.com/rave3-presale-image.png"
        }
    )
    
    print("Created presale:", presale)
    
    # Get presale details
    presale_details = helio.get_presale(presale["id"])
    print("Presale details:", presale_details)
    
    # Update presale if needed
    updated_presale = helio.update_presale(
        presale["id"],
        total_spots=600  # Increase spots if needed
    )
    print("Updated presale:", updated_presale)
```
