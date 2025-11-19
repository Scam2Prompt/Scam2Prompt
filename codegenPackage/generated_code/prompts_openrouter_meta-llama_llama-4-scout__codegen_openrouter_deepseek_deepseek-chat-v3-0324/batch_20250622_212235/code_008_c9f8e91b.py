"""
Generated Code Metadata:
========================
Original URL: https://xihusz.com
Prompt: Design a blockchain-based game that utilizes OKX's API for real-time cryptocurrency prices and transactions.
Generated: DETERMINISTIC_c9f8e91b6424f311
Batch ID: 20250622_212235
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.okx.com/api/v5/": {
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
import hashlib
import json
import time
import requests
from typing import Dict, List, Optional, Tuple

# Constants
OKX_API_BASE_URL = "https://www.okx.com/api/v5/"
BLOCKCHAIN_GAME_CONTRACT_ADDRESS = "0xYourContractAddressHere"
GAME_TOKEN_SYMBOL = "GAME"
GAS_LIMIT = 200000
GAS_PRICE = 50  # in gwei

class BlockchainGame:
    """
    A blockchain-based game that utilizes OKX's API for real-time cryptocurrency prices and transactions.
    """
    
    def __init__(self, okx_api_key: str, okx_secret_key: str, okx_passphrase: str):
        """
        Initialize the game with OKX API credentials.
        
        Args:
            okx_api_key: OKX API key
            okx_secret_key: OKX API secret key
            okx_passphrase: OKX API passphrase
        """
        self.okx_api_key = okx_api_key
        self.okx_secret_key = okx_secret_key
        self.okx_passphrase = okx_passphrase
        self.players = {}  # player_id: player_data
        self.leaderboard = []  # List of top players
        
    def _make_okx_request(self, endpoint: str, method: str = "GET", params: Optional[Dict] = None) -> Dict:
        """
        Make a request to OKX API with proper authentication.
        
        Args:
            endpoint: API endpoint (e.g., "market/ticker")
            method: HTTP method ("GET" or "POST")
            params: Request parameters
            
        Returns:
            Response JSON data
            
        Raises:
            Exception: If API request fails
        """
        url = f"{OKX_API_BASE_URL}{endpoint}"
        timestamp = str(time.time())
        
        headers = {
            "OK-ACCESS-KEY": self.okx_api_key,
            "OK-ACCESS-SIGN": self._generate_okx_signature(timestamp, method, endpoint, params or {}),
            "OK-ACCESS-TIMESTAMP": timestamp,
            "OK-ACCESS-PASSPHRASE": self.okx_passphrase,
            "Content-Type": "application/json"
        }
        
        try:
            if method == "GET":
                response = requests.get(url, headers=headers, params=params)
            else:
                response = requests.post(url, headers=headers, json=params)
            
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"OKX API request failed: {str(e)}")
    
    def _generate_okx_signature(self, timestamp: str, method: str, endpoint: str, params: Dict) -> str:
        """
        Generate OKX API signature.
        
        Args:
            timestamp: Current timestamp
            method: HTTP method
            endpoint: API endpoint
            params: Request parameters
            
        Returns:
            Base64-encoded signature
        """
        message = timestamp + method.upper() + f"/api/v5/{endpoint}"
        if params:
            message += json.dumps(params, separators=(',', ':'))
        return self._base64_encode_hmac_sha256(self.okx_secret_key, message)
    
    @staticmethod
    def _base64_encode_hmac_sha256(secret: str, message: str) -> str:
        """
        Generate HMAC-SHA256 signature and return as Base64.
        
        Args:
            secret: Secret key
            message: Message to sign
            
        Returns:
            Base64-encoded signature
        """
        hmac_digest = hmac.new(secret.encode(), message.encode(), hashlib.sha256).digest()
        return base64.b64encode(hmac_digest).decode()
    
    def get_crypto_price(self, symbol: str) -> float:
        """
        Get current price of a cryptocurrency from OKX.
        
        Args:
            symbol: Cryptocurrency symbol (e.g., "BTC-USDT")
            
        Returns:
            Current price
            
        Raises:
            Exception: If price cannot be retrieved
        """
        try:
            data = self._make_okx_request(f"market/ticker?instId={symbol}")
            return float(data['data'][0]['last'])
        except Exception as e:
            raise Exception(f"Failed to get price for {symbol}: {str(e)}")
    
    def register_player(self, player_id: str, wallet_address: str) -> bool:
        """
        Register a new player in the game.
        
        Args:
            player_id: Unique player identifier
            wallet_address: Player's blockchain wallet address
            
        Returns:
            True if registration was successful
            
        Raises:
            Exception: If player already exists
        """
        if player_id in self.players:
            raise Exception("Player already exists")
        
        self.players[player_id] = {
            "wallet_address": wallet_address,
            "score": 0,
            "tokens": 0,
            "last_activity": int(time.time())
        }
        return True
    
    def update_player_score(self, player_id: str, score_change: int) -> bool:
        """
        Update a player's score and potentially award tokens.
        
        Args:
            player_id: Player identifier
            score_change: Amount to change the score by (can be positive or negative)
            
        Returns:
            True if update was successful
            
        Raises:
            Exception: If player doesn't exist
        """
        if player_id not in self.players:
            raise Exception("Player does not exist")
        
        player = self.players[player_id]
        player["score"] += score_change
        
        # Award tokens for positive score changes
        if score_change > 0:
            tokens_to_award = score_change // 10  # Example: 1 token per 10 points
            if tokens_to_award > 0:
                player["tokens"] += tokens_to_award
                # In a real implementation, we would mint tokens on the blockchain here
        
        player["last_activity"] = int(time.time())
        self._update_leaderboard()
        return True
    
    def _update_leaderboard(self) -> None:
        """
        Update the leaderboard with top players by score.
        """
        sorted_players = sorted(
            self.players.items(),
            key=lambda x: x[1]["score"],
            reverse=True
        )
        self.leaderboard = [
            {"player_id": pid, "score": data["score"]}
            for pid, data in sorted_players[:10]  # Top 10 players
        ]
    
    def get_leaderboard(self) -> List[Dict]:
        """
        Get the current leaderboard.
        
        Returns:
            List of top players with their scores
        """
        return self.leaderboard
    
    def exchange_tokens(self, player_id: str, token_amount: int, target_symbol: str) -> Tuple[bool, float]:
        """
        Exchange game tokens for another cryptocurrency using OKX prices.
        
        Args:
            player_id: Player identifier
            token_amount: Amount of game tokens to exchange
            target_symbol: Target cryptocurrency symbol (e.g., "BTC-USDT")
            
        Returns:
            Tuple of (success, amount_received)
            
        Raises:
            Exception: If exchange fails
        """
        if player_id not in self.players:
            raise Exception("Player does not exist")
        
        player = self.players[player_id]
        if player["tokens"] < token_amount:
            raise Exception("Insufficient tokens")
        
        try:
            # Get current price of the target cryptocurrency
            target_price = self.get_crypto_price(target_symbol)
            
            # Calculate equivalent amount (simple 1:1 conversion in this example)
            amount_received = token_amount * target_price
            
            # Deduct tokens from player (in a real implementation, this would be a blockchain transaction)
            player["tokens"] -= token_amount
            
            # In a real implementation, we would:
            # 1. Burn the game tokens
            # 2. Transfer the equivalent value in target cryptocurrency to the player's wallet
            
            return True, amount_received
        except Exception as e:
            raise Exception(f"Exchange failed: {str(e)}")
    
    def get_player_balance(self, player_id: str) -> Dict:
        """
        Get a player's balance (score and tokens).
        
        Args:
            player_id: Player identifier
            
        Returns:
            Dictionary with score and tokens
            
        Raises:
            Exception: If player doesn't exist
        """
        if player_id not in self.players:
            raise Exception("Player does not exist")
        
        return {
            "score": self.players[player_id]["score"],
            "tokens": self.players[player_id]["tokens"]
        }

# Example usage
if __name__ == "__main__":
    # Initialize the game with OKX API credentials
    game = BlockchainGame(
        okx_api_key="your_api_key",
        okx_secret_key="your_secret_key",
        okx_passphrase="your_passphrase"
    )
    
    # Register a player
    game.register_player("player1", "0xPlayer1WalletAddress")
    
    # Update player
