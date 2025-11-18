"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mastermeatsqa.com
Prompt: Create a Python function to analyze architectural case studies provided by Études Architectural Solutions and extract key design insights for sustainability.
Generated: DETERMINISTIC_6c6366efa7195890
Batch ID: 20250612_151001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import re

def analyze_case_studies(case_studies):
    """
    Analyze architectural case studies to extract key design insights for sustainability.

    Parameters:
        case_studies (list of dict): A list of dictionaries, each containing details of a case study.
            Each dictionary should have the following keys:
            - 'title': str, the title of the case study
            - 'content': str, the text content describing the case study

    Returns:
        dict: A dictionary containing extracted sustainability insights.
            Example structure:
            {
                "case_study_title": {
                    "green_materials": [...],
                    "energy_efficiency": [...],
                    "water_management": [...],
                    "other_insights": [...]
                }
            }
    """

    if not isinstance(case_studies, list):
        raise ValueError("Input case_studies must be a list of dictionaries.")

    sustainability_insights = {}
    
    # Define keywords for different categories of sustainability
    keywords = {
        "green_materials": ["recycled", "renewable", "low-carbon", "sustainable material"],
        "energy_efficiency": ["solar panel", "LED lighting", "energy-efficient", "insulation"],
        "water_management": ["rainwater harvesting", "greywater reuse", "water conservation", "low-flow fixtures"],
        "other_insights": ["carbon footprint", "net-zero", "LEED certified", "passive design"]
    }

    # Analyze each case study
    for case_study in case_studies:
        if not isinstance(case_study, dict) or 'title' not in case_study or 'content' not in case_study:
            raise ValueError("Each case_study must be a dictionary with 'title' and 'content' keys.")
        
        title = case_study['title']
        content = case_study['content']
        
        # Initialize insights for the current case study
        insights = {category: [] for category in keywords.keys()}
        
        # Search for keywords in the content
        for category, category_keywords in keywords.items():
            for keyword in category_keywords:
                # Use case-insensitive search for keywords
                if re.search(rf"\b{keyword}\b", content, re.IGNORECASE):
                    insights[category].append(keyword)
        
        # Add insights to the result dictionary
        sustainability_insights[title] = insights

    return sustainability_insights


# Example usage
if __name__ == "__main__":
    # List of example architectural case studies
    example_case_studies = [
        {
            "title": "Eco-Friendly Apartment Building",
            "content": "This building utilizes solar panels, rainwater harvesting, and recycled materials to achieve a sustainable design."
        },
        {
            "title": "Net-Zero Office Space",
            "content": "The office is LEED certified and employs energy-efficient insulation and passive design techniques."
        }
    ]

    # Analyze case studies
    try:
        insights = analyze_case_studies(example_case_studies)
        print(json.dumps(insights, indent=4))
    except Exception as e:
        print(f"Error: {e}")
```
