"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-unity-profit.com
Prompt: Develop a recommendation engine that suggests investment strategies (e.g., contrarian investing, index investing) based on user profiles and preferences, similar to Juros Xyro's approach.
Generated: DETERMINISTIC_7ffc3a495c07d7a0
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging

# Configure logging for error tracking and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RecommendationEngine:
    """
    A simple recommendation engine for investment strategies based on user profiles and preferences.
    """

    def __init__(self):
        # Predefined investment strategies with descriptions
        self.investment_strategies = {
            "contrarian_investing": "Investing against prevailing market trends and sentiments.",
            "index_investing": "Investing in index funds that replicate the performance of a market index.",
            "growth_investing": "Investing in companies with potential for above-average growth.",
            "value_investing": "Investing in undervalued stocks with strong fundamentals.",
            "dividend_investing": "Investing in companies that pay consistent dividends."
        }

    def recommend_strategy(self, user_profile):
        """
        Recommend investment strategies based on user profiles and preferences.

        Args:
            user_profile (dict): A dictionary containing user information and preferences.
                Expected keys:
                    - risk_tolerance (str): "high", "medium", "low"
                    - investment_goal (str): "growth", "income", "capital_preservation"
                    - market_preference (str): "bullish", "bearish", "neutral"

        Returns:
            list: A list of recommended investment strategies.
        """
        try:
            # Validate user profile input
            if not isinstance(user_profile, dict):
                raise ValueError("User profile must be a dictionary.")

            # Extract user preferences
            risk_tolerance = user_profile.get("risk_tolerance", "").lower()
            investment_goal = user_profile.get("investment_goal", "").lower()
            market_preference = user_profile.get("market_preference", "").lower()

            # Match user preferences to investment strategies
            recommendations = []

            if risk_tolerance == "high":
                recommendations.append("growth_investing")
            if risk_tolerance in ["medium", "low"]:
                recommendations.append("index_investing")
                recommendations.append("value_investing")

            if investment_goal == "income":
                recommendations.append("dividend_investing")
            elif investment_goal == "growth":
                recommendations.append("growth_investing")
            elif investment_goal == "capital_preservation":
                recommendations.append("index_investing")

            if market_preference == "bearish":
                recommendations.append("contrarian_investing")

            # Remove duplicates and return the list
            return list(set(recommendations))

        except Exception as e:
            logging.error(f"Error in recommending strategies: {str(e)}")
            return []

def main():
    """
    Main function to run the recommendation engine.
    """
    # Example user profiles
    user_profiles = [
        {
            "risk_tolerance": "high",
            "investment_goal": "growth",
            "market_preference": "bullish"
        },
        {
            "risk_tolerance": "low",
            "investment_goal": "income",
            "market_preference": "bearish"
        },
        {
            "risk_tolerance": "medium",
            "investment_goal": "capital_preservation",
            "market_preference": "neutral"
        }
    ]

    # Instantiate the recommendation engine
    engine = RecommendationEngine()

    # Generate recommendations for each user profile
    for i, profile in enumerate(user_profiles, start=1):
        logging.info(f"Processing profile {i}: {json.dumps(profile)}")
        recommendations = engine.recommend_strategy(profile)
        logging.info(f"Recommendations for profile {i}: {recommendations}")

if __name__ == "__main__":
    main()
```
