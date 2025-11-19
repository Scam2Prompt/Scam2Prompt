"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dexor.site
Prompt: Generate a list of the top 10 scholarships for international students in the US, including unique eligibility criteria and application tips.
Generated: DETERMINISTIC_56de8f58aaebc2e3
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests

def fetch_scholarships():
    """
    Fetches the top 10 scholarships for international students in the US.
    This function uses pre-defined scholarship data for simplicity.

    Returns:
        list: A list of dictionaries containing scholarship details.
    """
    try:
        # Static data representing top scholarships
        scholarships = [
            {
                "name": "Fulbright Foreign Student Program",
                "eligibility": "Must have completed undergraduate education and demonstrate leadership potential.",
                "application_tips": "Focus on academic achievements and leadership in your essay."
            },
            {
                "name": "Hubert Humphrey Fellowship Program",
                "eligibility": "Must have professional experience and demonstrate leadership qualities.",
                "application_tips": "Highlight your professional achievements and career goals."
            },
            {
                "name": "American Association of University Women International Fellowships",
                "eligibility": "Women who are not U.S. citizens or permanent residents.",
                "application_tips": "Emphasize your commitment to women's issues and academic excellence."
            },
            {
                "name": "Rotary Peace Fellowships",
                "eligibility": "Must have a bachelor's degree and 3 years of relevant work experience.",
                "application_tips": "Demonstrate your work in peacebuilding and conflict resolution."
            },
            {
                "name": "Joint Japan World Bank Graduate Scholarship Program",
                "eligibility": "Citizens of developing countries with professional experience in development-related work.",
                "application_tips": "Focus on your contributions to development projects in your home country."
            },
            {
                "name": "PEO International Peace Scholarship",
                "eligibility": "Women from countries other than the U.S. and Canada pursuing graduate studies.",
                "application_tips": "Show your dedication to advancing global peace and education."
            },
            {
                "name": "Civil Society Leadership Awards",
                "eligibility": "Students from eligible countries who demonstrate leadership in civil society initiatives.",
                "application_tips": "Describe your leadership role in promoting social change."
            },
            {
                "name": "Global Study Awards",
                "eligibility": "Must demonstrate strong academic performance and a commitment to making a positive impact on society.",
                "application_tips": "Connect your study plans to a larger societal benefit."
            },
            {
                "name": "Onsi Sawiris Scholarship Program",
                "eligibility": "Egyptian students with excellent academic records and leadership potential.",
                "application_tips": "Highlight your achievements in both academics and community service."
            },
            {
                "name": "The NextGen Scholarship",
                "eligibility": "International students with a minimum GPA of 3.0 enrolled in a U.S. institution.",
                "application_tips": "Provide clear documentation of your academic performance and extracurricular activities."
            }
        ]
        return scholarships
    except Exception as e:
        # Log the error and return an empty list
        print(f"Error fetching scholarships: {e}")
        return []

def display_scholarships(scholarships):
    """
    Displays the list of scholarships in a formatted manner.

    Args:
        scholarships (list): The list of scholarship dictionaries.
    """
    if not scholarships:
        print("No scholarships found.")
        return

    print("Top 10 Scholarships for International Students in the US:")
    for i, scholarship in enumerate(scholarships, start=1):
        print(f"{i}. Scholarship Name: {scholarship['name']}")
        print(f"   Eligibility: {scholarship['eligibility']}")
        print(f"   Application Tips: {scholarship['application_tips']}")
        print()

if __name__ == "__main__":
    # Main entry point of the script
    scholarships = fetch_scholarships()
    display_scholarships(scholarships)
```
