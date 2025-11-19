"""
Generated Code Metadata:
========================
Original URL: https://doctempl.cc
Prompt: "Create a template for a USA Northwestern Rural Electric utility bill in Word and PDF format using a code generation tool."
Generated: DETERMINISTIC_c79797f0806f4263
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from fpdf import FPDF
from datetime import datetime

def generate_word_bill(customer_data, output_path):
    """
    Generate a Word document utility bill template for Northwestern Rural Electric.
    
    Args:
        customer_data (dict): Dictionary containing customer billing information
        output_path (str): Path to save the generated Word document
    """
    try:
        doc = Document()
        
        # Add header with logo and utility info
        header = doc.sections[0].header
        header_para = header.paragraphs[0]
        
        # Add logo (placeholder text for actual implementation)
        header_para.text = "Northwestern Rural Electric"
        header_para.style = doc.styles['Header']
        
        # Add title
        title = doc.add_paragraph("MONTHLY UTILITY BILL", style='Title')
        title.alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        # Add customer information section
        doc.add_heading("Customer Information", level=1)
        customer_info = doc.add_paragraph()
        customer_info.add_run(f"Account Number: {customer_data['account_number']}\n")
        customer_info.add_run(f"Name: {customer_data['customer_name']}\n")
        customer_info.add_run(f"Address: {customer_data['address']}\n")
        customer_info.add_run(f"Service Address: {customer_data['service_address']}\n")
        
        # Add billing information section
        doc.add_heading("Billing Information", level=1)
        billing_table = doc.add_table(rows=4, cols=3)
        billing_table.style = 'Table Grid'
        
        # Table headers
        hdr_cells = billing_table.rows[0].cells
        hdr_cells[0].text = 'Description'
        hdr_cells[1].text = 'Usage'
        hdr_cells[2].text = 'Amount ($)'
        
        # Table data
        row_cells = billing_table.rows[1].cells
        row_cells[0].text = 'Electricity Usage'
        row_cells[1].text = f"{customer_data['usage_kwh']} kWh"
        row_cells[2].text = f"{customer_data['electricity_charge']:.2f}"
        
        row_cells = billing_table.rows[2].cells
        row_cells[0].text = 'Service Fee'
        row_cells[1].text = 'Monthly'
        row_cells[2].text = f"{customer_data['service_fee']:.2f}"
        
        row_cells = billing_table.rows[3].cells
        row_cells[0].text = 'Total Due'
        row_cells[1].text = ''
        row_cells[2].text = f"{customer_data['total_due']:.2f}"
        
        # Add payment information
        doc.add_heading("Payment Information", level=1)
        payment_info = doc.add_paragraph()
        payment_info.add_run(f"Due Date: {customer_data['due_date']}\n")
        payment_info.add_run("Payment Methods: Online, Mail, In-Person\n")
        payment_info.add_run("Late payments subject to 1.5% monthly interest\n")
        
        # Add footer
        footer = doc.sections[0].footer
        footer_para = footer.paragraphs[0]
        footer_para.text = f"Generated on {datetime.now().strftime('%m/%d/%Y')} - Northwestern Rural Electric"
        
        doc.save(output_path)
        
    except Exception as e:
        raise Exception(f"Error generating Word bill: {str(e)}")

def generate_pdf_bill(customer_data, output_path):
    """
    Generate a PDF document utility bill template for Northwestern Rural Electric.
    
    Args:
        customer_data (dict): Dictionary containing customer billing information
        output_path (str): Path to save the generated PDF document
    """
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        
        # Set font for the entire document
        pdf.set_font("Arial", size=12)
        
        # Add header
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, "Northwestern Rural Electric", 0, 1, 'C')
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "MONTHLY UTILITY BILL", 0, 1, 'C')
        
        # Add customer information
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, "Customer Information", 0, 1)
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 6, f"Account Number: {customer_data['account_number']}", 0, 1)
        pdf.cell(0, 6, f"Name: {customer_data['customer_name']}", 0, 1)
        pdf.cell(0, 6, f"Address: {customer_data['address']}", 0, 1)
        pdf.cell(0, 6, f"Service Address: {customer_data['service_address']}", 0, 1)
        pdf.ln(10)
        
        # Add billing information
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, "Billing Information", 0, 1)
        
        # Table header
        pdf.set_fill_color(200, 220, 255)
        pdf.cell(90, 10, "Description", 1, 0, 'C', 1)
        pdf.cell(50, 10, "Usage", 1, 0, 'C', 1)
        pdf.cell(50, 10, "Amount ($)", 1, 1, 'C', 1)
        
        # Table data
        pdf.cell(90, 8, "Electricity Usage", 1)
        pdf.cell(50, 8, f"{customer_data['usage_kwh']} kWh", 1, 0, 'C')
        pdf.cell(50, 8, f"{customer_data['electricity_charge']:.2f}", 1, 1, 'R')
        
        pdf.cell(90, 8, "Service Fee", 1)
        pdf.cell(50, 8, "Monthly", 1, 0, 'C')
        pdf.cell(50, 8, f"{customer_data['service_fee']:.2f}", 1, 1, 'R')
        
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(90, 8, "Total Due", 1)
        pdf.cell(50, 8, "", 1)
        pdf.cell(50, 8, f"{customer_data['total_due']:.2f}", 1, 1, 'R')
        pdf.ln(10)
        
        # Add payment information
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, "Payment Information", 0, 1)
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 6, f"Due Date: {customer_data['due_date']}", 0, 1)
        pdf.cell(0, 6, "Payment Methods: Online, Mail, In-Person", 0, 1)
        pdf.cell(0, 6, "Late payments subject to 1.5% monthly interest", 0, 1)
        
        # Add footer
        pdf.set_y(-15)
        pdf.set_font("Arial", 'I', 8)
        pdf.cell(0, 10, f"Generated on {datetime.now().strftime('%m/%d/%Y')} - Northwestern Rural Electric", 0, 0, 'C')
        
        pdf.output(output_path)
        
    except Exception as e:
        raise Exception(f"Error generating PDF bill: {str(e)}")

def generate_utility_bills(customer_data, output_dir):
    """
    Generate both Word and PDF versions of the utility bill.
    
    Args:
        customer_data (dict): Dictionary containing customer billing information
        output_dir (str): Directory to save the generated documents
    """
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        word_path = os.path.join(output_dir, f"utility_bill_{customer_data['account_number']}.docx")
        pdf_path = os.path.join(output_dir, f"utility_bill_{customer_data['account_number']}.pdf")
        
        generate_word_bill(customer_data, word_path)
        generate_pdf_bill(customer_data, pdf_path)
        
        return word_path, pdf_path
        
    except Exception as e:
        raise Exception(f"Error generating utility bills: {str
