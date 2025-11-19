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
"""
Proof of Pitch Competition - Evaluation Report Template Generator

This script generates a detailed 10-page evaluation report template for participants
in the Proof of Pitch competition. The report includes sections for:
- Executive Summary
- Evaluation Criteria
- Detailed Scoring
- Feedback
- Next Steps
"""

from datetime import datetime
from fpdf import FPDF
import os

class ReportGenerator:
    """Generates PDF reports for Proof of Pitch competition participants"""
    
    def __init__(self, participant_name, company_name):
        """
        Initialize the report generator with participant details
        
        Args:
            participant_name (str): Name of the participant
            company_name (str): Name of the participant's company
        """
        self.participant_name = participant_name
        self.company_name = company_name
        self.report_date = datetime.now().strftime("%B %d, %Y")
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)
        
    def _add_header(self, title):
        """Add a standardized header to each page"""
        self.pdf.set_font('Arial', 'B', 12)
        self.pdf.cell(0, 10, f"Proof of Pitch Competition - {title}", 0, 1, 'C')
        self.pdf.set_font('Arial', '', 10)
        self.pdf.cell(0, 5, f"Participant: {self.participant_name} | Company: {self.company_name} | Date: {self.report_date}", 0, 1, 'C')
        self.pdf.ln(10)
        
    def _add_footer(self):
        """Add a standardized footer to each page"""
        self.pdf.set_y(-15)
        self.pdf.set_font('Arial', 'I', 8)
        self.pdf.cell(0, 10, f"Page {self.pdf.page_no()}", 0, 0, 'C')
        
    def _add_page(self, title):
        """Add a new page with header and footer"""
        self.pdf.add_page()
        self._add_header(title)
        self._add_footer()
        
    def _add_section_title(self, title):
        """Add a section title with consistent formatting"""
        self.pdf.set_font('Arial', 'B', 14)
        self.pdf.cell(0, 10, title, 0, 1)
        self.pdf.set_font('Arial', '', 12)
        self.pdf.ln(5)
        
    def _add_subsection(self, title):
        """Add a subsection with consistent formatting"""
        self.pdf.set_font('Arial', 'B', 12)
        self.pdf.cell(0, 8, title, 0, 1)
        self.pdf.set_font('Arial', '', 11)
        self.pdf.ln(2)
        
    def _add_placeholder_text(self, text):
        """Add placeholder text with proper formatting"""
        self.pdf.multi_cell(0, 6, text)
        self.pdf.ln(5)
        
    def generate_executive_summary(self):
        """Generate the executive summary page"""
        self._add_page("Executive Summary")
        self._add_section_title("Executive Summary")
        
        summary_text = (
            f"This report provides a comprehensive evaluation of {self.participant_name}'s "
            f"pitch for {self.company_name} in the Proof of Pitch competition. The evaluation "
            "was conducted by our panel of expert judges based on the established criteria "
            "including innovation, feasibility, market potential, presentation quality, and "
            "overall impact.\n\n"
            "The following pages contain detailed scoring across all evaluation dimensions, "
            "specific feedback from judges, and recommendations for next steps in the "
            "competition process."
        )
        self._add_placeholder_text(summary_text)
        
        self._add_subsection("Key Highlights")
        highlights = [
            "- Overall score: [Insert Score] / 100",
            "- Strengths: [List key strengths]",
            "- Areas for improvement: [List key areas]",
            "- Next steps: [Brief overview of next steps]"
        ]
        for item in highlights:
            self.pdf.cell(0, 6, item, 0, 1)
            self.pdf.ln(2)
            
    def generate_evaluation_criteria(self):
        """Generate the evaluation criteria page"""
        self._add_page("Evaluation Criteria")
        self._add_section_title("Evaluation Criteria")
        
        criteria = [
            ("Innovation (25%)", "Novelty and creativity of the proposed solution"),
            ("Feasibility (20%)", "Technical and operational practicality"),
            ("Market Potential (20%)", "Size of opportunity and target market fit"),
            ("Presentation Quality (15%)", "Clarity, structure, and delivery of the pitch"),
            ("Business Model (10%)", "Revenue potential and sustainability"),
            ("Team (10%)", "Relevant experience and capabilities")
        ]
        
        for criterion, description in criteria:
            self._add_subsection(criterion)
            self._add_placeholder_text(description)
            
    def generate_detailed_scoring(self):
        """Generate the detailed scoring pages (3 pages)"""
        for i in range(1, 4):
            self._add_page(f"Detailed Scoring - Part {i}")
            self._add_section_title(f"Detailed Evaluation - Part {i}")
            
            if i == 1:
                self._add_subsection("Innovation Scoring")
                self._add_placeholder_text(
                    "Score: [X]/25\n\n"
                    "Comments: [Detailed comments about the innovation aspect of the pitch, "
                    "including what worked well and what could be improved]"
                )
                
                self._add_subsection("Feasibility Scoring")
                self._add_placeholder_text(
                    "Score: [X]/20\n\n"
                    "Comments: [Detailed comments about the feasibility of implementation, "
                    "including technical considerations and operational challenges]"
                )
                
            elif i == 2:
                self._add_subsection("Market Potential Scoring")
                self._add_placeholder_text(
                    "Score: [X]/20\n\n"
                    "Comments: [Detailed analysis of market size, target audience, "
                    "competitive landscape, and growth potential]"
                )
                
                self._add_subsection("Presentation Quality Scoring")
                self._add_placeholder_text(
                    "Score: [X]/15\n\n"
                    "Comments: [Feedback on pitch delivery, slide quality, storytelling, "
                    "and overall presentation effectiveness]"
                )
                
            else:
                self._add_subsection("Business Model Scoring")
                self._add_placeholder_text(
                    "Score: [X]/10\n\n"
                    "Comments: [Evaluation of revenue streams, cost structure, pricing strategy, "
                    "and overall business viability]"
                )
                
                self._add_subsection("Team Scoring")
                self._add_placeholder_text(
                    "Score: [X]/10\n\n"
                    "Comments: [Assessment of team composition, relevant experience, "
                    "and ability to execute on the proposed solution]"
                )
                
    def generate_feedback(self):
        """Generate the feedback pages (2 pages)"""
        for i in range(1, 3):
            self._add_page(f"Judge Feedback - Part {i}")
            self._add_section_title(f"Judge Feedback - Part {i}")
            
            if i == 1:
                judges = ["Judge 1", "Judge 2"]
            else:
                judges = ["Judge 3", "Judge 4"]
                
            for judge in judges:
                self._add_subsection(f"{judge}'s Comments")
                self._add_placeholder_text(
                    f"[{judge}'s detailed feedback goes here. This should include specific "
                    "praise for what worked well, constructive criticism for areas needing "
                    "improvement, and any additional thoughts or suggestions.]\n\n"
                    "Overall Impression: [Brief summary of judge's overall impression]"
                )
                
    def generate_next_steps(self):
        """Generate the next steps page"""
        self._add_page("Next Steps")
        self._add_section_title("Next Steps")
        
        steps = [
            "1. Competition Advancement: [Status in competition and next stages]",
            "2. Feedback Implementation: [Key areas to focus on for improvement]",
            "3. Mentorship Opportunities: [Available resources for participants]",
            "4. Follow-up Timeline: [Important dates and deadlines]",
            "5. Additional Resources: [Recommended reading or contacts]"
        ]
        
        for step in steps:
            self.pdf.cell(0, 8, step, 0, 1)
            self.pdf.ln(2)
            
        self._add_subsection("Contact Information")
        self._add_placeholder_text(
            "For any questions about this evaluation or the competition process, "
            "please contact:\n\n"
            "Proof of Pitch Competition Committee\n"
            "Email: committee@proofofpitch.com\n"
            "Phone: (123) 456-7890"
        )
        
    def generate_report(self, output_path):
        """
        Generate the complete 10-page report and save to specified path
        
        Args:
            output_path (str): Path to save the generated
