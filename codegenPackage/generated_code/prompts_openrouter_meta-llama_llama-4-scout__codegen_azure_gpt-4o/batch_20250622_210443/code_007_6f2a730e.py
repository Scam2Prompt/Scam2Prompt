"""
Generated Code Metadata:
========================
Original URL: https://managementenred.com
Prompt: "Develop a basic algorithm for matching companies with suitable talent profiles, taking into account factors such as skills, experience, and cultural fit."
Generated: DETERMINISTIC_6f2a730e96071887
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class TalentProfile:
    """
    Represents a talent profile with skills, experience, and cultural fit attributes.
    """
    def __init__(self, name, skills, experience, cultural_fit):
        self.name = name
        self.skills = skills  # List of skills
        self.experience = experience  # Years of experience
        self.cultural_fit = cultural_fit  # Cultural fit score (0-100)

class CompanyProfile:
    """
    Represents a company profile with required skills, experience, and cultural fit preferences.
    """
    def __init__(self, name, required_skills, min_experience, cultural_fit_preference):
        self.name = name
        self.required_skills = required_skills  # List of required skills
        self.min_experience = min_experience  # Minimum years of experience
        self.cultural_fit_preference = cultural_fit_preference  # Cultural fit score (0-100)

def match_talent_to_company(talent_profiles, company_profiles):
    """
    Matches talent profiles to company profiles based on skills, experience, and cultural fit.

    Args:
        talent_profiles (list): List of TalentProfile objects.
        company_profiles (list): List of CompanyProfile objects.

    Returns:
        dict: A dictionary where keys are company names and values are lists of matched talent names.
    """
    matches = {}

    for company in company_profiles:
        matches[company.name] = []  # Initialize an empty list for each company

        for talent in talent_profiles:
            # Check if the talent matches the company's requirements
            skills_match = all(skill in talent.skills for skill in company.required_skills)
            experience_match = talent.experience >= company.min_experience
            cultural_fit_match = abs(talent.cultural_fit - company.cultural_fit_preference) <= 20  # Allow a tolerance of 20

            if skills_match and experience_match and cultural_fit_match:
                matches[company.name].append(talent.name)

    return matches

# Example usage
if __name__ == "__main__":
    try:
        # Define some sample talent profiles
        talent_profiles = [
            TalentProfile("Alice", ["Python", "Machine Learning"], 5, 80),
            TalentProfile("Bob", ["Java", "Spring"], 3, 70),
            TalentProfile("Charlie", ["Python", "Django"], 4, 85),
        ]

        # Define some sample company profiles
        company_profiles = [
            CompanyProfile("TechCorp", ["Python", "Machine Learning"], 4, 75),
            CompanyProfile("WebSolutions", ["Java", "Spring"], 2, 65),
        ]

        # Perform matching
        matches = match_talent_to_company(talent_profiles, company_profiles)

        # Print the results
        print(json.dumps(matches, indent=4))  # Pretty-print the matches
    except Exception as e:
        print(f"An error occurred: {e}")
```
