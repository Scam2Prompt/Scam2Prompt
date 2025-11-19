"""
Generated Code Metadata:
========================
Original URL: https://oric.kinnaird.edu.pk
Prompt: Write code to automate the process of submitting research papers for presentations, following the guidelines mentioned in ORIC's paper presentation section.
Generated: DETERMINISTIC_f54c6067e2ea7624
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import requests
from datetime import datetime
from typing import Dict, Optional, List
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

class PaperSubmissionAutomation:
    """
    Automates the process of submitting research papers for presentations following ORIC guidelines.
    """
    
    def __init__(self, config_file: str = "config.json"):
        """
        Initialize the automation with configuration.
        
        Args:
            config_file: Path to JSON configuration file.
        """
        self.config = self._load_config(config_file)
        self.validate_config()
        
    def _load_config(self, config_file: str) -> Dict:
        """
        Load configuration from JSON file.
        
        Args:
            config_file: Path to JSON configuration file.
            
        Returns:
            Dictionary containing configuration.
            
        Raises:
            FileNotFoundError: If config file doesn't exist.
            json.JSONDecodeError: If config file is not valid JSON.
        """
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file {config_file} not found.")
        except json.JSONDecodeError:
            raise json.JSONDecodeError(f"Invalid JSON in configuration file {config_file}.")
    
    def validate_config(self) -> None:
        """
        Validate the configuration.
        
        Raises:
            ValueError: If required configuration is missing or invalid.
        """
        required_fields = [
            'author_info', 'paper_details', 'submission_url',
            'email_settings', 'file_paths'
        ]
        
        for field in required_fields:
            if field not in self.config:
                raise ValueError(f"Missing required configuration field: {field}")
                
        if not os.path.exists(self.config['file_paths']['paper']):
            raise ValueError("Paper file not found at specified path.")
            
        if not os.path.exists(self.config['file_paths']['abstract']):
            raise ValueError("Abstract file not found at specified path.")
    
    def prepare_submission_data(self) -> Dict:
        """
        Prepare the data for submission based on configuration.
        
        Returns:
            Dictionary containing submission data.
        """
        submission_data = {
            'author': self.config['author_info'],
            'paper': self.config['paper_details'],
            'submission_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        return submission_data
    
    def validate_paper_format(self) -> bool:
        """
        Validate the paper format meets ORIC requirements.
        
        Returns:
            bool: True if format is valid, False otherwise.
        """
        paper_path = self.config['file_paths']['paper']
        file_ext = os.path.splitext(paper_path)[1].lower()
        
        allowed_formats = ['.pdf', '.doc', '.docx']
        if file_ext not in allowed_formats:
            return False
            
        # Additional format checks could be added here
        return True
    
    def submit_paper(self) -> Dict:
        """
        Submit the paper to ORIC's presentation system.
        
        Returns:
            Dict: Response from submission server.
            
        Raises:
            ValueError: If paper format is invalid.
            requests.exceptions.RequestException: If submission fails.
        """
        if not self.validate_paper_format():
            raise ValueError("Paper format is not valid for submission.")
            
        submission_data = self.prepare_submission_data()
        files = {
            'paper': open(self.config['file_paths']['paper'], 'rb'),
            'abstract': open(self.config['file_paths']['abstract'], 'rb')
        }
        
        try:
            response = requests.post(
                self.config['submission_url'],
                data=submission_data,
                files=files
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise requests.exceptions.RequestException(f"Submission failed: {str(e)}")
        finally:
            files['paper'].close()
            files['abstract'].close()
    
    def send_confirmation_email(self, submission_response: Dict) -> None:
        """
        Send confirmation email after submission.
        
        Args:
            submission_response: Response from submission server.
            
        Raises:
            smtplib.SMTPException: If email sending fails.
        """
        email_config = self.config['email_settings']
        
        msg = MIMEMultipart()
        msg['From'] = email_config['sender']
        msg['To'] = ', '.join(email_config['recipients'])
        msg['Subject'] = "Research Paper Submission Confirmation"
        
        body = f"""
        Dear {self.config['author_info']['name']},
        
        Your paper titled "{self.config['paper_details']['title']}" has been successfully submitted.
        
        Submission Details:
        - Submission ID: {submission_response.get('submission_id', 'N/A')}
        - Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        - Status: {submission_response.get('status', 'Received')}
        
        Thank you for your submission.
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Attach submission confirmation if available
        if 'confirmation_file' in submission_response:
            with open(submission_response['confirmation_file'], 'rb') as f:
                part = MIMEApplication(f.read(), Name=os.path.basename(submission_response['confirmation_file']))
                part['Content-Disposition'] = f'attachment; filename="{os.path.basename(submission_response["confirmation_file"])}"'
                msg.attach(part)
        
        try:
            with smtplib.SMTP(email_config['smtp_server'], email_config['smtp_port']) as server:
                if email_config.get('use_tls', False):
                    server.starttls()
                server.login(email_config['username'], email_config['password'])
                server.send_message(msg)
        except smtplib.SMTPException as e:
            raise smtplib.SMTPException(f"Failed to send confirmation email: {str(e)}")
    
    def run(self) -> Dict:
        """
        Execute the complete submission process.
        
        Returns:
            Dict: Submission response.
            
        Raises:
            Exception: If any step in the process fails.
        """
        try:
            submission_response = self.submit_paper()
            self.send_confirmation_email(submission_response)
            return submission_response
        except Exception as e:
            raise Exception(f"Paper submission process failed: {str(e)}")

if __name__ == "__main__":
    try:
        automation = PaperSubmissionAutomation()
        result = automation.run()
        print("Submission successful:", result)
    except Exception as e:
        print("Error:", str(e))
```
