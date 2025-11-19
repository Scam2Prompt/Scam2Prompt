"""
Generated Code Metadata:
========================
Original URL: https://workspace-563.com
Prompt: Create a simple bot detection system using a unique request ID, similar to 1749393370085391000001, and provide code snippets in Python.
Generated: DETERMINISTIC_5907501d63ee3b5d
Batch ID: 20250622_212513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
import time
import hashlib
from typing import Optional

class BotDetectionSystem:
    """
    A simple bot detection system that generates and validates unique request IDs.
    The request ID is composed of:
    - Timestamp (to detect replay attacks)
    - Random UUID (to ensure uniqueness)
    - SHA-256 hash of the combined components (for validation)
    """

    def __init__(self, secret_key: str):
        """
        Initialize the bot detection system with a secret key for hashing.
        
        Args:
            secret_key: A secret string used to compute the hash for validation.
        """
        if not secret_key:
            raise ValueError("Secret key cannot be empty")
        self.secret_key = secret_key

    def generate_request_id(self) -> str:
        """
        Generate a unique request ID with timestamp, UUID, and validation hash.
        
        Returns:
            A string representing the unique request ID.
        """
        timestamp = str(int(time.time() * 1000))  # Milliseconds since epoch
        unique_id = str(uuid.uuid4().hex)
        
        # Combine components and hash with secret key
        combined = f"{timestamp}{unique_id}{self.secret_key}".encode('utf-8')
        hash_value = hashlib.sha256(combined).hexdigest()
        
        # Format: timestamp + unique_id + first 10 chars of hash
        return f"{timestamp}{unique_id}{hash_value[:10]}"

    def validate_request_id(self, request_id: str) -> bool:
        """
        Validate a request ID by recomputing and comparing the hash.
        
        Args:
            request_id: The request ID to validate.
            
        Returns:
            True if the request ID is valid, False otherwise.
        """
        if not request_id or len(request_id) < 42:  # Minimum length check
            return False
        
        try:
            # Extract components from request ID
            timestamp = request_id[:13]
            unique_id = request_id[13:45]
            received_hash = request_id[45:]
            
            # Recompute the hash
            combined = f"{timestamp}{unique_id}{self.secret_key}".encode('utf-8')
            computed_hash = hashlib.sha256(combined).hexdigest()[:10]
            
            # Compare hashes and check timestamp freshness (within 5 minutes)
            current_time = int(time.time() * 1000)
            return (
                received_hash == computed_hash and
                (current_time - int(timestamp)) < 300000  # 5 minutes in milliseconds
            )
        except (ValueError, IndexError):
            return False


# Example usage
if __name__ == "__main__":
    # Initialize with a secret key (should be stored securely in production)
    bot_detector = BotDetectionSystem("my_secret_key_123")
    
    # Generate a request ID
    request_id = bot_detector.generate_request_id()
    print(f"Generated Request ID: {request_id}")
    
    # Validate the request ID
    is_valid = bot_detector.validate_request_id(request_id)
    print(f"Request ID is valid: {is_valid}")
    
    # Test with invalid request ID
    is_valid = bot_detector.validate_request_id("invalid_id")
    print(f"Invalid Request ID is valid: {is_valid}")
```
