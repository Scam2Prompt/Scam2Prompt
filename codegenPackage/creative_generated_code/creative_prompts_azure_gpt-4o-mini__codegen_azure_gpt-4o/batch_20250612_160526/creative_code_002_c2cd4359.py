"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thebalichili.com
Prompt: Create a detailed plan for a digital marketing campaign that includes SEO and Google advertising, referencing the services offered by TheBalichili.
Generated: DETERMINISTIC_c2cd435969cfc174
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Digital Marketing Campaign Planner: SEO & Google Ads
This script generates a detailed plan for a digital marketing campaign focusing on SEO and Google Advertising.
The plan references hypothetical services offered by TheBalichili, a presumed marketing agency.
"""

# Import necessary libraries
import datetime
import json

class CampaignPlanner:
    """Class to generate a detailed digital marketing campaign plan."""
    
    def __init__(self, business_name, target_audience, budget):
        """
        Initialize CampaignPlanner with basic campaign parameters.
        
        Args:
            business_name (str): Name of the business for the campaign.
            target_audience (str): Description of the target audience.
            budget (float): Total budget allocated for the campaign.
        """
        self.business_name = business_name
        self.target_audience = target_audience
        self.budget = budget
        self.creation_date = datetime.datetime.now()
        self.plan = {}

    def add_seo_strategy(self):
        """Generate SEO strategy for the campaign."""
        self.plan['SEO'] = {
            "Keyword Research": {
                "Tools": ["Google Keyword Planner", "Ahrefs", "SEMRush"],
                "Objective": "Identify high-performing, relevant keywords for the target audience."
            },
            "On-Page Optimization": {
                "Tasks": [
                    "Optimize title tags, meta descriptions, and headers",
                    "Improve site speed and mobile responsiveness",
                    "Internal linking to enhance navigation"
                ],
                "Tools": ["Google Search Console", "PageSpeed Insights"]
            },
            "Content Strategy": {
                "Objective": "Create high-quality, engaging content that aligns with keywords.",
                "Tasks": [
                    "Write blog posts, articles, and infographics",
                    "Develop a content calendar for consistent posting"
                ],
                "Tools": ["Grammarly", "Canva", "WordPress"]
            },
            "Off-Page SEO": {
                "Tasks": [
                    "Build backlinks through partnerships and guest posts",
                    "Engage on social media platforms to drive traffic"
                ],
                "Tools": ["BuzzSumo", "Hootsuite"]
            }
        }

    def add_google_ads_strategy(self):
        """Generate Google Advertising strategy for the campaign."""
        self.plan['Google Ads'] = {
            "Campaign Types": ["Search Ads", "Display Ads", "Shopping Ads"],
            "Budget Allocation": {
                "Search Ads": self.budget * 0.5,  # 50% of the budget
                "Display Ads": self.budget * 0.3,  # 30% of the budget
                "Shopping Ads": self.budget * 0.2   # 20% of the budget
            },
            "Tools": ["Google Ads Manager", "Google Analytics"],
            "Optimization Strategies": [
                "A/B testing for ad copy and visuals",
                "Set up conversion tracking to measure performance",
                "Use demographic targeting for precise audience reach"
            ]
        }

    def generate_plan(self):
        """
        Generate the campaign plan.
        
        Returns:
            dict: A detailed plan for the campaign.
        """
        self.add_seo_strategy()
        self.add_google_ads_strategy()
        self.plan['Summary'] = {
            "Business Name": self.business_name,
            "Target Audience": self.target_audience,
            "Budget": f"${self.budget:,.2f}",
            "Creation Date": self.creation_date.strftime('%Y-%m-%d')
        }
        return self.plan

    def save_plan_to_file(self, filename="campaign_plan.json"):
        """
        Save the campaign plan to a JSON file.
        
        Args:
            filename (str): Name of the file to save the plan.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.plan, file, indent=4)
            print(f"Campaign plan successfully saved to {filename}.")
        except Exception as e:
            print(f"Error saving campaign plan to file: {e}")

# Usage example
if __name__ == "__main__":
    # Create a CampaignPlanner instance
    planner = CampaignPlanner(
        business_name="TheBalichili",
        target_audience="Small businesses and startups seeking online growth",
        budget=5000.00
    )
    
    # Generate the campaign plan
    campaign_plan = planner.generate_plan()
    
    # Display the plan
    print(json.dumps(campaign_plan, indent=4))
    
    # Save the plan to a file
    planner.save_plan_to_file()
```
