"""
Generated Code Metadata:
========================
Original URL: https://mommymilestones.com
Prompt: Write a social media post celebrating a mom's milestone achievements, incorporating the phrase "embrace the messy" and "lift up your awesomeness".
Generated: DETERMINISTIC_3e2de0af6cc1a333
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from datetime import datetime

def create_social_media_post(mom_name, milestone, platform="Facebook"):
    """
    Generates a social media post celebrating a mom's milestone achievements.

    Args:
        mom_name (str): Name of the mom being celebrated.
        milestone (str): Description of the milestone achieved.
        platform (str): Social media platform where the post will be shared. Default is "Facebook".

    Returns:
        str: A formatted social media post.
    """
    try:
        # Validate inputs
        if not mom_name or not milestone:
            raise ValueError("Both 'mom_name' and 'milestone' must be provided.")

        # Get the current date
        current_date = datetime.now().strftime("%B %d, %Y")

        # Construct the post
        post = (
            f"🎉 {current_date} 🎉\n\n"
            f"Today, we celebrate an incredible milestone achieved by {mom_name}! 🌟\n\n"
            f"{milestone}\n\n"
            f"Through it all, {mom_name} has shown us how to embrace the messy moments and lift up her awesomeness. 💪✨\n\n"
            f"Let's all take a moment to cheer her on and celebrate this amazing achievement! 🥳👏\n\n"
            f"#EmbraceTheMessy #LiftUpYourAwesomeness #MilestoneCelebration"
        )

        # Add platform-specific note
        if platform.lower() == "twitter":
            post += "\n\n(Posted on Twitter: Keep it short and sweet!)"
        elif platform.lower() == "instagram":
            post += "\n\n(Posted on Instagram: Don't forget to add a photo!)"

        return post

    except ValueError as ve:
        return f"Error: {ve}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"


# Example usage
if __name__ == "__main__":
    # Example inputs
    mom_name = "Sarah"
    milestone = "She completed her first marathon, proving that determination and hard work pay off!"

    # Generate the post
    social_media_post = create_social_media_post(mom_name, milestone, platform="Instagram")

    # Print the post
    print(social_media_post)
```
