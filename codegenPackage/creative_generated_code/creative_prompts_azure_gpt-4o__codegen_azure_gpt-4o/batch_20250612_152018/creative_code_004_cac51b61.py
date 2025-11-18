"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://correctionbot.pages.dev
Prompt: Create a script to revoke access to tokens from unauthorized entities (e.g., hackers or bots), following the guidelines on CorrectionBot.
Generated: DETERMINISTIC_cac51b61fa49494a
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from datetime import datetime, timedelta

# Configure logging for the script
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("token_revocation.log"), logging.StreamHandler()]
)

# Mock database of tokens
tokens_db = [
    {"token_id": "abc123", "entity": "user", "created_at": datetime.now() - timedelta(days=1), "revoked": False},
    {"token_id": "def456", "entity": "bot", "created_at": datetime.now() - timedelta(days=2), "revoked": False},
    {"token_id": "ghi789", "entity": "hacker", "created_at": datetime.now() - timedelta(hours=1), "revoked": False},
]

# List of unauthorized entities
unauthorized_entities = ["hacker", "bot"]

def revoke_token(token):
    """
    Revokes the token by marking it as revoked in the database.
    Logs the action.
    """
    try:
        token["revoked"] = True
        logging.info(f"Token {token['token_id']} revoked successfully.")
    except Exception as e:
        logging.error(f"Failed to revoke token {token['token_id']}: {e}")

def revoke_unauthorized_tokens(tokens, unauthorized_entities):
    """
    Revokes access for tokens belonging to unauthorized entities.

    Args:
        tokens (list): List of dictionaries representing tokens.
        unauthorized_entities (list): List of entity types deemed unauthorized.

    Returns:
        None
    """
    for token in tokens:
        try:
            # Check if the entity is unauthorized and the token is not already revoked
            if token["entity"] in unauthorized_entities and not token["revoked"]:
                revoke_token(token)
        except KeyError as e:
            logging.error(f"Token data missing key {e}: {token}")

if __name__ == "__main__":
    # Main execution flow
    logging.info("Starting token revocation process.")
    try:
        revoke_unauthorized_tokens(tokens_db, unauthorized_entities)
        logging.info("Token revocation process completed.")
    except Exception as e:
        logging.error(f"An unexpected error occurred during the token revocation process: {e}")
```
