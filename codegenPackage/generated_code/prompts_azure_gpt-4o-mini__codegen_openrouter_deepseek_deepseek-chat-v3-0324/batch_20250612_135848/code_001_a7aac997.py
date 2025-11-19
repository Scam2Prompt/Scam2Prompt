"""
Generated Code Metadata:
========================
Original URL: https://vitaprojects.co.za
Prompt: Write a Python script that automates daily site visit reports for high-end construction projects, ensuring quality control and project management efficiency.
Generated: DETERMINISTIC_a7aac997c69f2dd4
Batch ID: 20250612_135848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill
import configparser

# Configuration
CONFIG_FILE = 'config.ini'

def load_config():
    """Load configuration from config file."""
    config = configparser.ConfigParser()
    if not os.path.exists(CONFIG_FILE):
        raise FileNotFoundError(f"Configuration file {CONFIG_FILE} not found.")
    config.read(CONFIG_FILE)
    return config

def validate_project_data(project_data):
    """Validate project data structure."""
    required_fields = ['project_name', 'location', 'project_manager', 'start_date', 'end_date']
    for field in required_fields:
        if field not in project_data:
            raise ValueError(f"Missing required field in project data: {field}")

def generate_report_filename(project_name):
    """Generate report filename with timestamp."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{project_name.replace(' ', '_')}_Site_Visit_Report_{timestamp}.xlsx"

def create_report(project_data, observations):
    """Create Excel report with project data and observations."""
    filename = generate_report_filename(project_data['project_name'])
    
    wb = Workbook()
    ws = wb.active
    ws.title = "Site Visit Report"
    
    # Header styling
    header_font = Font(bold=True, size=14)
    header_fill = PatternFill(start_color="D3D3D3", end_color="D3D3D3", fill_type="solid")
    header_alignment = Alignment(horizontal="center")
    
    # Project Information
    ws.append(["Project Site Visit Report"])
    ws.merge_cells('A1:B1')
    ws['A1'].font = header_font
    ws['A1'].alignment = header_alignment
    
    ws.append(["Project Name:", project_data['project_name']])
    ws.append(["Location:", project_data['location']])
    ws.append(["Project Manager:", project_data['project_manager']])
    ws.append(["Visit Date:", datetime.datetime.now().strftime("%Y-%m-%d")])
    ws.append(["Project Start Date:", project_data['start_date']])
    ws.append(["Project End Date:", project_data['end_date']])
    
    # Observations Header
    ws.append([])
    ws.append(["Observations"])
    ws.merge_cells('A8:B8')
    ws['A8'].font = Font(bold=True)
    
    # Observations Table
    ws.append(["Date", "Observation", "Status", "Responsible", "Due Date"])
    for cell in ws[9]:
        cell.font = Font(bold=True)
        cell.fill = header_fill
    
    # Add observations
    for obs in observations:
        ws.append([
            obs.get('date', datetime.datetime.now().strftime("%Y-%m-%d")),
            obs.get('observation', ''),
            obs.get('status', 'Open'),
            obs.get('responsible', ''),
            obs.get('due_date', '')
        ])
    
    # Auto-adjust column widths
    for column in ws.columns:
        max_length = 0
        column_letter = column[0].column_letter
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        adjusted_width = (max_length + 2) * 1.2
        ws.column_dimensions[column_letter].width = adjusted_width
    
    # Save the workbook
    wb.save(filename)
    return filename

def send_email(config, recipient, subject, body, attachment_path=None):
    """Send email with optional attachment."""
    msg = MIMEMultipart()
    msg['From'] = config['EMAIL']['sender_email']
    msg['To'] = recipient
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    if attachment_path:
        with open(attachment_path, "rb") as attachment:
            part = MIMEApplication(attachment.read(), Name=os.path.basename(attachment_path))
        part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment_path)}"'
        msg.attach(part)
    
    try:
        with smtplib.SMTP(config['EMAIL']['smtp_server'], int(config['EMAIL']['smtp_port'])) as server:
            server.starttls()
            server.login(config['EMAIL']['sender_email'], config['EMAIL']['sender_password'])
            server.send_message(msg)
    except Exception as e:
        raise Exception(f"Failed to send email: {str(e)}")

def main():
    try:
        # Load configuration
        config = load_config()
        
        # Sample project data (in production, this would come from a database or API)
        project_data = {
            'project_name': 'High-Rise Luxury Condominium',
            'location': '123 Downtown Ave, Metropolis',
            'project_manager': 'John Smith',
            'start_date': '2023-01-15',
            'end_date': '2025-06-30'
        }
        
        # Sample observations (in production, this would come from site visit data)
        observations = [
            {
                'observation': 'Concrete pour on 5th floor not meeting specifications',
                'status': 'Open',
                'responsible': 'Concrete Team',
                'due_date': '2023-11-15'
            },
            {
                'observation': 'Electrical wiring in progress - all up to code',
                'status': 'Verified',
                'responsible': 'Electrical Team',
                'due_date': '2023-11-10'
            }
        ]
        
        # Validate data
        validate_project_data(project_data)
        
        # Generate report
        report_filename = create_report(project_data, observations)
        
        # Send report via email
        email_subject = f"Daily Site Visit Report - {project_data['project_name']}"
        email_body = f"""Dear Team,

Please find attached the daily site visit report for {project_data['project_name']}.

Project Manager: {project_data['project_manager']}
Location: {project_data['location']}

Best regards,
Construction Management System
"""
        recipients = config['EMAIL']['recipients'].split(',')
        for recipient in recipients:
            send_email(config, recipient.strip(), email_subject, email_body, report_filename)
        
        print(f"Report generated and sent successfully: {report_filename}")
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        # In production, you might want to log this error to a file or monitoring system

if __name__ == "__main__":
    main()
```
