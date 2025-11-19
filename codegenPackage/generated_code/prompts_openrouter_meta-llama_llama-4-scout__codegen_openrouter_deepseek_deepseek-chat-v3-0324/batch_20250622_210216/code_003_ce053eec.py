"""
Generated Code Metadata:
========================
Original URL: https://betswirl.xyz
Prompt: "Design a system architecture for a decentralized gaming platform that incorporates DeFi features, similar to BetSwirl's integration with decentralized finance."
Generated: DETERMINISTIC_ce053eec15e52023
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
"""
Decentralized Gaming Platform with DeFi Integration
Core Architecture Components
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
import hashlib
import json
from web3 import Web3, HTTPProvider
from web3.contract import Contract
from web3.exceptions import ContractLogicError, TransactionNotFound
from eth_account import Account
from eth_typing import Address, ChecksumAddress, HexStr


class GameStatus(Enum):
    CREATED = 0
    ACTIVE = 1
    COMPLETED = 2
    CANCELLED = 3


class BetStatus(Enum):
    PENDING = 0
    WON = 1
    LOST = 2
    REFUNDED = 3


@dataclass
class Game:
    game_id: int
    creator: ChecksumAddress
    title: str
    description: str
    min_bet: int
    max_bet: int
    status: GameStatus
    created_at: int
    updated_at: int


@dataclass
class Bet:
    bet_id: int
    game_id: int
    player: ChecksumAddress
    amount: int
    status: BetStatus
    created_at: int
    resolved_at: Optional[int]


class DecentralizedGamingPlatform:
    """
    Core smart contract interface for decentralized gaming platform with DeFi integration.
    """
    
    def __init__(self, web3: Web3, contract_address: ChecksumAddress, abi: str):
        self.web3 = web3
        self.contract = self.web3.eth.contract(address=contract_address, abi=abi)
        self.account = None
        
    def set_account(self, private_key: str) -> None:
        """Set the account for transaction signing."""
        self.account = Account.from_key(private_key)
        
    def _send_transaction(self, function_name: str, *args) -> HexStr:
        """Helper method to send transactions."""
        if not self.account:
            raise ValueError("Account not set")
            
        nonce = self.web3.eth.get_transaction_count(self.account.address)
        tx = getattr(self.contract.functions, function_name)(*args).build_transaction({
            'from': self.account.address,
            'nonce': nonce,
            'gas': 2000000,
            'gasPrice': self.web3.to_wei('50', 'gwei')
        })
        
        signed_tx = self.account.sign_transaction(tx)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return tx_hash.hex()
    
    def create_game(
        self,
        title: str,
        description: str,
        min_bet: int,
        max_bet: int
    ) -> HexStr:
        """Create a new game."""
        return self._send_transaction(
            "createGame",
            title,
            description,
            min_bet,
            max_bet
        )
    
    def place_bet(self, game_id: int, amount: int) -> HexStr:
        """Place a bet on a game."""
        return self._send_transaction("placeBet", game_id, amount)
    
    def resolve_game(self, game_id: int, winner: ChecksumAddress) -> HexStr:
        """Resolve a game and distribute winnings."""
        return self._send_transaction("resolveGame", game_id, winner)
    
    def cancel_game(self, game_id: int) -> HexStr:
        """Cancel a game and refund all bets."""
        return self._send_transaction("cancelGame", game_id)
    
    def claim_winnings(self, bet_id: int) -> HexStr:
        """Claim winnings from a resolved bet."""
        return self._send_transaction("claimWinnings", bet_id)
    
    def get_game(self, game_id: int) -> Game:
        """Get game details."""
        game_data = self.contract.functions.getGame(game_id).call()
        return Game(
            game_id=game_data[0],
            creator=game_data[1],
            title=game_data[2],
            description=game_data[3],
            min_bet=game_data[4],
            max_bet=game_data[5],
            status=GameStatus(game_data[6]),
            created_at=game_data[7],
            updated_at=game_data[8]
        )
    
    def get_bet(self, bet_id: int) -> Bet:
        """Get bet details."""
        bet_data = self.contract.functions.getBet(bet_id).call()
        return Bet(
            bet_id=bet_data[0],
            game_id=bet_data[1],
            player=bet_data[2],
            amount=bet_data[3],
            status=BetStatus(bet_data[4]),
            created_at=bet_data[5],
            resolved_at=bet_data[6] if bet_data[6] != 0 else None
        )
    
    def get_active_games(self) -> List[Game]:
        """Get list of active games."""
        games = []
        game_ids = self.contract.functions.getActiveGames().call()
        for game_id in game_ids:
            games.append(self.get_game(game_id))
        return games


class DeFiIntegration:
    """
    DeFi integration layer for staking, yield farming, and token utilities.
    """
    
    def __init__(self, web3: Web3, gaming_platform: DecentralizedGamingPlatform):
        self.web3 = web3
        self.gaming_platform = gaming_platform
        
    def stake_tokens(self, amount: int) -> HexStr:
        """Stake platform tokens to earn rewards."""
        return self.gaming_platform._send_transaction("stake", amount)
    
    def unstake_tokens(self, amount: int) -> HexStr:
        """Unstake tokens and claim rewards."""
        return self.gaming_platform._send_transaction("unstake", amount)
    
    def claim_rewards(self) -> HexStr:
        """Claim staking rewards."""
        return self.gaming_platform._send_transaction("claimRewards")
    
    def get_staked_balance(self, address: ChecksumAddress) -> int:
        """Get staked token balance for an address."""
        return self.gaming_platform.contract.functions.getStakedBalance(address).call()
    
    def get_rewards(self, address: ChecksumAddress) -> int:
        """Get pending rewards for an address."""
        return self.gaming_platform.contract.functions.getRewards(address).call()


class GamingPlatformAPI:
    """
    REST API interface for the decentralized gaming platform.
    """
    
    def __init__(self, gaming_platform: DecentralizedGamingPlatform, defi: DeFiIntegration):
        self.gaming_platform = gaming_platform
        self.defi = defi
        
    def get_game_endpoint(self, game_id: int) -> Dict:
        """API endpoint to get game details."""
        try:
            game = self.gaming_platform.get_game(game_id)
            return {
                "success": True,
                "game": {
                    "id": game.game_id,
                    "title": game.title,
                    "description": game.description,
                    "status": game.status.name,
                    "min_bet": game.min_bet,
                    "max_bet": game.max_bet,
                    "created_at": game.created_at
                }
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def create_game_endpoint(self, request_data: Dict) -> Dict:
        """API endpoint to create a new game."""
        try:
            tx_hash = self.gaming_platform.create_game(
                request_data["title"],
                request_data["description"],
                request_data["min_bet"],
                request_data["max_bet"]
            )
            return {"success": True, "tx_hash": tx_hash}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def place_bet_endpoint(self, game_id: int, amount: int) -> Dict:
        """API endpoint to place a bet."""
        try:
            tx_hash = self.gaming_platform.place_bet(game_id, amount)
            return {"success": True, "tx_hash": tx_hash}
        except Exception as e:
            return {"success": False, "error": str(e)}


def initialize_platform(rpc_url: str, contract_address: str, abi_path: str) -> Tuple[DecentralizedGamingPlatform, DeFiIntegration, GamingPlatformAPI]:
    """Initialize the gaming platform components."""
    web3 = Web3(HTTPProvider(rpc_url))
    
    with open(abi_path) as f:
        abi = json.load(f)
    
    contract_address = Web3.to_checksum_address(contract_address)
    gaming_platform = DecentralizedGamingPlatform(web3, contract_address, abi)
    defi = DeFiIntegration(web3, gaming_platform)
    api = GamingPlatformAPI(gaming_platform, defi)
    
    return gaming_platform, defi, api
```
