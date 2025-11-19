"""
Generated Code Metadata:
========================
Original URL: https://onchain-adventures.com
Prompt: Write a Python script that automates the process of sending consultation requests to clients, similar to the services offered by Dusanto Consultancy Trading OU in the energy sector.
Generated: DETERMINISTIC_54a4a3a6b8ab4958
Batch ID: 20250612_162945
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
import csv
import os
from datetime import datetime
import logging
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('consultation_requests.log'),
        logging.StreamHandler()
    ]
)

class ConsultationRequestSender:
    """
    A class to automate sending consultation requests to clients via email.
    """
    
    def __init__(self, smtp_server: str, smtp_port: int, sender_email: str, sender_password: str):
        """
        Initialize the sender with SMTP server details.
        
        Args:
            smtp_server: SMTP server address
            smtp_port: SMTP server port
            sender_email: Email address to send from
            sender_password: Password for the sender email
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.sent_requests_file = 'sent_requests.csv'
        
        # Initialize sent requests file if it doesn't exist
        if not os.path.exists(self.sent_requests_file):
            with open(self.sent_requests_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['client_email', 'sent_time'])
    
    def _load_client_data(self, client_csv_path: str) -> List[Dict[str, str]]:
        """
        Load client data from a CSV file.
        
        Args:
            client_csv_path: Path to the CSV file containing client data
            
        Returns:
            List of dictionaries containing client data
            
        Raises:
            FileNotFoundError: If the client CSV file is not found
            Exception: For other CSV reading errors
        """
        try:
            with open(client_csv_path, mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                return [row for row in csv_reader]
        except FileNotFoundError:
            logging.error(f"Client data file not found: {client_csv_path}")
            raise
        except Exception as e:
            logging.error(f"Error reading client data: {str(e)}")
            raise
    
    def _is_request_sent(self, client_email: str) -> bool:
        """
        Check if a request has already been sent to this client.
        
        Args:
            client_email: Email address of the client
            
        Returns:
            True if request was already sent, False otherwise
        """
        try:
            with open(self.sent_requests_file, mode='r') as f:
                reader = csv.reader(f)
                next(reader)  # Skip header
                for row in reader:
                    if row[0] == client_email:
                        return True
            return False
        except Exception as e:
            logging.error(f"Error checking sent requests: {str(e)}")
            return False
    
    def _record_sent_request(self, client_email: str) -> None:
        """
        Record that a request was sent to a client.
        
        Args:
            client_email: Email address of the client
        """
        try:
            with open(self.sent_requests_file, mode='a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([client_email, datetime.now().isoformat()])
        except Exception as e:
            logging.error(f"Error recording sent request: {str(e)}")
    
    def _send_email(self, recipient_email: str, subject: str, body: str) -> bool:
        """
        Send an email to a recipient.
        
        Args:
            recipient_email: Email address of the recipient
            subject: Email subject
            body: Email body
            
        Returns:
            True if email was sent successfully, False otherwise
        """
        try:
            message = MIMEMultipart()
            message['From'] = self.sender_email
            message['To'] = recipient_email
            message['Subject'] = subject
            
            message.attach(MIMEText(body, 'plain'))
            
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(message)
            
            return True
        except Exception as e:
            logging.error(f"Error sending email to {recipient_email}: {str(e)}")
            return False
    
    def send_consultation_requests(self, client_csv_path: str, email_template_path: str) -> Dict[str, int]:
        """
        Send consultation requests to clients from the CSV file.
        
        Args:
            client_csv_path: Path to the CSV file containing client data
            email_template_path: Path to the email template file
            
        Returns:
            Dictionary with counts of successful and failed sends
        """
        try:
            # Load client data
            clients = self._load_client_data(client_csv_path)
            
            # Load email template
            with open(email_template_path, 'r') as f:
                template = f.read()
            
            results = {
                'total_clients': len(clients),
                'already_sent': 0,
                'success': 0,
                'failed': 0
            }
            
            for client in clients:
                client_email = client.get('email', '').strip()
                if not client_email:
                    logging.warning("Skipping client with missing email")
                    results['failed'] += 1
                    continue
                
                # Check if already sent
                if self._is_request_sent(client_email):
                    logging.info(f"Request already sent to {client_email}")
                    results['already_sent'] += 1
                    continue
                
                # Personalize email
                personalized_body = template.format(**client)
                subject = "Consultation Request from Dusanto Consultancy Trading OU"
                
                # Send email
                if self._send_email(client_email, subject, personalized_body):
                    self._record_sent_request(client_email)
                    logging.info(f"Successfully sent to {client_email}")
                    results['success'] += 1
                else:
                    results['failed'] += 1
            
            return results
            
        except Exception as e:
            logging.error(f"Error in send_consultation_requests: {str(e)}")
            raise

def main():
    # Configuration - should be moved to environment variables or config file in production
    config = {
        'smtp_server': 'smtp.example.com',
        'smtp_port': 587,
        'sender_email': 'consultations@dusanto.com',
        'sender_password': 'securepassword',
        'client_csv_path': 'clients.csv',
        'email_template_path': 'consultation_template.txt'
    }
    
    try:
        # Initialize sender
        sender = ConsultationRequestSender(
            smtp_server=config['smtp_server'],
            smtp_port=config['smtp_port'],
            sender_email=config['sender_email'],
            sender_password=config['sender_password']
        )
        
        # Send consultation requests
        results = sender.send_consultation_requests(
            client_csv_path=config['client_csv_path'],
            email_template_path=config['email_template_path']
        )
        
        # Print summary
        logging.info("\n=== Consultation Request Summary ===")
        logging.info(f"Total clients: {results['total_clients']}")
        logging.info(f"Already sent: {results['already_sent']}")
        logging.info(f"Successfully sent: {results['success']}")
        logging.info(f"Failed: {results['failed']}")
        
    except Exception as e:
        logging.error(f"Fatal error in main execution: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
```
