"""
Generated Code Metadata:
========================
Original URL: https://proofoftalk.pages.dev
Prompt: Generate a detailed report template that mimics the 10-page evaluation report provided to participants in the Proof of Pitch competition.
Generated: DETERMINISTIC_28d5167cfabc30a0
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from fpdf import FPDF

class EvaluationReport(FPDF):
    def __init__(self, participant_name, competition_name, evaluation_data):
        super().__init__()
        self.participant_name = participant_name
        self.competition_name = competition_name
        self.evaluation_data = evaluation_data
        self.set_auto_page_break(auto=True, margin=15)
        self.add_page()
        self.set_font("Arial", size=12)

    def header(self):
        """Header for each page."""
        self.set_font("Arial", style="B", size=14)
        self.cell(0, 10, f"{self.competition_name} Evaluation Report", border=False, ln=True, align="C")
        self.ln(10)

    def footer(self):
        """Footer for each page."""
        self.set_y(-15)
        self.set_font("Arial", size=10)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def add_section(self, title, content):
        """Add a section to the report."""
        self.set_font("Arial", style="B", size=12)
        self.cell(0, 10, title, ln=True)
        self.ln(5)
        self.set_font("Arial", size=12)
        self.multi_cell(0, 10, content)
        self.ln(10)

    def generate_report(self):
        """Generate the full report."""
        # Cover Page
        self.set_font("Arial", style="B", size=16)
        self.cell(0, 10, "Evaluation Report", ln=True, align="C")
        self.ln(20)
        self.set_font("Arial", size=12)
        self.cell(0, 10, f"Participant: {self.participant_name}", ln=True, align="C")
        self.cell(0, 10, f"Competition: {self.competition_name}", ln=True, align="C")
        self.ln(30)
        self.cell(0, 10, "Prepared by: Proof of Pitch Team", ln=True, align="C")
        self.add_page()

        # Add evaluation sections
        for section_title, section_content in self.evaluation_data.items():
            self.add_section(section_title, section_content)

        # Closing Page
        self.add_page()
        self.set_font("Arial", style="B", size=14)
        self.cell(0, 10, "Thank You!", ln=True, align="C")
        self.ln(20)
        self.set_font("Arial", size=12)
        self.multi_cell(0, 10, "We appreciate your participation in the Proof of Pitch competition. "
                               "We hope this evaluation report provides valuable insights for your growth and success.")
        self.ln(10)

def create_evaluation_report(participant_name, competition_name, evaluation_data, output_file):
    """
    Create and save the evaluation report as a PDF file.

    :param participant_name: Name of the participant
    :param competition_name: Name of the competition
    :param evaluation_data: Dictionary containing evaluation sections and their content
    :param output_file: Path to save the generated PDF file
    """
    try:
        report = EvaluationReport(participant_name, competition_name, evaluation_data)
        report.generate_report()
        report.output(output_file)
        print(f"Report successfully generated: {output_file}")
    except Exception as e:
        print(f"An error occurred while generating the report: {e}")

if __name__ == "__main__":
    # Example usage
    participant_name = "John Doe"
    competition_name = "Proof of Pitch 2023"
    evaluation_data = {
        "Introduction": "This section provides an overview of the participant's pitch and its objectives.",
        "Strengths": "The participant demonstrated strong communication skills and a clear understanding of the problem.",
        "Areas for Improvement": "The pitch could benefit from more detailed financial projections and market analysis.",
        "Feedback from Judges": "Judges appreciated the innovative approach but suggested refining the business model.",
        "Conclusion": "Overall, the pitch was well-received, and the participant showed great potential."
    }
    output_file = os.path.join(os.getcwd(), "evaluation_report.pdf")

    create_evaluation_report(participant_name, competition_name, evaluation_data, output_file)
```
