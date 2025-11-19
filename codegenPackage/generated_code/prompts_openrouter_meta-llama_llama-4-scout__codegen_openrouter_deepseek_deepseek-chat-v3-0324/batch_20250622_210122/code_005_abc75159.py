"""
Generated Code Metadata:
========================
Original URL: https://bitcoindog.pages.dev
Prompt: Develop a blockchain-based game, similar to the "Duel Race" feature on Bitcoin Dogs, using a metaverse platform and incorporating betting systems.
Generated: DETERMINISTIC_abc75159310562bb
Batch ID: 20250622_210122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
import hashlib
import json
import time
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
import random
from web3 import Web3
from web3.contract import Contract
from web3.exceptions import ContractLogicError, TransactionNotFound
from eth_account import Account
from eth_account.messages import encode_defunct


class GameStatus(Enum):
    WAITING = "WAITING"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"


class RaceResult(Enum):
    WIN = "WIN"
    LOSE = "LOSE"
    DRAW = "DRAW"


@dataclass
class Player:
    address: str
    bet_amount: float
    character_id: int
    signed_up: bool = False


@dataclass
class Race:
    race_id: str
    players: List[Player]
    status: GameStatus = GameStatus.WAITING
    winner: Optional[str] = None
    start_time: Optional[float] = None
    end_time: Optional[float] = None


class BlockchainGame:
    def __init__(self, web3_provider: str, contract_address: str, contract_abi: str):
        self.web3 = Web3(Web3.HTTPProvider(web3_provider))
        self.contract_address = contract_address
        self.contract_abi = json.loads(contract_abi)
        self.contract: Contract = self.web3.eth.contract(
            address=self.contract_address, abi=self.contract_abi
        )
        self.races: Dict[str, Race] = {}
        self.min_bet = 0.01  # Minimum bet in ETH
        self.max_players = 2  # Currently supports 1v1 duels

    def create_race(self) -> str:
        """Create a new race and return its ID."""
        race_id = hashlib.sha256(str(time.time()).encode()).hexdigest()
        self.races[race_id] = Race(race_id=race_id, players=[])
        return race_id

    def join_race(
        self, race_id: str, player_address: str, bet_amount: float, character_id: int
    ) -> bool:
        """Join an existing race with a bet."""
        if race_id not in self.races:
            raise ValueError("Race does not exist")

        if self.races[race_id].status != GameStatus.WAITING:
            raise ValueError("Race is not accepting new players")

        if bet_amount < self.min_bet:
            raise ValueError(f"Bet amount must be at least {self.min_bet} ETH")

        if len(self.races[race_id].players) >= self.max_players:
            raise ValueError("Race is full")

        player = Player(
            address=player_address, bet_amount=bet_amount, character_id=character_id
        )
        self.races[race_id].players.append(player)
        return True

    def start_race(self, race_id: str) -> bool:
        """Start the race if conditions are met."""
        if race_id not in self.races:
            raise ValueError("Race does not exist")

        race = self.races[race_id]

        if race.status != GameStatus.WAITING:
            raise ValueError("Race cannot be started")

        if len(race.players) != self.max_players:
            raise ValueError("Not enough players to start")

        race.status = GameStatus.IN_PROGRESS
        race.start_time = time.time()
        return True

    def _simulate_race(self, race_id: str) -> Tuple[str, RaceResult]:
        """Simulate race outcome (in a real game, this would be actual gameplay)."""
        race = self.races[race_id]
        if len(race.players) != 2:
            raise ValueError("Invalid number of players for duel")

        # Simple random outcome for simulation
        outcome = random.choice([0, 1, 2])  # 0: player1 wins, 1: player2 wins, 2: draw

        if outcome == 0:
            return race.players[0].address, RaceResult.WIN
        elif outcome == 1:
            return race.players[1].address, RaceResult.WIN
        else:
            return None, RaceResult.DRAW

    def complete_race(self, race_id: str) -> bool:
        """Complete the race and distribute winnings."""
        if race_id not in self.races:
            raise ValueError("Race does not exist")

        race = self.races[race_id]

        if race.status != GameStatus.IN_PROGRESS:
            raise ValueError("Race is not in progress")

        winner_address, result = self._simulate_race(race_id)
        race.winner = winner_address
        race.status = GameStatus.COMPLETED
        race.end_time = time.time()

        # Distribute winnings on-chain
        if result == RaceResult.WIN and winner_address:
            self._distribute_winnings(race_id, winner_address)
        elif result == RaceResult.DRAW:
            self._refund_bets(race_id)

        return True

    def _distribute_winnings(self, race_id: str, winner_address: str) -> None:
        """Distribute winnings to the winner on the blockchain."""
        race = self.races[race_id]
        total_pot = sum(p.bet_amount for p in race.players)

        try:
            tx_hash = self.contract.functions.distributeWinnings(
                race_id, winner_address, Web3.toWei(total_pot, "ether")
            ).transact({"from": winner_address})
            receipt = self.web3.eth.waitForTransactionReceipt(tx_hash)
            if receipt.status != 1:
                raise Exception("Transaction failed")
        except ContractLogicError as e:
            raise Exception(f"Contract error: {str(e)}")
        except Exception as e:
            raise Exception(f"Failed to distribute winnings: {str(e)}")

    def _refund_bets(self, race_id: str) -> None:
        """Refund bets to players in case of a draw."""
        race = self.races[race_id]

        for player in race.players:
            try:
                tx_hash = self.contract.functions.refundBet(
                    race_id, player.address, Web3.toWei(player.bet_amount, "ether")
                ).transact({"from": player.address})
                receipt = self.web3.eth.waitForTransactionReceipt(tx_hash)
                if receipt.status != 1:
                    raise Exception("Transaction failed")
            except ContractLogicError as e:
                raise Exception(f"Contract error: {str(e)}")
            except Exception as e:
                raise Exception(f"Failed to refund bet: {str(e)}")

    def get_race_status(self, race_id: str) -> Dict:
        """Get current status of a race."""
        if race_id not in self.races:
            raise ValueError("Race does not exist")

        race = self.races[race_id]
        return {
            "race_id": race.race_id,
            "status": race.status.value,
            "players": [
                {
                    "address": p.address,
                    "bet_amount": p.bet_amount,
                    "character_id": p.character_id,
                }
                for p in race.players
            ],
            "winner": race.winner,
            "start_time": race.start_time,
            "end_time": race.end_time,
        }

    def sign_message(self, private_key: str, message: str) -> str:
        """Sign a message with a private key."""
        try:
            signed_message = Account.sign_message(
                encode_defunct(text=message), private_key=private_key
            )
            return signed_message.signature.hex()
        except Exception as e:
            raise Exception(f"Failed to sign message: {str(e)}")

    def verify_signature(self, address: str, message: str, signature: str) -> bool:
        """Verify a signed message."""
        try:
            signer = Account.recover_message(
                encode_defunct(text=message), signature=signature
            )
            return signer.lower() == address.lower()
        except Exception as e:
            raise Exception(f"Failed to verify signature: {str(e)}")


# Example Contract ABI (simplified)
EXAMPLE_CONTRACT_ABI = """
[
    {
        "inputs": [
            {"internalType": "string", "name": "raceId", "type": "string"},
            {"internalType": "address", "name": "winner", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"}
        ],
        "name": "distributeWinnings",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "string", "name": "raceId", "type": "string"},
            {"internalType": "address", "name": "player", "type": "address"},
