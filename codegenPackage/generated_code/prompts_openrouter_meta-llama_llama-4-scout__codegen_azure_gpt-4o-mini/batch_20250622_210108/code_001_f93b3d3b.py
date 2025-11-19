"""
Generated Code Metadata:
========================
Original URL: https://ousd-event.org
Prompt: Recommend a TV show to watch on TV8 based on the user's interest in cooking competitions, and provide a brief description of the show.
Generated: DETERMINISTIC_f93b3d3b38221f79
Batch ID: 20250622_210108
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TVShowRecommender:
    """
    A class to recommend TV shows based on user interests.
    """

    def __init__(self):
        """
        Initializes the recommender with a predefined list of shows.
        """
        self.shows = {
            "MasterChef": {
                "description": "Aspiring chefs compete in various cooking challenges to win the title of MasterChef.",
                "genre": "cooking competition"
            },
            "The Great British Bake Off": {
                "description": "Amateur bakers compete in a series of rounds, attempting to impress a group of judges with their baking skills.",
                "genre": "cooking competition"
            },
            "Chopped": {
                "description": "Chefs compete in a timed cooking competition using mystery ingredients to create dishes.",
                "genre": "cooking competition"
            },
            "Hell's Kitchen": {
                "description": "Chefs compete under the watchful eye of Chef Gordon Ramsay in a high-pressure kitchen environment.",
                "genre": "cooking competition"
            }
        }

    def recommend_show(self, interest):
        """
        Recommends a TV show based on the user's interest.

        Args:
            interest (str): The user's interest in a specific genre.

        Returns:
            str: A recommendation message with the show title and description.
        """
        try:
            # Normalize the interest to lowercase for comparison
            interest = interest.lower()
            # Filter shows based on the user's interest
            recommended_shows = [
                show for show, details in self.shows.items() if interest in details['genre']
            ]

            if not recommended_shows:
                return "No shows found for your interest."

            # Select the first recommended show
            show_title = recommended_shows[0]
            show_description = self.shows[show_title]['description']
            return f"Recommended Show: {show_title}\nDescription: {show_description}"

        except Exception as e:
            return f"An error occurred while recommending a show: {str(e)}"


if __name__ == "__main__":
    # Create an instance of the recommender
    recommender = TVShowRecommender()
    
    # User interest input
    user_interest = "cooking competition"
    
    # Get and print the recommendation
    recommendation = recommender.recommend_show(user_interest)
    print(recommendation)
```
