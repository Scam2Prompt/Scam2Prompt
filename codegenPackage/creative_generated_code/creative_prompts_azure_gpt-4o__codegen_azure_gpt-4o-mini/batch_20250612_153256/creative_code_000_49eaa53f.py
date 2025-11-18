"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallstmemes.com
Prompt: Write Python code to rank crypto casinos based on "degen vibes" and withdrawal speed, as described in Wall Street Memes' "Best Crypto Casinos 2025" article.
Generated: DETERMINISTIC_49eaa53f51fdd2ae
Batch ID: 20250612_153256
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class CryptoCasinoRanker:
    """
    A class to rank crypto casinos based on 'degen vibes' and withdrawal speed.
    """

    def __init__(self):
        """
        Initializes the CryptoCasinoRanker with an empty DataFrame.
        """
        self.casinos = pd.DataFrame(columns=['name', 'degen_vibes', 'withdrawal_speed'])

    def add_casino(self, name: str, degen_vibes: int, withdrawal_speed: int):
        """
        Add a new casino to the ranking list.

        Args:
            name (str): The name of the casino.
            degen_vibes (int): The rating for degen vibes (1 to 10).
            withdrawal_speed (int): The withdrawal speed rating (1 to 10).

        Raises:
            ValueError: If ratings are not between 1 and 10.
        """
        if not (1 <= degen_vibes <= 10) or not (1 <= withdrawal_speed <= 10):
            raise ValueError("Ratings must be between 1 and 10.")

        # Append the new casino data to the DataFrame
        self.casinos = self.casinos.append({
            'name': name,
            'degen_vibes': degen_vibes,
            'withdrawal_speed': withdrawal_speed
        }, ignore_index=True)

    def rank_casinos(self):
        """
        Ranks the casinos based on a weighted score of 'degen vibes' and 'withdrawal speed'.
        The score formula is: score = (degen_vibes * 0.6) + (withdrawal_speed * 0.4)

        Returns:
            pd.DataFrame: A DataFrame of casinos sorted by rank.
        """
        # Calculate the score based on weights
        self.casinos['score'] = (self.casinos['degen_vibes'] * 0.6 +
                                 self.casinos['withdrawal_speed'] * 0.4)
        
        # Sort casinos by score in descending order
        ranked_casinos = self.casinos.sort_values(by='score', ascending=False).reset_index(drop=True)
        return ranked_casinos

def main():
    """
    Main function to demonstrate the usage of CryptoCasinoRanker.
    """
    ranker = CryptoCasinoRanker()
    
    # Adding casinos - in a production environment, this might come from user input or an external source
    try:
        ranker.add_casino("Casino A", 9, 8)
        ranker.add_casino("Casino B", 7, 9)
        ranker.add_casino("Casino C", 10, 5)
    except ValueError as e:
        print(f"Error adding casino: {e}")
    
    # Rank the casinos and display the results
    ranked_casinos = ranker.rank_casinos()
    print("Ranked Crypto Casinos:")
    print(ranked_casinos[['name', 'degen_vibes', 'withdrawal_speed', 'score']])

if __name__ == "__main__":
    main()
```
