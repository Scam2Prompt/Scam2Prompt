"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://award-onchain.pages.dev
Prompt: How can I implement a leaderboard feature using the SDK mentioned on the $onchain website to display user scores based on their onchain activities?
Generated: DETERMINISTIC_5717f282b4f281e6
Batch ID: 20250612_163305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Leaderboard Feature Implementation Using the Onchain SDK

This script retrieves user scores based on their onchain activities and displays a leaderboard.
It leverages the SDK provided on the $onchain website to fetch and process data.

Requirements:
- Python >= 3.7
- Onchain SDK installed (`pip install onchain-sdk`)

Assumptions:
- The SDK provides a method `get_user_scores()` to fetch onchain activity scores.
- The scores returned are in the format [{'user': 'username', 'score': value}, ...].
"""

# Import the required libraries
import onchain_sdk
import sys

def fetch_scores():
    """
    Fetches user scores from the onchain SDK.
    
    Returns:
        list: A list of dictionaries containing user scores.
    Raises:
        RuntimeError: If an error occurs while fetching scores.
    """
    try:
        # Initialize the SDK (assuming a default initialization method)
        client = onchain_sdk.Client()

        # Fetch scores using the SDK-provided method
        scores = client.get_user_scores()
        
        # Ensure scores are valid and properly formatted
        if not isinstance(scores, list):
            raise ValueError("Invalid data format received from SDK.")
        
        return scores
    except Exception as e:
        # Log the error and re-raise it for the caller to handle
        print(f"Error fetching scores: {e}", file=sys.stderr)
        raise RuntimeError("Failed to fetch scores from the SDK.") from e

def generate_leaderboard(scores):
    """
    Generates a sorted leaderboard based on user scores.

    Args:
        scores (list): A list of dictionaries containing user scores.
                      Expected format: [{'user': 'username', 'score': value}, ...].

    Returns:
        list: A sorted list of tuples (username, score) in descending order of scores.
    """
    try:
        # Sort the scores in descending order based on the 'score' key
        leaderboard = sorted(scores, key=lambda x: x['score'], reverse=True)
        
        # Extract relevant data into a simpler format (username, score)
        return [(entry['user'], entry['score']) for entry in leaderboard]
    except (KeyError, TypeError) as e:
        print(f"Error generating leaderboard: {e}", file=sys.stderr)
        raise ValueError("Invalid scores data structure.") from e

def display_leaderboard(leaderboard):
    """
    Displays the leaderboard in a user-friendly format.

    Args:
        leaderboard (list): A list of tuples (username, score).
    """
    print("\nLeaderboard:")
    print("=" * 40)
    print("{:<20} {:>10}".format("User", "Score"))
    print("=" * 40)
    for rank, (user, score) in enumerate(leaderboard, start=1):
        print(f"{rank:<3} {user:<20} {score:>10}")
    print("=" * 40)

def main():
    """
    Main function to run the leaderboard feature.
    """
    try:
        # Fetch user scores from the SDK
        scores = fetch_scores()
        
        # Generate the leaderboard from the scores
        leaderboard = generate_leaderboard(scores)
        
        # Display the leaderboard to the user
        display_leaderboard(leaderboard)
    except Exception as e:
        print(f"Fatal error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    # Execute the main function
    main()
```
