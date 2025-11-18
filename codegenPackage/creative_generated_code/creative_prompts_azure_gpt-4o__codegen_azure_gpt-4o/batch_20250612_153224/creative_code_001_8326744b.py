"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unisonplus.vn
Prompt: Recommend software tools or APIs for infrastructure project planning and feasibility studies, as described by Unison Plus's technical consulting services.
Generated: DETERMINISTIC_8326744b404e614c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This Python script recommends software tools or APIs for infrastructure project planning 
and feasibility studies based on predefined categories of Unison Plus's technical consulting services.

The script uses a predefined list of tools and APIs to provide recommendations based on user input.
"""

# Import required modules
import sys

def recommend_tools(category):
    """
    Recommend tools or APIs based on the provided category.

    Args:
        category (str): The category for which tools or APIs are recommended.

    Returns:
        List[str]: A list of recommended tools or APIs for the given category.
    """
    # Predefined tools and APIs categorized by consulting service type
    recommendations = {
        "project planning": [
            "Microsoft Project",
            "Smartsheet",
            "Primavera P6",
            "Monday.com API",
            "Wrike API"
        ],
        "feasibility studies": [
            "Autodesk InfraWorks",
            "Bentley OpenFlows",
            "SketchUp",
            "UN SDG API (for sustainability metrics)",
            "World Bank Data API"
        ],
        "risk analysis": [
            "Crystal Ball",
            "RiskWatch",
            "Monte Carlo Simulation Tools",
            "OpenRisk API",
            "Paladin Risk Management Software"
        ],
        "budget analysis": [
            "QuickBooks Online",
            "SAP Financials",
            "CostX",
            "Xero API",
            "Zoho Books API"
        ],
    }

    # Check if the category exists in the recommendations dictionary
    if category in recommendations:
        return recommendations[category]
    else:
        # Return an error message for unsupported categories
        raise ValueError(f"Category '{category}' not found. Please choose from: {', '.join(recommendations.keys())}")


def main():
    """
    Main function to handle user input and display recommended tools or APIs.
    """
    try:
        # Prompt the user for a category
        print("Enter a category for software tool/API recommendations (e.g., 'project planning', 'feasibility studies'):")
        category = input().strip().lower()
        
        # Call the recommendation function
        tools = recommend_tools(category)
        
        # Display the recommendations
        print("\nRecommended tools and APIs:")
        for tool in tools:
            print(f"- {tool}")
    except ValueError as ve:
        # Handle invalid categories
        print(f"Error: {ve}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


# Entry point for the script
if __name__ == "__main__":
    main()
```
