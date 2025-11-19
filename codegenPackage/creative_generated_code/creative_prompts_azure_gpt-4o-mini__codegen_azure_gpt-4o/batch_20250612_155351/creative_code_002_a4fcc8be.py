"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fast-offer.online
Prompt: What are the steps to set up personalized cover letters for auto-applications using FastOffer?
Generated: DETERMINISTIC_a4fcc8be63014e4c
Batch ID: 20250612_155351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json

# Constants
TEMPLATE_FILE = "cover_letter_template.txt"
OUTPUT_DIRECTORY = "generated_cover_letters"
PROFILE_DATA_FILE = "profiles.json"

def load_template(file_path):
    """
    Load the cover letter template from a file.

    :param file_path: Path to the template file
    :return: Template string
    :raises FileNotFoundError: If the template file is not found
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Template file '{file_path}' does not exist.")
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def load_profiles(file_path):
    """
    Load user profiles from a JSON file.

    :param file_path: Path to the JSON file containing profiles
    :return: List of profiles
    :raises FileNotFoundError: If the profiles file is not found
    :raises ValueError: If the profiles file contains invalid JSON
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Profiles file '{file_path}' does not exist.")
    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in profiles file: {e}")

def generate_cover_letter(template, profile):
    """
    Generate a personalized cover letter using the template and profile.

    :param template: Cover letter template string
    :param profile: Dictionary containing profile data
    :return: Personalized cover letter
    """
    try:
        return template.format(**profile)
    except KeyError as e:
        raise ValueError(f"Missing placeholder in profile data: {e}")

def save_cover_letter(content, file_name):
    """
    Save the generated cover letter to a file.

    :param content: Cover letter content
    :param file_name: Name of the output file
    """
    if not os.path.exists(OUTPUT_DIRECTORY):
        os.makedirs(OUTPUT_DIRECTORY)
    output_path = os.path.join(OUTPUT_DIRECTORY, file_name)
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(content)

def main():
    """
    Main function to generate personalized cover letters using profiles.
    """
    try:
        # Load the template
        template = load_template(TEMPLATE_FILE)
        
        # Load profiles
        profiles = load_profiles(PROFILE_DATA_FILE)
        
        # Generate and save cover letters for each profile
        for profile in profiles:
            try:
                cover_letter = generate_cover_letter(template, profile)
                file_name = f"{profile.get('name', 'unknown')}_cover_letter.txt"
                save_cover_letter(cover_letter, file_name)
                print(f"Cover letter generated for {profile.get('name', 'unknown')}")
            except ValueError as e:
                print(f"Error generating cover letter for profile: {e}")
    except FileNotFoundError as e:
        print(f"Setup error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

### Notes on Usage:
1. **Template File (`cover_letter_template.txt`)**: This should contain placeholders formatted like `{name}`, `{position}`, `{company}`, etc.
2. **Profiles File (`profiles.json`)**: This should contain an array of JSON objects where each object represents a user profile, e.g., `{"name": "John Doe", "position": "Software Engineer", "company": "TechCorp"}`.
3. You need to ensure both files exist in the same directory as the script before running the code.
