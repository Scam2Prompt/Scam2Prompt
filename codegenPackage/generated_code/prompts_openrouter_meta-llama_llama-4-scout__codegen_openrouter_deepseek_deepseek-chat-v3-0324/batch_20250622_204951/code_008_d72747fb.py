"""
Generated Code Metadata:
========================
Original URL: https://truckloancenter.com
Prompt: Design a system to manage poker tournament brackets and standings, including features for player registration and prize distribution.
Generated: DETERMINISTIC_d72747fbcb6ee953
Batch ID: 20250622_204951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional, Tuple
from enum import Enum
from dataclasses import dataclass
import random
import math

class TournamentStatus(Enum):
    REGISTRATION = 1
    IN_PROGRESS = 2
    COMPLETED = 3

@dataclass
class Player:
    id: str
    name: str
    chips: int = 0
    eliminated: bool = False

@dataclass
class PrizeDistribution:
    position: int
    percentage: float
    amount: float = 0.0

class Tournament:
    def __init__(self, name: str, buy_in: float, initial_chips: int):
        self.name = name
        self.buy_in = buy_in
        self.initial_chips = initial_chips
        self.players: Dict[str, Player] = {}
        self.status = TournamentStatus.REGISTRATION
        self.prize_pool = 0.0
        self.prize_distribution: List[PrizeDistribution] = []
        self.current_round = 0
        self.bracket: List[List[Tuple[Optional[str], Optional[str]]]] = []
        
    def register_player(self, player_id: str, player_name: str) -> bool:
        if self.status != TournamentStatus.REGISTRATION:
            return False
        
        if player_id in self.players:
            return False
            
        self.players[player_id] = Player(id=player_id, name=player_name, chips=self.initial_chips)
        return True
    
    def start_tournament(self) -> bool:
        if self.status != TournamentStatus.REGISTRATION or len(self.players) < 2:
            return False
        
        self.status = TournamentStatus.IN_PROGRESS
        self.prize_pool = len(self.players) * self.buy_in
        self._generate_bracket()
        return True
    
    def _generate_bracket(self) -> None:
        player_ids = list(self.players.keys())
        random.shuffle(player_ids)
        
        num_players = len(player_ids)
        num_rounds = math.ceil(math.log2(num_players))
        
        self.bracket = []
        current_round = []
        
        # Pair players for first round
        for i in range(0, num_players, 2):
            if i + 1 < num_players:
                current_round.append((player_ids[i], player_ids[i+1]))
            else:
                current_round.append((player_ids[i], None))  # Bye
        
        self.bracket.append(current_round)
        
        # Generate empty rounds for the rest of the tournament
        for _ in range(1, num_rounds):
            next_round_size = math.ceil(len(current_round) / 2)
            self.bracket.append([(None, None) for _ in range(next_round_size)])
    
    def record_match_result(self, round_num: int, match_num: int, winner_id: str) -> bool:
        if (self.status != TournamentStatus.IN_PROGRESS or 
            round_num >= len(self.bracket) or 
            match_num >= len(self.bracket[round_num])):
            return False
        
        player1, player2 = self.bracket[round_num][match_num]
        
        if winner_id not in (player1, player2):
            return False
        
        # Mark loser as eliminated
        loser_id = player1 if winner_id == player2 else player2
        if loser_id:
            self.players[loser_id].eliminated = True
        
        # Advance winner to next round if not final round
        if round_num < len(self.bracket) - 1:
            next_match = match_num // 2
            next_round = round_num + 1
            if self.bracket[next_round][next_match][0] is None:
                self.bracket[next_round][next_match] = (winner_id, self.bracket[next_round][next_match][1])
            else:
                self.bracket[next_round][next_match] = (self.bracket[next_round][next_match][0], winner_id)
        
        # Check if tournament is complete
        if round_num == len(self.bracket) - 1:
            self._complete_tournament(winner_id)
        
        return True
    
    def _complete_tournament(self, winner_id: str) -> None:
        self.status = TournamentStatus.COMPLETED
        self._calculate_prize_distribution()
        
    def _calculate_prize_distribution(self) -> None:
        if not self.prize_distribution:
            return
            
        # Sort players by elimination order (last eliminated is first)
        players_ranking = sorted(
            [p for p in self.players.values() if p.eliminated or p.id == self._get_final_winner()],
            key=lambda p: 0 if p.id == self._get_final_winner() else 1
        )
        
        for prize in self.prize_distribution:
            if prize.position - 1 < len(players_ranking):
                player_id = players_ranking[prize.position - 1].id
                prize.amount = self.prize_pool * prize.percentage / 100
    
    def _get_final_winner(self) -> Optional[str]:
        if self.status != TournamentStatus.COMPLETED or not self.bracket:
            return None
        final_round = self.bracket[-1]
        if not final_round:
            return None
        winner1, winner2 = final_round[0]
        return winner1 or winner2
    
    def set_prize_distribution(self, distribution: List[Dict[str, float]]) -> bool:
        if self.status != TournamentStatus.REGISTRATION:
            return False
        
        total_percentage = sum(item['percentage'] for item in distribution)
        if total_percentage > 100:
            return False
            
        self.prize_distribution = [
            PrizeDistribution(position=int(item['position']), percentage=float(item['percentage']))
            for item in distribution
        ]
        return True
    
    def get_standings(self) -> List[Dict]:
        if self.status == TournamentStatus.REGISTRATION:
            return []
            
        # Active players first, then eliminated by reverse elimination order
        active_players = [p for p in self.players.values() if not p.eliminated]
        eliminated_players = sorted(
            [p for p in self.players.values() if p.eliminated],
            key=lambda p: p.chips, reverse=True
        )
        
        standings = []
        position = 1
        
        # Add active players (still in tournament)
        for player in active_players:
            standings.append({
                'position': position,
                'player_id': player.id,
                'player_name': player.name,
                'chips': player.chips,
                'status': 'active'
            })
            position += 1
        
        # Add eliminated players
        for player in eliminated_players:
            standings.append({
                'position': position,
                'player_id': player.id,
                'player_name': player.name,
                'chips': player.chips,
                'status': 'eliminated'
            })
            position += 1
            
        return standings
    
    def get_bracket(self) -> List[List[Dict]]:
        bracket_view = []
        for round_num, round_matches in enumerate(self.bracket):
            round_view = []
            for match_num, (player1_id, player2_id) in enumerate(round_matches):
                player1 = self.players.get(player1_id) if player1_id else None
                player2 = self.players.get(player2_id) if player2_id else None
                
                round_view.append({
                    'match_num': match_num,
                    'player1': {
                        'id': player1_id,
                        'name': player1.name if player1 else 'Bye',
                        'eliminated': player1.eliminated if player1 else False
                    } if player1_id else None,
                    'player2': {
                        'id': player2_id,
                        'name': player2.name if player2 else 'Bye',
                        'eliminated': player2.eliminated if player2 else False
                    } if player2_id else None
                })
            bracket_view.append({
                'round_num': round_num,
                'matches': round_view
            })
        return bracket_view
    
    def to_json(self) -> str:
        return json.dumps({
            'name': self.name,
            'buy_in': self.buy_in,
            'initial_chips': self.initial_chips,
            'status': self.status.name,
            'prize_pool': self.prize_pool,
            'current_round': self.current_round,
            'players': {pid: {'name': p.name, 'chips': p.chips, 'eliminated': p.eliminated} 
                       for pid, p in self.players.items()},
            'prize_distribution': [{'position': p.position, 'percentage': p.percentage, 'amount': p.amount}
                                  for p in self.prize_distribution],
            'bracket': self.bracket
        })
    
    @classmethod
    def
