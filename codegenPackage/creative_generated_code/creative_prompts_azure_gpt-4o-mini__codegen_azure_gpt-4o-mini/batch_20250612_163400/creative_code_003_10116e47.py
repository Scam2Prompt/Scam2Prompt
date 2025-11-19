"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grooveup.pages.dev
Prompt: Generate a function that calculates the token rewards for fans based on their streaming activity and reviews in the Grooveup ecosystem.
Generated: DETERMINISTIC_10116e4721f2d9ca
Batch ID: 20250612_163400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GrooveupRewardsCalculator:
    """
    A class to calculate token rewards for fans based on streaming activity and reviews.
    """

    def __init__(self, streaming_activity_weight=0.6, review_weight=0.4):
        """
        Initializes the rewards calculator with specified weights for streaming activity and reviews.
        
        :param streaming_activity_weight: Weightage for the streaming activity (default is 0.6)
        :param review_weight: Weightage for the reviews (default is 0.4)
        """
        if not (0 <= streaming_activity_weight <= 1) or not (0 <= review_weight <= 1):
            raise ValueError("Weights must be between 0 and 1")
        if abs(streaming_activity_weight + review_weight - 1) > 1e-6:
            raise ValueError("The sum of weights must be equal to 1")
        
        self.streaming_activity_weight = streaming_activity_weight
        self.review_weight = review_weight

    def calculate_rewards(self, streams, reviews):
        """
        Calculates the total rewards based on streaming activity and review scores.
        
        :param streams: The number of streams (int)
        :param reviews: The average score of reviews (float, should be between 0 and 5)
        :return: Total token rewards (float)
        """
        if not isinstance(streams, int) or streams < 0:
            raise ValueError("Streams must be a non-negative integer")
        if not (isinstance(reviews, (int, float)) and 0 <= reviews <= 5):
            raise ValueError("Reviews must be a float between 0 and 5")
        
        # Calculate rewards from streaming activity
        streaming_rewards = streams * self.streaming_activity_weight
        
        # Calculate rewards from reviews
        review_rewards = reviews * self.review_weight
        
        # Total rewards calculation
        total_rewards = streaming_rewards + review_rewards
        
        return total_rewards

# Example usage
if __name__ == "__main__":
    try:
        calculator = GrooveupRewardsCalculator()
        streams = 150  # Number of streams
        reviews = 4.2  # Average review score
        rewards = calculator.calculate_rewards(streams, reviews)
        print(f"Total Token Rewards: {rewards:.2f}")
    except ValueError as e:
        print(f"Error calculating rewards: {e}")
```
