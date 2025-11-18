"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://casinouniswap.com
Prompt: Write code to implement a voting system for rating online casinos, using the star-rating system described on Santa Claus Casino.
Generated: DETERMINISTIC_dcd09c2c39c73550
Batch ID: 20250612_151539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# voting_system.py

class CasinoVote:
    """
    A class to represent a voting system for rating online casinos using a star-rating system.
    """

    def __init__(self):
        """
        Initializes the CasinoVote object with an empty dictionary to store votes.
        """
        self.votes = {}

    def add_vote(self, casino_name: str, rating: int) -> None:
        """
        Adds a vote for a specified casino.

        Parameters:
        - casino_name (str): The name of the casino being rated.
        - rating (int): The rating given to the casino (1-5 stars).
        
        Raises:
        - ValueError: If the rating is not between 1 and 5.
        - KeyError: If the casino name is an empty string.
        """
        if not casino_name:
            raise KeyError("Casino name cannot be empty.")
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5.")
        
        # Initialize the casino's entry if it does not exist
        if casino_name not in self.votes:
            self.votes[casino_name] = []

        # Add the rating to the respective casino
        self.votes[casino_name].append(rating)

    def get_average_rating(self, casino_name: str) -> float:
        """
        Calculates the average rating for a specified casino.

        Parameters:
        - casino_name (str): The name of the casino.

        Returns:
        - float: The average rating of the casino.

        Raises:
        - KeyError: If the casino does not exist.
        """
        if casino_name not in self.votes:
            raise KeyError(f"No votes recorded for {casino_name}.")
        
        # Calculate the average rating
        total_votes = len(self.votes[casino_name])
        total_score = sum(self.votes[casino_name])
        average_rating = total_score / total_votes
        return average_rating

    def get_all_ratings(self) -> dict:
        """
        Retrieves all casinos and their current ratings.

        Returns:
        - dict: A dictionary containing casino names and their average ratings.
        """
        ratings = {}
        for casino, ratings_list in self.votes.items():
            ratings[casino] = sum(ratings_list) / len(ratings_list) if ratings_list else 0
        return ratings


if __name__ == "__main__":
    # Example usage of the voting system
    voting_system = CasinoVote()
    
    # Adding votes
    try:
        voting_system.add_vote("Santa Claus Casino", 5)
        voting_system.add_vote("Santa Claus Casino", 4)
        voting_system.add_vote("North Pole Casino", 3)

        # Retrieving average ratings
        print("Average rating for Santa Claus Casino:", voting_system.get_average_rating("Santa Claus Casino"))
        print("Average rating for North Pole Casino:", voting_system.get_average_rating("North Pole Casino"))

        # Retrieving all ratings
        print("All ratings:", voting_system.get_all_ratings())

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
