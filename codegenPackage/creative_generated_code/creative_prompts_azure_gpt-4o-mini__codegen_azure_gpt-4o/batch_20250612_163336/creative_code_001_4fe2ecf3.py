"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idex.marketing
Prompt: Generate a sample social media marketing campaign plan for a business in Jordan, incorporating effective strategies mentioned by IDEX Marketing for platforms like Facebook and Instagram.
Generated: DETERMINISTIC_4fe2ecf3bfa708eb
Batch ID: 20250612_163336
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script generates a sample social media marketing campaign plan for a business in Jordan.
The campaign plan is designed for Facebook and Instagram and incorporates effective strategies
such as audience targeting, engaging content, ad placements, and performance tracking.

This program is written in Python and outputs the plan in a structured format.
"""

import json

def generate_marketing_campaign(business_name, location, platforms):
    """
    Generates a marketing campaign plan based on the provided business name, location, and platforms.
    
    Args:
        business_name (str): The name of the business.
        location (str): The geographic location of the target audience.
        platforms (list): A list of social media platforms to target (e.g., Facebook, Instagram).
    
    Returns:
        dict: A structured marketing campaign plan.
    """
    try:
        # Define target audience
        target_audience = {
            "age_range": "18-45",
            "gender": "All",
            "location": location,
            "interests": ["Travel", "Food", "Fashion", "Technology"]  # Example interests
        }

        # Define content strategy
        content_strategy = {
            "types": ["Images", "Videos", "Stories", "Reels"],
            "frequency": "3-5 posts per week",
            "tone": "Friendly, Informative, Engaging"
        }

        # Define ad strategy
        ad_strategy = {
            "budget": "500 JOD per month",
            "ad_types": ["Carousel Ads", "Video Ads", "Story Ads"],
            "optimization": "Targeted by location and interests"
        }

        # Define performance tracking strategy
        performance_tracking = {
            "metrics": ["Engagement Rate", "Click-Through Rate (CTR)", "Conversion Rate"],
            "tools": ["Facebook Insights", "Instagram Analytics"],
            "frequency": "Weekly Reviews"
        }

        # Combine all strategies into a campaign plan
        campaign_plan = {
            "business_name": business_name,
            "platforms": platforms,
            "target_audience": target_audience,
            "content_strategy": content_strategy,
            "ad_strategy": ad_strategy,
            "performance_tracking": performance_tracking
        }

        return campaign_plan

    except Exception as e:
        print(f"Error generating campaign plan: {e}")
        return None


def main():
    """
    Main function to generate and display the marketing campaign plan.
    """
    # Example input
    business_name = "Jordanian Delights"
    location = "Jordan"
    platforms = ["Facebook", "Instagram"]

    # Generate campaign plan
    campaign_plan = generate_marketing_campaign(business_name, location, platforms)

    if campaign_plan:
        # Print campaign plan as a formatted JSON
        print("Generated Marketing Campaign Plan:")
        print(json.dumps(campaign_plan, indent=4))
    else:
        print("Failed to generate marketing campaign plan.")


if __name__ == "__main__":
    main()
```
