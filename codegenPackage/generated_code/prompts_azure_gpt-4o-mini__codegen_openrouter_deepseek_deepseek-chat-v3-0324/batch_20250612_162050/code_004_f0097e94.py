"""
Generated Code Metadata:
========================
Original URL: https://carolcrespo.com.br
Prompt: Create a program that automates the process of sending workout plans to users after they complete an assessment, reflecting the steps outlined by Carol Crespo's consulting service.
Generated: DETERMINISTIC_f0097e94fdb1e605
Batch ID: 20250612_162050
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
import json
import os
from datetime import datetime
import logging
from typing import Dict, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('workout_planner.log'),
        logging.StreamHandler()
    ]
)

class WorkoutPlanSender:
    """
    A class to handle the automation of sending workout plans to users after assessment completion.
    """
    
    def __init__(self, config_path: str = 'config.json'):
        """
        Initialize the WorkoutPlanSender with configuration.
        
        Args:
            config_path (str): Path to the configuration file. Defaults to 'config.json'.
        """
        self.config = self._load_config(config_path)
        self.smtp_server = self.config.get('smtp_server')
        self.smtp_port = self.config.get('smtp_port')
        self.sender_email = self.config.get('sender_email')
        self.sender_password = self.config.get('sender_password')
        self.workout_plans_dir = self.config.get('workout_plans_dir', 'workout_plans')
        
        # Validate configuration
        if not all([self.smtp_server, self.smtp_port, self.sender_email, self.sender_password]):
            raise ValueError("Missing required configuration parameters")
            
        # Create workout plans directory if it doesn't exist
        os.makedirs(self.workout_plans_dir, exist_ok=True)
    
    def _load_config(self, config_path: str) -> Dict:
        """
        Load configuration from JSON file.
        
        Args:
            config_path (str): Path to the configuration file.
            
        Returns:
            Dict: Configuration dictionary.
            
        Raises:
            FileNotFoundError: If config file doesn't exist.
            json.JSONDecodeError: If config file is not valid JSON.
        """
        try:
            with open(config_path) as f:
                return json.load(f)
        except FileNotFoundError:
            logging.error(f"Configuration file not found: {config_path}")
            raise
        except json.JSONDecodeError:
            logging.error(f"Invalid JSON in configuration file: {config_path}")
            raise
    
    def _get_workout_plan(self, user_id: str) -> Optional[str]:
        """
        Retrieve workout plan for a user from the workout plans directory.
        
        Args:
            user_id (str): Unique identifier for the user.
            
        Returns:
            Optional[str]: The workout plan content if found, None otherwise.
        """
        plan_path = os.path.join(self.workout_plans_dir, f"{user_id}.txt")
        try:
            with open(plan_path, 'r') as f:
                return f.read()
        except FileNotFoundError:
            logging.warning(f"No workout plan found for user {user_id}")
            return None
    
    def _send_email(self, recipient_email: str, subject: str, body: str) -> bool:
        """
        Send an email to the recipient.
        
        Args:
            recipient_email (str): Email address of the recipient.
            subject (str): Email subject.
            body (str): Email body content.
            
        Returns:
            bool: True if email was sent successfully, False otherwise.
        """
        message = MIMEMultipart()
        message['From'] = self.sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))
        
        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(message)
            logging.info(f"Email sent successfully to {recipient_email}")
            return True
        except smtplib.SMTPException as e:
            logging.error(f"Failed to send email to {recipient_email}: {str(e)}")
            return False
    
    def process_assessment_completion(self, user_id: str, user_email: str) -> bool:
        """
        Process a completed assessment and send the workout plan to the user.
        
        Args:
            user_id (str): Unique identifier for the user.
            user_email (str): Email address of the user.
            
        Returns:
            bool: True if the workout plan was sent successfully, False otherwise.
        """
        # Get the workout plan
        workout_plan = self._get_workout_plan(user_id)
        if not workout_plan:
            logging.error(f"No workout plan available for user {user_id}")
            return False
        
        # Prepare email content
        subject = "Your Personalized Workout Plan"
        body = f"""Hello,\n\nThank you for completing your assessment. Here is your personalized workout plan:\n\n{workout_plan}\n\nBest regards,\nCarol Crespo's Fitness Team"""
        
        # Send the email
        return self._send_email(user_email, subject, body)
    
    def log_activity(self, user_id: str, action: str, status: str) -> None:
        """
        Log an activity for audit purposes.
        
        Args:
            user_id (str): Unique identifier for the user.
            action (str): Description of the action performed.
            status (str): Status of the action (success/failure).
        """
        timestamp = datetime.now().isoformat()
        log_entry = {
            'timestamp': timestamp,
            'user_id': user_id,
            'action': action,
            'status': status
        }
        
        log_file = os.path.join(self.workout_plans_dir, 'activity_log.json')
        try:
            with open(log_file, 'a') as f:
                f.write(json.dumps(log_entry) + '\n')
        except IOError as e:
            logging.error(f"Failed to log activity: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        sender = WorkoutPlanSender()
        
        # Simulate processing a completed assessment
        user_id = "user123"
        user_email = "client@example.com"
        
        success = sender.process_assessment_completion(user_id, user_email)
        if success:
            sender.log_activity(user_id, "workout_plan_sent", "success")
        else:
            sender.log_activity(user_id, "workout_plan_sent", "failed")
            
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
```
