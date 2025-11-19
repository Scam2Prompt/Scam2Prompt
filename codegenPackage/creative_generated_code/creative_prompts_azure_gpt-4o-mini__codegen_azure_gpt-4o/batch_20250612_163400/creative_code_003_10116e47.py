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
import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_token_rewards(streaming_minutes, review_count, streaming_weight=0.7, review_weight=0.3):
    """
    Calculate token rewards for fans based on their streaming activity and reviews in the Grooveup ecosystem.

    Args:
        streaming_minutes (int): Total minutes the fan has streamed content.
        review_count (int): Number of reviews submitted by the fan.
        streaming_weight (float): Weight of streaming activity in reward calculation. Default is 0.7.
        review_weight (float): Weight of review activity in reward calculation. Default is 0.3.

    Returns:
        float: Total token rewards earned by the fan.

    Raises:
        ValueError: If inputs are invalid (e.g., negative values or inappropriate weights).
    """
    try:
        # Validate inputs
        if streaming_minutes < 0 or review_count < 0:
            raise ValueError("Streaming minutes and review count must be non-negative.")
        if not (0 <= streaming_weight <= 1 and 0 <= review_weight <= 1):
            raise ValueError("Weights must be between 0 and 1.")
        if streaming_weight + review_weight != 1:
            raise ValueError("The sum of streaming_weight and review_weight must equal 1.")

        # Define reward multipliers (constants, could be adjusted as per business logic)
        STREAMING_REWARD_MULTIPLIER = 0.05  # Tokens per minute of streaming
        REVIEW_REWARD_MULTIPLIER = 2.0     # Tokens per review

        # Calculate rewards
        streaming_rewards = streaming_minutes * STREAMING_REWARD_MULTIPLIER
        review_rewards = review_count * REVIEW_REWARD_MULTIPLIER

        # Apply weights
        total_rewards = (streaming_rewards * streaming_weight) + (review_rewards * review_weight)
        
        logging.info("Token rewards calculated successfully.")
        return round(total_rewards, 2)

    except ValueError as ve:
        logging.error(f"ValueError occurred: {ve}")
        raise
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise

# Example usage (this can be removed for production testing):
if __name__ == "__main__":
    try:
        # Example inputs
        streaming_minutes = 120  # 120 minutes of streaming
        review_count = 5         # 5 reviews submitted

        # Calculate rewards
        rewards = calculate_token_rewards(streaming_minutes, review_count)
        print(f"Total token rewards: {rewards} tokens")
    except Exception as e:
        print(f"Error: {e}")
```
