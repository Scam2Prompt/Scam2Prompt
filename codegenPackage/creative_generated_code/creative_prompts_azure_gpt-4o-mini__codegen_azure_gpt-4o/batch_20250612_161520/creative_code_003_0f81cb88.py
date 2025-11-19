"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soldragon.vercel.app
Prompt: Generate a function that allows users to share their achievements on Twitter after earning $SHEN tokens in a gaming context.
Generated: DETERMINISTIC_0f81cb88a55645a8
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import tweepy

def share_achievement_on_twitter(api_key, api_key_secret, access_token, access_token_secret, username, achievement, shen_tokens):
    """
    Share an achievement on Twitter after earning $SHEN tokens in a gaming context.

    Args:
        api_key (str): Twitter API Key.
        api_key_secret (str): Twitter API Key Secret.
        access_token (str): Twitter Access Token.
        access_token_secret (str): Twitter Access Token Secret.
        username (str): The user's Twitter username.
        achievement (str): Description of the achievement earned.
        shen_tokens (int): Number of $SHEN tokens earned.

    Returns:
        str: Confirmation message or error details.
    """
    try:
        # Authenticate with the Twitter API
        auth = tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret)
        api = tweepy.API(auth)

        # Compose the tweet message
        tweet_message = (f"🎉 {username} just achieved '{achievement}' and earned {shen_tokens} $SHEN tokens! 🚀 "
                         f"Join the game and start earning today! #Gaming #Achievements")

        # Post the tweet
        api.update_status(tweet_message)

        return "Achievement shared successfully on Twitter!"

    except tweepy.TweepyException as e:
        # Handle Twitter API errors
        return f"Failed to share achievement on Twitter: {str(e)}"

    except Exception as e:
        # Handle other potential errors
        return f"An unexpected error occurred: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Replace with actual credentials and data
    API_KEY = "your_api_key"
    API_KEY_SECRET = "your_api_key_secret"
    ACCESS_TOKEN = "your_access_token"
    ACCESS_TOKEN_SECRET = "your_access_token_secret"
    USERNAME = "Player123"
    ACHIEVEMENT = "Master of the Arena"
    SHEN_TOKENS = 500

    result = share_achievement_on_twitter(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, USERNAME, ACHIEVEMENT, SHEN_TOKENS)
    print(result)
```
