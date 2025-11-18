"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sautikenya.com
Prompt: Recommend tools or libraries for creating short films or theater scripts for community engagement, inspired by Sauti Kenya's use of film in advocacy.
Generated: DETERMINISTIC_6a608f64fcd768f1
Batch ID: 20250612_150653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Tool Recommendation Script for Creative Projects
This script recommends tools and libraries for creating short films or theater scripts 
focused on community engagement, inspired by Sauti Kenya's advocacy efforts. 
"""

# Import necessary modules
import json

def get_recommended_tools(category):
    """
    Recommend tools and libraries for the given category.
    
    Parameters:
        category (str): The category of the creative project ('film' or 'script').
        
    Returns:
        list: A list of recommended tools for the specified category.
    """
    try:
        # Dictionary of recommendations
        tools = {
            "film": [
                {"name": "DaVinci Resolve", "description": "A professional-grade video editing tool, free and paid versions available."},
                {"name": "Adobe Premiere Pro", "description": "An industry-standard video editing tool for creating high-quality films."},
                {"name": "Canva", "description": "Easy-to-use graphic design tool with templates for short film posters and visuals."},
                {"name": "Final Draft", "description": "Screenwriting software for developing film scripts effectively."},
            ],
            "script": [
                {"name": "WriterDuet", "description": "Collaborative screenwriting software for co-creating theater scripts."},
                {"name": "Scrivener", "description": "A powerful tool for scriptwriting and creative writing organization."},
                {"name": "Fade In", "description": "Screenwriting software with modern features for theater and film scripts."},
                {"name": "Trello", "description": "Organizational tool to plan and manage creative projects, including script development."},
            ]
        }
        
        # Fetch tools for the given category
        if category in tools:
            return tools[category]
        else:
            raise ValueError("Invalid category provided. Please use 'film' or 'script'.")
    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred while fetching recommendations: {e}")
        return []

def display_recommendations(recommendations):
    """
    Display the list of recommended tools in a user-friendly format.
    
    Parameters:
        recommendations (list): A list of tool recommendations.
    """
    if not recommendations:
        print("No recommendations available.")
        return
    
    print("Recommended Tools:")
    for tool in recommendations:
        print(f"- {tool['name']}: {tool['description']}")

# Main program
if __name__ == "__main__":
    # Prompt user for the type of project
    print("Welcome! Get recommendations for tools to help with your creative project.")
    category = input("Enter the type of project ('film' or 'script'): ").strip().lower()
    
    # Fetch and display recommended tools
    recommendations = get_recommended_tools(category)
    display_recommendations(recommendations)
```
