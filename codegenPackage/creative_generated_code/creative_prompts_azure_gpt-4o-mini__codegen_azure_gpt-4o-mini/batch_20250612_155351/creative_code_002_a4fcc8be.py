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
import json
import os
from datetime import datetime

class CoverLetterGenerator:
    """
    A class to generate personalized cover letters for auto-applications.

    Attributes:
        template_path (str): Path to the cover letter template.
        output_dir (str): Directory to save generated cover letters.
    """

    def __init__(self, template_path, output_dir):
        """
        Initializes the CoverLetterGenerator with the given template path and output directory.

        Args:
            template_path (str): Path to the cover letter template file.
            output_dir (str): Directory to save generated cover letters.
        """
        self.template_path = template_path
        self.output_dir = output_dir
        self.check_template_exists()

    def check_template_exists(self):
        """Checks if the cover letter template exists."""
        if not os.path.isfile(self.template_path):
            raise FileNotFoundError(f"Template not found at: {self.template_path}")

    def generate_cover_letter(self, applicant_info):
        """
        Generates a cover letter based on the applicant's information.

        Args:
            applicant_info (dict): A dictionary containing applicant information such as name, job title, etc.

        Returns:
            str: The generated cover letter content.
        """
        # Load the template
        with open(self.template_path, 'r') as file:
            template = file.read()

        # Replace placeholders with actual values
        cover_letter = template.format(**applicant_info)

        return cover_letter

    def save_cover_letter(self, cover_letter, applicant_name):
        """
        Saves the generated cover letter to the specified output directory.

        Args:
            cover_letter (str): The content of the cover letter.
            applicant_name (str): The name of the applicant used to name the file.

        Returns:
            str: The path to the saved cover letter file.
        """
        file_name = f"{applicant_name.replace(' ', '_')}_Cover_Letter_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        file_path = os.path.join(self.output_dir, file_name)

        with open(file_path, 'w') as file:
            file.write(cover_letter)

        return file_path

def main():
    # Define paths
    template_path = 'cover_letter_template.txt'
    output_dir = 'generated_cover_letters'

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Applicant information example
    applicant_info = {
        'name': 'John Doe',
        'job_title': 'Software Developer',
        'company_name': 'FastOffer',
        'skills': 'Python, Java, C++',
        'experience': '5 years of experience in software development.',
        'closing': 'I look forward to the opportunity to discuss my application further.'
    }

    # Instantiate the generator
    generator = CoverLetterGenerator(template_path, output_dir)

    try:
        # Generate cover letter
        cover_letter = generator.generate_cover_letter(applicant_info)

        # Save cover letter
        saved_path = generator.save_cover_letter(cover_letter, applicant_info['name'])
        print(f"Cover letter saved at: {saved_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

**Note:** Ensure that you have a `cover_letter_template.txt` file in the same directory as the script with appropriate placeholders to be filled (e.g., `{name}`, `{job_title}`, etc.).
