"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://register-stormwarfarecom.pages.dev
Prompt: Describe how to set up a turn-based strategy game that utilizes command points as a resource, following the mechanics outlined in Storm Warfare.
Generated: DETERMINISTIC_3116da2300bb6cc7
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CommandPointManager:
    """
    Manages command points for a player in a turn-based strategy game.
    Command points are used to perform actions during a player's turn.
    """

    def __init__(self, initial_points: int):
        """
        Initializes the command point manager with a specified number of initial command points.

        :param initial_points: The initial command points for the player.
        :raises ValueError: If initial_points is negative.
        """
        if initial_points < 0:
            raise ValueError("Initial command points cannot be negative.")
        
        self.command_points = initial_points

    def spend_points(self, points: int):
        """
        Spend command points to perform an action.

        :param points: The number of points to spend.
        :raises ValueError: If points is negative or exceeds available command points.
        """
        if points < 0:
            raise ValueError("Cannot spend negative command points.")
        if points > self.command_points:
            raise ValueError("Not enough command points available.")
        
        self.command_points -= points

    def replenish_points(self, points: int):
        """
        Replenish command points after a turn.

        :param points: The number of points to replenish.
        :raises ValueError: If points is negative.
        """
        if points < 0:
            raise ValueError("Cannot replenish negative command points.")

        self.command_points += points

    def get_current_points(self) -> int:
        """
        Returns the current number of command points available.

        :return: Current command points.
        """
        return self.command_points


class Action:
    """
    Represents an action in the game that can be performed using command points.
    """

    def __init__(self, name: str, cost: int):
        """
        Initializes an action with a name and command point cost.

        :param name: The name of the action.
        :param cost: The command point cost of the action.
        :raises ValueError: If cost is negative.
        """
        if cost < 0:
            raise ValueError("Action cost cannot be negative.")
        
        self.name = name
        self.cost = cost

    def perform(self, command_point_manager: CommandPointManager):
        """
        Performs the action, deducting the cost from the command point manager.

        :param command_point_manager: The command point manager to deduct points from.
        :raises ValueError: If not enough command points to perform the action.
        """
        command_point_manager.spend_points(self.cost)
        print(f"Performed action: {self.name}, Cost: {self.cost} CP")


class Player:
    """
    Represents a player in the turn-based strategy game.
    """

    def __init__(self, name: str, initial_command_points: int):
        """
        Initializes a player with a name and initial command points.

        :param name: The name of the player.
        :param initial_command_points: The initial command points for the player.
        """
        self.name = name
        self.command_point_manager = CommandPointManager(initial_command_points)

    def perform_action(self, action: Action):
        """
        The player performs an action, if they have enough command points.

        :param action: The action to perform.
        """
        try:
            action.perform(self.command_point_manager)
        except ValueError as e:
            print(f"Error performing action '{action.name}': {e}")

    def end_turn(self, points_to_replenish: int):
        """
        Ends the player's turn and replenishes command points.

        :param points_to_replenish: The number of points to restore.
        """
        self.command_point_manager.replenish_points(points_to_replenish)
        print(f"{self.name} ended their turn. Replenished {points_to_replenish} CP.")


# Example usage
if __name__ == "__main__":
    try:
        # Create a player with initial command points
        player = Player("Warrior", initial_command_points=10)

        # Define some actions
        attack_action = Action(name="Attack", cost=3)
        defend_action = Action(name="Defend", cost=2)

        # Player performs some actions
        player.perform_action(attack_action)  # Should succeed
        player.perform_action(defend_action)   # Should succeed

        # Attempt to perform an action with insufficient command points
        player.perform_action(Action(name="Special Attack", cost=8))  # Should fail

        # End turn and replenish command points
        player.end_turn(points_to_replenish=5)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
