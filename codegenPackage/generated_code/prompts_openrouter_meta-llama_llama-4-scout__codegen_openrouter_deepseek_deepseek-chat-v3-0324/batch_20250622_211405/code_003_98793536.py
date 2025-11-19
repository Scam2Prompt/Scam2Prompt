"""
Generated Code Metadata:
========================
Original URL: https://clearpool.pages.dev
Prompt: What are the key differences between staking CPOOL with Wintermute, Sino Global Capital, and Hex Trust oracles on Clearpool, and how do their APRs and oracle sizes compare?
Generated: DETERMINISTIC_987935367ae247bd
Batch ID: 20250622_211405
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.clearpool.finance/oracles": {
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
from typing import List, Dict, Optional

class ClearpoolOracle:
    """
    Represents a Clearpool oracle with its staking details.
    """
    def __init__(self, name: str, apr: float, oracle_size: float):
        self.name = name
        self.apr = apr
        self.oracle_size = oracle_size

    def __str__(self) -> str:
        return f"{self.name}: APR={self.apr}%, Oracle Size={self.oracle_size}"

class ClearpoolStakingComparison:
    """
    Compares staking CPOOL with different oracles on Clearpool.
    """
    def __init__(self):
        self.oracles: List[ClearpoolOracle] = []

    def add_oracle(self, oracle: ClearpoolOracle) -> None:
        """Add an oracle to the comparison list."""
        self.oracles.append(oracle)

    def get_oracle_by_name(self, name: str) -> Optional[ClearpoolOracle]:
        """Retrieve an oracle by its name."""
        for oracle in self.oracles:
            if oracle.name.lower() == name.lower():
                return oracle
        return None

    def compare_aprs(self) -> Dict[str, float]:
        """Return a dictionary of oracle names and their APRs."""
        return {oracle.name: oracle.apr for oracle in self.oracles}

    def compare_oracle_sizes(self) -> Dict[str, float]:
        """Return a dictionary of oracle names and their sizes."""
        return {oracle.name: oracle.oracle_size for oracle in self.oracles}

    def fetch_live_data(self, api_url: str) -> bool:
        """
        Fetch live data from Clearpool API and update oracles.
        Returns True if successful, False otherwise.
        """
        try:
            response = requests.get(api_url, timeout=10)
            response.raise_for_status()
            data = response.json()

            # Example parsing (adjust based on actual API response)
            for oracle_data in data.get('oracles', []):
                oracle = ClearpoolOracle(
                    name=oracle_data['name'],
                    apr=oracle_data['apr'],
                    oracle_size=oracle_data['oracle_size']
                )
                self.add_oracle(oracle)
            return True
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return False

def main():
    """Example usage of ClearpoolStakingComparison."""
    comparison = ClearpoolStakingComparison()

    # Add oracles with example data (replace with live data fetch in production)
    comparison.add_oracle(ClearpoolOracle("Wintermute", 12.5, 5000000))
    comparison.add_oracle(ClearpoolOracle("Sino Global Capital", 10.8, 3500000))
    comparison.add_oracle(ClearpoolOracle("Hex Trust", 9.2, 2000000))

    # Compare APRs and oracle sizes
    print("APR Comparison:")
    for name, apr in comparison.compare_aprs().items():
        print(f"{name}: {apr}%")

    print("\nOracle Size Comparison:")
    for name, size in comparison.compare_oracle_sizes().items():
        print(f"{name}: {size}")

    # Uncomment to fetch live data in production
    # if comparison.fetch_live_data("https://api.clearpool.finance/oracles"):
    #     print("\nLive Data Fetched Successfully")

if __name__ == "__main__":
    main()
```
