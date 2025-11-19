"""
Generated Code Metadata:
========================
Original URL: https://lyast.org
Prompt: Generate a function that compares the best online slot games based on the criteria outlined in "Perbandingan Slot Online Terbaik dari Berbagai Provider" from lyast.org.
Generated: DETERMINISTIC_62ca6befd9e8d285
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

"""
Module for comparing online slot games based on various criteria.

Classes:
    SlotGame: Represents an online slot game with its characteristics.
    SlotGameComparator: Compares slot games based on different criteria.

Functions:
    compare_slot_games: Compares a list of slot games based on specified criteria.

"""

import operator

class SlotGame:
    """
    Represents an online slot game with its characteristics.

    Attributes:
        name (str): The name of the slot game.
        provider (str): The provider of the slot game.
        rtp (float): The Return to Player (RTP) percentage of the slot game.
        volatility (str): The volatility level of the slot game (e.g., 'low', 'medium', 'high').
        max_win (int): The maximum win amount of the slot game.
    """

    def __init__(self, name, provider, rtp, volatility, max_win):
        """
        Initializes a SlotGame object.

        Args:
            name (str): The name of the slot game.
            provider (str): The provider of the slot game.
            rtp (float): The Return to Player (RTP) percentage of the slot game.
            volatility (str): The volatility level of the slot game (e.g., 'low', 'medium', 'high').
            max_win (int): The maximum win amount of the slot game.

        Raises:
            ValueError: If the RTP is not between 0 and 100.
        """
        if not 0 <= rtp <= 100:
            raise ValueError("RTP must be between 0 and 100")

        self.name = name
        self.provider = provider
        self.rtp = rtp
        self.volatility = volatility
        self.max_win = max_win

    def __repr__(self):
        return f"SlotGame('{self.name}', '{self.provider}', {self.rtp}, '{self.volatility}', {self.max_win})"


class SlotGameComparator:
    """
    Compares slot games based on different criteria.

    Attributes:
        slot_games (list[SlotGame]): A list of slot games to compare.
    """

    def __init__(self, slot_games):
        """
        Initializes a SlotGameComparator object.

        Args:
            slot_games (list[SlotGame]): A list of slot games to compare.
        """
        self.slot_games = slot_games

    def compare_by_rtp(self):
        """
        Compares slot games by their RTP in descending order.

        Returns:
            list[SlotGame]: A list of slot games sorted by RTP in descending order.
        """
        return sorted(self.slot_games, key=operator.attrgetter('rtp'), reverse=True)

    def compare_by_max_win(self):
        """
        Compares slot games by their maximum win amount in descending order.

        Returns:
            list[SlotGame]: A list of slot games sorted by maximum win amount in descending order.
        """
        return sorted(self.slot_games, key=operator.attrgetter('max_win'), reverse=True)

    def compare_by_volatility(self):
        """
        Compares slot games by their volatility level.

        Returns:
            dict[str, list[SlotGame]]: A dictionary with volatility levels as keys and lists of slot games as values.
        """
        volatility_levels = {}
        for game in self.slot_games:
            if game.volatility not in volatility_levels:
                volatility_levels[game.volatility] = []
            volatility_levels[game.volatility].append(game)
        return volatility_levels


def compare_slot_games(slot_games, criteria):
    """
    Compares a list of slot games based on specified criteria.

    Args:
        slot_games (list[SlotGame]): A list of slot games to compare.
        criteria (str): The criteria to use for comparison (e.g., 'rtp', 'max_win', 'volatility').

    Returns:
        The comparison result based on the specified criteria.

    Raises:
        ValueError: If the criteria is not supported.
    """
    comparator = SlotGameComparator(slot_games)

    if criteria == 'rtp':
        return comparator.compare_by_rtp()
    elif criteria == 'max_win':
        return comparator.compare_by_max_win()
    elif criteria == 'volatility':
        return comparator.compare_by_volatility()
    else:
        raise ValueError("Unsupported criteria")


# Example usage:
if __name__ == "__main__":
    slot_games = [
        SlotGame('Game 1', 'Provider 1', 95.0, 'medium', 10000),
        SlotGame('Game 2', 'Provider 2', 92.0, 'low', 5000),
        SlotGame('Game 3', 'Provider 3', 98.0, 'high', 20000),
    ]

    try:
        rtp_comparison = compare_slot_games(slot_games, 'rtp')
        max_win_comparison = compare_slot_games(slot_games, 'max_win')
        volatility_comparison = compare_slot_games(slot_games, 'volatility')

        print("RTP Comparison:")
        for game in rtp_comparison:
            print(game)

        print("\nMax Win Comparison:")
        for game in max_win_comparison:
            print(game)

        print("\nVolatility Comparison:")
        for volatility, games in volatility_comparison.items():
            print(f"{volatility}:")
            for game in games:
                print(game)

    except Exception as e:
        print(f"An error occurred: {e}")
```
