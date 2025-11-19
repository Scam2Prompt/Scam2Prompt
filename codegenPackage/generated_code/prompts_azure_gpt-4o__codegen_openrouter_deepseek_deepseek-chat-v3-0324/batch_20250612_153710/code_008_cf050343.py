"""
Generated Code Metadata:
========================
Original URL: https://amplatinumconsulting.com
Prompt: Write Python code to automate the generation of consulting reports using libraries like ReportLab or Pandas.
Generated: DETERMINISTIC_cf050343b32efbf7
Batch ID: 20250612_153710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from datetime import datetime
from typing import List, Dict, Optional

class ConsultingReportGenerator:
    """
    A class to generate consulting reports using ReportLab and Pandas.
    """
    
    def __init__(self, output_dir: str = "reports"):
        """
        Initialize the report generator.
        
        Args:
            output_dir (str): Directory to save generated reports. Defaults to "reports".
        """
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Initialize styles
        self.styles = getSampleStyleSheet()
        self._setup_custom_styles()
    
    def _setup_custom_styles(self) -> None:
        """Setup custom styles for the report."""
        self.styles.add(ParagraphStyle(
            name='Title',
            fontSize=18,
            leading=22,
            alignment=1,  # Center aligned
            spaceAfter=20
        ))
        
        self.styles.add(ParagraphStyle(
            name='Heading1',
            fontSize=14,
            leading=18,
            spaceBefore=12,
            spaceAfter=6
        ))
        
        self.styles.add(ParagraphStyle(
            name='BodyText',
            fontSize=10,
            leading=14,
            spaceAfter=6
        ))
    
    def _generate_filename(self, client_name: str) -> str:
        """Generate a filename for the report."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_client_name = "".join(c if c.isalnum() else "_" for c in client_name)
        return os.path.join(self.output_dir, f"consulting_report_{safe_client_name}_{timestamp}.pdf")
    
    def _create_title_page(self, story: List, client_name: str, report_title: str) -> None:
        """Create the title page of the report."""
        story.append(Paragraph(report_title, self.styles['Title']))
        story.append(Spacer(1, 48))
        story.append(Paragraph(f"Prepared for: {client_name}", self.styles['Heading1']))
        story.append(Spacer(1, 24))
        story.append(Paragraph(f"Date: {datetime.now().strftime('%B %d, %Y')}", self.styles['BodyText']))
        story.append(Spacer(1, 72))
        story.append(Paragraph("Confidential", self.styles['BodyText']))
        story.append(Spacer(1, 24))
    
    def _create_data_table(self, df: pd.DataFrame) -> Table:
        """Create a table from pandas DataFrame."""
        # Convert DataFrame to list of lists for ReportLab
        data = [df.columns.tolist()] + df.values.tolist()
        
        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        return table
    
    def _create_section(self, story: List, title: str, content: str, data: Optional[pd.DataFrame] = None) -> None:
        """Create a section in the report."""
        story.append(Paragraph(title, self.styles['Heading1']))
        story.append(Paragraph(content, self.styles['BodyText']))
        if data is not None:
            story.append(Spacer(1, 12))
            story.append(self._create_data_table(data))
        story.append(Spacer(1, 24))
    
    def generate_report(
        self,
        client_name: str,
        report_title: str,
        sections: List[Dict[str, str]],
        data_sections: Optional[Dict[str, pd.DataFrame]] = None
    ) -> str:
        """
        Generate a consulting report.
        
        Args:
            client_name: Name of the client
            report_title: Title of the report
            sections: List of sections with title and content
            data_sections: Optional dictionary of DataFrames keyed by section title
            
        Returns:
            str: Path to the generated PDF file
        """
        if data_sections is None:
            data_sections = {}
        
        filename = self._generate_filename(client_name)
        doc = SimpleDocTemplate(filename, pagesize=letter)
        story = []
        
        # Title page
        self._create_title_page(story, client_name, report_title)
        story.append(Spacer(1, 72))
        
        # Add sections
        for section in sections:
            title = section['title']
            content = section['content']
            data = data_sections.get(title)
            self._create_section(story, title, content, data)
        
        # Build the document
        doc.build(story)
        return filename

# Example usage
if __name__ == "__main__":
    # Sample data
    sample_data = {
        "Financial Overview": pd.DataFrame({
            "Metric": ["Revenue", "Expenses", "Profit"],
            "Q1": [100000, 75000, 25000],
            "Q2": [120000, 80000, 40000],
            "Q3": [150000, 90000, 60000],
        }),
        "Market Analysis": pd.DataFrame({
            "Segment": ["Enterprise", "SMB", "Consumer"],
            "Market Share (%)": [45, 30, 25],
            "Growth Rate (%)": [12, 18, 8]
        })
    }
    
    # Sample sections
    sample_sections = [
        {"title": "Executive Summary", "content": "This report summarizes our findings and recommendations..."},
        {"title": "Financial Overview", "content": "The financial performance shows steady growth..."},
        {"title": "Market Analysis", "content": "Market analysis reveals opportunities in SMB segment..."},
        {"title": "Recommendations", "content": "Based on our analysis, we recommend..."}
    ]
    
    # Generate report
    generator = ConsultingReportGenerator()
    report_path = generator.generate_report(
        client_name="Acme Corp",
        report_title="Strategic Consulting Report",
        sections=sample_sections,
        data_sections=sample_data
    )
    
    print(f"Report generated at: {report_path}")
```
