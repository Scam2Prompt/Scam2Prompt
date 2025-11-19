"""
Generated Code Metadata:
========================
Original URL: https://www.mooveweb.com
Prompt: Create a script to automate client feedback collection for services like video production and social media management, tailored for a marketing agency like MoOve Marketing.
Generated: DETERMINISTIC_a9351922c64c265d
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
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from typing import List, Dict, Optional

class FeedbackCollector:
    """
    A class to automate client feedback collection for marketing services.
    Handles survey generation, distribution, and response collection.
    """
    
    def __init__(self, config: Dict):
        """
        Initialize the FeedbackCollector with configuration.
        
        Args:
            config (Dict): Configuration dictionary containing:
                - 'email_settings': SMTP server details and credentials
                - 'survey_questions': List of survey questions
                - 'clients_csv': Path to CSV file with client details
                - 'output_dir': Directory to store feedback results
        """
        self.config = config
        self.clients = self._load_clients()
        self.ensure_output_dir()
        
    def _load_clients(self) -> List[Dict]:
        """
        Load client data from CSV file.
        
        Returns:
            List[Dict]: List of client dictionaries with contact info
            
        Raises:
            FileNotFoundError: If clients CSV file doesn't exist
            ValueError: If CSV file is malformed
        """
        try:
            with open(self.config['clients_csv'], mode='r') as file:
                reader = csv.DictReader(file)
                return [row for row in reader]
        except FileNotFoundError:
            raise FileNotFoundError(f"Client CSV file not found at {self.config['clients_csv']}")
        except Exception as e:
            raise ValueError(f"Error reading client CSV: {str(e)}")
    
    def ensure_output_dir(self) -> None:
        """Ensure the output directory for feedback results exists."""
        os.makedirs(self.config['output_dir'], exist_ok=True)
    
    def generate_survey_email(self, client: Dict) -> str:
        """
        Generate HTML email content with survey questions.
        
        Args:
            client (Dict): Client information including name
            
        Returns:
            str: HTML formatted email content
        """
        questions_html = "\n".join(
            f"<p><b>Q{i+1}:</b> {q}</p>" 
            for i, q in enumerate(self.config['survey_questions'])
        )
        
        return f"""
        <html>
            <body>
                <p>Dear {client['name']},</p>
                <p>Thank you for working with MoOve Marketing! We'd love to hear your feedback about our services.</p>
                {questions_html}
                <p>Please reply to this email with your responses.</p>
                <p>Best regards,<br>The MoOve Marketing Team</p>
            </body>
        </html>
        """
    
    def send_survey_emails(self) -> None:
        """
        Send survey emails to all clients.
        
        Raises:
            smtplib.SMTPException: If email sending fails
        """
        email_settings = self.config['email_settings']
        
        try:
            with smtplib.SMTP(email_settings['smtp_server'], email_settings['smtp_port']) as server:
                server.starttls()
                server.login(email_settings['username'], email_settings['password'])
                
                for client in self.clients:
                    msg = MIMEMultipart()
                    msg['From'] = email_settings['from_email']
                    msg['To'] = client['email']
                    msg['Subject'] = "MoOve Marketing Service Feedback Request"
                    
                    body = self.generate_survey_email(client)
                    msg.attach(MIMEText(body, 'html'))
                    
                    server.send_message(msg)
                    print(f"Survey sent to {client['email']}")
                    
        except smtplib.SMTPException as e:
            raise smtplib.SMTPException(f"Failed to send surveys: {str(e)}")
    
    def process_response(self, email_content: str, client_email: str) -> None:
        """
        Process a client's email response and save to feedback file.
        
        Args:
            email_content (str): The full email response content
            client_email (str): The client's email address
            
        Raises:
            ValueError: If client email is not found in records
        """
        client = next((c for c in self.clients if c['email'] == client_email), None)
        if not client:
            raise ValueError(f"No client found with email {client_email}")
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{client['name'].replace(' ', '_')}_{timestamp}.txt"
        filepath = os.path.join(self.config['output_dir'], filename)
        
        with open(filepath, 'w') as f:
            f.write(f"Client: {client['name']}\n")
            f.write(f"Email: {client_email}\n")
            f.write(f"Date: {timestamp}\n\n")
            f.write("Feedback:\n")
            f.write(email_content)
    
    def generate_report(self) -> str:
        """
        Generate a summary report of collected feedback.
        
        Returns:
            str: Path to the generated report file
        """
        report_path = os.path.join(self.config['output_dir'], "feedback_summary.csv")
        
        feedback_files = [
            f for f in os.listdir(self.config['output_dir']) 
            if f.endswith('.txt') and f != "feedback_summary.csv"
        ]
        
        with open(report_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Client Name', 'Email', 'Date', 'Feedback Excerpt'])
            
            for filename in feedback_files:
                filepath = os.path.join(self.config['output_dir'], filename)
                with open(filepath, 'r') as f:
                    content = f.read()
                    lines = content.split('\n')
                    client_name = lines[0].split(': ')[1]
                    email = lines[1].split(': ')[1]
                    date = lines[2].split(': ')[1]
                    excerpt = content[:200] + "..." if len(content) > 200 else content
                    
                    writer.writerow([client_name, email, date, excerpt])
        
        return report_path

# Example Configuration
if __name__ == "__main__":
    config = {
        'email_settings': {
            'smtp_server': 'smtp.example.com',
            'smtp_port': 587,
            'username': 'your_email@example.com',
            'password': 'your_password',
            'from_email': 'feedback@moovemarketing.com'
        },
        'survey_questions': [
            "How satisfied are you with our video production services?",
            "Did our social media management meet your expectations?",
            "What could we improve in our services?",
            "Would you recommend MoOve Marketing to others?"
        ],
        'clients_csv': 'clients.csv',
        'output_dir': 'feedback_results'
    }
    
    try:
        collector = FeedbackCollector(config)
        collector.send_survey_emails()
        print("Surveys sent successfully!")
    except Exception as e:
        print(f"Error: {str(e)}")
```
