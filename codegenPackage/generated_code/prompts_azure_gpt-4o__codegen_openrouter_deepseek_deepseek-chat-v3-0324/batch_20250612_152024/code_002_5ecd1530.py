"""
Generated Code Metadata:
========================
Original URL: https://rnwinternational.com
Prompt: Generate code to automate the creation of SOPs and resumes for study abroad applications, referencing the SOP writing services mentioned by RNW International.
Generated: DETERMINISTIC_5ecd15300abd919f
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from datetime import datetime
from typing import Dict, List, Optional

class SOPGenerator:
    """
    A class to generate Statements of Purpose (SOP) for study abroad applications.
    """
    
    def __init__(self, template_path: str = "sop_template.txt"):
        """
        Initialize the SOP generator with a template file.
        
        Args:
            template_path (str): Path to the SOP template file.
        """
        self.template_path = template_path
        self.template = self._load_template()
        
    def _load_template(self) -> str:
        """
        Load the SOP template from file.
        
        Returns:
            str: The template content.
            
        Raises:
            FileNotFoundError: If template file doesn't exist.
        """
        try:
            with open(self.template_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"SOP template file not found at {self.template_path}")
    
    def generate_sop(self, user_data: Dict[str, str], output_path: Optional[str] = None) -> str:
        """
        Generate an SOP by filling in the template with user data.
        
        Args:
            user_data (Dict[str, str]): Dictionary containing user information.
            output_path (Optional[str]): Path to save the generated SOP. If None, returns the content.
            
        Returns:
            str: The generated SOP content if output_path is None, otherwise empty string.
            
        Raises:
            ValueError: If required fields are missing in user_data.
        """
        required_fields = ['name', 'program', 'university', 'background', 'goals']
        for field in required_fields:
            if field not in user_data:
                raise ValueError(f"Missing required field: {field}")
        
        sop_content = self.template.format(
            name=user_data['name'],
            program=user_data['program'],
            university=user_data['university'],
            background=user_data['background'],
            goals=user_data['goals'],
            date=datetime.now().strftime("%B %d, %Y")
        )
        
        if output_path:
            self._save_sop(sop_content, output_path)
            return ""
        return sop_content
    
    def _save_sop(self, content: str, output_path: str) -> None:
        """
        Save the generated SOP to a file.
        
        Args:
            content (str): The SOP content to save.
            output_path (str): Path to save the file.
            
        Raises:
            IOError: If there's an issue writing the file.
        """
        try:
            with open(output_path, 'w') as file:
                file.write(content)
        except IOError as e:
            raise IOError(f"Failed to save SOP: {str(e)}")

class ResumeGenerator:
    """
    A class to generate resumes for study abroad applications.
    """
    
    def __init__(self, template_path: str = "resume_template.json"):
        """
        Initialize the resume generator with a template file.
        
        Args:
            template_path (str): Path to the resume template file.
        """
        self.template_path = template_path
        self.template = self._load_template()
        
    def _load_template(self) -> Dict:
        """
        Load the resume template from JSON file.
        
        Returns:
            Dict: The template content.
            
        Raises:
            FileNotFoundError: If template file doesn't exist.
            json.JSONDecodeError: If template is not valid JSON.
        """
        try:
            with open(self.template_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Resume template file not found at {self.template_path}")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in template: {str(e)}", e.doc, e.pos)
    
    def generate_resume(self, user_data: Dict[str, str], output_path: Optional[str] = None) -> Dict:
        """
        Generate a resume by filling in the template with user data.
        
        Args:
            user_data (Dict[str, str]): Dictionary containing user information.
            output_path (Optional[str]): Path to save the generated resume. If None, returns the content.
            
        Returns:
            Dict: The generated resume content if output_path is None, otherwise empty dict.
            
        Raises:
            ValueError: If required fields are missing in user_data.
        """
        required_fields = ['name', 'email', 'education', 'experience', 'skills']
        for field in required_fields:
            if field not in user_data:
                raise ValueError(f"Missing required field: {field}")
        
        resume_content = self.template.copy()
        resume_content.update({
            "personal_info": {
                "name": user_data['name'],
                "email": user_data['email'],
                "phone": user_data.get('phone', ''),
                "address": user_data.get('address', '')
            },
            "education": user_data['education'],
            "experience": user_data['experience'],
            "skills": user_data['skills'],
            "last_updated": datetime.now().strftime("%Y-%m-%d")
        })
        
        if output_path:
            self._save_resume(resume_content, output_path)
            return {}
        return resume_content
    
    def _save_resume(self, content: Dict, output_path: str) -> None:
        """
        Save the generated resume to a JSON file.
        
        Args:
            content (Dict): The resume content to save.
            output_path (str): Path to save the file.
            
        Raises:
            IOError: If there's an issue writing the file.
        """
        try:
            with open(output_path, 'w') as file:
                json.dump(content, file, indent=2)
        except IOError as e:
            raise IOError(f"Failed to save resume: {str(e)}")

class StudyAbroadApplication:
    """
    Main class to handle study abroad application document generation.
    """
    
    def __init__(self):
        self.sop_generator = SOPGenerator()
        self.resume_generator = ResumeGenerator()
    
    def generate_application(self, user_data: Dict[str, str], output_dir: str = "output") -> None:
        """
        Generate all required documents for study abroad application.
        
        Args:
            user_data (Dict[str, str]): Dictionary containing user information.
            output_dir (str): Directory to save generated documents.
            
        Raises:
            ValueError: If user data is invalid.
            OSError: If output directory cannot be created.
        """
        try:
            os.makedirs(output_dir, exist_ok=True)
            
            # Generate SOP
            sop_path = os.path.join(output_dir, f"{user_data['name'].replace(' ', '_')}_sop.txt")
            self.sop_generator.generate_sop(user_data, sop_path)
            
            # Generate Resume
            resume_path = os.path.join(output_dir, f"{user_data['name'].replace(' ', '_')}_resume.json")
            self.resume_generator.generate_resume(user_data, resume_path)
            
        except ValueError as e:
            raise ValueError(f"Invalid user data: {str(e)}")
        except OSError as e:
            raise OSError(f"Failed to create output directory: {str(e)}")
        except Exception as e:
            raise Exception(f"Failed to generate application: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Sample user data
    user_data = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "+1234567890",
        "program": "Computer Science",
        "university": "Stanford University",
        "background": "Bachelor's in Software Engineering with 2 years of work experience.",
        "goals": "To specialize in AI and contribute to cutting-edge research.",
        "education": [
            {
                "degree": "BSc Software Engineering",
                "institution": "Tech University",
                "year": "2020"
            }
        ],
        "experience": [
            {
                "position": "Software Developer",
                "company": "Tech Corp",
                "duration": "2020-2022",
                "description": "Developed web applications using Python and Django."
            }
        ],
        "skills": ["Python", "Machine Learning", "Django", "SQL"]
    }
    
    try:
        app = StudyAbroadApplication()
        app.generate_application(user_data)
        print("Application documents generated successfully!")
    except Exception as e:
        print(f"Error: {str(e)}")
```
