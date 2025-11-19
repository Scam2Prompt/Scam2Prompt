"""
Generated Code Metadata:
========================
Original URL: https://fullmoonbird-next.vercel.app
Prompt: Write a Python script that can reset or mint a token ID for a digital character, inspired by the functionality implied on https://fullmoonbird-next.vercel.app.
Generated: DETERMINISTIC_4e95b95d0f55f8f5
Batch ID: 20250622_204755
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import hashlib
from datetime import datetime
from typing import Optional, Dict, Any

class TokenManager:
    """
    A class to manage token operations including minting and resetting tokens for digital characters.
    """
    
    def __init__(self, token_data_file: str = "tokens.json"):
        """
        Initialize the TokenManager with a data file to store token information.
        
        Args:
            token_data_file (str): Path to the JSON file storing token data. Defaults to "tokens.json".
        """
        self.token_data_file = token_data_file
        self.tokens = self._load_tokens()
    
    def _load_tokens(self) -> Dict[str, Any]:
        """
        Load token data from the JSON file.
        
        Returns:
            Dict[str, Any]: Dictionary containing token data.
            
        Raises:
            FileNotFoundError: If the token data file doesn't exist.
            json.JSONDecodeError: If the file contains invalid JSON.
        """
        try:
            with open(self.token_data_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in {self.token_data_file}", e.doc, e.pos)
    
    def _save_tokens(self) -> None:
        """
        Save the current token data to the JSON file.
        
        Raises:
            IOError: If there's an error writing to the file.
        """
        try:
            with open(self.token_data_file, 'w') as f:
                json.dump(self.tokens, f, indent=2)
        except IOError as e:
            raise IOError(f"Error saving token data: {str(e)}")
    
    def _generate_token_id(self, character_id: str) -> str:
        """
        Generate a unique token ID based on character ID and current timestamp.
        
        Args:
            character_id (str): The ID of the digital character.
            
        Returns:
            str: Generated token ID.
        """
        timestamp = datetime.now().isoformat()
        unique_string = f"{character_id}-{timestamp}"
        return hashlib.sha256(unique_string.encode()).hexdigest()
    
    def mint_token(self, character_id: str, metadata: Optional[Dict[str, Any]] = None) -> str:
        """
        Mint a new token for a digital character.
        
        Args:
            character_id (str): The ID of the digital character.
            metadata (Optional[Dict[str, Any]]): Additional metadata to associate with the token.
            
        Returns:
            str: The newly minted token ID.
            
        Raises:
            ValueError: If character_id is empty or None.
        """
        if not character_id:
            raise ValueError("Character ID cannot be empty")
        
        token_id = self._generate_token_id(character_id)
        
        self.tokens[token_id] = {
            "character_id": character_id,
            "created_at": datetime.now().isoformat(),
            "metadata": metadata or {}
        }
        
        self._save_tokens()
        return token_id
    
    def reset_token(self, token_id: str) -> str:
        """
        Reset an existing token by generating a new token ID for the same character.
        
        Args:
            token_id (str): The existing token ID to reset.
            
        Returns:
            str: The new token ID.
            
        Raises:
            ValueError: If token_id doesn't exist or is invalid.
        """
        if token_id not in self.tokens:
            raise ValueError("Invalid token ID")
        
        character_data = self.tokens[token_id]
        del self.tokens[token_id]
        
        new_token_id = self.mint_token(
            character_data["character_id"],
            character_data.get("metadata", {})
        )
        
        return new_token_id
    
    def get_token_info(self, token_id: str) -> Dict[str, Any]:
        """
        Retrieve information about a specific token.
        
        Args:
            token_id (str): The token ID to look up.
            
        Returns:
            Dict[str, Any]: Token information including character ID and metadata.
            
        Raises:
            ValueError: If token_id doesn't exist.
        """
        if token_id not in self.tokens:
            raise ValueError("Token not found")
        return self.tokens[token_id]

# Example usage
if __name__ == "__main__":
    try:
        manager = TokenManager()
        
        # Mint a new token
        character_id = "fullmoonbird123"
        token_id = manager.mint_token(character_id, {"rarity": "legendary"})
        print(f"Minted token: {token_id}")
        
        # Get token info
        token_info = manager.get_token_info(token_id)
        print(f"Token info: {json.dumps(token_info, indent=2)}")
        
        # Reset token
        new_token_id = manager.reset_token(token_id)
        print(f"Reset token. New token ID: {new_token_id}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
