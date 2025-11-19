"""
Generated Code Metadata:
========================
Original URL: https://landrocker.pages.dev
Prompt: Design a simple game mode, like a material hunt, using the LandRocker game engine and describe its key features.
Generated: DETERMINISTIC_480828fbd23156a6
Batch ID: 20250622_204603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules from the LandRocker game engine
from landrocker.engine import GameMode, Player, Material, World, Event

# Define the MaterialHunt game mode class
class MaterialHunt(GameMode):
    """
    MaterialHunt Game Mode:
    Players compete to collect specific materials scattered across the game world.
    The player with the most materials collected within the time limit wins.
    """

    def __init__(self, world: World, target_material: Material, time_limit: int):
        """
        Initialize the MaterialHunt game mode.

        :param world: The game world where the hunt takes place.
        :param target_material: The material players need to collect.
        :param time_limit: Time limit for the game mode in seconds.
        """
        super().__init__(world)
        self.target_material = target_material
        self.time_limit = time_limit
        self.player_scores = {}  # Dictionary to track player scores
        self.game_active = False

    def start_game(self):
        """
<<<<<<< HEAD
        Start the MaterialHunt game mode.
=======
        Start the Material Hunt game mode.
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
        """
        self.game_active = True
        self.player_scores = {player.id: 0 for player in self.world.players}
        self.world.broadcast_message("Material Hunt has started! Collect as much {} as you can!".format(self.target_material.name))
        self.world.schedule_event(self.end_game, self.time_limit)

    def end_game(self):
        """
<<<<<<< HEAD
        End the MaterialHunt game mode and announce the winner.
        """
        self.game_active = False
        winner = max(self.player_scores, key=self.player_scores.get)
        self.world.broadcast_message("Material Hunt has ended! The winner is Player {} with {} materials collected!".format(winner, self.player_scores[winner]))
=======
        End the Material Hunt game mode and announce the winner.
        """
        self.game_active = False
        winner = max(self.player_scores, key=self.player_scores.get)
        winning_score = self.player_scores[winner]
        self.world.broadcast_message("Material Hunt has ended! Player {} wins with {} {} collected!".format(winner, winning_score, self.target_material.name))
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)

    def on_material_collected(self, event: Event):
        """
        Handle the event when a player collects a material.

        :param event: The event containing details about the material collection.
        """
        if not self.game_active:
<<<<<<< HEAD
            return
=======
            return  # Ignore events if the game is not active
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)

        player = event.player
        material = event.material

        # Check if the collected material matches the target material
        if material == self.target_material:
            self.player_scores[player.id] += 1
            player.send_message("You collected {}! Your current score: {}".format(material.name, self.player_scores[player.id]))

    def register_event_handlers(self):
        """
        Register event handlers for the game mode.
        """
        self.world.register_event_handler("material_collected", self.on_material_collected)

<<<<<<< HEAD
# Example usage
if __name__ == "__main__":
    # Create a game world and players
    game_world = World()
    player1 = Player(id=1, name="Player1")
    player2 = Player(id=2, name="Player2")
    game_world.add_player(player1)
    game_world.add_player(player2)

    # Define the target material and time limit
    gold_material = Material(name="Gold")
    time_limit_seconds = 300  # 5 minutes

    # Initialize and start the MaterialHunt game mode
    material_hunt_mode = MaterialHunt(world=game_world, target_material=gold_material, time_limit=time_limit_seconds)
    material_hunt_mode.register_event_handlers()
    material_hunt_mode.start_game()
=======
# Example usage:
if __name__ == "__main__":
    # Create a game world and players (mocked for demonstration purposes)
    game_world = World()
    target_material = Material(name="Gold Nugget")
    time_limit = 300  # 5 minutes

    # Initialize and start the Material Hunt game mode
    material_hunt = MaterialHunt(game_world, target_material, time_limit)
    material_hunt.register_event_handlers()
    material_hunt.start_game()
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
```
