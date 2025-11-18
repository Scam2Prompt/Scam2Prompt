"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://budbeeindia.com
Prompt: Recommend tools or libraries to create a visually appealing ad campaign, inspired by BudBee India's "Advertising & Eye-Candy" services.
Generated: DETERMINISTIC_2474ea284dbcc834
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# This script provides recommendations for tools and libraries to create a visually appealing ad campaign. 
# These recommendations are based on the concept of combining design, animation, and data-driven insights.

import json

# Define a function to recommend tools based on the needs of the ad campaign
def recommend_ad_tools(objective):
    """
    Recommend tools and libraries for creating a visually appealing ad campaign.
    
    :param objective: str - Objective of the ad campaign (e.g., 'animation', 'design', 'data-driven insights')
    :return: dict - Recommended tools and libraries
    """
    try:
        # Dictionary containing recommendations based on objectives
        recommendations = {
            "animation": [
                "Adobe After Effects - Industry-standard tool for creating complex animations and motion graphics.",
                "Blender - Open-source 3D creation suite for animations and modeling.",
                "LottieFiles - Lightweight library for adding interactive animations to web and mobile apps."
            ],
            "design": [
                "Canva - User-friendly platform for creating visually stunning designs.",
                "Figma - Collaborative interface design tool for teams.",
                "Sketch - Vector graphics editor for digital design."
            ],
            "data-driven insights": [
                "Tableau - Data visualization software for creating impactful charts and dashboards.",
                "Google Data Studio - Free tool for turning data into shareable reports and dashboards.",
                "Chart.js - Lightweight library for creating beautiful charts in web applications."
            ],
        }
        
        # Check if the objective is valid and return appropriate recommendations
        if objective in recommendations:
            return {
                "status": "success",
                "objective": objective,
                "tools": recommendations[objective]
            }
        else:
            return {
                "status": "error",
                "message": f"Unknown objective '{objective}'. Please choose one of the following: {', '.join(recommendations.keys())}"
            }
    except Exception as e:
        # Handle unexpected errors
        return {
            "status": "error",
            "message": f"An unexpected error occurred: {str(e)}"
        }


# Main function to test the recommendations
if __name__ == "__main__":
    # Input: Objective provided by the user
    user_input = input("Enter the objective for your ad campaign (animation/design/data-driven insights): ").strip().lower()
    
    # Fetch recommendations
    result = recommend_ad_tools(user_input)
    
    # Output the recommendations in a nicely formatted JSON structure
    print(json.dumps(result, indent=4))
```
