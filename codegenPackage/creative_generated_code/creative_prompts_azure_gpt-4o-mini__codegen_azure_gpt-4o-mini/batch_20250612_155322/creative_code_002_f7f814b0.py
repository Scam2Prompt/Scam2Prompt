"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rnwinternational.com
Prompt: Generate a sample Statement of Purpose (SOP) for a student applying to study abroad, incorporating tips from RNW International's SOP writing services.
Generated: DETERMINISTIC_f7f814b01c154ef5
Batch ID: 20250612_155322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StatementOfPurpose:
    """
    A class to generate a Statement of Purpose (SOP) for students applying to study abroad.
    
    Attributes:
        name (str): The name of the student.
        program (str): The program the student is applying for.
        university (str): The university the student is applying to.
        background (str): A brief background of the student.
        goals (str): The academic and career goals of the student.
        motivations (str): Reasons for choosing the specific program and university.
    """

    def __init__(self, name, program, university, background, goals, motivations):
        """
        Initializes the Statement of Purpose with student details.
        
        Parameters:
            name (str): Student's name.
            program (str): Program of study.
            university (str): Name of the university.
            background (str): Student's background.
            goals (str): Student's academic and career goals.
            motivations (str): Student's motivations for applying.
        """
        self.name = name
        self.program = program
        self.university = university
        self.background = background
        self.goals = goals
        self.motivations = motivations

    def generate_sop(self):
        """
        Generates the Statement of Purpose based on the provided attributes.
        
        Returns:
            str: Formatted Statement of Purpose.
        """
        try:
            sop = f"""
            Statement of Purpose

            Name: {self.name}
            Program: {self.program}
            University: {self.university}

            Background:
            {self.background}

            Academic and Career Goals:
            {self.goals}

            Motivations for Choosing This Program:
            {self.motivations}
            """
            return sop.strip()  # Remove leading/trailing whitespace
        except Exception as e:
            return f"An error occurred while generating the SOP: {str(e)}"

# Example usage
if __name__ == "__main__":
    try:
        # Sample data for the SOP
        student_name = "John Doe"
        program_of_study = "Master of Science in Computer Science"
        university_name = "ABC University"
        student_background = "I have completed my Bachelor's degree in Computer Science with a focus on software development."
        academic_goals = "I aim to specialize in artificial intelligence and contribute to innovative projects."
        motivations = "I am drawn to ABC University due to its cutting-edge research in AI and its collaborative environment."

        # Create an instance of StatementOfPurpose
        sop_generator = StatementOfPurpose(
            name=student_name,
            program=program_of_study,
            university=university_name,
            background=student_background,
            goals=academic_goals,
            motivations=motivations
        )

        # Generate and print the SOP
        print(sop_generator.generate_sop())
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
