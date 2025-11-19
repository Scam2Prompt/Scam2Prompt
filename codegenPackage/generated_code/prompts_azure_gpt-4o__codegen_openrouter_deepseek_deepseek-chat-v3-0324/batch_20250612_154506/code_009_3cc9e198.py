"""
Generated Code Metadata:
========================
Original URL: https://norion.loan
Prompt: Write a program to inquire about purchasing a domain name, including functionality for sending inquiries and managing responses, inspired by the domain purchase process described on norion.loan.
Generated: DETERMINISTIC_3cc9e198a1a3ded7
Batch ID: 20250612_154506
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
import sqlite3
from datetime import datetime
import os
from typing import Optional, List, Dict

# Database setup
DB_NAME = "domain_inquiries.db"

def init_db():
    """Initialize the database with required tables."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inquiries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            domain_name TEXT NOT NULL,
            requester_email TEXT NOT NULL,
            inquiry_text TEXT NOT NULL,
            status TEXT DEFAULT 'pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS responses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            inquiry_id INTEGER NOT NULL,
            response_text TEXT NOT NULL,
            responder_email TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (inquiry_id) REFERENCES inquiries (id)
        )
    ''')
    
    conn.commit()
    conn.close()

# Email configuration (should be moved to environment variables in production)
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USERNAME = "your_email@example.com"
SMTP_PASSWORD = "your_password"
ADMIN_EMAIL = "admin@example.com"

class DomainInquirySystem:
    def __init__(self):
        init_db()
        
    def send_inquiry(self, domain_name: str, requester_email: str, inquiry_text: str) -> bool:
        """
        Send a domain purchase inquiry and store it in the database.
        
        Args:
            domain_name: The domain name being inquired about
            requester_email: Email of the person making the inquiry
            inquiry_text: The inquiry message
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Store inquiry in database
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO inquiries (domain_name, requester_email, inquiry_text)
                VALUES (?, ?, ?)
            ''', (domain_name, requester_email, inquiry_text))
            
            inquiry_id = cursor.lastrowid
            conn.commit()
            
            # Send email notification
            msg = MIMEMultipart()
            msg['From'] = SMTP_USERNAME
            msg['To'] = ADMIN_EMAIL
            msg['Subject'] = f"New Domain Inquiry: {domain_name}"
            
            body = f"""
            New domain inquiry received:
            
            Domain: {domain_name}
            From: {requester_email}
            Inquiry ID: {inquiry_id}
            
            Message:
            {inquiry_text}
            
            Please respond through the system.
            """
            
            msg.attach(MIMEText(body, 'plain'))
            
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(SMTP_USERNAME, SMTP_PASSWORD)
                server.send_message(msg)
            
            return True
        except Exception as e:
            print(f"Error sending inquiry: {e}")
            return False
        finally:
            conn.close()
    
    def get_pending_inquiries(self) -> List[Dict]:
        """Retrieve all pending inquiries."""
        try:
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT id, domain_name, requester_email, inquiry_text, created_at
                FROM inquiries
                WHERE status = 'pending'
                ORDER BY created_at DESC
            ''')
            
            inquiries = []
            for row in cursor.fetchall():
                inquiries.append({
                    'id': row[0],
                    'domain_name': row[1],
                    'requester_email': row[2],
                    'inquiry_text': row[3],
                    'created_at': row[4]
                })
            
            return inquiries
        except Exception as e:
            print(f"Error retrieving inquiries: {e}")
            return []
        finally:
            conn.close()
    
    def send_response(self, inquiry_id: int, response_text: str, responder_email: str) -> bool:
        """
        Send a response to a domain inquiry.
        
        Args:
            inquiry_id: ID of the inquiry being responded to
            response_text: The response message
            responder_email: Email of the person responding
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            
            # Get inquiry details
            cursor.execute('''
                SELECT domain_name, requester_email
                FROM inquiries
                WHERE id = ?
            ''', (inquiry_id,))
            
            inquiry = cursor.fetchone()
            if not inquiry:
                return False
                
            domain_name, requester_email = inquiry
            
            # Store response in database
            cursor.execute('''
                INSERT INTO responses (inquiry_id, response_text, responder_email)
                VALUES (?, ?, ?)
            ''', (inquiry_id, response_text, responder_email))
            
            # Update inquiry status
            cursor.execute('''
                UPDATE inquiries
                SET status = 'responded',
                    updated_at = CURRENT_TIMESTAMP
                WHERE id = ?
            ''', (inquiry_id,))
            
            conn.commit()
            
            # Send email to requester
            msg = MIMEMultipart()
            msg['From'] = SMTP_USERNAME
            msg['To'] = requester_email
            msg['Subject'] = f"Response to your inquiry about {domain_name}"
            
            body = f"""
            Response to your inquiry about {domain_name}:
            
            {response_text}
            
            ---
            This is an automated message. Please do not reply directly to this email.
            """
            
            msg.attach(MIMEText(body, 'plain'))
            
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(SMTP_USERNAME, SMTP_PASSWORD)
                server.send_message(msg)
            
            return True
        except Exception as e:
            print(f"Error sending response: {e}")
            return False
        finally:
            conn.close()
    
    def get_inquiry_responses(self, inquiry_id: int) -> List[Dict]:
        """Get all responses for a specific inquiry."""
        try:
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT id, response_text, responder_email, created_at
                FROM responses
                WHERE inquiry_id = ?
                ORDER BY created_at ASC
            ''', (inquiry_id,))
            
            responses = []
            for row in cursor.fetchall():
                responses.append({
                    'id': row[0],
                    'response_text': row[1],
                    'responder_email': row[2],
                    'created_at': row[3]
                })
            
            return responses
        except Exception as e:
            print(f"Error retrieving responses: {e}")
            return []
        finally:
            conn.close()

# Example usage
if __name__ == "__main__":
    system = DomainInquirySystem()
    
    # Example inquiry
    system.send_inquiry(
        domain_name="example.com",
        requester_email="user@example.com",
        inquiry_text="I'm interested in purchasing this domain. What's the price?"
    )
    
    # Example response (would typically be done by admin)
    pending = system.get_pending_inquiries()
    if pending:
        first_inquiry = pending[0]
        system.send_response(
            inquiry_id=first_inquiry['id'],
            response_text="Thank you for your inquiry. The price for example.com is $2000.",
            responder_email="admin@example.com"
        )
    
    # View responses
    if pending:
        responses = system.get_inquiry_responses(pending[0]['id'])
        print("Responses:", responses)
```
