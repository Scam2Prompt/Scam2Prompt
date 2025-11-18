"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoindogeclaim.pages.dev
Prompt: Generate code to simulate a PvP Duel Race betting system for the Bitcoin Dogs game, incorporating token staking and rewards based on the outcome of the race.
Generated: DETERMINISTIC_fe629ecd6baf0f00
Batch ID: 20250612_151343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class BitcoinDogsPvPDuelRace:
    def __init__(self):
        """
        Initializes the race system with default values.
        """
        self.players = {}  # Stores player information including staked tokens
        self.race_results = {}  # Stores race outcomes

    def register_player(self, player_id, staked_tokens):
        """
        Registers a player for the duel race.
        
        :param player_id: Unique identifier for the player.
        :param staked_tokens: Number of tokens the player is staking on the race.
        """
        if player_id in self.players:
            raise ValueError("Player is already registered.")
        if staked_tokens <= 0:
            raise ValueError("Staked tokens must be greater than zero.")

        self.players[player_id] = {
            'staked_tokens': staked_tokens,
            'reward_tokens': 0
        }

    def simulate_race(self):
        """
        Simulates the PvP race between registered players and determines the winner.
        """
        if len(self.players) != 2:
            raise ValueError("Exactly two players must be registered for the race.")

        player_ids = list(self.players.keys())
        winner = random.choice(player_ids)  # Randomly selects a winner
        loser = player_ids[1] if winner == player_ids[0] else player_ids[0]

        # Reward distribution
        total_staked = self.players[player_ids[0]]['staked_tokens'] + self.players[player_ids[1]]['staked_tokens']
        self.players[winner]['reward_tokens'] = total_staked  # Winner gets total staked tokens
        self.players[loser]['reward_tokens'] = 0  # Loser gets nothing

        # Save race result
        self.race_results = {
            'winner': winner,
            'loser': loser
        }

    def get_race_results(self):
        """
        Returns the results of the last race.
        """
        if not self.race_results:
            raise ValueError("No race has been simulated yet.")
        return self.race_results

    def get_player_details(self, player_id):
        """
        Retrieves the details of a specific player.
        
        :param player_id: Unique identifier for the player.
        :return: Dictionary containing player details.
        """
        if player_id not in self.players:
            raise ValueError("Player not found.")
        return self.players[player_id]


# Example usage
if __name__ == "__main__":
    # Initialize the duel race system
    race_system = BitcoinDogsPvPDuelRace()

    try:
        # Register players with their staked tokens
        race_system.register_player('Player1', 50)
        race_system.register_player('Player2', 30)

        # Simulate the race
        race_system.simulate_race()

        # Get and display race results
        results = race_system.get_race_results()
        print(f"Race Results: Winner: {results['winner']}, Loser: {results['loser']}")

        # Display players' details
        print("Player Details:")
        for player_id in race_system.players:
            print(f"{player_id}: {race_system.get_player_details(player_id)}")
    
    except ValueError as e:
        print(f"Error: {e}")
```
