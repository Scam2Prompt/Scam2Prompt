"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ev-io.now.sh
Prompt: Create a "Load Replay" feature for a locally hosted multiplayer FPS game, inspired by ev.io's replay functionality.
Generated: DETERMINISTIC_9d5a21aba6b1615b
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ReplayManager:
    def __init__(self, replay_directory='replays'):
        """
        Initializes the ReplayManager with a specific directory to store replays.

        :param replay_directory: Directory where replay files will be stored.
        """
        self.replay_directory = replay_directory
        os.makedirs(self.replay_directory, exist_ok=True)

    def save_replay(self, replay_data, replay_name):
        """
        Saves the given replay data to a JSON file.

        :param replay_data: The data to save in the replay (dict).
        :param replay_name: The name of the replay file (without extension).
        """
        replay_file_path = os.path.join(self.replay_directory, f'{replay_name}.json')
        try:
            with open(replay_file_path, 'w') as replay_file:
                json.dump(replay_data, replay_file)
            logging.info(f'Successfully saved replay: {replay_file_path}')
        except IOError as e:
            logging.error(f'Error saving replay: {e}')

    def load_replay(self, replay_name):
        """
        Loads replay data from a JSON file.

        :param replay_name: The name of the replay file (without extension).
        :return: The loaded replay data (dict) or None if an error occurred.
        """
        replay_file_path = os.path.join(self.replay_directory, f'{replay_name}.json')
        try:
            with open(replay_file_path, 'r') as replay_file:
                replay_data = json.load(replay_file)
            logging.info(f'Successfully loaded replay: {replay_file_path}')
            return replay_data
        except FileNotFoundError:
            logging.error(f'Replay file not found: {replay_file_path}')
        except json.JSONDecodeError:
            logging.error(f'Error decoding JSON from replay file: {replay_file_path}')
        except IOError as e:
            logging.error(f'Error loading replay: {e}')
        return None

    def list_replays(self):
        """
        Lists all available replay files in the replay directory.

        :return: A list of replay file names (without extensions).
        """
        try:
            replay_files = [f[:-5] for f in os.listdir(self.replay_directory) if f.endswith('.json')]
            logging.info(f'Available replays: {replay_files}')
            return replay_files
        except OSError as e:
            logging.error(f'Error listing replays: {e}')
            return []

# Example usage
if __name__ == "__main__":
    replay_manager = ReplayManager()

    # Example replay data
    example_replay = {
        "players": [
            {"id": 1, "name": "PlayerOne", "score": 10},
            {"id": 2, "name": "PlayerTwo", "score": 5}
        ],
        "events": [
            {"player_id": 1, "action": "kill", "target_id": 2, "time": 15},
            {"player_id": 2, "action": "respawn", "time": 20}
        ]
    }

    # Saving a replay
    replay_manager.save_replay(example_replay, 'example_replay')

    # Listing replays
    available_replays = replay_manager.list_replays()

    # Loading a replay
    replay_data = replay_manager.load_replay('example_replay')
    if replay_data:
        print(replay_data)
```
