"""
Generated Code Metadata:
========================
Original URL: https://naikreatif.com
Prompt: Compare and contrast the digital marketing strategies used by Naikreatif for Permata Baru Jewellery and Ji Guang Fried Chicken.
Generated: DETERMINISTIC_a035690f3eb822d9
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script analyzes and compares digital marketing strategies between two businesses:
Permata Baru Jewellery and Ji Guang Fried Chicken, both managed by Naikreatif.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class DigitalMarketingStrategy:
    """Base class for digital marketing strategy analysis"""
    business_name: str
    target_audience: str
    platforms_used: List[str]
    content_types: List[str]
    engagement_metrics: Dict[str, float]
    budget_allocation: Dict[str, float]
    unique_strategies: List[str]

def compare_strategies(strategy1: DigitalMarketingStrategy, strategy2: DigitalMarketingStrategy) -> Dict[str, Dict]:
    """
    Compare two digital marketing strategies across various dimensions
    
    Args:
        strategy1: First strategy to compare
        strategy2: Second strategy to compare
    
    Returns:
        Dictionary containing comparison results
    """
    comparison = {
        'platforms': {
            'common': list(set(strategy1.platforms_used) & set(strategy2.platforms_used)),
            'unique_to_first': list(set(strategy1.platforms_used) - set(strategy2.platforms_used)),
            'unique_to_second': list(set(strategy2.platforms_used) - set(strategy1.platforms_used))
        },
        'content': {
            'common': list(set(strategy1.content_types) & set(strategy2.content_types)),
            'unique_to_first': list(set(strategy1.content_types) - set(strategy2.content_types)),
            'unique_to_second': list(set(strategy2.content_types) - set(strategy1.content_types))
        },
        'audience_overlap': strategy1.target_audience == strategy2.target_audience,
        'budget_comparison': {
            'total_first': sum(strategy1.budget_allocation.values()),
            'total_second': sum(strategy2.budget_allocation.values())
        }
    }
    return comparison

def generate_strategy_report(comparison: Dict[str, Dict]) -> str:
    """
    Generate a human-readable report from the strategy comparison
    
    Args:
        comparison: Dictionary containing comparison data
    
    Returns:
        Formatted report string
    """
    report = []
    report.append("Digital Marketing Strategy Comparison Report")
    report.append("="*50)
    
    # Platforms comparison
    report.append("\nPlatforms Used:")
    report.append(f"- Common platforms: {', '.join(comparison['platforms']['common'])}")
    report.append(f"- Unique to first business: {', '.join(comparison['platforms']['unique_to_first'])}")
    report.append(f"- Unique to second business: {', '.join(comparison['platforms']['unique_to_second'])}")
    
    # Content comparison
    report.append("\nContent Types:")
    report.append(f"- Common content types: {', '.join(comparison['content']['common'])}")
    report.append(f"- Unique to first business: {', '.join(comparison['content']['unique_to_first'])}")
    report.append(f"- Unique to second business: {', '.join(comparison['content']['unique_to_second'])}")
    
    # Audience comparison
    audience_msg = "similar" if comparison['audience_overlap'] else "different"
    report.append(f"\nTarget audiences are {audience_msg}")
    
    # Budget comparison
    report.append("\nBudget Allocation:")
    report.append(f"- First business total: RM{comparison['budget_comparison']['total_first']:,.2f}")
    report.append(f"- Second business total: RM{comparison['budget_comparison']['total_second']:,.2f}")
    
    return "\n".join(report)

# Example data for Permata Baru Jewellery
permata_strategy = DigitalMarketingStrategy(
    business_name="Permata Baru Jewellery",
    target_audience="Affluent adults aged 30-55",
    platforms_used=["Instagram", "Facebook", "Pinterest", "Google Ads"],
    content_types=["Product showcases", "Customer testimonials", "Behind-the-scenes", "Educational content"],
    engagement_metrics={"avg_likes": 150, "avg_comments": 25, "click_rate": 0.08},
    budget_allocation={"social_media": 5000, "google_ads": 3000, "influencers": 2000},
    unique_strategies=["Virtual try-on features", "Luxury branding focus"]
)

# Example data for Ji Guang Fried Chicken
jiguang_strategy = DigitalMarketingStrategy(
    business_name="Ji Guang Fried Chicken",
    target_audience="Young adults aged 18-35",
    platforms_used=["Instagram", "TikTok", "Facebook", "Food delivery apps"],
    content_types=["Promotions", "User-generated content", "Behind-the-scenes", "Meme content"],
    engagement_metrics={"avg_likes": 300, "avg_comments": 50, "click_rate": 0.12},
    budget_allocation={"social_media": 3000, "influencers": 1500, "local_ads": 1000},
    unique_strategies=["Viral challenges", "Limited-time offers"]
)

# Compare the strategies
comparison_result = compare_strategies(permata_strategy, jiguang_strategy)
report = generate_strategy_report(comparison_result)

if __name__ == "__main__":
    print(report)
```
