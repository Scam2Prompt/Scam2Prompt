"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tgcasino-app.pages.dev
Prompt: Develop a script to analyze the wagering data of TG.Casino players and calculate eligibility for seasonal token airdrops.
Generated: DETERMINISTIC_7b86be7ac78f52ae
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
from datetime import datetime
from typing import List, Dict


class Player:
    """
    Represents a player and their wagering data.
    """
    def __init__(self, player_id: str, total_wagered: float, active_days: int):
        self.player_id = player_id
        self.total_wagered = total_wagered
        self.active_days = active_days
        self.is_eligible = False

    def check_eligibility(self, min_wagered: float, min_active_days: int):
        """
        Checks if the player is eligible for the airdrop based on given thresholds.
        """
        self.is_eligible = (
            self.total_wagered >= min_wagered and self.active_days >= min_active_days
        )


def read_wagering_data(file_path: str) -> List[Dict[str, str]]:
    """
    Reads wagering data from a CSV file.
    :param file_path: Path to the CSV file.
    :return: List of dictionaries containing player data.
    """
    try:
        with open(file_path, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except Exception as e:
        raise RuntimeError(f"Error reading the file: {e}")


def parse_player_data(wagering_data: List[Dict[str, str]]) -> List[Player]:
    """
    Parses raw wagering data into Player objects.
    :param wagering_data: List of dictionaries containing player data.
    :return: List of Player objects.
    """
    players = []
    for record in wagering_data:
        try:
            player_id = record["player_id"]
            total_wagered = float(record["total_wagered"])
            active_days = int(record["active_days"])
            players.append(Player(player_id, total_wagered, active_days))
        except (ValueError, KeyError) as e:
            print(f"Error parsing record {record}: {e}")
    return players


def calculate_eligibility(players: List[Player], min_wagered: float, min_active_days: int):
    """
    Calculate eligibility for token airdrops.
    :param players: List of Player objects.
    :param min_wagered: Minimum wagered amount to qualify.
    :param min_active_days: Minimum active days to qualify.
    """
    for player in players:
        player.check_eligibility(min_wagered, min_active_days)


def export_eligibility_results(players: List[Player], output_file: str):
    """
    Exports the eligibility results to a CSV file.
    :param players: List of Player objects.
    :param output_file: Path to the output CSV file.
    """
    try:
        with open(output_file, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["player_id", "total_wagered", "active_days", "is_eligible"])
            for player in players:
                writer.writerow(
                    [
                        player.player_id,
                        player.total_wagered,
                        player.active_days,
                        player.is_eligible,
                    ]
                )
    except Exception as e:
        raise RuntimeError(f"Error writing to the file: {e}")


def main():
    """
    Main script to analyze wagering data and calculate eligibility for airdrops.
    """
    # Configuration: thresholds for eligibility
    MIN_WAGERED = 1000.0  # Minimum amount wagered (e.g., in casino credits)
    MIN_ACTIVE_DAYS = 10  # Minimum number of active days during the season

    # Input and output file paths
    INPUT_FILE = "wagering_data.csv"
    OUTPUT_FILE = "eligibility_results.csv"

    try:
        print("Reading wagering data...")
        wagering_data = read_wagering_data(INPUT_FILE)

        print("Parsing player data...")
        players = parse_player_data(wagering_data)

        print("Calculating eligibility...")
        calculate_eligibility(players, MIN_WAGERED, MIN_ACTIVE_DAYS)

        print("Exporting results...")
        export_eligibility_results(players, OUTPUT_FILE)

        print(f"Eligibility results successfully exported to {OUTPUT_FILE}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
