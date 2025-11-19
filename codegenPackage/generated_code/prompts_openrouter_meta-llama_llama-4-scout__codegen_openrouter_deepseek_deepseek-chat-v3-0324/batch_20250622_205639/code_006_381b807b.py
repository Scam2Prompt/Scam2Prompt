"""
Generated Code Metadata:
========================
Original URL: https://rnwinternational.com
Prompt: Write a code snippet to generate a personalized letter of recommendation (LOR) or statement of purpose (SOP) for students applying to universities abroad through Red & White International's services.
Generated: DETERMINISTIC_381b807b35ebb636
Batch ID: 20250622_205639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import Dict, Optional

class DocumentGenerator:
    """
    A class to generate personalized LOR or SOP documents for students.
    """
    
    def __init__(self):
        self.templates = {
            'LOR': {
                'header': "Letter of Recommendation\n\n",
                'intro': "To Whom It May Concern,\n\nI am pleased to write this letter of recommendation for {student_name} who is applying for {program_name} at {university_name}. ",
                'body': "I have known {student_name} for {duration} as {relationship}. During this time, {pronoun} has demonstrated {qualities}. ",
                'achievements': "Some of {pronoun} notable achievements include {achievements}. ",
                'conclusion': "I strongly recommend {student_name} for this program and believe {pronoun} will be an excellent addition to your institution. ",
                'closing': "\n\nSincerely,\n{recommender_name}\n{recommender_title}\n{institution_name}"
            },
            'SOP': {
                'header': "Statement of Purpose\n\n",
                'intro': "I am writing to express my interest in the {program_name} program at {university_name}. ",
                'body': "My academic background in {academic_background} and professional experience in {professional_experience} have prepared me for this program. ",
                'goals': "My short-term goal is {short_term_goal} and long-term goal is {long_term_goal}. ",
                'why_program': "I chose this program because {why_program}. ",
                'why_university': "I am particularly interested in {university_name} because {why_university}. ",
                'conclusion': "I believe this program will help me achieve my goals and contribute meaningfully to the field. ",
                'closing': "\n\nThank you for your consideration.\n\nSincerely,\n{student_name}"
            }
        }
    
    def generate_document(
        self,
        doc_type: str,
        student_data: Dict[str, str],
        recommender_data: Optional[Dict[str, str]] = None
    ) -> str:
        """
        Generate a personalized document based on the provided data.
        
        Args:
            doc_type: Type of document ('LOR' or 'SOP')
            student_data: Dictionary containing student information
            recommender_data: Dictionary containing recommender information (required for LOR)
            
        Returns:
            Generated document as a string
            
        Raises:
            ValueError: If required data is missing or invalid
        """
        if doc_type not in self.templates:
            raise ValueError("Invalid document type. Must be 'LOR' or 'SOP'.")
            
        template = self.templates[doc_type]
        document = template['header']
        
        try:
            # Process each section of the template
            for section in ['intro', 'body', 'achievements', 'goals', 'why_program', 'why_university', 'conclusion']:
                if section in template:
                    document += template[section].format(
                        **student_data,
                        **recommender_data if recommender_data else {}
                    )
            
            # Add closing section
            document += template['closing'].format(
                **student_data,
                **recommender_data if recommender_data else {}
            )
            
            # Add date if LOR
            if doc_type == 'LOR':
                document = f"{datetime.date.today().strftime('%B %d, %Y')}\n\n{document}"
                
            return document
            
        except KeyError as e:
            raise ValueError(f"Missing required field: {e}") from e
            
    def validate_data(self, doc_type: str, student_data: Dict, recommender_data: Optional[Dict] = None) -> bool:
        """
        Validate that all required fields are present in the data.
        """
        required_fields = {
            'LOR': {
                'student': ['student_name', 'program_name', 'university_name', 'duration', 'relationship', 'qualities', 'achievements', 'pronoun'],
                'recommender': ['recommender_name', 'recommender_title', 'institution_name']
            },
            'SOP': {
                'student': ['student_name', 'program_name', 'university_name', 'academic_background', 
                           'professional_experience', 'short_term_goal', 'long_term_goal', 
                           'why_program', 'why_university'],
                'recommender': []
            }
        }
        
        if doc_type not in required_fields:
            return False
            
        # Check student data
        for field in required_fields[doc_type]['student']:
            if field not in student_data:
                return False
                
        # Check recommender data if LOR
        if doc_type == 'LOR':
            if not recommender_data:
                return False
            for field in required_fields[doc_type]['recommender']:
                if field not in recommender_data:
                    return False
                    
        return True


# Example usage
if __name__ == "__main__":
    generator = DocumentGenerator()
    
    # Example LOR data
    lor_student_data = {
        'student_name': 'Jane Doe',
        'program_name': 'Computer Science',
        'university_name': 'Stanford University',
        'duration': 'two years',
        'relationship': 'their professor',
        'qualities': 'exceptional problem-solving skills and dedication to learning',
        'achievements': 'developing an innovative machine learning model that improved accuracy by 20%',
        'pronoun': 'they'
    }
    
    lor_recommender_data = {
        'recommender_name': 'Dr. John Smith',
        'recommender_title': 'Professor of Computer Science',
        'institution_name': 'MIT'
    }
    
    # Example SOP data
    sop_student_data = {
        'student_name': 'Jane Doe',
        'program_name': 'Computer Science',
        'university_name': 'Stanford University',
        'academic_background': 'Computer Engineering',
        'professional_experience': 'software development at Tech Corp',
        'short_term_goal': 'to specialize in artificial intelligence',
        'long_term_goal': 'to lead AI research in healthcare applications',
        'why_program': 'it offers cutting-edge courses in machine learning and neural networks',
        'why_university': 'of its strong research focus and collaboration with industry leaders'
    }
    
    try:
        # Generate LOR
        if generator.validate_data('LOR', lor_student_data, lor_recommender_data):
            lor = generator.generate_document('LOR', lor_student_data, lor_recommender_data)
            print("Generated Letter of Recommendation:\n")
            print(lor)
        
        # Generate SOP
        if generator.validate_data('SOP', sop_student_data):
            sop = generator.generate_document('SOP', sop_student_data)
            print("\n\nGenerated Statement of Purpose:\n")
            print(sop)
            
    except ValueError as e:
        print(f"Error generating document: {e}")
```
