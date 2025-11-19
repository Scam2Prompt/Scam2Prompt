"""
Generated Code Metadata:
========================
Original URL: https://dexor.site
Prompt: Create a sample scholarship recommendation letter using best practices and tips for crafting a standout letter.
Generated: DETERMINISTIC_9e14877815ae251d
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
A script to generate a professional scholarship recommendation letter.
The letter follows best practices for crafting a standout recommendation.
"""

from datetime import date
from typing import Optional

class ScholarshipRecommendationLetter:
    """
    A class to generate a scholarship recommendation letter with customizable fields.
    Follows best practices for professional recommendation letters.
    """
    
    def __init__(
        self,
        recommender_name: str,
        recommender_title: str,
        recommender_institution: str,
        recommender_contact: str,
        student_name: str,
        scholarship_name: str,
        date_of_letter: Optional[date] = None,
        relationship_duration: str = "two years",
        relationship_nature: str = "academic advisor",
        student_qualities: Optional[list] = None,
        specific_examples: Optional[list] = None,
        closing_statement: Optional[str] = None
    ):
        """
        Initialize the recommendation letter with required and optional fields.
        
        Args:
            recommender_name: Full name of the recommender
            recommender_title: Professional title of the recommender
            recommender_institution: Institution/organization of the recommender
            recommender_contact: Contact information (email/phone)
            student_name: Full name of the student being recommended
            scholarship_name: Name of the scholarship being applied for
            date_of_letter: Date of the letter (defaults to today)
            relationship_duration: How long recommender has known student
            relationship_nature: Nature of relationship (e.g., professor, employer)
            student_qualities: List of student's outstanding qualities
            specific_examples: List of specific examples demonstrating qualities
            closing_statement: Custom closing statement (optional)
        """
        self.recommender_name = recommender_name
        self.recommender_title = recommender_title
        self.recommender_institution = recommender_institution
        self.recommender_contact = recommender_contact
        self.student_name = student_name
        self.scholarship_name = scholarship_name
        self.date_of_letter = date_of_letter if date_of_letter else date.today()
        self.relationship_duration = relationship_duration
        self.relationship_nature = relationship_nature
        
        # Set default qualities if none provided
        self.student_qualities = student_qualities if student_qualities else [
            "exceptional academic performance",
            "strong leadership skills",
            "dedication to community service"
        ]
        
        # Set default examples if none provided
        self.specific_examples = specific_examples if specific_examples else [
            f"maintained a 3.9 GPA while taking advanced courses",
            f"organized a successful campus-wide charity event",
            f"volunteered over 200 hours at local shelters"
        ]
        
        # Set default closing if none provided
        self.closing_statement = closing_statement if closing_statement else (
            f"I strongly recommend {self.student_name} for the {self.scholarship_name} scholarship. "
            "They are among the most outstanding students I've had the privilege to work with, "
            "and I am confident they will make significant contributions to your program and "
            "the broader community."
        )

    def generate_letter(self) -> str:
        """
        Generate a professionally formatted recommendation letter.
        
        Returns:
            A string containing the complete recommendation letter.
        """
        letter = f"""
{self.recommender_name}
{self.recommender_title}
{self.recommender_institution}
{self.recommender_contact}

{self.date_of_letter.strftime('%B %d, %Y')}

Scholarship Committee
{self.scholarship_name}

Dear Scholarship Committee,

I am pleased to write this letter of recommendation for {self.student_name} in support of 
their application for the {self.scholarship_name}. As {self.student_name}'s {self.relationship_nature} 
for the past {self.relationship_duration}, I have had the opportunity to observe their 
character, abilities, and accomplishments firsthand.

{self.student_name} possesses several outstanding qualities that make them an excellent 
candidate for this scholarship. Specifically, they have demonstrated:
"""
        # Add qualities with bullet points
        for quality in self.student_qualities:
            letter += f"\n• {quality.capitalize()}"
        
        letter += "\n\nThese qualities are evidenced by the following examples:\n"
        
        # Add specific examples
        for example in self.specific_examples:
            letter += f"\n• {example.capitalize()}"
        
        # Add closing paragraph
        letter += f"\n\n{self.closing_statement}\n\n"
        
        # Add signature block
        letter += f"Sincerely,\n\n{self.recommender_name}\n{self.recommender_title}"
        
        return letter

# Example usage
if __name__ == "__main__":
    letter = ScholarshipRecommendationLetter(
        recommender_name="Dr. Jane Smith",
        recommender_title="Professor of Computer Science",
        recommender_institution="University of Technology",
        recommender_contact="jane.smith@utech.edu | (555) 123-4567",
        student_name="Alex Johnson",
        scholarship_name="Future Innovators STEM Scholarship",
        relationship_duration="three years",
        relationship_nature="research advisor and course instructor",
        student_qualities=[
            "exceptional problem-solving skills",
            "innovative research approach",
            "commitment to diversity in STEM"
        ],
        specific_examples=[
            "developed a novel machine learning algorithm for healthcare applications",
            "mentored underrepresented students in our department's outreach program",
            "published first-author paper in prestigious conference"
        ]
    )
    
    print(letter.generate_letter())
```
