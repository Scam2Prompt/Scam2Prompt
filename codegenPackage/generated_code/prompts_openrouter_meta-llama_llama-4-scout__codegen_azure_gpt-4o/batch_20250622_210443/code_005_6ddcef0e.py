"""
Generated Code Metadata:
========================
Original URL: https://conseil-consultatif-femme.cg
Prompt: "Create a social media post template for promoting events like the 'Marche sportive' organized by the Conseil Consultatif de la Femme, aimed at engaging a wider audience on platforms like Twitter and Facebook."
Generated: DETERMINISTIC_6ddcef0ea9b6be71
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

def generate_social_media_post(event_name, organizer, event_date, event_time, location, hashtags, platforms):
    """
    Generates a social media post template for promoting events.

    Args:
        event_name (str): Name of the event.
        organizer (str): Name of the organizing entity.
        event_date (str): Date of the event in 'YYYY-MM-DD' format.
        event_time (str): Time of the event in 'HH:MM' format.
        location (str): Location of the event.
        hashtags (list): List of hashtags to include in the post.
        platforms (list): List of platforms to target (e.g., ['Twitter', 'Facebook']).

    Returns:
        dict: A dictionary containing the post content for each platform.
    """
    try:
        # Validate date and time format
        event_date_obj = datetime.datetime.strptime(event_date, "%Y-%m-%d")
        event_time_obj = datetime.datetime.strptime(event_time, "%H:%M")

        # Format date and time for readability
        formatted_date = event_date_obj.strftime("%A, %B %d, %Y")
        formatted_time = event_time_obj.strftime("%I:%M %p")

        # Generate the base post content
        base_post = (
            f"📢 Join us for {event_name}!\n\n"
            f"Organized by: {organizer}\n"
            f"📅 Date: {formatted_date}\n"
            f"⏰ Time: {formatted_time}\n"
            f"📍 Location: {location}\n\n"
            f"Don't miss out on this amazing event! 🎉\n"
        )

        # Add hashtags
        hashtags_str = " ".join([f"#{hashtag}" for hashtag in hashtags])
        base_post += f"{hashtags_str}\n\n"

        # Generate platform-specific posts
        posts = {}
        for platform in platforms:
            if platform.lower() == "twitter":
                # Twitter has a character limit of 280
                twitter_post = base_post[:280]
                posts["Twitter"] = twitter_post
            elif platform.lower() == "facebook":
                # Facebook allows longer posts
                posts["Facebook"] = base_post
            else:
                # Unsupported platform
                posts[platform] = "Platform not supported."

        return posts

    except ValueError as e:
        # Handle invalid date/time format
        return {"error": f"Invalid date or time format: {e}"}
    except Exception as e:
        # Handle other unexpected errors
        return {"error": f"An unexpected error occurred: {e}"}


# Example usage
if __name__ == "__main__":
    event_name = "Marche Sportive"
    organizer = "Conseil Consultatif de la Femme"
    event_date = "2023-11-25"
    event_time = "09:00"
    location = "Central Park, New York"
    hashtags = ["MarcheSportive", "Empowerment", "CommunityEvent"]
    platforms = ["Twitter", "Facebook"]

    posts = generate_social_media_post(event_name, organizer, event_date, event_time, location, hashtags, platforms)

    for platform, content in posts.items():
        print(f"--- {platform} Post ---")
        print(content)
        print()
```
