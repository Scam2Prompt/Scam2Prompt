"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agora-next-k675d77o0-voteagora.vercel.app
Prompt: Create a Python script that calculates the quorum percentage for Optimism governance proposals using the delegated and total supply values provided on the Agora website.
Generated: DETERMINISTIC_2ff5db977688c3b5
Batch ID: 20250612_145706
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.agora.example.com/supply": {
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
from typing import Optional

def get_quorum_percentage(delegated_supply: float, total_supply: float) -> Optional[float]:
    """
    Calculate the quorum percentage for governance proposals.
    
    Args:
        delegated_supply (float): The amount of tokens delegated for the proposal.
        total_supply (float): The total supply of tokens.

    Returns:
        Optional[float]: The quorum percentage if total_supply is greater than zero, 
                         None otherwise.
    """
    if total_supply <= 0:
        print("Error: Total supply must be greater than zero.")
        return None
    
    quorum_percentage = (delegated_supply / total_supply) * 100
    return quorum_percentage

def fetch_supply_data(url: str) -> Optional[dict]:
    """
    Fetch delegated and total supply data from the given URL.
    
    Args:
        url (str): The URL from which to fetch the supply data.

    Returns:
        Optional[dict]: A dictionary containing 'delegated_supply' and 'total_supply' 
                         if the request is successful, None otherwise.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        
        # Assuming the data contains 'delegated_supply' and 'total_supply'
        return {
            'delegated_supply': data.get('delegated_supply', 0.0),
            'total_supply': data.get('total_supply', 0.0)
        }
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    except ValueError:
        print("Error parsing JSON response.")
        return None

def main():
    """
    Main function to execute the quorum percentage calculation.
    """
    # URL to fetch the supply data (replace with the actual Agora API endpoint)
    url = "https://api.agora.example.com/supply"  
    
    # Fetch the supply data
    supply_data = fetch_supply_data(url)
    
    if supply_data is not None:
        delegated_supply = supply_data['delegated_supply']
        total_supply = supply_data['total_supply']
        
        # Calculate the quorum percentage
        quorum_pct = get_quorum_percentage(delegated_supply, total_supply)
        
        if quorum_pct is not None:
            print(f"Quorum Percentage: {quorum_pct:.2f}%")

if __name__ == "__main__":
    main()
```
