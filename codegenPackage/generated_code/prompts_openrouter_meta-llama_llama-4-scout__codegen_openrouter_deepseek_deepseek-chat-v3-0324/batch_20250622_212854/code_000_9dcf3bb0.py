"""
Generated Code Metadata:
========================
Original URL: https://ikogwelimited.com
Prompt: Write a Python script to manage student visa applications for studying abroad, including tracking application status and sending reminders for required documents, considering the services offered by Ikogwe International Limited.
Generated: DETERMINISTIC_9dcf3bb07b045fb8
Batch ID: 20250622_212854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Dict, List, Optional, Tuple

# Configuration file path
CONFIG_FILE = "config.json"

class VisaApplicationManager:
    """
    Manages student visa applications including tracking status and sending reminders.
    """
    
    def __init__(self):
        """
        Initialize the application manager with configuration and data storage.
        """
        self.config = self._load_config()
        self.applications_file = self.config.get("applications_file", "applications.json")
        self.applications = self._load_applications()
        
    def _load_config(self) -> Dict:
        """
        Load configuration from JSON file.
        
        Returns:
            Dict: Configuration dictionary
            
        Raises:
            FileNotFoundError: If config file doesn't exist
            json.JSONDecodeError: If config file is malformed
        """
        try:
            with open(CONFIG_FILE, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError("Configuration file not found")
        except json.JSONDecodeError:
            raise ValueError("Invalid configuration file format")
    
    def _load_applications(self) -> Dict:
        """
        Load applications from JSON file.
        
        Returns:
            Dict: Applications data
            
        Raises:
            FileNotFoundError: If applications file doesn't exist (returns empty dict)
            json.JSONDecodeError: If applications file is malformed
        """
        try:
            with open(self.applications_file, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            raise ValueError("Invalid applications file format")
    
    def _save_applications(self) -> None:
        """
        Save applications to JSON file.
        
        Raises:
            IOError: If file cannot be written
        """
        try:
            with open(self.applications_file, "w") as f:
                json.dump(self.applications, f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save applications: {str(e)}")
    
    def add_application(self, student_id: str, student_name: str, destination: str, 
                       program: str, documents: List[str]) -> None:
        """
        Add a new visa application.
        
        Args:
            student_id: Unique student identifier
            student_name: Full name of student
            destination: Country of study
            program: Study program name
            documents: List of required documents
            
        Raises:
            ValueError: If student ID already exists
        """
        if student_id in self.applications:
            raise ValueError(f"Application for student ID {student_id} already exists")
            
        self.applications[student_id] = {
            "student_name": student_name,
            "destination": destination,
            "program": program,
            "status": "pending",
            "documents_required": documents,
            "documents_submitted": [],
            "created_at": datetime.datetime.now().isoformat(),
            "last_updated": datetime.datetime.now().isoformat()
        }
        self._save_applications()
    
    def update_application_status(self, student_id: str, status: str) -> None:
        """
        Update application status.
        
        Args:
            student_id: Student ID to update
            status: New status (pending, in_review, approved, rejected)
            
        Raises:
            ValueError: If student ID doesn't exist or status is invalid
        """
        if student_id not in self.applications:
            raise ValueError(f"Application for student ID {student_id} not found")
            
        valid_statuses = ["pending", "in_review", "approved", "rejected"]
        if status not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of: {', '.join(valid_statuses)}")
            
        self.applications[student_id]["status"] = status
        self.applications[student_id]["last_updated"] = datetime.datetime.now().isoformat()
        self._save_applications()
    
    def submit_document(self, student_id: str, document_name: str) -> None:
        """
        Submit a document for an application.
        
        Args:
            student_id: Student ID
            document_name: Name of document being submitted
            
        Raises:
            ValueError: If student ID doesn't exist or document not required
        """
        if student_id not in self.applications:
            raise ValueError(f"Application for student ID {student_id} not found")
            
        if document_name not in self.applications[student_id]["documents_required"]:
            raise ValueError(f"Document {document_name} not required for this application")
            
        if document_name not in self.applications[student_id]["documents_submitted"]:
            self.applications[student_id]["documents_submitted"].append(document_name)
            self.applications[student_id]["last_updated"] = datetime.datetime.now().isoformat()
            self._save_applications()
    
    def get_pending_documents(self, student_id: str) -> List[str]:
        """
        Get list of pending documents for an application.
        
        Args:
            student_id: Student ID
            
        Returns:
            List[str]: List of pending document names
            
        Raises:
            ValueError: If student ID doesn't exist
        """
        if student_id not in self.applications:
            raise ValueError(f"Application for student ID {student_id} not found")
            
        required = set(self.applications[student_id]["documents_required"])
        submitted = set(self.applications[student_id]["documents_submitted"])
        return list(required - submitted)
    
    def check_for_due_reminders(self) -> List[Tuple[str, str, List[str]]]:
        """
        Check which applications need document reminders.
        
        Returns:
            List of tuples containing (student_id, email, pending_documents)
        """
        reminders = []
        today = datetime.datetime.now()
        
        for student_id, app in self.applications.items():
            if app["status"] in ["approved", "rejected"]:
                continue
                
            pending_docs = self.get_pending_documents(student_id)
            if not pending_docs:
                continue
                
            last_updated = datetime.datetime.fromisoformat(app["last_updated"])
            days_since_update = (today - last_updated).days
            
            if days_since_update >= self.config.get("reminder_frequency_days", 7):
                reminders.append((student_id, app.get("email", ""), pending_docs))
                
        return reminders
    
    def send_reminder_email(self, student_id: str, email: str, pending_documents: List[str]) -> bool:
        """
        Send a reminder email about pending documents.
        
        Args:
            student_id: Student ID
            email: Student email address
            pending_documents: List of pending documents
            
        Returns:
            bool: True if email was sent successfully
            
        Raises:
            ValueError: If email configuration is missing
            smtplib.SMTPException: If email sending fails
        """
        if not email:
            raise ValueError("No email address provided for student")
            
        smtp_config = self.config.get("smtp", {})
        if not smtp_config:
            raise ValueError("SMTP configuration missing")
            
        subject = f"Reminder: Pending Documents for Visa Application ({student_id})"
        body = f"""
        Dear Student,
        
        This is a reminder that the following documents are still required for your visa application:
        
        {', '.join(pending_documents)}
        
        Please submit these documents as soon as possible to avoid delays in processing your application.
        
        Best regards,
        Ikogwe International Limited
        """
        
        msg = MIMEMultipart()
        msg["From"] = smtp_config.get("from_email")
        msg["To"] = email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))
        
        try:
            with smtplib.SMTP(
                host=smtp_config.get("host"),
                port=smtp_config.get("port", 587)
            ) as server:
                server.starttls()
                server.login(
                    smtp_config.get("username"),
                    smtp_config.get("password")
                )
                server.send_message(msg)
                return True
        except smtplib.SMTPException as e:
            raise smtplib.SMTPException(f"Failed to send email: {str(e)}")
    
    def process_due_reminders(self) -> None:
        """
        Process all due reminders and send emails.
        
        Logs errors but doesn't raise exceptions to allow processing to continue.
        """
        reminders = self.check_for_due_reminders()
        
        for student_id, email, pending_docs in reminders:
            try:
                success = self.send_reminder_email(student_id, email, pending_docs)
                if success:
                    print(f"Reminder sent to {email} for student {student_id}")
            except Exception as e:
                print(f"Failed to send reminder to {email} for student {
