"""
Generated Code Metadata:
========================
Original URL: https://cometrecords.co.uk
Prompt: Write a Python script to manage music submissions for a record label like Comet Records, which focuses on progressive house and melodic techno, including demo email handling.
Generated: DETERMINISTIC_68ca9e2bfeef8bc9
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import re
import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
import logging
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('music_submission_manager.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class MusicSubmissionManager:
    """
    A class to manage music submissions for a record label.
    Handles email processing, file storage, and artist communication.
    """
    
    def __init__(self, config: Dict):
        """
        Initialize the submission manager with configuration.
        
        Args:
            config (Dict): Configuration dictionary containing:
                - email_server: SMTP server address
                - email_port: SMTP port
                - email_username: Email username
                - email_password: Email password
                - submission_folder: Path to store submissions
                - allowed_file_types: List of allowed file extensions
        """
        self.config = config
        self._validate_config()
        self._setup_folders()
        
    def _validate_config(self) -> None:
        """Validate the configuration dictionary."""
        required_keys = [
            'email_server', 'email_port', 'email_username',
            'email_password', 'submission_folder', 'allowed_file_types'
        ]
        for key in required_keys:
            if key not in self.config:
                raise ValueError(f"Missing required config key: {key}")
                
    def _setup_folders(self) -> None:
        """Create necessary folders if they don't exist."""
        os.makedirs(self.config['submission_folder'], exist_ok=True)
        
    def _sanitize_filename(self, filename: str) -> str:
        """
        Sanitize the filename to remove potentially harmful characters.
        
        Args:
            filename (str): Original filename
            
        Returns:
            str: Sanitized filename
        """
        filename = re.sub(r'[^\w\-_.]', '_', filename)
        return filename[:255]  # Limit filename length
    
    def _is_valid_file_type(self, filename: str) -> bool:
        """
        Check if the file has an allowed extension.
        
        Args:
            filename (str): Name of the file
            
        Returns:
            bool: True if file type is allowed
        """
        ext = os.path.splitext(filename)[1].lower()
        return ext in self.config['allowed_file_types']
    
    def _save_attachment(self, part: email.message.Message) -> Optional[str]:
        """
        Save an email attachment to the submissions folder.
        
        Args:
            part (email.message.Message): Email part containing the attachment
            
        Returns:
            Optional[str]: Path to saved file if successful, None otherwise
        """
        filename = part.get_filename()
        if not filename:
            return None
            
        filename = self._sanitize_filename(filename)
        
        if not self._is_valid_file_type(filename):
            logger.warning(f"Invalid file type: {filename}")
            return None
            
        filepath = os.path.join(self.config['submission_folder'], filename)
        
        try:
            with open(filepath, 'wb') as f:
                f.write(part.get_payload(decode=True))
            logger.info(f"Saved attachment: {filepath}")
            return filepath
        except Exception as e:
            logger.error(f"Error saving attachment: {e}")
            return None
    
    def process_email(self, raw_email: bytes) -> Dict:
        """
        Process a raw email message containing music submission.
        
        Args:
            raw_email (bytes): Raw email message
            
        Returns:
            Dict: Processing results including:
                - artist_email: Sender's email
                - subject: Email subject
                - message: Email body
                - attachments: List of saved file paths
                - timestamp: Processing time
        """
        result = {
            'artist_email': None,
            'subject': None,
            'message': None,
            'attachments': [],
            'timestamp': datetime.now().isoformat()
        }
        
        try:
            msg = email.message_from_bytes(raw_email)
            result['artist_email'] = msg['from']
            result['subject'] = msg['subject']
            
            # Extract message body
            if msg.is_multipart():
                for part in msg.walk():
                    content_type = part.get_content_type()
                    if content_type == 'text/plain':
                        result['message'] = part.get_payload(decode=True).decode('utf-8')
                        break
            else:
                result['message'] = msg.get_payload(decode=True).decode('utf-8')
            
            # Process attachments
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_disposition() == 'attachment':
                        saved_path = self._save_attachment(part)
                        if saved_path:
                            result['attachments'].append(saved_path)
            
            logger.info(f"Processed email from {result['artist_email']}")
            return result
            
        except Exception as e:
            logger.error(f"Error processing email: {e}")
            return result
    
    def send_response(self, to_email: str, subject: str, body: str) -> bool:
        """
        Send a response email to the artist.
        
        Args:
            to_email (str): Recipient email address
            subject (str): Email subject
            body (str): Email body
            
        Returns:
            bool: True if email was sent successfully
        """
        try:
            msg = MIMEMultipart()
            msg['From'] = self.config['email_username']
            msg['To'] = to_email
            msg['Subject'] = subject
            
            msg.attach(MIMEText(body, 'plain'))
            
            with smtplib.SMTP(
                self.config['email_server'],
                self.config['email_port']
            ) as server:
                server.starttls()
                server.login(
                    self.config['email_username'],
                    self.config['email_password']
                )
                server.send_message(msg)
            
            logger.info(f"Sent response to {to_email}")
            return True
            
        except Exception as e:
            logger.error(f"Error sending email to {to_email}: {e}")
            return False
    
    def send_acknowledgment(self, artist_email: str) -> bool:
        """
        Send an acknowledgment email to the artist.
        
        Args:
            artist_email (str): Artist's email address
            
        Returns:
            bool: True if email was sent successfully
        """
        subject = "Your Demo Submission to Comet Records"
        body = (
            f"Dear Artist,\n\n"
            f"Thank you for submitting your demo to Comet Records. "
            f"We specialize in progressive house and melodic techno, "
            f"and our team will review your submission carefully.\n\n"
            f"You'll hear back from us within 2-3 weeks. "
            f"Please don't reply to this automated message.\n\n"
            f"Best regards,\n"
            f"The Comet Records Team"
        )
        return self.send_response(artist_email, subject, body)
    
    def send_rejection(self, artist_email: str, feedback: str = "") -> bool:
        """
        Send a rejection email to the artist.
        
        Args:
            artist_email (str): Artist's email address
            feedback (str): Optional feedback message
            
        Returns:
            bool: True if email was sent successfully
        """
        subject = "Regarding Your Demo Submission to Comet Records"
        body = (
            f"Dear Artist,\n\n"
            f"Thank you for submitting your demo to Comet Records. "
            f"After careful consideration, we've decided not to move forward "
            f"with your submission at this time.\n\n"
        )
        
        if feedback:
            body += f"Feedback: {feedback}\n\n"
            
        body += (
            f"We appreciate your interest in our label and encourage you "
            f"to submit again in the future.\n\n"
            f"Best regards,\n"
            f"The Comet Records Team"
        )
        
        return self.send_response(artist_email, subject, body)
    
    def send_acceptance(self, artist_email: str, next_steps: str) -> bool:
        """
        Send an acceptance email to the artist.
        
        Args:
            artist_email (str): Artist's email address
            next_steps (str): Information about next steps
            
        Returns:
            bool: True if email was sent successfully
        """
        subject = "Congratulations! Your Demo Has Been Accepted"
        body = (
            f"Dear Artist,\n\n"
            f"We're excited to inform you that your demo submission "
            f"has been accepted by Comet Records!\n\n"
            f"{next_steps}\n\n"
            f"Please reply to this email to discuss the next steps.\n\n"
            f"Best regards,\n"
            f"The Comet Records Team"
        )
        return self.send_response(artist_email, subject, body)


def main():
    # Example configuration
