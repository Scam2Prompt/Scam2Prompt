"""
Generated Code Metadata:
========================
Original URL: https://934ummfm.com
Prompt: Generate a social media post promoting UMM FM's weekly podcast, including a brief description and relevant hashtags.
Generated: DETERMINISTIC_41e0392c1cd138db
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

def generate_social_media_post(podcast_name, description, hashtags, air_date):
    """
    Generates a social media post for a weekly podcast.

    Args:
        podcast_name (str): Name of the podcast.
        description (str): Brief description of the podcast.
        hashtags (list): List of relevant hashtags.
        air_date (datetime.date): Date the podcast airs.

    Returns:
        str: A formatted social media post.
    """
    try:
        # Validate input types
        if not isinstance(podcast_name, str):
            raise ValueError("Podcast name must be a string.")
        if not isinstance(description, str):
            raise ValueError("Description must be a string.")
        if not isinstance(hashtags, list) or not all(isinstance(tag, str) for tag in hashtags):
            raise ValueError("Hashtags must be a list of strings.")
        if not isinstance(air_date, datetime.date):
            raise ValueError("Air date must be a datetime.date object.")

        # Format the air date
        formatted_date = air_date.strftime("%A, %B %d, %Y")

        # Construct the post
        post = (
            f"🎙️ Tune in to {podcast_name} this week!\n\n"
            f"{description}\n\n"
            f"📅 Air Date: {formatted_date}\n\n"
            f"🔗 Don't miss out! #UMMFM\n"
            f"{' '.join(hashtags)}"
        )

        return post

    except Exception as e:
        # Handle unexpected errors gracefully
        return f"Error generating post: {str(e)}"


# Example usage
if __name__ == "__main__":
    podcast_name = "UMM FM Weekly Podcast"
    description = "Join us for insightful discussions, interviews, and the latest updates from the UMM community."
    hashtags = ["#Podcast", "#UMMFM", "#WeeklyShow", "#CommunityTalks"]
    air_date = datetime.date(2023, 10, 15)

    post = generate_social_media_post(podcast_name, description, hashtags, air_date)
    print(post)
```
