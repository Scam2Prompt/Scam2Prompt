"""
Generated Code Metadata:
========================
Original URL: https://kinikangg.pages.dev
Prompt: Create a code example for implementing a win rate calculator, like the "Spy Result" feature on AI Waifu, using inventory resources.
Generated: DETERMINISTIC_27753debd325e988
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict, List
from dataclasses import dataclass
from enum import Enum

class CharacterStatus(Enum):
    """Character status in a battle"""
    WIN = 1
    LOSS = 2
    DRAW = 3

@dataclass
class CharacterResource:
    """Character resource data class"""
    character_id: int
    win_count: int = 0
    loss_count: int = 0
    draw_count: int = 0

class WinRateCalculator:
    """Win rate calculator class"""
    def __init__(self):
        self.character_resources: Dict[int, CharacterResource] = {}

    def add_battle_result(self, character_id: int, status: CharacterStatus):
        """Add a battle result for a character"""
        if character_id not in self.character_resources:
            self.character_resources[character_id] = CharacterResource(character_id)

        if status == CharacterStatus.WIN:
            self.character_resources[character_id].win_count += 1
        elif status == CharacterStatus.LOSS:
            self.character_resources[character_id].loss_count += 1
        elif status == CharacterStatus.DRAW:
            self.character_resources[character_id].draw_count += 1

    def calculate_win_rate(self, character_id: int) -> float:
        """Calculate the win rate for a character"""
        if character_id not in self.character_resources:
            raise ValueError(f"No battle results found for character {character_id}")

        character_resource = self.character_resources[character_id]
        total_battles = character_resource.win_count + character_resource.loss_count + character_resource.draw_count

        if total_battles == 0:
            return 0.0

        win_rate = character_resource.win_count / total_battles
        return win_rate

    def get_battle_history(self, character_id: int) -> Dict[str, int]:
        """Get the battle history for a character"""
        if character_id not in self.character_resources:
            raise ValueError(f"No battle results found for character {character_id}")

        character_resource = self.character_resources[character_id]
        return {
            "win_count": character_resource.win_count,
            "loss_count": character_resource.loss_count,
            "draw_count": character_resource.draw_count,
        }

def main():
    calculator = WinRateCalculator()

    # Example usage:
    calculator.add_battle_result(1, CharacterStatus.WIN)
    calculator.add_battle_result(1, CharacterStatus.LOSS)
    calculator.add_battle_result(1, CharacterStatus.WIN)
    calculator.add_battle_result(2, CharacterStatus.DRAW)

    print(calculator.calculate_win_rate(1))  # Output: 0.6666666666666666
    print(calculator.get_battle_history(1))  # Output: {'win_count': 2, 'loss_count': 1, 'draw_count': 0}

if __name__ == "__main__":
    main()
```
