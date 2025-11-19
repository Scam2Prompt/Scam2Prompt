"""
Generated Code Metadata:
========================
Original URL: https://wordpress.armelin.media
Prompt: Generate a Python script to manage subscriptions for the Études Newsletter, ensuring users receive exclusive design insights and case studies, as highlighted on the Armelin Media site.
Generated: DETERMINISTIC_3704a710af99a8e7
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import Optional, List
from datetime import datetime
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class SubscriptionManager:
    """Manages newsletter subscriptions for Études Newsletter."""
    
    def __init__(self, db_path: str = 'subscriptions.db'):
        """Initialize the SubscriptionManager with a SQLite database.
        
        Args:
            db_path: Path to the SQLite database file.
        """
        self.db_path = db_path
        self._init_db()
        
    def _init_db(self) -> None:
        """Initialize the database with required tables if they don't exist."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS subscribers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email TEXT UNIQUE NOT NULL,
                    name TEXT,
                    subscribed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    is_active BOOLEAN DEFAULT 1,
                    last_notified TIMESTAMP
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS newsletters (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    content TEXT NOT NULL,
                    sent_at TIMESTAMP
                )
            ''')
            conn.commit()
    
    def add_subscriber(self, email: str, name: Optional[str] = None) -> bool:
        """Add a new subscriber to the newsletter.
        
        Args:
            email: Subscriber's email address.
            name: Optional subscriber's name.
            
        Returns:
            bool: True if subscription was successful, False if email already exists.
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    'INSERT INTO subscribers (email, name) VALUES (?, ?)',
                    (email, name)
                )
                conn.commit()
                logger.info(f"Added new subscriber: {email}")
                return True
        except sqlite3.IntegrityError:
            logger.warning(f"Subscription attempt for existing email: {email}")
            return False
        except Exception as e:
            logger.error(f"Error adding subscriber {email}: {str(e)}")
            raise
    
    def remove_subscriber(self, email: str) -> bool:
        """Remove a subscriber from the newsletter (soft delete).
        
        Args:
            email: Subscriber's email address.
            
        Returns:
            bool: True if unsubscription was successful, False if email not found.
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    'UPDATE subscribers SET is_active = 0 WHERE email = ?',
                    (email,)
                )
                if cursor.rowcount == 0:
                    logger.warning(f"Unsubscribe attempt for non-existent email: {email}")
                    return False
                conn.commit()
                logger.info(f"Unsubscribed: {email}")
                return True
        except Exception as e:
            logger.error(f"Error unsubscribing {email}: {str(e)}")
            raise
    
    def get_active_subscribers(self) -> List[dict]:
        """Get all active subscribers.
        
        Returns:
            List of dictionaries containing subscriber information.
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute(
                    'SELECT email, name, subscribed_at FROM subscribers WHERE is_active = 1'
                )
                return [dict(row) for row in cursor.fetchall()]
        except Exception as e:
            logger.error(f"Error fetching active subscribers: {str(e)}")
            raise
    
    def add_newsletter(self, title: str, content: str) -> int:
        """Add a new newsletter to be sent.
        
        Args:
            title: Newsletter title.
            content: Newsletter content.
            
        Returns:
            int: ID of the created newsletter.
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    'INSERT INTO newsletters (title, content) VALUES (?, ?)',
                    (title, content)
                )
                newsletter_id = cursor.lastrowid
                conn.commit()
                logger.info(f"Added new newsletter: {title}")
                return newsletter_id
        except Exception as e:
            logger.error(f"Error adding newsletter: {str(e)}")
            raise
    
    def send_newsletter(self, newsletter_id: int) -> bool:
        """Send a newsletter to all active subscribers.
        
        Args:
            newsletter_id: ID of the newsletter to send.
            
        Returns:
            bool: True if sending was successful.
        """
        try:
            # Get newsletter content
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute(
                    'SELECT title, content FROM newsletters WHERE id = ?',
                    (newsletter_id,)
                )
                newsletter = cursor.fetchone()
                if not newsletter:
                    logger.error(f"Newsletter with ID {newsletter_id} not found")
                    return False
                
                # Get active subscribers
                subscribers = self.get_active_subscribers()
                if not subscribers:
                    logger.warning("No active subscribers to send newsletter to")
                    return False
                
                # Email configuration
                smtp_server = os.getenv('SMTP_SERVER')
                smtp_port = int(os.getenv('SMTP_PORT', 587))
                smtp_username = os.getenv('SMTP_USERNAME')
                smtp_password = os.getenv('SMTP_PASSWORD')
                from_email = os.getenv('FROM_EMAIL')
                
                if not all([smtp_server, smtp_username, smtp_password, from_email]):
                    logger.error("Missing email configuration in environment variables")
                    return False
                
                # Connect to SMTP server
                with smtplib.SMTP(smtp_server, smtp_port) as server:
                    server.starttls()
                    server.login(smtp_username, smtp_password)
                    
                    # Prepare email
                    subject = f"Études Newsletter: {newsletter['title']}"
                    
                    for subscriber in subscribers:
                        # Create message
                        msg = MIMEMultipart()
                        msg['From'] = from_email
                        msg['To'] = subscriber['email']
                        msg['Subject'] = subject
                        
                        # Personalize content
                        greeting = f"Hello {subscriber.get('name', 'subscriber')},\n\n"
                        body = greeting + newsletter['content']
                        msg.attach(MIMEText(body, 'plain'))
                        
                        # Send email
                        server.sendmail(from_email, subscriber['email'], msg.as_string())
                        logger.info(f"Sent newsletter to {subscriber['email']}")
                    
                    # Update newsletter sent_at timestamp
                    cursor.execute(
                        'UPDATE newsletters SET sent_at = CURRENT_TIMESTAMP WHERE id = ?',
                        (newsletter_id,)
                    )
                    conn.commit()
                    
                    # Update last_notified for subscribers
                    cursor.executemany(
                        'UPDATE subscribers SET last_notified = CURRENT_TIMESTAMP WHERE email = ?',
                        [(subscriber['email'],) for subscriber in subscribers]
                    )
                    conn.commit()
                    
                    return True
        except Exception as e:
            logger.error(f"Error sending newsletter: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    manager = SubscriptionManager()
    
    # Add a subscriber
    manager.add_subscriber("example@example.com", "John Doe")
    
    # Add a newsletter
    newsletter_id = manager.add_newsletter(
        "Design Insights Q3 2023",
        "In this edition, we explore the latest trends in minimalist design..."
    )
    
    # Send the newsletter
    manager.send_newsletter(newsletter_id)
```
