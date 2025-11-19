"""
Generated Code Metadata:
========================
Original URL: https://freejobsindubai.com
Prompt: Write a code snippet for a chatbot that assists users in finding suitable jobs in Dubai, UAE, based on their skills and experience, considering various job categories like Engineering, Hotel, or Hospital jobs.
Generated: DETERMINISTIC_51648ada596c034c
Batch ID: 20250622_212358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random

class Job:
    """Class representing a job listing."""
    def __init__(self, title, category, skills_required, experience_required):
        self.title = title
        self.category = category
        self.skills_required = skills_required
        self.experience_required = experience_required

    def to_dict(self):
        """Convert job to dictionary for easy JSON serialization."""
        return {
            "title": self.title,
            "category": self.category,
            "skills_required": self.skills_required,
            "experience_required": self.experience_required
        }

class JobChatbot:
    """Chatbot for assisting users in finding jobs."""
    def __init__(self):
        self.jobs = self.load_jobs()

    def load_jobs(self):
        """Load job listings from a JSON file."""
        try:
            with open('jobs.json', 'r') as file:
                jobs_data = json.load(file)
                return [Job(**job) for job in jobs_data]
        except FileNotFoundError:
            print("Error: jobs.json file not found.")
            return []
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON from jobs.json.")
            return []

    def find_jobs(self, skills, experience):
        """Find suitable jobs based on user skills and experience."""
        suitable_jobs = []
        for job in self.jobs:
            if (set(job.skills_required).issubset(set(skills)) and
                experience >= job.experience_required):
                suitable_jobs.append(job)
        return suitable_jobs

    def chat(self):
        """Start the chatbot interaction."""
        print("Welcome to the Job Finder Chatbot!")
        skills = input("Please enter your skills (comma-separated): ").split(',')
        skills = [skill.strip() for skill in skills]
        experience = input("Please enter your years of experience: ")

        try:
            experience = int(experience)
        except ValueError:
            print("Error: Please enter a valid number for years of experience.")
            return

        suitable_jobs = self.find_jobs(skills, experience)

        if suitable_jobs:
            print("\nHere are some suitable jobs for you:")
            for job in suitable_jobs:
                print(f"- {job.title} ({job.category})")
        else:
            print("Sorry, no suitable jobs found for your skills and experience.")

if __name__ == "__main__":
    chatbot = JobChatbot()
    chatbot.chat()
```

**Note:** Ensure you have a `jobs.json` file in the same directory with the following structure for the code to work:

```json
[
    {
        "title": "Software Engineer",
        "category": "Engineering",
        "skills_required": ["Python", "Django"],
        "experience_required": 2
    },
    {
        "title": "Hotel Manager",
        "category": "Hotel",
        "skills_required": ["Management", "Customer Service"],
        "experience_required": 3
    },
    {
        "title": "Nurse",
        "category": "Hospital",
        "skills_required": ["Patient Care", "Communication"],
        "experience_required": 1
    }
]
```
