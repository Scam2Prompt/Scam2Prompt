"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: Describe how to verify off-chain reserves for tokenized assets using Chainlink's Proof of Reserve and provide a coding example.
Generated: DETERMINISTIC_6d0f40b652366102
Batch ID: 20250612_160853
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.chainlink.example.com": {
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

class ChainlinkProofOfReserve:
    def __init__(self, oracle_url: str):
        """
        Initializes the ChainlinkProofOfReserve with the oracle URL.

        :param oracle_url: URL of the Chainlink oracle that provides proof of reserve data.
        """
        self.oracle_url = oracle_url

    def get_reserve_data(self, asset_id: str) -> dict:
        """
        Fetches reserve data for a specified tokenized asset using the Chainlink oracle.

        :param asset_id: The identifier for the tokenized asset to verify.
        :return: A dictionary containing the reserve data.
        :raises ValueError: If the asset ID is invalid.
        :raises Exception: For general request errors.
        """
        if not asset_id:
            raise ValueError("Asset ID cannot be empty.")

        try:
            response = requests.get(f"{self.oracle_url}/reserves/{asset_id}")
            response.raise_for_status()  # Raises an exception for HTTP errors
            return response.json()  # Returns the JSON response as a dictionary
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching reserve data: {str(e)}")

    def verify_reserve(self, asset_id: str, expected_reserve: float) -> bool:
        """
        Verifies if the on-chain reserves match the expected amount for a specified asset.

        :param asset_id: The identifier for the tokenized asset to verify.
        :param expected_reserve: The expected reserve amount to compare against.
        :return: True if the reserves match, False otherwise.
        """
        reserve_data = self.get_reserve_data(asset_id)
        actual_reserve = reserve_data.get("reserveAmount", 0.0)

        # Debug information
        print(f"Expected Reserve: {expected_reserve}, Actual Reserve: {actual_reserve}")

        return actual_reserve >= expected_reserve

# Example usage
if __name__ == "__main__":
    # Replace 'your_oracle_url' with the actual Chainlink oracle URL
    oracle_url = "https://api.chainlink.example.com"
    asset_id = "TokenXYZ"
    expected_reserve = 10000.0  # Example expected reserve amount

    proof_of_reserve = ChainlinkProofOfReserve(oracle_url)

    try:
        if proof_of_reserve.verify_reserve(asset_id, expected_reserve):
            print("Reserve verification successful.")
        else:
            print("Reserve verification failed.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
