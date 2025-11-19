"""
Generated Code Metadata:
========================
Original URL: https://play-gamer.com
Prompt: Create a Python script to analyze player performance in a racing game with features like drifting and handbrake turns, similar to those in Rally Racer Dirt.
Generated: DETERMINISTIC_9800174851fbacf2
Batch ID: 20250622_211548
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import statistics

class PlayerPerformanceAnalyzer:
    """
    A class to analyze player performance in a racing game.
    """

    def __init__(self, player_data):
        """
        Initialize the analyzer with player data.

        :param player_data: List of dictionaries containing player performance metrics.
        """
        self.player_data = player_data

    def calculate_average_speed(self):
        """
        Calculate the average speed of all players.

        :return: Average speed as a float.
        """
        try:
            speeds = [player['average_speed'] for player in self.player_data]
            return statistics.mean(speeds)
        except KeyError:
            raise ValueError("Missing 'average_speed' key in player data.")
        except statistics.StatisticsError:
            raise ValueError("No data available to calculate average speed.")

    def calculate_drift_score(self):
        """
        Calculate the average drift score of all players.

        :return: Average drift score as a float.
        """
        try:
            drift_scores = [player['drift_score'] for player in self.player_data]
            return statistics.mean(drift_scores)
        except KeyError:
            raise ValueError("Missing 'drift_score' key in player data.")
        except statistics.StatisticsError:
            raise ValueError("No data available to calculate drift score.")

    def calculate_handbrake_turns(self):
        """
        Calculate the total number of handbrake turns performed by all players.

        :return: Total handbrake turns as an integer.
        """
        try:
            handbrake_turns = [player['handbrake_turns'] for player in self.player_data]
            return sum(handbrake_turns)
        except KeyError:
            raise ValueError("Missing 'handbrake_turns' key in player data.")

    def generate_report(self):
        """
        Generate a performance report for all players.

        :return: Dictionary containing performance metrics.
        """
        try:
            report = {
                "average_speed": self.calculate_average_speed(),
                "average_drift_score": self.calculate_drift_score(),
                "total_handbrake_turns": self.calculate_handbrake_turns()
            }
            return report
        except ValueError as e:
            return {"error": str(e)}

def load_player_data(file_path):
    """
    Load player data from a JSON file.

    :param file_path: Path to the JSON file containing player data.
    :return: List of player data dictionaries.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file: {file_path}")

def main():
    """
    Main function to analyze player performance.
    """
    # Path to the JSON file containing player data
    file_path = 'player_data.json'

    try:
        # Load player data
        player_data = load_player_data(file_path)

        # Initialize the analyzer
        analyzer = PlayerPerformanceAnalyzer(player_data)

        # Generate and print the report
        report = analyzer.generate_report()
        print("Player Performance Report:")
        for key, value in report.items():
            print(f"{key}: {value}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
