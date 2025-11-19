"""
Generated Code Metadata:
========================
Original URL: https://kleanproutah.com
Prompt: Write a Python script to automate sending service estimates for concrete cleaning and fleet washing, inspired by Klean-Pro Utah's service model.
Generated: DETERMINISTIC_9e1345c7417bb3a8
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os
import json
import datetime
from typing import Dict, List, Optional

class EstimateAutomation:
    """
    A class to automate sending service estimates for concrete cleaning and fleet washing.
    """
    
    def __init__(self, config_path: str = "config.json"):
        """
        Initialize the EstimateAutomation with configuration.
        
        Args:
            config_path (str): Path to the configuration file. Defaults to "config.json".
        """
        self.config = self._load_config(config_path)
        self.smtp_server = self.config.get("smtp_server")
        self.smtp_port = self.config.get("smtp_port")
        self.email = self.config.get("email")
        self.password = self.config.get("password")
        self.template_path = self.config.get("template_path", "estimate_template.html")
        
    def _load_config(self, config_path: str) -> Dict:
        """
        Load configuration from a JSON file.
        
        Args:
            config_path (str): Path to the configuration file.
            
        Returns:
            Dict: Configuration dictionary.
            
        Raises:
            FileNotFoundError: If config file is not found.
            json.JSONDecodeError: If config file is not valid JSON.
        """
        try:
            with open(config_path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file not found at {config_path}")
        except json.JSONDecodeError:
            raise json.JSONDecodeError("Invalid JSON configuration file", doc=config_path, pos=0)
    
    def _load_template(self) -> str:
        """
        Load the email template from file.
        
        Returns:
            str: The template content.
            
        Raises:
            FileNotFoundError: If template file is not found.
        """
        try:
            with open(self.template_path, "r") as f:
                return f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"Template file not found at {self.template_path}")
    
    def _generate_estimate_content(self, customer_data: Dict, service_data: Dict) -> str:
        """
        Generate the estimate content by replacing placeholders in the template.
        
        Args:
            customer_data (Dict): Customer information.
            service_data (Dict): Service details and pricing.
            
        Returns:
            str: The generated estimate content.
        """
        template = self._load_template()
        
        # Replace customer placeholders
        for key, value in customer_data.items():
            template = template.replace(f"{{customer_{key}}}", str(value))
            
        # Replace service placeholders
        for key, value in service_data.items():
            template = template.replace(f"{{service_{key}}}", str(value))
            
        # Replace date placeholders
        today = datetime.date.today()
        template = template.replace("{date}", today.strftime("%B %d, %Y"))
        template = template.replace("{expiry_date}", (today + datetime.timedelta(days=30)).strftime("%B %d, %Y"))
        
        return template
    
    def _attach_pdf(self, msg: MIMEMultipart, pdf_path: str) -> None:
        """
        Attach a PDF file to the email.
        
        Args:
            msg (MIMEMultipart): The email message object.
            pdf_path (str): Path to the PDF file.
            
        Raises:
            FileNotFoundError: If PDF file is not found.
        """
        try:
            with open(pdf_path, "rb") as f:
                part = MIMEApplication(f.read(), Name=os.path.basename(pdf_path))
            part['Content-Disposition'] = f'attachment; filename="{os.path.basename(pdf_path)}"'
            msg.attach(part)
        except FileNotFoundError:
            raise FileNotFoundError(f"PDF file not found at {pdf_path}")
    
    def send_estimate(
        self,
        customer_data: Dict,
        service_data: Dict,
        to_email: str,
        subject: str = "Your Service Estimate",
        pdf_attachment: Optional[str] = None
    ) -> bool:
        """
        Send the service estimate email.
        
        Args:
            customer_data (Dict): Customer information.
            service_data (Dict): Service details and pricing.
            to_email (str): Recipient email address.
            subject (str): Email subject. Defaults to "Your Service Estimate".
            pdf_attachment (Optional[str]): Path to PDF attachment. Defaults to None.
            
        Returns:
            bool: True if email was sent successfully, False otherwise.
        """
        # Create message container
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = to_email
        msg['Subject'] = subject
        
        # Generate and attach HTML content
        html_content = self._generate_estimate_content(customer_data, service_data)
        msg.attach(MIMEText(html_content, 'html'))
        
        # Attach PDF if provided
        if pdf_attachment:
            try:
                self._attach_pdf(msg, pdf_attachment)
            except FileNotFoundError as e:
                print(f"Warning: {e}. Sending email without attachment.")
        
        # Send the email
        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.email, self.password)
                server.send_message(msg)
            return True
        except smtplib.SMTPException as e:
            print(f"Error sending email: {e}")
            return False

def main():
    # Example usage
    try:
        automation = EstimateAutomation()
        
        # Sample customer and service data
        customer_data = {
            "name": "John Doe",
            "company": "ABC Corporation",
            "address": "123 Main St, Salt Lake City, UT",
            "phone": "(555) 123-4567",
            "email": "john.doe@abccorp.com"
        }
        
        service_data = {
            "type": "Concrete Cleaning",
            "area": "5000 sq ft",
            "price_per_unit": "$0.25",
            "total_price": "$1250.00",
            "notes": "Includes pressure washing and stain removal"
        }
        
        # Send the estimate
        success = automation.send_estimate(
            customer_data=customer_data,
            service_data=service_data,
            to_email=customer_data["email"],
            pdf_attachment="estimate.pdf"  # Optional
        )
        
        if success:
            print("Estimate sent successfully!")
        else:
            print("Failed to send estimate.")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
