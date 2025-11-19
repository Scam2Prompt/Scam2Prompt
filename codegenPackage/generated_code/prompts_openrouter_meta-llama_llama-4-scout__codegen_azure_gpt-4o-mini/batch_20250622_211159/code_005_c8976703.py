"""
Generated Code Metadata:
========================
Original URL: https://smartauthdecentral.pages.dev
Prompt: Design a system to handle KYC claims and issues using a decentralized protocol, incorporating features like whitelisting and snapshot management.
Generated: DETERMINISTIC_c89767034aacc39e
Batch ID: 20250622_211159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any, Optional

class KYCClaim:
    """Class to represent a KYC claim."""
    
    def __init__(self, user_id: str, claim_data: Dict[str, Any]):
        self.user_id = user_id
        self.claim_data = claim_data
        self.is_whitelisted = False

    def whitelist(self):
        """Whitelists the KYC claim."""
        self.is_whitelisted = True

    def __repr__(self):
        return f"KYCClaim(user_id={self.user_id}, is_whitelisted={self.is_whitelisted})"


class KYCManager:
    """Class to manage KYC claims and issues."""
    
    def __init__(self):
        self.kyc_claims: Dict[str, KYCClaim] = {}
        self.snapshot_history: List[Dict[str, Any]] = []

    def add_claim(self, user_id: str, claim_data: Dict[str, Any]) -> None:
        """Adds a new KYC claim."""
        if user_id in self.kyc_claims:
            raise ValueError(f"Claim for user_id {user_id} already exists.")
        self.kyc_claims[user_id] = KYCClaim(user_id, claim_data)

    def whitelist_claim(self, user_id: str) -> None:
        """Whitelists a KYC claim for a given user_id."""
        if user_id not in self.kyc_claims:
            raise KeyError(f"No claim found for user_id {user_id}.")
        self.kyc_claims[user_id].whitelist()

    def take_snapshot(self) -> None:
        """Takes a snapshot of the current KYC claims."""
        snapshot = {user_id: claim.__dict__ for user_id, claim in self.kyc_claims.items()}
        self.snapshot_history.append(snapshot)

    def get_snapshot(self, index: int) -> Optional[Dict[str, Any]]:
        """Retrieves a snapshot by index."""
        if index < 0 or index >= len(self.snapshot_history):
            raise IndexError("Snapshot index out of range.")
        return self.snapshot_history[index]

    def get_all_claims(self) -> List[KYCClaim]:
        """Returns all KYC claims."""
        return list(self.kyc_claims.values())

    def __repr__(self):
        return f"KYCManager(kyc_claims={self.kyc_claims}, snapshot_history={self.snapshot_history})"


# Example usage
if __name__ == "__main__":
    kyc_manager = KYCManager()

    # Adding claims
    try:
        kyc_manager.add_claim("user123", {"name": "Alice", "age": 30})
        kyc_manager.add_claim("user456", {"name": "Bob", "age": 25})
    except ValueError as e:
        print(f"Error adding claim: {e}")

    # Whitelisting a claim
    try:
        kyc_manager.whitelist_claim("user123")
    except KeyError as e:
        print(f"Error whitelisting claim: {e}")

    # Taking a snapshot
    kyc_manager.take_snapshot()

    # Retrieving a snapshot
    try:
        snapshot = kyc_manager.get_snapshot(0)
        print("Snapshot:", json.dumps(snapshot, indent=2))
    except IndexError as e:
        print(f"Error retrieving snapshot: {e}")

    # Display all claims
    print("All KYC Claims:", kyc_manager.get_all_claims())
```
