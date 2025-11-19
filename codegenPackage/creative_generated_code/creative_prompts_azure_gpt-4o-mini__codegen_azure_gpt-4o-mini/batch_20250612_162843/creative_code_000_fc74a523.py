"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://armourersandbrasiers.co.uk
Prompt: Generate a Python script that utilizes the Armourers & Brasiers' Gauntlet Trust's funding criteria to evaluate potential grant applications for educational projects in Materials Science.
Generated: DETERMINISTIC_fc74a52392147b9e
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GrantApplication:
    """
    Class representing a grant application for educational projects in Materials Science.
    """
    
    def __init__(self, applicant_name, project_title, project_description, funding_amount, project_duration):
        """
        Initializes a new GrantApplication instance.
        
        :param applicant_name: Name of the applicant
        :param project_title: Title of the project
        :param project_description: Description of the project
        :param funding_amount: Amount of funding requested
        :param project_duration: Duration of the project in months
        """
        self.applicant_name = applicant_name
        self.project_title = project_title
        self.project_description = project_description
        self.funding_amount = funding_amount
        self.project_duration = project_duration

    def is_valid(self):
        """
        Validates the grant application based on Armourers & Brasiers' Gauntlet Trust funding criteria.
        
        :return: True if valid, False otherwise
        """
        return (self.funding_amount <= 50000 and  # Maximum funding limit
                self.project_duration <= 24 and  # Maximum project duration
                len(self.project_description) > 50)  # Project description must be sufficient

def evaluate_applications(applications):
    """
    Evaluates a list of grant applications.
    
    :param applications: List of GrantApplication instances
    :return: List of valid applications
    """
    valid_applications = []
    
    for app in applications:
        if app.is_valid():
            valid_applications.append(app)
            logging.info(f"Application '{app.project_title}' by '{app.applicant_name}' is valid.")
        else:
            logging.warning(f"Application '{app.project_title}' by '{app.applicant_name}' is invalid.")
    
    return valid_applications

def load_applications_from_json(file_path):
    """
    Loads grant applications from a JSON file.
    
    :param file_path: Path to the JSON file
    :return: List of GrantApplication instances
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            applications = [GrantApplication(**item) for item in data]
            return applications
    except FileNotFoundError:
        logging.error(f"File '{file_path}' not found.")
        return []
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON from file '{file_path}'.")
        return []
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return []

def main():
    """
    Main function to load applications and evaluate them.
    """
    applications = load_applications_from_json('grant_applications.json')
    valid_applications = evaluate_applications(applications)
    
    logging.info(f"Total valid applications: {len(valid_applications)}")

if __name__ == "__main__":
    main()
```

In the provided script, ensure that the `grant_applications.json` file exists in the same directory as the script and is formatted correctly to match the expected structure for the `GrantApplication` class.
