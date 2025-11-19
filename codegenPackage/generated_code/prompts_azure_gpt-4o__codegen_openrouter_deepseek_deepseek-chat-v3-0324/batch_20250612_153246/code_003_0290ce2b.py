"""
Generated Code Metadata:
========================
Original URL: https://sanurisupplies.com
Prompt: Write code to automate the generation of branded stationery items, such as calendars, yearbooks, and document holders, using the stationery list provided by Sanuri Supplies.
Generated: DETERMINISTIC_0290ce2b67a073d6
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import os
from datetime import datetime
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.units import inch
from PIL import Image as PILImage

class StationeryGenerator:
    """
    A class to automate the generation of branded stationery items.
    Supported items: calendars, yearbooks, document holders.
    """
    
    def __init__(self, stationery_list_path, output_dir='output'):
        """
        Initialize the StationeryGenerator with the path to the stationery list.
        
        Args:
            stationery_list_path (str): Path to the CSV file containing stationery items
            output_dir (str): Directory to save generated files (default: 'output')
        """
        self.stationery_list_path = stationery_list_path
        self.output_dir = output_dir
        self.stationery_items = []
        self.brand_logo = None
        self.brand_name = "Sanuri Supplies"
        self.brand_primary_color = colors.HexColor("#2E86C1")
        self.brand_secondary_color = colors.HexColor("#F4D03F")
        
        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)
        
    def load_stationery_list(self):
        """
        Load stationery items from the provided CSV file.
        
        Raises:
            FileNotFoundError: If the stationery list file is not found
            ValueError: If the CSV file is malformed
        """
        try:
            with open(self.stationery_list_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.stationery_items.append(row)
        except FileNotFoundError:
            raise FileNotFoundError(f"Stationery list file not found: {self.stationery_list_path}")
        except Exception as e:
            raise ValueError(f"Error reading stationery list: {str(e)}")
    
    def set_brand_logo(self, logo_path):
        """
        Set the brand logo to be used on stationery items.
        
        Args:
            logo_path (str): Path to the logo image file
            
        Raises:
            FileNotFoundError: If the logo file is not found
        """
        if not os.path.exists(logo_path):
            raise FileNotFoundError(f"Logo file not found: {logo_path}")
        self.brand_logo = logo_path
    
    def generate_calendar(self, year, output_filename="calendar.pdf"):
        """
        Generate a branded calendar for the specified year.
        
        Args:
            year (int): Year for the calendar
            output_filename (str): Name of the output PDF file
            
        Returns:
            str: Path to the generated calendar file
        """
        output_path = os.path.join(self.output_dir, output_filename)
        doc = SimpleDocTemplate(output_path, pagesize=letter)
        
        styles = getSampleStyleSheet()
        title_style = ParagraphStyle(
            'Title',
            parent=styles['Title'],
            textColor=self.brand_primary_color,
            spaceAfter=20
        )
        
        elements = []
        
        # Add header with logo and brand name
        if self.brand_logo:
            logo = Image(self.brand_logo, width=1.5*inch, height=1*inch)
            elements.append(logo)
        
        title = Paragraph(f"{self.brand_name} {year} Calendar", title_style)
        elements.append(title)
        elements.append(Spacer(1, 0.5*inch))
        
        # Generate calendar months
        for month in range(1, 13):
            month_name = datetime(year, month, 1).strftime('%B')
            month_title = Paragraph(month_name, styles['Heading2'])
            elements.append(month_title)
            
            # Create calendar grid
            cal_data = self._create_month_calendar(year, month)
            cal_table = Table(cal_data, colWidths=[0.8*inch]*7, rowHeights=[0.5*inch]*6)
            cal_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), self.brand_secondary_color),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 10),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ]))
            
            elements.append(cal_table)
            elements.append(Spacer(1, 0.5*inch))
        
        doc.build(elements)
        return output_path
    
    def _create_month_calendar(self, year, month):
        """
        Create a calendar grid for a specific month.
        
        Args:
            year (int): Year
            month (int): Month (1-12)
            
        Returns:
            list: 2D list representing the calendar grid
        """
        import calendar
        
        cal = calendar.Calendar()
        month_days = cal.monthdayscalendar(year, month)
        
        # Header row with day names
        day_names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        month_grid = [day_names]
        
        # Add days
        for week in month_days:
            week_days = [str(day) if day != 0 else '' for day in week]
            month_grid.append(week_days)
            
        return month_grid
    
    def generate_yearbook(self, title, content, output_filename="yearbook.pdf"):
        """
        Generate a branded yearbook with the given title and content.
        
        Args:
            title (str): Title of the yearbook
            content (list): List of strings representing yearbook content
            output_filename (str): Name of the output PDF file
            
        Returns:
            str: Path to the generated yearbook file
        """
        output_path = os.path.join(self.output_dir, output_filename)
        doc = SimpleDocTemplate(output_path, pagesize=letter)
        
        styles = getSampleStyleSheet()
        title_style = ParagraphStyle(
            'Title',
            parent=styles['Title'],
            textColor=self.brand_primary_color,
            spaceAfter=20
        )
        
        elements = []
        
        # Add header with logo and brand name
        if self.brand_logo:
            logo = Image(self.brand_logo, width=1.5*inch, height=1*inch)
            elements.append(logo)
        
        yearbook_title = Paragraph(f"{self.brand_name} {title}", title_style)
        elements.append(yearbook_title)
        elements.append(Spacer(1, 0.5*inch))
        
        # Add content
        for item in content:
            para = Paragraph(item, styles['BodyText'])
            elements.append(para)
            elements.append(Spacer(1, 0.2*inch))
        
        doc.build(elements)
        return output_path
    
    def generate_document_holder(self, title, documents, output_filename="document_holder.pdf"):
        """
        Generate a branded document holder with the given title and documents.
        
        Args:
            title (str): Title of the document holder
            documents (list): List of document paths to include
            output_filename (str): Name of the output PDF file
            
        Returns:
            str: Path to the generated document holder file
        """
        output_path = os.path.join(self.output_dir, output_filename)
        doc = SimpleDocTemplate(output_path, pagesize=letter)
        
        styles = getSampleStyleSheet()
        title_style = ParagraphStyle(
            'Title',
            parent=styles['Title'],
            textColor=self.brand_primary_color,
            spaceAfter=20
        )
        
        elements = []
        
        # Add header with logo and brand name
        if self.brand_logo:
            logo = Image(self.brand_logo, width=1.5*inch, height=1*inch)
            elements.append(logo)
        
        holder_title = Paragraph(f"{self.brand_name} {title}", title_style)
        elements.append(holder_title)
        elements.append(Spacer(1, 0.5*inch))
        
        # Add document list
        doc_list_style = styles['BodyText']
        doc_list_style.leftIndent = 20
        
        for doc_path in documents:
            if not os.path.exists(doc_path):
                continue
                
            doc_name = os.path.basename(doc_path)
            doc_item = Paragraph(f"• {doc_name}", doc_list_style)
            elements.append(doc_item)
            elements.append(Spacer(1, 0.1*inch))
        
        doc.build(e
