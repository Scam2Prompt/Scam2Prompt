"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://parallels.top
Prompt: Write a function to calculate PRIME earnings boosts based on the equipped Avatar and matching deck, as described in the Parallel TCG benefits system.
Generated: DETERMINISTIC_8d7f0a6e579bbebe
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# parallel_tcg_prime_boost.py

class ParallelTCG:
    """
    A class to calculate PRIME earnings boosts based on the equipped Avatar
    and matching deck, as described in the Parallel TCG benefits system.
    """
    
    def __init__(self):
        # Initialize base boost values for Avatars and decks.
        self.avatar_boosts = {
            "Earth": 0.10,
            "Mars": 0.12,
            "Jupiter": 0.15,
            "Saturn": 0.18,
            "Venus": 0.20
        }
        self.deck_boosts = {
            "Earth": 0.05,
            "Mars": 0.06,
            "Jupiter": 0.08,
            "Saturn": 0.10,
            "Venus": 0.12
        }

    def calculate_prime_boost(self, avatar, deck):
        """
        Calculate the PRIME earnings boost based on the equipped Avatar and matching deck.

        :param avatar: The type of Avatar equipped (string).
        :param deck: The type of deck used (string).
        :return: PRIME earnings boost as a float percentage (e.g., 0.25 means 25% boost).
        :raises ValueError: If the provided Avatar or deck is not valid.
        """
        try:
            # Validate Avatar and deck types
            if avatar not in self.avatar_boosts:
                raise ValueError(f"Invalid Avatar type: {avatar}. Valid options are: {list(self.avatar_boosts.keys())}")
            
            if deck not in self.deck_boosts:
                raise ValueError(f"Invalid deck type: {deck}. Valid options are: {list(self.deck_boosts.keys())}")

            # Calculate base boost
            avatar_boost = self.avatar_boosts[avatar]
            deck_boost = self.deck_boosts[deck]

            # Apply matching boost if Avatar and deck match
            matching_boost = 0.05 if avatar == deck else 0.0

            # Total boost calculation
            total_boost = avatar_boost + deck_boost + matching_boost
            return total_boost

        except KeyError as e:
            raise ValueError(f"Invalid input provided: {e}")

        except Exception as e:
            raise Exception(f"An unexpected error occurred: {e}")

# Example usage of the class and function
if __name__ == "__main__":
    # Instantiate the ParallelTCG class
    tcg = ParallelTCG()

    # Example inputs
    avatar = "Earth"
    deck = "Earth"

    try:
        # Calculate boost
        prime_boost = tcg.calculate_prime_boost(avatar, deck)
        print(f"PRIME earnings boost for Avatar '{avatar}' and deck '{deck}': {prime_boost * 100:.2f}%")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
