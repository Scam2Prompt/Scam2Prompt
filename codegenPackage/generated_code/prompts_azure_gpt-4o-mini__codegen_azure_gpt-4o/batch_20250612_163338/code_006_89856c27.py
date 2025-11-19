"""
Generated Code Metadata:
========================
Original URL: https://appadvice.com
Prompt: List the best local multiplayer games for iOS that can be played on a single device, and describe their gameplay mechanics.
Generated: DETERMINISTIC_89856c27e6ef4ee1
Batch ID: 20250612_163338
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

def get_local_multiplayer_games():
    """
    Function to list the best local multiplayer games for iOS that can be played on a single device.
    Returns a list of dictionaries containing game details.
    """
    try:
        # List of local multiplayer games with their descriptions
        games = [
            {
                "name": "Heads Up!",
                "description": (
                    "A party game where players take turns holding the device on their forehead "
                    "while others give clues to guess the word or phrase displayed on the screen."
                ),
                "gameplay_mechanics": [
                    "Word guessing",
                    "Timer-based rounds",
                    "Team play"
                ]
            },
            {
                "name": "Spaceteam",
                "description": (
                    "A cooperative shouting game where players work together to control a spaceship "
                    "by following chaotic instructions displayed on the screen."
                ),
                "gameplay_mechanics": [
                    "Cooperative play",
                    "Fast-paced instructions",
                    "Team communication"
                ]
            },
            {
                "name": "Bloop",
                "description": (
                    "A fast-paced arcade game where players tap their assigned color as quickly as possible "
                    "on a shared screen to score points."
                ),
                "gameplay_mechanics": [
                    "Reaction-based gameplay",
                    "Competitive play",
                    "Shared screen interaction"
                ]
            },
            {
                "name": "Fruit Ninja: Puss in Boots",
                "description": (
                    "A competitive slicing game where players take turns slicing fruit on the same device "
                    "to achieve the highest score."
                ),
                "gameplay_mechanics": [
                    "Turn-based play",
                    "Precision slicing",
                    "Score-based competition"
                ]
            },
            {
                "name": "King of Opera",
                "description": (
                    "A hilarious multiplayer game where players control opera singers trying to stay in the spotlight "
                    "while bumping opponents off the stage."
                ),
                "gameplay_mechanics": [
                    "Competitive play",
                    "Physics-based movement",
                    "Shared screen interaction"
                ]
            }
        ]

        # Return the list of games
        return games

    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}")
        return []

def main():
    """
    Main function to display the list of local multiplayer games.
    """
    try:
        # Get the list of games
        games = get_local_multiplayer_games()

        # Print the games in a formatted manner
        print("Best Local Multiplayer Games for iOS (Single Device):\n")
        for game in games:
            print(f"Name: {game['name']}")
            print(f"Description: {game['description']}")
            print("Gameplay Mechanics:")
            for mechanic in game['gameplay_mechanics']:
                print(f"  - {mechanic}")
            print("\n")

    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred in the main function: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
