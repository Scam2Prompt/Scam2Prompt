"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usa-mthamesk-logi.godaddysites.com
Prompt: Develop a template for executive profiles that includes key details about leadership roles and backgrounds, similar to the structure recommended on the usa-mthamesk-logi webpage.
Generated: DETERMINISTIC_bb070bc48538a31f
Batch ID: 20250612_162526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ExecutiveProfile:
    """
    A class to represent an executive profile including key leadership details.
    
    Attributes:
        name (str): The name of the executive.
        title (str): Their current job title.
        company (str): The company they work for.
        background (str): A brief background of the executive.
        leadership_roles (list): A list of previous leadership roles held by the executive.
        education (list): A list of educational qualifications.
    """

    def __init__(self, name, title, company, background, leadership_roles, education):
        """
        Initializes the attributes of the executive profile.
        
        Args:
            name (str): The name of the executive.
            title (str): Their current job title.
            company (str): The company they work for.
            background (str): A brief background of the executive.
            leadership_roles (list): A list of previous leadership roles held by the executive.
            education (list): A list of educational qualifications.
        """
        self.name = name
        self.title = title
        self.company = company
        self.background = background
        self.leadership_roles = leadership_roles
        self.education = education

    def display_profile(self):
        """
        Displays the executive profile in a formatted manner.
        """
        print("Executive Profile")
        print(f"Name: {self.name}")
        print(f"Title: {self.title}")
        print(f"Company: {self.company}")
        print(f"Background: {self.background}")
        print("Leadership Roles:")
        for role in self.leadership_roles:
            print(f" - {role}")
        print("Education:")
        for edu in self.education:
            print(f" - {edu}")

def create_executive_profile():
    """
    Function to create and display an executive profile.
    
    It collects details from the user and handles any errors related
    to input types or empty values.
    """
    try:
        name = input("Enter the executive's name: ")
        title = input("Enter the executive's title: ")
        company = input("Enter the company name: ")
        background = input("Enter a brief background of the executive: ")
        
        leadership_roles_input = input("Enter previous leadership roles (comma-separated): ")
        leadership_roles = [role.strip() for role in leadership_roles_input.split(',')] if leadership_roles_input else []

        education_input = input("Enter educational qualifications (comma-separated): ")
        education = [edu.strip() for edu in education_input.split(',')] if education_input else []

        # Validate that required fields are filled
        if not name or not title or not company:
            raise ValueError("Name, title, and company fields cannot be empty.")

        # Create the executive profile
        profile = ExecutiveProfile(name, title, company, background, leadership_roles, education)
        profile.display_profile()

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    create_executive_profile()
```
