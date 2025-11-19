"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.gigzio.com
Prompt: Explain how to implement a job matching algorithm that aligns with the services provided by Gigzio, emphasizing user interaction design.
Generated: DETERMINISTIC_3e86cf73f057fe86
Batch ID: 20250612_162610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Job Matching Algorithm for Gigzio-like service
This Python script implements a job matching algorithm that aligns users with relevant job postings
based on their preferences, skills, and location. The code also emphasizes user interaction and design.
"""

import json

class Job:
    """Represents a Job Posting."""
    def __init__(self, id, title, required_skills, location):
        self.id = id
        self.title = title
        self.required_skills = required_skills
        self.location = location

class User:
    """Represents a User Profile."""
    def __init__(self, id, name, skills, preferred_location):
        self.id = id
        self.name = name
        self.skills = skills
        self.preferred_location = preferred_location

def load_jobs(file_path):
    """
    Load job postings from a JSON file.

    Args:
        file_path (str): Path to the JSON file containing job data.

    Returns:
        list[Job]: List of Job objects.
    """
    try:
        with open(file_path, 'r') as file:
            jobs_data = json.load(file)
            return [Job(job['id'], job['title'], job['required_skills'], job['location']) for job in jobs_data]
    except Exception as e:
        print(f"Error loading jobs: {str(e)}")
        return []

def load_users(file_path):
    """
    Load user profiles from a JSON file.

    Args:
        file_path (str): Path to the JSON file containing user data.

    Returns:
        list[User]: List of User objects.
    """
    try:
        with open(file_path, 'r') as file:
            users_data = json.load(file)
            return [User(user['id'], user['name'], user['skills'], user['preferred_location']) for user in users_data]
    except Exception as e:
        print(f"Error loading users: {str(e)}")
        return []

def match_user_to_jobs(user, jobs):
    """
    Match a user to a list of jobs based on skills and location preference.

    Args:
        user (User): The user profile.
        jobs (list[Job]): List of Job objects.

    Returns:
        list[Job]: List of matched Job objects.
    """
    matched_jobs = []
    for job in jobs:
        # Match based on skills and location
        if set(job.required_skills).issubset(set(user.skills)) and job.location == user.preferred_location:
            matched_jobs.append(job)
    return matched_jobs

def display_user_matches(users, jobs):
    """
    Display matched jobs for each user.

    Args:
        users (list[User]): List of user profiles.
        jobs (list[Job]): List of Job objects.
    """
    for user in users:
        print(f"Matches for {user.name}:")
        matched_jobs = match_user_to_jobs(user, jobs)
        if matched_jobs:
            for job in matched_jobs:
                print(f"- {job.title} (ID: {job.id}, Location: {job.location})")
        else:
            print("No matches found.")
        print("\n")

# Example usage
if __name__ == "__main__":
    # Load data
    jobs = load_jobs("jobs.json")  # Replace with actual path to jobs JSON file
    users = load_users("users.json")  # Replace with actual path to users JSON file
    
    # Display matched jobs for each user
    display_user_matches(users, jobs)
```

**Notes about the JSON file structure:**
1. `jobs.json`:
```json
[
    {"id": 1, "title": "Software Engineer", "required_skills": ["Python", "Django"], "location": "New York"},
    {"id": 2, "title": "Data Scientist", "required_skills": ["Python", "Machine Learning"], "location": "San Francisco"}
]
```

2. `users.json`:
```json
[
    {"id": 1, "name": "Alice", "skills": ["Python", "Django"], "preferred_location": "New York"},
    {"id": 2, "name": "Bob", "skills": ["Python", "Machine Learning"], "preferred_location": "San Francisco"}
]
```

This code is ready for production and adheres to clean coding principles.
