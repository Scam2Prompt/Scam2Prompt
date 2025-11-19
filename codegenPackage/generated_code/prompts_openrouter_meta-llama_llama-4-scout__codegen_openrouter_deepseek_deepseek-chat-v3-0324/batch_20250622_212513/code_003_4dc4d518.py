"""
Generated Code Metadata:
========================
Original URL: https://www.gigzio.com
Prompt: Create a sales pitch for a startup job seeker using Gigzio's platform, highlighting the benefits of job matching and career alignment.
Generated: DETERMINISTIC_4dc4d51802cf2844
Batch ID: 20250622_212513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def generate_sales_pitch(name: str, job_title: str, skills: list) -> str:
    """
    Generate a personalized sales pitch for a job seeker using Gigzio's platform.
    
    Args:
        name (str): The job seeker's name
        job_title (str): Their desired job title/role
        skills (list): List of their key skills
    
    Returns:
        str: Personalized sales pitch highlighting Gigzio's benefits
    """
    
    # Input validation
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Name must be a non-empty string")
    if not isinstance(job_title, str) or not job_title.strip():
        raise ValueError("Job title must be a non-empty string")
    if not isinstance(skills, list) or not all(isinstance(skill, str) for skill in skills):
        raise ValueError("Skills must be a list of strings")
    
    skills_str = ", ".join(skills[:-1]) + f", and {skills[-1]}" if len(skills) > 1 else skills[0]
    
    pitch = f"""
    Hi {name},
    
    Are you tired of endlessly scrolling through job boards that don't understand your unique skills in {skills_str}? 
    Gigzio's AI-powered platform matches you with opportunities that truly align with your expertise as a {job_title}.
    
    Here's what we offer:
    - Smart Matching: Our algorithm analyzes your profile to connect you with roles that fit both your skills AND career goals
    - Time Savings: No more manual applications - we surface the right opportunities automatically
    - Career Growth: We prioritize positions that will help you progress toward your long-term aspirations
    - Personalized Support: Get tailored advice to help you stand out in your {job_title} job search
    
    With Gigzio, you're not just finding a job - you're finding the right next step in your career journey.
    
    Ready to transform your job search? Let's get started!
    """
    
    return pitch.strip()

# Example usage
try:
    example_pitch = generate_sales_pitch(
        name="Alex",
        job_title="Senior Data Scientist",
        skills=["machine learning", "data visualization", "statistical modeling"]
    )
    print(example_pitch)
except ValueError as e:
    print(f"Error generating pitch: {e}")
```
