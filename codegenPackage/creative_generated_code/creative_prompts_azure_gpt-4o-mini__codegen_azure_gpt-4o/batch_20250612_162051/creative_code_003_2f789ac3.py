"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://searchhr.com.ar
Prompt: Create a code snippet that simulates a personalized advisory service for job seekers, similar to the approach taken by Search HR.
Generated: DETERMINISTIC_2f789ac3adca9940
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: job_advisory_service.py

import sys

def get_advisory(job_seeker_info, industry_data):
    """
    Simulates a personalized advisory service for job seekers.

    Parameters:
    job_seeker_info (dict): Information about the job seeker.
                            Expected keys: 'name', 'skills', 'experience', 'desired_role'.
    industry_data (dict): Industry-specific data.
                          Expected keys: 'roles', 'skills_in_demand', 'salary_range'.

    Returns:
    str: Advisory message for the job seeker.
    """
    try:
        # Validate inputs
        if not isinstance(job_seeker_info, dict):
            raise ValueError("Invalid job_seeker_info format. Expected a dictionary.")
        if not isinstance(industry_data, dict):
            raise ValueError("Invalid industry_data format. Expected a dictionary.")

        # Extract information
        name = job_seeker_info.get("name", "Job Seeker")
        skills = set(job_seeker_info.get("skills", []))
        experience = job_seeker_info.get("experience", 0)
        desired_role = job_seeker_info.get("desired_role", "Not specified")
        roles_available = industry_data.get("roles", {})
        skills_in_demand = set(industry_data.get("skills_in_demand", []))
        salary_range = industry_data.get("salary_range", {})

        # Advisory logic
        if desired_role in roles_available:
            role_details = roles_available[desired_role]
            matching_skills = skills.intersection(role_details.get("required_skills", set()))
            recommended_skills = skills_in_demand.difference(skills)

            advisory_message = f"Hello {name},\n\n" \
                               f"Based on your desired role '{desired_role}', here is our advice:\n" \
                               f"- Matching Skills: {', '.join(matching_skills) if matching_skills else 'None'}\n" \
                               f"- Recommended Skills to Learn: {', '.join(recommended_skills) if recommended_skills else 'None'}\n" \
                               f"- Experience Needed: {role_details.get('experience_needed', 'Not specified')} years\n" \
                               f"- Expected Salary Range: {salary_range.get(desired_role, 'Not specified')}\n"

            if experience < role_details.get("experience_needed", 0):
                advisory_message += "You may want to gain more experience to match the requirements for this role.\n"

        else:
            advisory_message = f"Hello {name},\n\n" \
                               f"Unfortunately, we couldn't find information for your desired role '{desired_role}'.\n" \
                               f"Consider exploring other roles or enhancing your skillset based on industry demands.\n"

        return advisory_message

    except Exception as e:
        return f"An error occurred while generating advisory: {str(e)}"


if __name__ == "__main__":
    try:
        # Example job seeker information
        example_job_seeker = {
            "name": "Alice",
            "skills": ["Python", "Data Analysis", "Machine Learning"],
            "experience": 3,
            "desired_role": "Data Scientist"
        }

        # Example industry data
        example_industry_data = {
            "roles": {
                "Data Scientist": {
                    "required_skills": {"Python", "Machine Learning", "Statistics"},
                    "experience_needed": 2
                },
                "Software Engineer": {
                    "required_skills": {"Python", "Java", "Software Design"},
                    "experience_needed": 1
                }
            },
            "skills_in_demand": {"Cloud Computing", "AI", "Python", "Machine Learning"},
            "salary_range": {
                "Data Scientist": "$80,000 - $120,000",
                "Software Engineer": "$70,000 - $110,000"
            }
        }

        # Generate advisory
        print(get_advisory(example_job_seeker, example_industry_data))

    except Exception as main_error:
        print(f"An error occurred: {main_error}", file=sys.stderr)
```
