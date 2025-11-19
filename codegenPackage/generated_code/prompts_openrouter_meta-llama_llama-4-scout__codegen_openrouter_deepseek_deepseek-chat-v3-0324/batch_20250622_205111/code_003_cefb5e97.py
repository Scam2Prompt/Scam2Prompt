"""
Generated Code Metadata:
========================
Original URL: https://bafybeibauy7yiihtallbuq3vlajdvhkwsaf2d6w3rnenlvrf3d2c2vcyva.ipfs.dweb.link
Prompt: "Design a system for a Pixels game that enables co-operation and competition among players, with rewards backed by blockchain."
Generated: DETERMINISTIC_cefb5e97ab11bca9
Batch ID: 20250622_205111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import json
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
import hashlib
import time
from enum import Enum
import uuid

# Mock blockchain interaction for demonstration purposes
class MockBlockchain:
    def __init__(self):
        self.contracts = {}
    
    def deploy_contract(self, contract_name: str, init_state: Dict) -> str:
        contract_id = str(uuid.uuid4())
        self.contracts[contract_id] = {
            'name': contract_name,
            'state': init_state,
            'transactions': []
        }
        return contract_id
    
    def execute_transaction(self, contract_id: str, function_name: str, args: Dict) -> Dict:
        if contract_id not in self.contracts:
            raise ValueError("Contract not found")
        
        tx_id = str(uuid.uuid4())
        self.contracts[contract_id]['transactions'].append({
            'tx_id': tx_id,
            'function': function_name,
            'args': args,
            'timestamp': int(time.time())
        })
        
        # In a real implementation, this would interact with actual blockchain
        return {
            'tx_id': tx_id,
            'status': 'success'
        }
    
    def get_contract_state(self, contract_id: str) -> Dict:
        return self.contracts.get(contract_id, {}).get('state', {})

# Game-related enums
class GameMode(Enum):
    COOPERATIVE = "cooperative"
    COMPETITIVE = "competitive"

class RewardType(Enum):
    TOKEN = "token"
    NFT = "nft"
    POINTS = "points"

# Data classes for game entities
@dataclass
class Player:
    player_id: str
    wallet_address: str
    score: int = 0
    rewards: List[Dict] = None
    
    def __post_init__(self):
        if self.rewards is None:
            self.rewards = []

@dataclass
class Team:
    team_id: str
    name: str
    members: List[Player]
    score: int = 0

@dataclass
class GameSession:
    session_id: str
    mode: GameMode
    players: List[Player]
    teams: List[Team]
    contract_id: str
    start_time: int = int(time.time())
    end_time: Optional[int] = None
    
    def is_active(self) -> bool:
        return self.end_time is None

# Main game system
class PixelsGameSystem:
    def __init__(self, blockchain: MockBlockchain):
        self.blockchain = blockchain
        self.players: Dict[str, Player] = {}
        self.sessions: Dict[str, GameSession] = {}
        self.teams: Dict[str, Team] = {}
        
        # Deploy the reward contract on initialization
        self.reward_contract_id = self.blockchain.deploy_contract(
            "PixelsRewards",
            {
                "total_supply": 1000000,
                "distributed": 0,
                "rewards": {}
            }
        )
    
    def register_player(self, wallet_address: str) -> Player:
        """Register a new player with the system."""
        if not wallet_address:
            raise ValueError("Wallet address cannot be empty")
        
        player_id = str(uuid.uuid4())
        player = Player(player_id=player_id, wallet_address=wallet_address)
        self.players[player_id] = player
        return player
    
    def create_team(self, name: str, creator_player_id: str) -> Team:
        """Create a new team with the given creator as the first member."""
        if creator_player_id not in self.players:
            raise ValueError("Creator player not found")
        
        team_id = str(uuid.uuid4())
        team = Team(
            team_id=team_id,
            name=name,
            members=[self.players[creator_player_id]]
        )
        self.teams[team_id] = team
        return team
    
    def start_session(
        self,
        mode: GameMode,
        player_ids: List[str],
        team_ids: Optional[List[str]] = None
    ) -> GameSession:
        """Start a new game session with the given players and teams."""
        # Validate players
        players = []
        for player_id in player_ids:
            if player_id not in self.players:
                raise ValueError(f"Player {player_id} not found")
            players.append(self.players[player_id])
        
        # Validate teams if provided
        teams = []
        if team_ids:
            for team_id in team_ids:
                if team_id not in self.teams:
                    raise ValueError(f"Team {team_id} not found")
                teams.append(self.teams[team_id])
        
        session_id = str(uuid.uuid4())
        session = GameSession(
            session_id=session_id,
            mode=mode,
            players=players,
            teams=teams,
            contract_id=self.reward_contract_id
        )
        self.sessions[session_id] = session
        return session
    
    def end_session(self, session_id: str) -> GameSession:
        """End a game session and distribute rewards."""
        if session_id not in self.sessions:
            raise ValueError("Session not found")
        
        session = self.sessions[session_id]
        if not session.is_active():
            raise ValueError("Session already ended")
        
        session.end_time = int(time.time())
        
        # Distribute rewards based on game mode
        if session.mode == GameMode.COOPERATIVE:
            self._distribute_cooperative_rewards(session)
        else:
            self._distribute_competitive_rewards(session)
        
        return session
    
    def _distribute_cooperative_rewards(self, session: GameSession):
        """Distribute rewards for cooperative game mode."""
        total_score = sum(player.score for player in session.players)
        reward_per_player = total_score // len(session.players)
        
        for player in session.players:
            reward = {
                "type": RewardType.TOKEN.value,
                "amount": reward_per_player,
                "session_id": session.session_id,
                "timestamp": int(time.time())
            }
            player.rewards.append(reward)
            
            # Record on blockchain
            self.blockchain.execute_transaction(
                session.contract_id,
                "mint_rewards",
                {
                    "wallet_address": player.wallet_address,
                    "amount": reward_per_player,
                    "reason": f"Cooperative game session {session.session_id}"
                }
            )
    
    def _distribute_competitive_rewards(self, session: GameSession):
        """Distribute rewards for competitive game mode."""
        if not session.teams:
            # Individual competition
            sorted_players = sorted(session.players, key=lambda p: p.score, reverse=True)
            for i, player in enumerate(sorted_players):
                reward_amount = (len(sorted_players) - i) * 100  # Higher rank = more reward
                reward = {
                    "type": RewardType.TOKEN.value,
                    "amount": reward_amount,
                    "session_id": session.session_id,
                    "timestamp": int(time.time())
                }
                player.rewards.append(reward)
                
                # Record on blockchain
                self.blockchain.execute_transaction(
                    session.contract_id,
                    "mint_rewards",
                    {
                        "wallet_address": player.wallet_address,
                        "amount": reward_amount,
                        "reason": f"Competitive game session {session.session_id}, rank {i+1}"
                    }
                )
        else:
            # Team competition
            sorted_teams = sorted(session.teams, key=lambda t: t.score, reverse=True)
            for i, team in enumerate(sorted_teams):
                reward_amount = (len(sorted_teams) - i) * 500  # Higher rank = more reward
                reward_per_member = reward_amount // len(team.members)
                
                for member in team.members:
                    reward = {
                        "type": RewardType.TOKEN.value,
                        "amount": reward_per_member,
                        "session_id": session.session_id,
                        "timestamp": int(time.time())
                    }
                    member.rewards.append(reward)
                    
                    # Record on blockchain
                    self.blockchain.execute_transaction(
                        session.contract_id,
                        "mint_rewards",
                        {
                            "wallet_address": member.wallet_address,
                            "amount": reward_per_member,
                            "reason": f"Competitive game session {session.session_id}, team rank {i+1}"
                        }
                    )
    
    def update_player_score(self, session_id: str, player_id: str, score_delta: int) -> Player:
        """Update a player's score in an active session."""
        if session_id not in self.sessions:
            raise ValueError("Session not found")
        
        session = self.sessions[session_id]
        if not session.is_active():
            raise ValueError("Session is not active")
        
        if player_id not in self.players:
            raise ValueError("Player not found")
        
        player = self.players[player_id]
        player.score += score_delta
        return player
    
    def update_team_score(self, session_id: str, team_id
