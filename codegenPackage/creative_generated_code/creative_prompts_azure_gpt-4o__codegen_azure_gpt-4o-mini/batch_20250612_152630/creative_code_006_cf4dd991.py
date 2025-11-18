"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim.skymoney.world
Prompt: Generate code to check user eligibility for token claims based on a 24-hour time window, as described in the Sky Treasury Claims process.
Generated: DETERMINISTIC_cf4dd9917a9469ab
Batch ID: 20250612_152630
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
from typing import List, Dict, Any

class TokenClaimEligibilityChecker:
    """
    A class to check user eligibility for token claims based on a 24-hour time window.
    """

    def __init__(self):
        """
        Initializes the TokenClaimEligibilityChecker.
        """
        self.claim_records: List[Dict[str, Any]] = []

    def record_claim(self, user_id: str) -> None:
        """
        Records a claim for a user with the current timestamp.

        Args:
            user_id (str): The ID of the user claiming tokens.

        Raises:
            ValueError: If the user_id is empty.
        """
        if not user_id:
            raise ValueError("User ID cannot be empty.")
        
        self.claim_records.append({
            'user_id': user_id,
            'timestamp': datetime.now()
        })

    def is_eligible(self, user_id: str) -> bool:
        """
        Checks if the user is eligible for a new token claim based on a 24-hour window.

        Args:
            user_id (str): The ID of the user to check eligibility for.

        Returns:
            bool: True if eligible, False otherwise.

        Raises:
            ValueError: If the user_id is empty.
        """
        if not user_id:
            raise ValueError("User ID cannot be empty.")
        
        # Get the current time
        current_time = datetime.now()

        # Filter claims made by the user in the last 24 hours
        recent_claims = [
            claim for claim in self.claim_records
            if claim['user_id'] == user_id and
            current_time - claim['timestamp'] < timedelta(days=1)
        ]

        # If there are no recent claims, the user is eligible
        return len(recent_claims) == 0

    def clear_old_claims(self) -> None:
        """
        Clears claims that are older than 24 hours.
        """
        current_time = datetime.now()
        self.claim_records = [
            claim for claim in self.claim_records
            if current_time - claim['timestamp'] < timedelta(days=1)
        ]

# Example usage:
if __name__ == "__main__":
    checker = TokenClaimEligibilityChecker()

    # Record a claim for user 'user123'
    checker.record_claim('user123')

    # Check eligibility for the same user
    eligible = checker.is_eligible('user123')
    print(f"User 'user123' eligibility: {eligible}")

    # Wait for some time (e.g., 1 second) before recording another claim
    import time
    time.sleep(1)

    # Check eligibility again after the claim
    eligible = checker.is_eligible('user123')
    print(f"User 'user123' eligibility after a claim: {eligible}")

    # Clear claims older than 24 hours (not strictly necessary in this example, but good practice)
    checker.clear_old_claims()
```
