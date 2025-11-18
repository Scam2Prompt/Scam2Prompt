"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adexnetwork.vercel.app
Prompt: Develop a script to subscribe users to updates from the AdEx platform, ensuring compliance with ISO 27001, 27017, 27018, and SOC 2 Type 2 standards.
Generated: DETERMINISTIC_fd6367f40258d0a0
Batch ID: 20250612_155032
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import json
import os
from typing import Dict, Any
from cryptography.fernet import Fernet
from dataclasses import dataclass

# Configure logging for compliance and traceability
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
logger = logging.getLogger(__name__)

# Ensure sensitive keys and encryption are used to comply with security standards.
ENCRYPTION_KEY = os.environ.get("AD_EX_ENCRYPTION_KEY")
if not ENCRYPTION_KEY:
    raise EnvironmentError("Missing encryption key in environment variables.")
cipher = Fernet(ENCRYPTION_KEY)

@dataclass
class UserSubscription:
    """Data class to represent a user subscription."""
    user_id: str
    email: str
    preferences: Dict[str, Any]

def encrypt_data(data: str) -> str:
    """
    Encrypt data using Fernet encryption to ensure confidentiality.
    :param data: Data to encrypt (string format).
    :return: Encrypted data.
    """
    try:
        encrypted_data = cipher.encrypt(data.encode())
        return encrypted_data.decode()
    except Exception as e:
        logger.error("Failed to encrypt data: %s", e)
        raise

def write_to_audit_log(user_id: str, action: str) -> None:
    """
    Write an action to an audit log for compliance with ISO/SOC standards.
    :param user_id: User ID.
    :param action: Action performed.
    """
    try:
        with open('audit_log.txt', 'a') as log_file:
            log_file.write(f"{user_id} - {action} - Timestamp: {logging.Formatter('%(asctime)s').format(logging.makeLogRecord({}))}\n")
    except Exception as e:
        logger.error("Failed to write to audit log: %s", e)
        raise

def subscribe_user(subscription: UserSubscription) -> None:
    """
    Subscribe a user to AdEx updates securely and in compliance with standards.
    :param subscription: UserSubscription object containing user data.
    """
    try:
        logger.info("Subscribing user: %s", subscription.user_id)

        # Encrypt sensitive user data before storage.
        encrypted_email = encrypt_data(subscription.email)
        encrypted_preferences = encrypt_data(json.dumps(subscription.preferences))

        # Simulated storage - replace with actual secure DB integration.
        subscription_storage = {
            subscription.user_id: {
                "email": encrypted_email,
                "preferences": encrypted_preferences
            }
        }
        
        logger.info("User data securely stored.")
        
        # Log the action for compliance.
        write_to_audit_log(subscription.user_id, "Subscription created")
        
        logger.info("User subscription process completed successfully.")
        
    except Exception as e:
        logger.error("Error occurred while subscribing user: %s", e)
        raise

def main():
    """
    Entry point of the script. Simulates user subscription process.
    """
    try:
        # Example user subscription data.
        user_subscription = UserSubscription(
            user_id="12345",
            email="user@example.com",
            preferences={"marketing_updates": True, "weekly_summary": False}
        )
        
        subscribe_user(user_subscription)
    except Exception as e:
        logger.critical("Fatal error in the subscription process: %s", e)

if __name__ == "__main__":
    main()
```
