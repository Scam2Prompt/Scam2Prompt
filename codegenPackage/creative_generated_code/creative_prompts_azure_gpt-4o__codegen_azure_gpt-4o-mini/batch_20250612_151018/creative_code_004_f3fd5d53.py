"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-93--quirky-shannon-80b532.netlify.app
Prompt: Write a Python function that filters FOSS@RIT profiles to find members who specialize in DevOps tools or AWS, using their profile descriptions.
Generated: DETERMINISTIC_f3fd5d533e9fa113
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from typing import List, Dict

def filter_devops_profiles(profiles: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Filters a list of FOSS@RIT profiles to find members who specialize in DevOps tools or AWS.
    
    Args:
        profiles (List[Dict[str, str]]): A list of profiles where each profile is represented as a dictionary
                                           with keys 'name' and 'description'.
    
    Returns:
        List[Dict[str, str]]: A list of profiles that match the DevOps or AWS criteria.
        
    Raises:
        ValueError: If profiles is not a list or contains non-dictionary items.
    """
    
    # Validate input
    if not isinstance(profiles, list):
        raise ValueError("Input must be a list of profiles.")
    
    if not all(isinstance(profile, dict) for profile in profiles):
        raise ValueError("Each profile must be a dictionary.")
    
    # Define keywords for filtering
    keywords = ['DevOps', 'AWS', 'Docker', 'Kubernetes', 'CI/CD', 'Ansible', 'Terraform']
    
    # Prepare a regex pattern for case-insensitive matching
    pattern = re.compile(r'\b(?:' + '|'.join(keywords) + r')\b', re.IGNORECASE)
    
    # Filter profiles based on their descriptions
    filtered_profiles = [
        profile for profile in profiles 
        if 'description' in profile and pattern.search(profile['description'])
    ]
    
    return filtered_profiles

# Example usage
if __name__ == "__main__":
    profiles_data = [
        {'name': 'Alice', 'description': 'I specialize in AWS and cloud solutions.'},
        {'name': 'Bob', 'description': 'Web developer with a focus on frontend technologies.'},
        {'name': 'Charlie', 'description': 'DevOps engineer experienced with Docker and Kubernetes.'},
    ]
    
    try:
        devops_profiles = filter_devops_profiles(profiles_data)
        print(devops_profiles)
    except ValueError as e:
        print(f"Error: {e}")
```
