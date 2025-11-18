"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://finance-masa.pages.dev
Prompt: Develop a system for issuing and managing Masa's soulbound tokens, including ZettaKey, Blaze SBT, and opBNB Guide SBT.
Generated: DETERMINISTIC_85a72f4b5b5e36b9
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Soulbound Token Management System
# This system manages the issuance and management of soulbound tokens
# including ZettaKey, Blaze SBT, and opBNB Guide SBT.

from enum import Enum
from typing import Dict, List
import uuid

# Enum for token types
class TokenType(Enum):
    ZETTAKEY = "ZettaKey"
    BLAZE_SBT = "Blaze SBT"
    OPNB_GUIDE_SBT = "opBNB Guide SBT"

# Class to represent a soulbound token
class SoulboundToken:
    def __init__(self, token_type: TokenType, owner: str):
        self.token_id = str(uuid.uuid4())  # Unique identifier for the token
        self.token_type = token_type
        self.owner = owner
        self.is_revoked = False  # Indicates if the token has been revoked

    def revoke(self):
        """Revokes the token, making it invalid for the owner."""
        self.is_revoked = True

    def __repr__(self):
        return f"SoulboundToken(token_id={self.token_id}, type={self.token_type}, owner={self.owner}, revoked={self.is_revoked})"

# Class to manage soulbound tokens
class TokenManager:
    def __init__(self):
        self.tokens: Dict[str, SoulboundToken] = {}  # Dictionary to store tokens by their ID

    def issue_token(self, token_type: TokenType, owner: str) -> SoulboundToken:
        """Issues a new soulbound token to the specified owner."""
        if owner not in self.tokens:
            new_token = SoulboundToken(token_type, owner)
            self.tokens[new_token.token_id] = new_token
            return new_token
        else:
            raise ValueError(f"Owner {owner} already has a token.")

    def revoke_token(self, token_id: str):
        """Revokes a token by its ID."""
        if token_id in self.tokens:
            self.tokens[token_id].revoke()
        else:
            raise KeyError(f"Token ID {token_id} does not exist.")

    def get_token_info(self, token_id: str) -> SoulboundToken:
        """Returns the information of a token by its ID."""
        if token_id in self.tokens:
            return self.tokens[token_id]
        else:
            raise KeyError(f"Token ID {token_id} does not exist.")

    def list_tokens(self) -> List[SoulboundToken]:
        """Returns a list of all tokens managed by the system."""
        return list(self.tokens.values())

# Example Usage
if __name__ == "__main__":
    manager = TokenManager()
    
    # Issue new tokens for different owners
    try:
        token1 = manager.issue_token(TokenType.ZETTAKEY, "user1@example.com")
        token2 = manager.issue_token(TokenType.BLAZE_SBT, "user2@example.com")
        print("Issued Tokens:")
        print(token1)
        print(token2)
        
        # List all tokens
        print("\nAll Tokens:")
        for token in manager.list_tokens():
            print(token)

        # Revoke a token
        manager.revoke_token(token1.token_id)
        print("\nAfter revocation:")
        print(manager.get_token_info(token1.token_id))

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
