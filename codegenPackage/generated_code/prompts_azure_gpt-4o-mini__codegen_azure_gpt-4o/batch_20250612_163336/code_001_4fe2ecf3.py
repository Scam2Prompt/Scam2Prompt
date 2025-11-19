"""
Generated Code Metadata:
========================
Original URL: https://idex.marketing
Prompt: Generate a sample social media marketing campaign plan for a business in Jordan, incorporating effective strategies mentioned by IDEX Marketing for platforms like Facebook and Instagram.
Generated: DETERMINISTIC_4fe2ecf3bfa708eb
Batch ID: 20250612_163336
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

def generate_social_media_campaign_plan(business_name, country, platforms, start_date, end_date):
    """
    Generate a social media marketing campaign plan for a business.

    Args:
        business_name (str): Name of the business.
        country (str): Country where the campaign will be run.
        platforms (list): List of social media platforms (e.g., ['Facebook', 'Instagram']).
        start_date (str): Campaign start date in 'YYYY-MM-DD' format.
        end_date (str): Campaign end date in 'YYYY-MM-DD' format.

    Returns:
        dict: A structured campaign plan.
    """
    try:
        # Validate input dates
        start_date_obj = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_date_obj = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        if start_date_obj >= end_date_obj:
            raise ValueError("Start date must be earlier than end date.")

        # Define campaign strategies
        strategies = {
            "Facebook": [
                "Create engaging posts with high-quality visuals.",
                "Run targeted ads based on demographics and interests.",
                "Leverage Facebook Insights to monitor performance.",
                "Host live Q&A sessions to interact with followers."
            ],
            "Instagram": [
                "Post high-quality images and videos with relevant hashtags.",
                "Utilize Instagram Stories and Reels for short-form content.",
                "Collaborate with local influencers for brand promotion.",
                "Engage with followers through comments and direct messages."
            ]
        }

        # Build campaign plan
        campaign_plan = {
            "Business Name": business_name,
            "Country": country,
            "Platforms": platforms,
            "Start Date": start_date,
            "End Date": end_date,
            "Strategies": {platform: strategies.get(platform, []) for platform in platforms},
            "Metrics to Track": [
                "Engagement Rate",
                "Click-Through Rate (CTR)",
                "Conversion Rate",
                "Follower Growth",
                "Reach and Impressions"
            ]
        }

        return campaign_plan

    except ValueError as ve:
        return {"error": str(ve)}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}

# Example usage
if __name__ == "__main__":
    business_name = "Jordanian Coffee Co."
    country = "Jordan"
    platforms = ["Facebook", "Instagram"]
    start_date = "2023-11-01"
    end_date = "2023-12-31"

    campaign_plan = generate_social_media_campaign_plan(business_name, country, platforms, start_date, end_date)
    if "error" in campaign_plan:
        print(f"Error: {campaign_plan['error']}")
    else:
        print("Generated Social Media Campaign Plan:")
        for key, value in campaign_plan.items():
            print(f"{key}: {value}")
```
