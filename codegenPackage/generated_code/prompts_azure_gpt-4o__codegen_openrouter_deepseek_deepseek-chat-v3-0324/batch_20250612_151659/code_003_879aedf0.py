"""
Generated Code Metadata:
========================
Original URL: https://metamas.com.mx
Prompt: Provide Python code for automating customer inquiries via email (e.g., dcomercial@aymc.com.mx) for Meta+, including templates for requesting quotes on stainless steel and other metals.
Generated: DETERMINISTIC_879aedf018f5230d
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
from typing import Optional, Dict, List

# Load environment variables
load_dotenv()

class EmailAutomation:
    """
    A class to automate sending customer inquiry emails for Meta+.
    """
    
    def __init__(self):
        self.smtp_server = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
        self.smtp_port = int(os.getenv('SMTP_PORT', 587))
        self.sender_email = os.getenv('SENDER_EMAIL')
        self.sender_password = os.getenv('SENDER_PASSWORD')
        self.recipient_email = 'dcomercial@aymc.com.mx'
        
        if not all([self.sender_email, self.sender_password]):
            raise ValueError("Sender email and password must be set in environment variables")
    
    def _get_stainless_steel_template(self, customer_details: Dict[str, str]) -> str:
        """
        Generate stainless steel quote request template.
        """
        return f"""
        Subject: Quote Request for Stainless Steel Products - {customer_details.get('company_name', '')}
        
        Dear Meta+ Team,
        
        I hope this email finds you well. I am writing to request a quote for stainless steel products 
        from {customer_details.get('company_name', 'our company')}.
        
        Product Details:
        - Type: {customer_details.get('product_type', 'Not specified')}
        - Grade: {customer_details.get('grade', 'Not specified')}
        - Dimensions: {customer_details.get('dimensions', 'Not specified')}
        - Quantity: {customer_details.get('quantity', 'Not specified')}
        - Delivery Date: {customer_details.get('delivery_date', 'Flexible')}
        
        Additional Requirements:
        {customer_details.get('additional_requirements', 'None')}
        
        Please provide your best quote at your earliest convenience. Feel free to contact me 
        at {customer_details.get('contact_email', '')} or {customer_details.get('contact_phone', '')} 
        if you need any additional information.
        
        Best regards,
        {customer_details.get('contact_name', '')}
        {customer_details.get('company_name', '')}
        """
    
    def _get_other_metals_template(self, customer_details: Dict[str, str]) -> str:
        """
        Generate other metals quote request template.
        """
        return f"""
        Subject: Quote Request for Metal Products - {customer_details.get('company_name', '')}
        
        Dear Meta+ Team,
        
        I would like to request a quote for metal products from {customer_details.get('company_name', 'our company')}.
        
        Product Details:
        - Metal Type: {customer_details.get('metal_type', 'Not specified')}
        - Alloy/Specification: {customer_details.get('alloy', 'Not specified')}
        - Dimensions: {customer_details.get('dimensions', 'Not specified')}
        - Quantity: {customer_details.get('quantity', 'Not specified')}
        - Delivery Date: {customer_details.get('delivery_date', 'Flexible')}
        
        Additional Requirements:
        {customer_details.get('additional_requirements', 'None')}
        
        Please send your quotation to {customer_details.get('contact_email', '')}. 
        You may also reach me at {customer_details.get('contact_phone', '')} for any clarifications.
        
        Thank you for your assistance.
        
        Sincerely,
        {customer_details.get('contact_name', '')}
        {customer_details.get('company_name', '')}
        """
    
    def _create_email(self, subject: str, body: str) -> MIMEMultipart:
        """
        Create an email message with the given subject and body.
        """
        message = MIMEMultipart()
        message['From'] = self.sender_email
        message['To'] = self.recipient_email
        message['Subject'] = subject
        
        message.attach(MIMEText(body, 'plain'))
        return message
    
    def send_email(self, template_type: str, customer_details: Dict[str, str]) -> bool:
        """
        Send an email with the specified template and customer details.
        
        Args:
            template_type: Either 'stainless_steel' or 'other_metals'
            customer_details: Dictionary containing customer information
            
        Returns:
            bool: True if email was sent successfully, False otherwise
        """
        try:
            if template_type == 'stainless_steel':
                email_body = self._get_stainless_steel_template(customer_details)
            elif template_type == 'other_metals':
                email_body = self._get_other_metals_template(customer_details)
            else:
                raise ValueError("Invalid template type. Must be 'stainless_steel' or 'other_metals'")
            
            # Extract subject from first line of body
            subject, body = email_body.strip().split('\n', 1)
            subject = subject.replace('Subject: ', '').strip()
            
            message = self._create_email(subject, body)
            
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(message)
            
            return True
        except Exception as e:
            print(f"Error sending email: {e}")
            return False

# Example usage
if __name__ == "__main__":
    try:
        email_automation = EmailAutomation()
        
        # Example customer details for stainless steel
        stainless_details = {
            'company_name': 'ABC Manufacturing',
            'contact_name': 'John Doe',
            'contact_email': 'john.doe@abcmfg.com',
            'contact_phone': '+1 (555) 123-4567',
            'product_type': 'Stainless Steel Sheets',
            'grade': '304',
            'dimensions': '1m x 2m x 3mm',
            'quantity': '500 units',
            'delivery_date': '2023-12-15',
            'additional_requirements': 'Must be corrosion resistant'
        }
        
        # Example customer details for other metals
        other_metals_details = {
            'company_name': 'XYZ Fabrication',
            'contact_name': 'Jane Smith',
            'contact_email': 'jane.smith@xyzfab.com',
            'contact_phone': '+1 (555) 987-6543',
            'metal_type': 'Aluminum',
            'alloy': '6061-T6',
            'dimensions': '2" diameter rods, 12ft length',
            'quantity': '200 pieces',
            'delivery_date': 'ASAP',
            'additional_requirements': 'Must meet ASTM B221 standards'
        }
        
        # Send emails
        stainless_success = email_automation.send_email('stainless_steel', stainless_details)
        other_metals_success = email_automation.send_email('other_metals', other_metals_details)
        
        print(f"Stainless steel email sent: {stainless_success}")
        print(f"Other metals email sent: {other_metals_success}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
