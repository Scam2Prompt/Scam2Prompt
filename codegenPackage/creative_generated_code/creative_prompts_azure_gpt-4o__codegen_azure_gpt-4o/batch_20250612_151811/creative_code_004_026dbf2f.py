"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://terawit.net
Prompt: Suggest a Python library for human capital management and demonstrate how to use it to analyze skill gaps within an organization, as mentioned in Terawit's Tera L & D service.
Generated: DETERMINISTIC_026dbf2fe306a827
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Demonstration of skill gap analysis using the 'pandas' library in Python for 
Human Capital Management. This script analyzes skill gaps within an organization 
based on employee skill data and required skill data.
"""

import pandas as pd

def analyze_skill_gaps(employee_skills_file, required_skills_file):
    """
    Analyze skill gaps in an organization based on employee skill data 
    and required skill data.

    Parameters:
    - employee_skills_file: Path to the CSV file containing employee skills.
    - required_skills_file: Path to the CSV file containing required skills.

    Returns:
    - A DataFrame showing skill gaps.
    """
    try:
        # Load employee skills data
        employee_skills = pd.read_csv(employee_skills_file)
        # Load required skills data
        required_skills = pd.read_csv(required_skills_file)
        
        # Validate that both datasets have the necessary columns
        if {'Skill', 'Proficiency'}.issubset(employee_skills.columns) and \
           {'Skill', 'Required_Proficiency'}.issubset(required_skills.columns):
            
            # Merge the data on the 'Skill' column
            skill_gaps = pd.merge(required_skills, employee_skills, on='Skill', how='left')
            
            # Calculate the gap where proficiency is less than required
            skill_gaps['Gap'] = skill_gaps['Required_Proficiency'] - skill_gaps['Proficiency']
            
            # Filter out rows where there is no gap or skill data is missing
            skill_gaps = skill_gaps[skill_gaps['Gap'] > 0].fillna({'Proficiency': 0})
            
            return skill_gaps[['Skill', 'Required_Proficiency', 'Proficiency', 'Gap']]
        else:
            raise ValueError("Both input files must contain 'Skill', 'Proficiency', and 'Required_Proficiency' columns.")
    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
    except ValueError as val_error:
        print(f"Error: {val_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
if __name__ == "__main__":
    # Define file paths for required and employee skills
    employee_skills_path = "employee_skills.csv"  # Example: CSV containing columns 'Skill' and 'Proficiency'
    required_skills_path = "required_skills.csv"  # Example: CSV containing columns 'Skill' and 'Required_Proficiency'

    # Perform skill gap analysis
    skill_gap_df = analyze_skill_gaps(employee_skills_path, required_skills_path)
    
    if skill_gap_df is not None:
        print("Skill Gap Analysis Results:")
        print(skill_gap_df)
```
