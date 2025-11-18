"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vivadainfotech.com
Prompt: Recommend tools for creating eye-catching creatives and videos for hospital marketing campaigns, inspired by Vivada Infotech's case studies.
Generated: DETERMINISTIC_57bbd0ea9493e8ef
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Recommendation Tool for Hospital Marketing Campaign Creatives
This Python script recommends tools for creating eye-catching creatives and videos based on Vivada Infotech's case studies.
It uses a predefined list of tools categorized by use case and provides recommendations based on user input.
"""

# Import necessary libraries
import sys

def recommend_tools(marketing_type):
    """
    Function to recommend tools for creating marketing creatives and videos.
    Args:
        marketing_type (str): The type of marketing material (e.g., 'video', 'graphic').
    Returns:
        list: Recommended tools for the given type of marketing.
    """
    # Predefined tools categorized by use case
    tools = {
        "graphic": [
            "Canva - User-friendly platform for designing graphics.",
            "Adobe Photoshop - Advanced tool for professional graphic editing.",
            "Crello - Simplified tool for quick and engaging graphic creation."
        ],
        "video": [
            "Adobe Premiere Pro - Industry-standard video editing software.",
            "Final Cut Pro - Advanced video editing for macOS users.",
            "Animoto - Online tool for creating marketing videos easily."
        ],
        "animation": [
            "Blender - Free and open-source tool for 3D animation creation.",
            "After Effects - Powerful tool for motion graphics and animations.",
            "Powtoon - Simplified platform for animated video and presentation creation."
        ],
        "social_media": [
            "Hootsuite - Platform for social media content scheduling.",
            "Buffer - Tool to manage and analyze social media posts.",
            "Sprout Social - Advanced analytics and publishing for social marketing."
        ]
    }

    # Error handling for unsupported marketing types
    if marketing_type not in tools:
        return ["Error: Unsupported marketing type. Please choose from 'graphic', 'video', 'animation', or 'social_media'."]
    
    # Return the list of recommended tools
    return tools[marketing_type]

def main():
    """
    Main function to interact with the user and provide tool recommendations.
    """
    print("Welcome to the Hospital Marketing Tool Recommendation System!")
    print("Please enter the type of marketing material you need help with:")
    print("Options: 'graphic', 'video', 'animation', 'social_media'")
    
    # Get user input for marketing type
    marketing_type = input("Enter your choice: ").strip().lower()

    # Get recommendations based on user input
    recommendations = recommend_tools(marketing_type)
    
    # Display recommendations to the user
    print("\nRecommended Tools:")
    for tool in recommendations:
        print("- " + tool)

# Entry point for the script
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
```
