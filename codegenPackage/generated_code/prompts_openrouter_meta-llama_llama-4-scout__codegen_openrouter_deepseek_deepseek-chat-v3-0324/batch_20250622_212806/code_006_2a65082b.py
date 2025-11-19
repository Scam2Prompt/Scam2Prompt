"""
Generated Code Metadata:
========================
Original URL: https://foxlogy.com
Prompt: "Develop a social media marketing strategy for a small business in Bangladesh, using services similar to those provided by Foxlogy, a leading digital marketing agency in Dhaka."
Generated: DETERMINISTIC_2a65082b6cdccb74
Batch ID: 20250622_212806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Social Media Marketing Strategy Generator for Small Businesses in Bangladesh
This script generates a tailored social media marketing strategy based on business inputs.
"""

import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional

class SocialMediaStrategyGenerator:
    """
    Generates a social media marketing strategy for small businesses in Bangladesh.
    Inspired by services similar to Foxlogy's digital marketing approach.
    """
    
    def __init__(self):
        self.platforms = ["Facebook", "Instagram", "LinkedIn", "YouTube"]
        self.content_types = {
            "Facebook": ["Posts", "Stories", "Live Videos", "Polls"],
            "Instagram": ["Posts", "Stories", "Reels", "IGTV"],
            "LinkedIn": ["Articles", "Posts", "Videos"],
            "YouTube": ["Videos", "Shorts", "Live Streams"]
        }
        self.strategy_template = {
            "objectives": [],
            "target_audience": {},
            "platforms": [],
            "content_calendar": {},
            "budget_allocation": {},
            "performance_metrics": []
        }
    
    def get_business_inputs(self) -> Dict:
        """Collect business information from user."""
        print("=== Social Media Marketing Strategy Generator ===")
        print("Please provide the following information about your business:\n")
        
        business_info = {
            "business_name": input("Business Name: "),
            "industry": input("Industry: "),
            "target_age": input("Target Age Group (e.g., 18-35): "),
            "target_gender": input("Target Gender (Male/Female/Both): ").capitalize(),
            "location": input("Location (City/Region in Bangladesh): "),
            "budget": float(input("Monthly Marketing Budget (BDT): ")),
            "objectives": input("Main Objectives (comma separated - brand awareness, lead generation, sales, engagement): ").split(","),
            "current_social_media": input("Current Social Media Presence (comma separated platforms or 'none'): ").split(",")
        }
        
        return business_info
    
    def validate_inputs(self, business_info: Dict) -> bool:
        """Validate user inputs."""
        if not business_info["business_name"]:
            print("Error: Business name is required")
            return False
        
        if business_info["budget"] <= 0:
            print("Error: Budget must be positive")
            return False
            
        if not business_info["objectives"]:
            print("Error: At least one objective is required")
            return False
            
        return True
    
    def generate_strategy(self, business_info: Dict) -> Dict:
        """Generate marketing strategy based on business inputs."""
        strategy = self.strategy_template.copy()
        
        # Set basic info
        strategy["business_name"] = business_info["business_name"]
        strategy["generation_date"] = datetime.now().strftime("%Y-%m-%d")
        strategy["valid_until"] = (datetime.now() + timedelta(days=90)).strftime("%Y-%m-%d")
        
        # Set objectives
        strategy["objectives"] = [obj.strip() for obj in business_info["objectives"]]
        
        # Set target audience
        strategy["target_audience"] = {
            "age": business_info["target_age"],
            "gender": business_info["target_gender"],
            "location": business_info["location"],
            "interests": f"Related to {business_info['industry']}"
        }
        
        # Recommend platforms
        strategy["platforms"] = self._recommend_platforms(business_info)
        
        # Create content calendar
        strategy["content_calendar"] = self._create_content_calendar(strategy["platforms"])
        
        # Allocate budget
        strategy["budget_allocation"] = self._allocate_budget(business_info["budget"], strategy["platforms"])
        
        # Set performance metrics
        strategy["performance_metrics"] = self._set_performance_metrics(strategy["objectives"])
        
        return strategy
    
    def _recommend_platforms(self, business_info: Dict) -> List[Dict]:
        """Recommend social media platforms based on business info."""
        recommended = []
        
        # Always recommend Facebook for Bangladeshi market
        recommended.append({
            "platform": "Facebook",
            "reason": "Most popular platform in Bangladesh with high engagement",
            "content_types": self.content_types["Facebook"]
        })
        
        # Instagram if targeting younger audience
        if "18-35" in business_info["target_age"]:
            recommended.append({
                "platform": "Instagram",
                "reason": "Ideal for younger demographics and visual content",
                "content_types": self.content_types["Instagram"]
            })
        
        # LinkedIn for B2B or professional services
        if any(x in business_info["industry"].lower() for x in ["consulting", "professional", "b2b", "service"]):
            recommended.append({
                "platform": "LinkedIn",
                "reason": "Effective for professional networking and B2B marketing",
                "content_types": self.content_types["LinkedIn"]
            })
        
        # YouTube if budget allows for video content
        if business_info["budget"] > 10000:  # BDT
            recommended.append({
                "platform": "YouTube",
                "reason": "Video content performs well with proper investment",
                "content_types": self.content_types["YouTube"]
            })
        
        return recommended
    
    def _create_content_calendar(self, platforms: List[Dict]) -> Dict:
        """Generate a 30-day content calendar."""
        calendar = {}
        today = datetime.now()
        
        for i in range(30):
            date_str = (today + timedelta(days=i)).strftime("%Y-%m-%d")
            calendar[date_str] = []
            
            for platform in platforms:
                platform_name = platform["platform"]
                content_type = platform["content_types"][i % len(platform["content_types"])]
                
                calendar[date_str].append({
                    "platform": platform_name,
                    "content_type": content_type,
                    "theme": self._get_content_theme(platform_name, content_type)
                })
        
        return calendar
    
    def _get_content_theme(self, platform: str, content_type: str) -> str:
        """Get content theme based on platform and content type."""
        themes = {
            "Facebook": {
                "Posts": "Educational/Informative",
                "Stories": "Behind-the-scenes",
                "Live Videos": "Q&A or Product Demo",
                "Polls": "Customer Feedback"
            },
            "Instagram": {
                "Posts": "High-quality Visuals",
                "Stories": "User-generated Content",
                "Reels": "Trending Challenges",
                "IGTV": "Tutorials/How-tos"
            },
            "LinkedIn": {
                "Articles": "Industry Insights",
                "Posts": "Company Updates",
                "Videos": "Expert Interviews"
            },
            "YouTube": {
                "Videos": "Product Reviews",
                "Shorts": "Quick Tips",
                "Live Streams": "Webinars"
            }
        }
        
        return themes.get(platform, {}).get(content_type, "General Update")
    
    def _allocate_budget(self, total_budget: float, platforms: List[Dict]) -> Dict:
        """Allocate budget across recommended platforms."""
        allocation = {}
        platform_count = len(platforms)
        
        if platform_count == 0:
            return allocation
            
        base_allocation = total_budget * 0.6 / platform_count
        remaining = total_budget * 0.4
        
        for i, platform in enumerate(platforms):
            platform_name = platform["platform"]
            
            # YouTube gets higher allocation
            if platform_name == "YouTube":
                allocation[platform_name] = base_allocation + remaining * 0.5
                remaining -= remaining * 0.5
            else:
                allocation[platform_name] = base_allocation + remaining * (0.5 / (platform_count - 1))
        
        # Convert to BDT and round
        return {k: round(v, 2) for k, v in allocation.items()}
    
    def _set_performance_metrics(self, objectives: List[str]) -> List[str]:
        """Set performance metrics based on objectives."""
        metrics_map = {
            "brand awareness": ["Reach", "Impressions", "Follower Growth"],
            "lead generation": ["Click-through Rate", "Lead Form Completions", "Conversion Rate"],
            "sales": ["Conversion Rate", "Return on Ad Spend", "Revenue Generated"],
            "engagement": ["Likes", "Comments", "Shares", "Engagement Rate"]
        }
        
        metrics = []
        for objective in objectives:
            obj = objective.strip().lower()
            if obj in metrics_map:
                metrics.extend(metrics_map[obj])
        
        return list(set(metrics))  # Remove duplicates
    
    def save_strategy(self, strategy: Dict, filename: Optional[str] = None) -> None:
        """Save strategy to JSON file."""
        if not filename:
            filename = f"{strategy['business_name'].replace(' ', '_')}_social_media_strategy.json"
        
        with open(filename,
