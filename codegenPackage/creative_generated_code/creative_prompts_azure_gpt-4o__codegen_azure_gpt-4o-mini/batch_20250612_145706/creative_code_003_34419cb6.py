"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamstercombat.hk
Prompt: Write a function to manage special cards and daily combos for a blockchain-based game, referencing the Hamster Kombat roadmap for May 2024.
Generated: DETERMINISTIC_34419cb6f4cf6954
Batch ID: 20250612_145706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Optional

class SpecialCardManager:
    """
    A class to manage special cards and daily combos in a blockchain-based game.
    """

    def __init__(self):
        """
        Initializes the SpecialCardManager with an empty list of special cards and daily combos.
        """
        self.special_cards: List[Dict[str, Optional[str]]] = []
        self.daily_combos: List[Dict[str, str]] = []

    def add_special_card(self, card_name: str, card_description: str) -> None:
        """
        Adds a new special card to the manager.

        :param card_name: The name of the special card.
        :param card_description: A brief description of the special card.
        :raises ValueError: If card_name or card_description is empty.
        """
        if not card_name or not card_description:
            raise ValueError("Card name and description cannot be empty.")

        card = {
            "name": card_name,
            "description": card_description,
            "added_on": datetime.datetime.now().isoformat()
        }
        self.special_cards.append(card)

    def remove_special_card(self, card_name: str) -> None:
        """
        Removes a special card from the manager by its name.

        :param card_name: The name of the special card to remove.
        :raises ValueError: If card_name is empty or if the card does not exist.
        """
        if not card_name:
            raise ValueError("Card name cannot be empty.")

        for card in self.special_cards:
            if card["name"] == card_name:
                self.special_cards.remove(card)
                return
        
        raise ValueError("Special card not found.")

    def add_daily_combo(self, combo_name: str, combo_description: str) -> None:
        """
        Adds a new daily combo to the manager.

        :param combo_name: The name of the daily combo.
        :param combo_description: A brief description of the daily combo.
        :raises ValueError: If combo_name or combo_description is empty.
        """
        if not combo_name or not combo_description:
            raise ValueError("Combo name and description cannot be empty.")

        combo = {
            "name": combo_name,
            "description": combo_description,
            "date": datetime.datetime.now().date().isoformat()
        }
        self.daily_combos.append(combo)

    def get_special_cards(self) -> List[Dict[str, Optional[str]]]:
        """
        Retrieves the list of special cards.

        :return: A list of special cards.
        """
        return self.special_cards

    def get_daily_combos(self) -> List[Dict[str, str]]:
        """
        Retrieves the list of daily combos.

        :return: A list of daily combos.
        """
        return self.daily_combos

    def clear_cards(self) -> None:
        """
        Clears all special cards and daily combos from the manager.
        """
        self.special_cards.clear()
        self.daily_combos.clear()


# Example usage
if __name__ == "__main__":
    try:
        manager = SpecialCardManager()
        manager.add_special_card("Fireball", "A powerful fire attack.")
        manager.add_daily_combo("Combo1", "A basic attacking combo.")
        
        print("Special Cards:", manager.get_special_cards())
        print("Daily Combos:", manager.get_daily_combos())
        
        manager.remove_special_card("Fireball")
        print("Special Cards after removal:", manager.get_special_cards())

    except ValueError as e:
        print(f"Error: {e}")
```
