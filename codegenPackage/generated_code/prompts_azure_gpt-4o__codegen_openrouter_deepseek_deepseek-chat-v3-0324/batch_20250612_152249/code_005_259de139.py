"""
Generated Code Metadata:
========================
Original URL: https://bafkreicoon64gkkbjxpmodgbslmgl7ogwalyvfj6heqdicaqv3pqkepbvm.ipfs.dweb.link
Prompt: Create a script to enforce the 24-hour claim restriction for $BANANA rewards and handle claim failures due to congestion or price volatility.
Generated: DETERMINISTIC_259de13953445d4b
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random
from datetime import datetime, timedelta
from typing import Optional, Tuple

class BananaClaimManager:
    """
    Manages $BANANA token claims with 24-hour cooldown and handles claim failures.
    """
    
    def __init__(self):
        self.last_claim_time: Optional[datetime] = None
        self.claim_attempts = 0
        self.max_retries = 3
        self.retry_delay = 5  # seconds
        
    def can_claim(self) -> Tuple[bool, Optional[str]]:
        """
        Check if user can claim $BANANA based on 24-hour cooldown.
        
        Returns:
            Tuple of (can_claim: bool, reason: Optional[str])
        """
        if self.last_claim_time is None:
            return True, None
            
        time_since_last_claim = datetime.now() - self.last_claim_time
        if time_since_last_claim < timedelta(hours=24):
            remaining_time = timedelta(hours=24) - time_since_last_claim
            return False, f"Please wait {remaining_time} before claiming again."
            
        return True, None
    
    def claim_banana(self) -> Tuple[bool, str]:
        """
        Attempt to claim $BANANA tokens with retry logic for failures.
        
        Returns:
            Tuple of (success: bool, message: str)
        """
        can_claim, reason = self.can_claim()
        if not can_claim:
            return False, reason
            
        while self.claim_attempts < self.max_retries:
            try:
                # Simulate claim attempt (replace with actual blockchain call)
                success = self._attempt_claim()
                
                if success:
                    self.last_claim_time = datetime.now()
                    self.claim_attempts = 0
                    return True, "Successfully claimed $BANANA tokens!"
                else:
                    raise Exception("Claim failed due to network congestion")
                    
            except Exception as e:
                self.claim_attempts += 1
                if self.claim_attempts < self.max_retries:
                    time.sleep(self.retry_delay)
                else:
                    return False, f"Failed to claim after {self.max_retries} attempts: {str(e)}"
                    
        return False, "Unexpected error in claim process"
    
    def _attempt_claim(self) -> bool:
        """
        Internal method to simulate claim attempt.
        In production, replace with actual blockchain transaction.
        """
        # Simulate network conditions (80% success rate)
        if random.random() < 0.8:
            return True
        return False
    
    def get_claim_status(self) -> dict:
        """
        Get current claim status including cooldown information.
        
        Returns:
            Dictionary with claim status details
        """
        status = {
            "last_claim_time": self.last_claim_time.isoformat() if self.last_claim_time else None,
            "claim_attempts": self.claim_attempts,
            "can_claim": False,
            "next_claim_time": None
        }
        
        if self.last_claim_time:
            next_claim_time = self.last_claim_time + timedelta(hours=24)
            status["next_claim_time"] = next_claim_time.isoformat()
            status["can_claim"] = datetime.now() >= next_claim_time
        else:
            status["can_claim"] = True
            
        return status


# Example usage
if __name__ == "__main__":
    claim_manager = BananaClaimManager()
    
    # First claim attempt
    success, message = claim_manager.claim_banana()
    print(f"Claim 1: {success} - {message}")
    
    # Immediate second attempt (should fail)
    success, message = claim_manager.claim_banana()
    print(f"Claim 2: {success} - {message}")
    
    # Check status
    print("Current status:", claim_manager.get_claim_status())
```
