"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agenciainside.com
Prompt: Write a function that demonstrates how to create innovative digital marketing solutions, inspired by the creativity and flexibility principles of Agência inSIDE.
Generated: DETERMINISTIC_8e4c3438ab7d47f4
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import string

def generate_innovative_marketing_campaign(budget, target_audience, platform_list, campaign_duration_days):
    """
    Function to generate an innovative digital marketing campaign inspired by creativity and flexibility principles.

    Parameters:
        budget (float): Marketing budget in USD.
        target_audience (str): Description of the target audience (e.g., "millennials interested in fitness").
        platform_list (list): List of platforms to run the campaign (e.g., ['Instagram', 'Facebook', 'LinkedIn']).
        campaign_duration_days (int): Duration of the campaign in days.

    Returns:
        dict: A dictionary containing details of the generated marketing campaign.
    """
    
    # Error handling for invalid inputs
    if budget <= 0:
        raise ValueError("Budget must be greater than 0.")
    if not target_audience or not isinstance(target_audience, str):
        raise ValueError("Target audience must be a non-empty string.")
    if not platform_list or not isinstance(platform_list, list) or not all(isinstance(p, str) for p in platform_list):
        raise ValueError("Platform list must be a non-empty list of strings.")
    if campaign_duration_days <= 0:
        raise ValueError("Campaign duration must be greater than 0 days.")

    # Helper function to create unique campaign hashtags
    def generate_hashtag(base):
        """
        Generate a creative hashtag based on a base keyword.
        """
        suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        return f"#{base.capitalize()}{suffix}"
    
    # Define core campaign concepts
    campaign_name = f"Creative-{target_audience.replace(' ', '')}-Campaign"
    campaign_hashtags = [generate_hashtag(target_audience.split()[0]) for _ in range(3)]
    personalized_content = {
        "video_ads": f"{target_audience}-focused short videos tailored for {', '.join(platform_list)}.",
        "interactive_posts": f"Engaging posts with polls and quizzes targeting {target_audience}."
    }
    outreach_strategy = {
        "platform_optimization": f"Budget split proportionally for {', '.join(platform_list)}.",
        "performance_tracking": "Daily analytics to optimize content and ad spend."
    }

    # Assemble the campaign into a dictionary
    campaign_details = {
        "campaign_name": campaign_name,
        "campaign_duration_days": campaign_duration_days,
        "total_budget": budget,
        "platforms": platform_list,
        "target_audience": target_audience,
        "campaign_hashtags": campaign_hashtags,
        "personalized_content": personalized_content,
        "outreach_strategy": outreach_strategy,
    }

    return campaign_details

# Example usage
if __name__ == "__main__":
    try:
        marketing_campaign = generate_innovative_marketing_campaign(
            budget=10000,
            target_audience="tech-savvy millennials",
            platform_list=["Instagram", "TikTok", "LinkedIn"],
            campaign_duration_days=30
        )
        print("Generated Marketing Campaign:")
        for key, value in marketing_campaign.items():
            print(f"{key}: {value}")
    except ValueError as e:
        print(f"Error: {e}")
```
