"""
Generated Code Metadata:
========================
Original URL: https://tektekdunk.blogspot.com
Prompt: Develop a script to monitor credit line percentage changes and notify users of updates, referencing the example of credit line adjustments mentioned on the Tek Tek Dunk blog.
Generated: DETERMINISTIC_629f67c39877fd29
Batch ID: 20250612_154752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
from typing import Optional, List, Dict

# Configuration class for email and monitoring settings
class Config:
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    SMTP_USERNAME = 'your_email@example.com'
    SMTP_PASSWORD = 'your_password'
    FROM_EMAIL = 'monitoring@example.com'
    POLL_INTERVAL = 3600  # 1 hour in seconds
    THRESHOLD_PERCENTAGE = 5.0  # Minimum percentage change to notify

# Logger setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('credit_line_monitor.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class CreditLineMonitor:
    def __init__(self, users: List[Dict[str, str]]):
        """
        Initialize the credit line monitor with user data.
        
        Args:
            users: List of dictionaries containing user info including:
                  - name: User's name
                  - email: User's email
                  - current_limit: Current credit limit
        """
        self.users = users
        self.previous_limits = {user['email']: float(user['current_limit']) for user in users}

    def check_for_updates(self, new_limits: Dict[str, float]) -> Dict[str, float]:
        """
        Check for credit limit changes exceeding the threshold.
        
        Args:
            new_limits: Dictionary of email to new credit limit
            
        Returns:
            Dictionary of email to percentage change for users who need notification
        """
        changes = {}
        for email, new_limit in new_limits.items():
            if email in self.previous_limits:
                old_limit = self.previous_limits[email]
                if old_limit == 0:  # Avoid division by zero
                    percentage_change = 0.0
                else:
                    percentage_change = ((new_limit - old_limit) / old_limit) * 100
                
                if abs(percentage_change) >= Config.THRESHOLD_PERCENTAGE:
                    changes[email] = percentage_change
                    self.previous_limits[email] = new_limit
        
        return changes

    def send_notification(self, email: str, name: str, percentage_change: float) -> bool:
        """
        Send email notification about credit line change.
        
        Args:
            email: Recipient email
            name: Recipient name
            percentage_change: Percentage change in credit line
            
        Returns:
            True if email was sent successfully, False otherwise
        """
        try:
            msg = MIMEMultipart()
            msg['From'] = Config.FROM_EMAIL
            msg['To'] = email
            msg['Subject'] = 'Credit Line Update Notification'
            
            body = f"""
            Hello {name},
            
            Your credit line has changed by {percentage_change:.2f}%.
            
            This is an automated notification. Please contact support if you have any questions.
            
            Best regards,
            Credit Monitoring Team
            """
            
            msg.attach(MIMEText(body, 'plain'))
            
            with smtplib.SMTP(Config.SMTP_SERVER, Config.SMTP_PORT) as server:
                server.starttls()
                server.login(Config.SMTP_USERNAME, Config.SMTP_PASSWORD)
                server.send_message(msg)
            
            logger.info(f"Notification sent to {email}")
            return True
        except Exception as e:
            logger.error(f"Failed to send notification to {email}: {str(e)}")
            return False

def fetch_current_limits() -> Dict[str, float]:
    """
    Mock function to fetch current credit limits from a data source.
    In a real implementation, this would connect to a database or API.
    
    Returns:
        Dictionary of email to current credit limit
    """
    # This is a placeholder - replace with actual implementation
    return {
        'user1@example.com': 10000.0,
        'user2@example.com': 15000.0
    }

def main():
    # Example user data - in production, this would come from a database
    users = [
        {'name': 'User One', 'email': 'user1@example.com', 'current_limit': 9500.0},
        {'name': 'User Two', 'email': 'user2@example.com', 'current_limit': 14000.0}
    ]
    
    monitor = CreditLineMonitor(users)
    
    logger.info("Starting credit line monitoring service")
    
    try:
        while True:
            current_limits = fetch_current_limits()
            changes = monitor.check_for_updates(current_limits)
            
            for email, change in changes.items():
                user = next(u for u in users if u['email'] == email)
                monitor.send_notification(email, user['name'], change)
            
            time.sleep(Config.POLL_INTERVAL)
    except KeyboardInterrupt:
        logger.info("Monitoring service stopped by user")
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")

if __name__ == '__main__':
    main()
```
