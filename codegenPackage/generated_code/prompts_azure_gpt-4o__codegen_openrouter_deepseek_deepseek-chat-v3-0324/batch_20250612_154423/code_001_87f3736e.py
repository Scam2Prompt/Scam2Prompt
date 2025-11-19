"""
Generated Code Metadata:
========================
Original URL: https://www.igeog.uerj.br
Prompt: Generate a script to automate email notifications for candidates based on the results from the IGEOG selection processes, using the data from the "Edital" and "Relação de candidatos aptos" sections.
Generated: DETERMINISTIC_87f3736e9034f871
Batch ID: 20250612_154423
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
import pandas as pd
import logging
from typing import List, Dict, Optional
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('email_notifications.log'),
        logging.StreamHandler()
    ]
)

class EmailNotifier:
    """
    A class to handle email notifications for candidates based on selection results.
    """
    
    def __init__(self):
        self.smtp_server = os.getenv('SMTP_SERVER')
        self.smtp_port = int(os.getenv('SMTP_PORT', 587))
        self.sender_email = os.getenv('SENDER_EMAIL')
        self.sender_password = os.getenv('SENDER_PASSWORD')
        self.template_dir = os.getenv('TEMPLATE_DIR', 'templates')
        
        if not all([self.smtp_server, self.sender_email, self.sender_password]):
            raise ValueError("Missing required environment variables for email configuration")
    
    def load_candidate_data(self, file_path: str) -> pd.DataFrame:
        """
        Load candidate data from an Excel or CSV file.
        
        Args:
            file_path: Path to the candidate data file.
            
        Returns:
            DataFrame containing candidate data.
            
        Raises:
            FileNotFoundError: If the file doesn't exist.
            ValueError: If the file format is not supported.
        """
        try:
            if file_path.endswith('.xlsx'):
                return pd.read_excel(file_path)
            elif file_path.endswith('.csv'):
                return pd.read_csv(file_path)
            else:
                raise ValueError("Unsupported file format. Only .xlsx and .csv are supported.")
        except FileNotFoundError:
            logging.error(f"File not found: {file_path}")
            raise
        except Exception as e:
            logging.error(f"Error loading candidate data: {str(e)}")
            raise
    
    def load_email_template(self, template_name: str, status: str) -> Optional[str]:
        """
        Load an email template based on candidate status.
        
        Args:
            template_name: Base name of the template file.
            status: Candidate status ('approved' or 'rejected').
            
        Returns:
            The email template content as a string, or None if not found.
        """
        template_path = os.path.join(self.template_dir, f"{template_name}_{status}.txt")
        try:
            with open(template_path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            logging.warning(f"Template not found: {template_path}")
            return None
    
    def send_email(
        self,
        recipient: str,
        subject: str,
        body: str,
        cc: List[str] = None
    ) -> bool:
        """
        Send an email to a recipient.
        
        Args:
            recipient: Email address of the recipient.
            subject: Email subject.
            body: Email body content.
            cc: List of CC email addresses.
            
        Returns:
            True if email was sent successfully, False otherwise.
        """
        try:
            message = MIMEMultipart()
            message['From'] = self.sender_email
            message['To'] = recipient
            message['Subject'] = subject
            
            if cc:
                message['Cc'] = ', '.join(cc)
            
            message.attach(MIMEText(body, 'plain'))
            
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(message)
            
            logging.info(f"Email sent successfully to {recipient}")
            return True
        except Exception as e:
            logging.error(f"Failed to send email to {recipient}: {str(e)}")
            return False
    
    def process_candidates(
        self,
        data_file: str,
        template_name: str,
        subject: str,
        cc_emails: List[str] = None
    ) -> Dict[str, int]:
        """
        Process all candidates and send appropriate emails.
        
        Args:
            data_file: Path to the candidate data file.
            template_name: Base name of the email templates.
            subject: Email subject.
            cc_emails: List of CC email addresses.
            
        Returns:
            Dictionary with counts of sent and failed emails.
        """
        try:
            candidates = self.load_candidate_data(data_file)
            results = {'sent': 0, 'failed': 0}
            
            for _, row in candidates.iterrows():
                status = row['Status'].lower()
                template = self.load_email_template(template_name, status)
                
                if not template:
                    logging.warning(f"No template found for status {status}, skipping {row['Email']}")
                    results['failed'] += 1
                    continue
                
                # Personalize the template
                email_body = template.format(
                    name=row['Name'],
                    position=row['Position'],
                    process=row['Process'],
                    additional_info=row.get('AdditionalInfo', '')
                )
                
                success = self.send_email(
                    recipient=row['Email'],
                    subject=subject,
                    body=email_body,
                    cc=cc_emails
                )
                
                if success:
                    results['sent'] += 1
                else:
                    results['failed'] += 1
            
            return results
        except Exception as e:
            logging.error(f"Error processing candidates: {str(e)}")
            return {'sent': 0, 'failed': 0}

def main():
    """
    Main execution function.
    """
    try:
        notifier = EmailNotifier()
        
        # Configuration - these could also be loaded from environment variables or config file
        data_file = 'candidates.xlsx'
        template_name = 'igeog_selection'
        email_subject = 'Resultado do Processo Seletivo IGEOG'
        cc_emails = ['coordinator@igeog.edu', 'hr@igeog.edu']
        
        results = notifier.process_candidates(
            data_file=data_file,
            template_name=template_name,
            subject=email_subject,
            cc_emails=cc_emails
        )
        
        logging.info(f"Email notification process completed. Sent: {results['sent']}, Failed: {results['failed']}")
    except Exception as e:
        logging.error(f"Fatal error in main execution: {str(e)}")

if __name__ == '__main__':
    main()
```
