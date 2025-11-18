"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://craftintra.com
Prompt: Suggest tools for creating digital mockups of paper crafts, such as the cow mask made from paper plates featured on Craft Intra.
Generated: DETERMINISTIC_b414fa145919a5ae
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script suggests tools for creating digital mockups of paper crafts, such as masks made from paper plates.
It provides a list of tools based on the user's craft type and outputs recommendations accordingly.
"""

def suggest_mockup_tools(craft_type):
    """
    Suggests tools for creating digital mockups of paper crafts.

    Args:
        craft_type (str): The type of paper craft (e.g., "mask", "origami", "scrapbooking").

    Returns:
        list: A list of recommended tools for the given craft type.
    """
    # Define a dictionary of craft types and corresponding tools
    tools_recommendation = {
        "mask": ["Blender", "Adobe Illustrator", "Canva", "Tinkercad"],
        "origami": ["Origami Simulator", "Fusion 360", "SketchUp"],
        "scrapbooking": ["Canva", "Photoshop", "Figma"],
        "general_paper_craft": ["Silhouette Studio", "CorelDRAW", "Affinity Designer"]
    }
    
    # Fetch recommendations based on craft type
    try:
        recommendations = tools_recommendation.get(craft_type.lower(), [])
        if not recommendations:
            return ["No specific tools found for this craft type. Try general-purpose design tools."]
        return recommendations
    except Exception as e:
        # Handle any unexpected errors
        return [f"An error occurred while fetching recommendations: {str(e)}"]

def main():
    """
    Main function to interact with the user and provide tool suggestions.
    """
    print("Welcome to the Digital Mockup Tool Suggestion Program!")
    print("Please enter the type of paper craft you are working on.")
    print("Examples: mask, origami, scrapbooking, or general_paper_craft")
    
    # Get user input
    craft_type = input("Enter your craft type: ").strip()
    
    # Suggest tools based on user input
    recommendations = suggest_mockup_tools(craft_type)
    
    # Display the recommendations
    print("\nRecommended Tools:")
    for tool in recommendations:
        print(f"- {tool}")

if __name__ == "__main__":
    # Run the main function
    main()
```
