"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proofoftalk.pages.dev
Prompt: Generate a detailed report template that mimics the 10-page evaluation report provided to participants in the Proof of Pitch competition.
Generated: DETERMINISTIC_28d5167cfabc30a0
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from fpdf import FPDF

class EvaluationReport(FPDF):
    def __init__(self, title="Evaluation Report", participant_name="Participant Name"):
        super().__init__()
        self.title = title
        self.participant_name = participant_name
        self.set_auto_page_break(auto=True, margin=15)
    
    def header(self):
        """
        Header for each page of the evaluation report.
        Includes a title and a horizontal line.
        """
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, self.title, border=0, ln=1, align="C")
        self.ln(5)
        self.set_draw_color(0, 0, 0)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(5)

    def footer(self):
        """
        Footer for each page of the evaluation report.
        Includes a page number at the bottom of the page.
        """
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def add_section(self, section_title, content):
        """
        Add a new section to the report.

        :param section_title: Title of the section
        :param content: Body text for the section
        """
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, section_title, ln=1)
        self.ln(5)
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 10, content)
        self.ln(5)

    def generate_report(self, filename="evaluation_report.pdf"):
        """
        Generate and save the evaluation report.

        :param filename: Name of the PDF file to be generated
        """
        try:
            # Start the report creation process
            self.add_page()

            # Title Section
            self.set_font("Arial", "B", 16)
            self.cell(0, 10, self.title, ln=1, align="C")
            self.ln(10)
            self.set_font("Arial", "", 12)
            self.cell(0, 10, f"Participant: {self.participant_name}", ln=1, align="L")
            self.ln(10)

            # Add sections mimicking the 10-page evaluation report
            sections = [
                ("Introduction", "This section provides an overview of the competition goals, evaluation criteria, and participant expectations."),
                ("Pitch Summary", "Detailed summary of the pitch including key points, objectives, and outcomes."),
                ("Strengths", "Analysis of the strengths and highlights of the pitch."),
                ("Areas for Improvement", "Constructive feedback on areas that could be improved further."),
                ("Market Analysis", "Evaluation of the market viability and potential of the proposed idea."),
                ("Financial Feasibility", "Review of the financial aspects, including budget and projections."),
                ("Team Evaluation", "Assessment of the team structure, skills, and collaboration demonstrated."),
                ("Innovation", "Scoring and analysis of the uniqueness and innovation of the pitch."),
                ("Overall Score", "Aggregated scoring based on evaluation criteria."),
                ("Conclusion", "Final remarks and recommendations.")
            ]

            for section_title, content in sections:
                self.add_section(section_title, content)

            # Save the report to a file
            self.output(filename)
            print(f"Report successfully generated: {filename}")
        except Exception as e:
            print(f"An error occurred while generating the report: {e}")

# Example usage:
if __name__ == "__main__":
    # Create an instance of the EvaluationReport with sample data
    report = EvaluationReport(
        title="Proof of Pitch Evaluation Report",
        participant_name="John Doe"
    )
    # Generate the report
    report.generate_report("proof_of_pitch_evaluation_report.pdf")
```

**Dependencies:** Ensure you have the `fpdf` library installed before running this code. You can install it using `pip install fpdf`.
