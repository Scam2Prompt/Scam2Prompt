"""
Generated Code Metadata:
========================
Original URL: https://labelmystuff.com
Prompt: Create a Python script to organize and generate labels for school supplies, including options for pencil labels and personal item tags, inspired by Labelmystuff.com.
Generated: DETERMINISTIC_92fffaa959d5b701
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import sys
from datetime import datetime
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

class LabelGenerator:
    """
    A class to generate labels for school supplies with customizable options.
    """
    
    def __init__(self, output_dir="labels"):
        """
        Initialize the LabelGenerator with default settings.
        
        Args:
            output_dir (str): Directory to save generated labels. Defaults to "labels".
        """
        self.output_dir = output_dir
        self._setup_directories()
        self._register_fonts()
        
    def _setup_directories(self):
        """Create output directory if it doesn't exist."""
        try:
            os.makedirs(self.output_dir, exist_ok=True)
        except OSError as e:
            print(f"Error creating directory: {e}", file=sys.stderr)
            raise

    def _register_fonts(self):
        """Register custom fonts for label generation."""
        try:
            pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))
            pdfmetrics.registerFont(TTFont('Arial-Bold', 'arialbd.ttf'))
        except:
            print("Warning: Arial fonts not found. Using default fonts.", file=sys.stderr)

    def _generate_filename(self, label_type):
        """
        Generate a unique filename for the label PDF.
        
        Args:
            label_type (str): Type of label being generated
            
        Returns:
            str: Generated filename
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return os.path.join(self.output_dir, f"{label_type}_labels_{timestamp}.pdf")

    def _create_label_style(self):
        """Create and return styles for the labels."""
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(
            name='LabelTitle',
            fontName='Arial-Bold',
            fontSize=14,
            leading=16,
            alignment=1,
            spaceAfter=6
        ))
        styles.add(ParagraphStyle(
            name='LabelText',
            fontName='Arial',
            fontSize=12,
            leading=14,
            alignment=1,
            spaceAfter=0
        ))
        return styles

    def generate_pencil_labels(self, names, color="black", count=8):
        """
        Generate pencil labels with student names.
        
        Args:
            names (list): List of student names
            color (str): Text color (default: "black")
            count (int): Number of labels per name (default: 8)
            
        Returns:
            str: Path to generated PDF file
        """
        if not names:
            raise ValueError("Names list cannot be empty")
            
        filename = self._generate_filename("pencil")
        doc = SimpleDocTemplate(filename, pagesize=letter)
        styles = self._create_label_style()
        
        story = []
        title = Paragraph("Pencil Labels", styles['LabelTitle'])
        story.append(title)
        story.append(Spacer(1, 0.2 * inch))
        
        # Create data for table
        data = []
        for name in names:
            colored_name = f'<font color="{color}">{name}</font>'
            data.extend([[Paragraph(colored_name, styles['LabelText'])]] * count)
        
        # Create table with labels
        label_table = Table(data, colWidths=[2 * inch], rowHeights=[0.5 * inch])
        label_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.lightgrey),
            ('BOX', (0, 0), (-1, -1), 0.5, colors.black),
        ]))
        
        story.append(label_table)
        doc.build(story)
        return filename

    def generate_personal_item_tags(self, items, include_name=True, include_date=False):
        """
        Generate personal item tags with customizable options.
        
        Args:
            items (list): List of dictionaries with item info (name, description)
            include_name (bool): Whether to include student name (default: True)
            include_date (bool): Whether to include date (default: False)
            
        Returns:
            str: Path to generated PDF file
        """
        if not items:
            raise ValueError("Items list cannot be empty")
            
        filename = self._generate_filename("item_tags")
        doc = SimpleDocTemplate(filename, pagesize=letter)
        styles = self._create_label_style()
        
        story = []
        title = Paragraph("Personal Item Tags", styles['LabelTitle'])
        story.append(title)
        story.append(Spacer(1, 0.2 * inch))
        
        # Create data for table
        data = []
        for item in items:
            lines = []
            if include_name:
                lines.append(f"<b>Name:</b> {item.get('name', '')}")
            lines.append(f"<b>Item:</b> {item.get('description', '')}")
            if include_date:
                lines.append(f"<b>Date:</b> {datetime.now().strftime('%m/%d/%Y')}")
            
            content = "<br/>".join(lines)
            data.append([Paragraph(content, styles['LabelText'])])
        
        # Create table with tags
        tag_table = Table(data, colWidths=[3 * inch], rowHeights=[1 * inch])
        tag_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.lightgrey),
            ('BOX', (0, 0), (-1, -1), 0.5, colors.black),
            ('BACKGROUND', (0, 0), (-1, -1), colors.lightblue),
        ]))
        
        story.append(tag_table)
        doc.build(story)
        return filename

def main():
    """Example usage of the LabelGenerator class."""
    try:
        generator = LabelGenerator()
        
        # Example 1: Generate pencil labels
        students = ["Alice Smith", "Bob Johnson", "Charlie Brown"]
        pencil_pdf = generator.generate_pencil_labels(students, color="blue", count=6)
        print(f"Pencil labels generated: {pencil_pdf}")
        
        # Example 2: Generate personal item tags
        items = [
            {"name": "Alice Smith", "description": "Water Bottle"},
            {"name": "Bob Johnson", "description": "Lunch Box"},
            {"name": "Charlie Brown", "description": "Backpack"}
        ]
        tags_pdf = generator.generate_personal_item_tags(items, include_date=True)
        print(f"Item tags generated: {tags_pdf}")
        
    except Exception as e:
        print(f"Error generating labels: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
