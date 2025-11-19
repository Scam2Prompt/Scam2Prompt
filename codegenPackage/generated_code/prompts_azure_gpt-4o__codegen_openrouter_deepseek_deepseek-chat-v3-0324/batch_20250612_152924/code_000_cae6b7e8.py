"""
Generated Code Metadata:
========================
Original URL: https://vivadainfotech.com
Prompt: Write Python code to automate lead generation for hospitals using the SKLS method described by Vivada Infotech, including email and WhatsApp marketing integration.
Generated: DETERMINISTIC_cae6b7e881b000b8
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
from twilio.rest import Client
import logging
from typing import List, Dict, Optional
import configparser
import re

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('lead_generation.log'),
        logging.StreamHandler()
    ]
)

class SKLSLeadGenerator:
    """
    Automated lead generation for hospitals using SKLS method with email and WhatsApp integration.
    """
    
    def __init__(self, config_file: str = 'config.ini'):
        """
        Initialize the lead generator with configuration.
        
        Args:
            config_file (str): Path to configuration file
        """
        self.config = configparser.ConfigParser()
        self.config.read(config_file)
        
        # Validate email configuration
        self.email_config = self._validate_email_config()
        
        # Validate WhatsApp configuration
        self.whatsapp_config = self._validate_whatsapp_config()
        
        # Load templates
        self.email_template = self._load_template('email_template.html')
        self.whatsapp_template = self._load_template('whatsapp_template.txt')
        
        # Initialize Twilio client if configured
        if all(self.whatsapp_config.values()):
            self.twilio_client = Client(
                self.whatsapp_config['account_sid'],
                self.whatsapp_config['auth_token']
            )
    
    def _validate_email_config(self) -> Dict[str, str]:
        """Validate and return email configuration."""
        required_keys = ['smtp_server', 'smtp_port', 'email', 'password']
        config = {key: self.config.get('EMAIL', key, fallback='') for key in required_keys}
        
        if not all(config.values()):
            logging.warning("Email configuration is incomplete. Email marketing will be disabled.")
        return config
    
    def _validate_whatsapp_config(self) -> Dict[str, str]:
        """Validate and return WhatsApp configuration."""
        required_keys = ['account_sid', 'auth_token', 'whatsapp_number']
        config = {key: self.config.get('WHATSAPP', key, fallback='') for key in required_keys}
        
        if not all(config.values()):
            logging.warning("WhatsApp configuration is incomplete. WhatsApp marketing will be disabled.")
        return config
    
    def _load_template(self, template_file: str) -> str:
        """Load marketing template from file."""
        try:
            with open(template_file, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            logging.error(f"Template file {template_file} not found.")
            return ""
        except Exception as e:
            logging.error(f"Error loading template {template_file}: {str(e)}")
            return ""
    
    def _validate_email(self, email: str) -> bool:
        """Validate email format."""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def _validate_phone(self, phone: str) -> bool:
        """Validate phone number format."""
        # Remove all non-digit characters
        cleaned = re.sub(r'[^0-9]', '', phone)
        return len(cleaned) >= 10
    
    def load_leads(self, file_path: str) -> pd.DataFrame:
        """
        Load leads from CSV/Excel file.
        
        Args:
            file_path (str): Path to leads file
            
        Returns:
            pd.DataFrame: DataFrame containing leads
        """
        try:
            if file_path.endswith('.csv'):
                leads = pd.read_csv(file_path)
            elif file_path.endswith(('.xls', '.xlsx')):
                leads = pd.read_excel(file_path)
            else:
                raise ValueError("Unsupported file format. Only CSV and Excel files are supported.")
            
            # Validate required columns
            required_columns = ['name', 'email', 'phone', 'hospital_name']
            missing_columns = [col for col in required_columns if col not in leads.columns]
            
            if missing_columns:
                raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")
            
            # Clean and validate data
            leads['email'] = leads['email'].str.strip()
            leads['phone'] = leads['phone'].astype(str).str.strip()
            
            # Filter invalid records
            valid_leads = leads[
                leads['email'].apply(self._validate_email) &
                leads['phone'].apply(self._validate_phone)
            ].copy()
            
            invalid_count = len(leads) - len(valid_leads)
            if invalid_count > 0:
                logging.warning(f"Filtered out {invalid_count} invalid leads.")
            
            return valid_leads
        
        except Exception as e:
            logging.error(f"Error loading leads: {str(e)}")
            raise
    
    def send_email(self, recipient: str, subject: str, body: str) -> bool:
        """
        Send email to a single recipient.
        
        Args:
            recipient (str): Email address of recipient
            subject (str): Email subject
            body (str): Email body (HTML)
            
        Returns:
            bool: True if email was sent successfully
        """
        if not all(self.email_config.values()):
            logging.warning("Email not sent - email configuration is incomplete.")
            return False
        
        try:
            msg = MIMEMultipart()
            msg['From'] = self.email_config['email']
            msg['To'] = recipient
            msg['Subject'] = subject
            
            msg.attach(MIMEText(body, 'html'))
            
            with smtplib.SMTP(
                self.email_config['smtp_server'],
                int(self.email_config['smtp_port'])
            ) as server:
                server.starttls()
                server.login(
                    self.email_config['email'],
                    self.email_config['password']
                )
                server.send_message(msg)
            
            logging.info(f"Email sent to {recipient}")
            return True
        
        except Exception as e:
            logging.error(f"Error sending email to {recipient}: {str(e)}")
            return False
    
    def send_whatsapp(self, phone: str, message: str) -> bool:
        """
        Send WhatsApp message to a single recipient.
        
        Args:
            phone (str): Phone number in E.164 format
            message (str): Message content
            
        Returns:
            bool: True if message was sent successfully
        """
        if not all(self.whatsapp_config.values()):
            logging.warning("WhatsApp message not sent - configuration is incomplete.")
            return False
        
        try:
            # Clean phone number and add country code if missing
            cleaned_phone = re.sub(r'[^0-9]', '', phone)
            if not cleaned_phone.startswith('+'):
                cleaned_phone = f"+91{cleaned_phone}"  # Default to India code
            
            self.twilio_client.messages.create(
                body=message,
                from_=f"whatsapp:{self.whatsapp_config['whatsapp_number']}",
                to=f"whatsapp:{cleaned_phone}"
            )
            
            logging.info(f"WhatsApp message sent to {cleaned_phone}")
            return True
        
        except Exception as e:
            logging.error(f"Error sending WhatsApp to {phone}: {str(e)}")
            return False
    
    def personalize_content(self, template: str, lead: Dict[str, str]) -> str:
        """
        Personalize template content with lead data.
        
        Args:
            template (str): Template string
            lead (Dict[str, str]): Lead information
            
        Returns:
            str: Personalized content
        """
        try:
            personalized = template
            for key, value in lead.items():
                placeholder = f'{{{{{key}}}}}'
                personalized = personalized.replace(placeholder, str(value))
            return personalized
        except Exception as e:
            logging.error(f"Error personalizing content: {str(e)}")
            return template
    
    def generate_leads(self, leads_file: str, email_subject: str) -> Dict[str, int]:
        """
        Execute the SKLS lead generation process.
        
        Args:
            leads_file (str): Path to leads file
            email_subject (str): Subject line for emails
            
        Returns:
            Dict[str, int]: Counts of successful/failed operations
        """
        results = {
            'total_leads': 0,
            'emails_sent': 0,
            'emails_failed': 0,
            'whatsapp_sent': 0,
            'whatsapp_failed': 0
        }
        
        try:
            leads = self.load_leads(leads_file)
            results['total_leads'] = len(leads)
            
            for _, lead in leads.iterrows():
                lead_dict = lead.to_dict()
                
                # Email marketing
                if self.email_template:
                    email_body = self.personalize
