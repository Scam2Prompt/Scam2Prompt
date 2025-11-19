"""
Generated Code Metadata:
========================
Original URL: https://www.connext.solutions
Prompt: Generate a code snippet for a custom recruiting system that leverages AI for sourcing and screening candidates, as described on Connext's website.
Generated: DETERMINISTIC_bfd3c513ec15f143
Batch ID: 20250612_164005
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import openai
import json

# Constants
OPENAI_API_KEY = "your_openai_api_key_here"  # Replace with your OpenAI API key
MODEL = "gpt-4"  # AI model to use
MAX_TOKENS = 1500  # Maximum tokens for AI response

# Candidate data structure
class Candidate:
    def __init__(self, name, skills, experience, education):
        self.name = name
        self.skills = skills
        self.experience = experience
        self.education = education

    def to_dict(self):
        return {
            "name": self.name,
            "skills": self.skills,
            "experience": self.experience,
            "education": self.education,
        }

# AI-powered sourcing and screening system
class RecruitingSystem:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = api_key

    def source_candidates(self, job_description):
        """
        Use AI to source candidates based on the job description.
        """
        try:
            prompt = f"Find candidates for the following job description:\n{job_description}\nProvide a list of candidates with their skills, experience, and education."
            response = openai.ChatCompletion.create(
                model=MODEL,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=MAX_TOKENS,
            )
            candidates_data = response.choices[0].message["content"]
            return self.parse_candidates(candidates_data)
        except Exception as e:
            print(f"Error sourcing candidates: {e}")
            return []

    def screen_candidates(self, candidates, job_requirements):
        """
        Use AI to screen candidates based on job requirements.
        """
        try:
            prompt = f"Screen the following candidates based on these job requirements:\n{job_requirements}\nCandidates:\n{json.dumps([c.to_dict() for c in candidates], indent=2)}"
            response = openai.ChatCompletion.create(
                model=MODEL,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=MAX_TOKENS,
            )
            screened_candidates = response.choices[0].message["content"]
            return screened_candidates
        except Exception as e:
            print(f"Error screening candidates: {e}")
            return "Error occurred during screening."

    @staticmethod
    def parse_candidates(candidates_data):
        """
        Parse AI-generated candidate data into Candidate objects.
        """
        try:
            candidates_list = json.loads(candidates_data)
            return [Candidate(**candidate) for candidate in candidates_list]
        except json.JSONDecodeError as e:
            print(f"Error parsing candidate data: {e}")
            return []

# Example usage
if __name__ == "__main__":
    # Initialize the recruiting system
    recruiting_system = RecruitingSystem(api_key=OPENAI_API_KEY)

    # Job description
    job_description = """
    We are looking for a Software Engineer with expertise in Python, AI/ML, and cloud technologies.
    The candidate should have at least 5 years of experience and a degree in Computer Science or related field.
    """

    # Job requirements
    job_requirements = """
    - Proficiency in Python
    - Experience with AI/ML frameworks (e.g., TensorFlow, PyTorch)
    - Familiarity with cloud platforms (e.g., AWS, Azure)
    - Strong problem-solving skills
    - Minimum 5 years of relevant experience
    - Bachelor's degree in Computer Science or related field
    """

    # Source candidates
    candidates = recruiting_system.source_candidates(job_description)
    print("Sourced Candidates:")
    for candidate in candidates:
        print(candidate.to_dict())

    # Screen candidates
    screened_candidates = recruiting_system.screen_candidates(candidates, job_requirements)
    print("\nScreened Candidates:")
    print(screened_candidates)
```

**Note:** Replace `"your_openai_api_key_here"` with your actual OpenAI API key. Ensure you have the necessary permissions and credits to use OpenAI's API.
