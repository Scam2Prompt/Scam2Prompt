"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://roshako.com
Prompt: Using the brands listed on Roshako's website (e.g., Esab, Miller, Dewalt, Victor), write a script to recommend industrial tools based on user input for specific industries like oil & gas or marine engineering.
Generated: DETERMINISTIC_dd055eff3c1f1717
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Define a dictionary to store industrial tools based on industries and brands
tools_catalog = {
    "oil & gas": {
        "Esab": ["Cutting Torch", "Welding Machine", "Plasma Cutter"],
        "Miller": ["Arc Welder", "Generator", "Welding Helmet"],
        "Dewalt": ["Power Drill", "Impact Wrench", "Angle Grinder"],
        "Victor": ["Gas Regulator", "Oxygen Cylinder", "Acetylene Cylinder"]
    },
    "marine engineering": {
        "Esab": ["Marine Welding Kit", "Underwater Cutting Torch"],
        "Miller": ["Portable Generator", "Welders"],
        "Dewalt": ["Cordless Impact Driver", "Screw Gun"],
        "Victor": ["Marine Cutting Equipment", "Welding Rods"]
    }
}

def get_tools_by_industry_and_brand(industry, brand):
    """
    Retrieve a list of tools based on the specified industry and brand.

    Parameters:
    - industry (str): The industry for which tools are requested.
    - brand (str): The brand of tools to retrieve.

    Returns:
    - list: A list of tools if found, otherwise an error message.
    """
    try:
        # Check if the industry exists in the catalog
        if industry in tools_catalog:
            # Check if the brand exists under the specified industry
            if brand in tools_catalog[industry]:
                return tools_catalog[industry][brand]
            else:
                return f"Brand '{brand}' not found for industry '{industry}'."
        else:
            return f"Industry '{industry}' not found in the catalog."
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    """
    Main function to run the tool recommendation system.
    """
    print("Welcome to the Industrial Tool Recommendation System!")
    
    # Prompt user for industry
    industry = input("Please enter your industry (e.g., oil & gas, marine engineering): ").strip().lower()
    
    # Prompt user for brand
    brand = input("Please enter the brand (e.g., Esab, Miller, Dewalt, Victor): ").strip().capitalize()
    
    # Get the recommended tools
    recommendations = get_tools_by_industry_and_brand(industry, brand)
    
    # Display the results
    if isinstance(recommendations, list):
        print(f"\nRecommended tools for {brand} in {industry}:")
        for tool in recommendations:
            print(f"- {tool}")
    else:
        print(recommendations)

if __name__ == "__main__":
    main()
```
