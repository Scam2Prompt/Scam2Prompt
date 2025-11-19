"""
Generated Code Metadata:
========================
Original URL: https://www.igeog.uerj.br
Prompt: Generate a Python script to automate the application process for the Professor Substitute positions in Geography at IGEOG/UERJ, including handling document submissions and tracking application statuses.
Generated: DETERMINISTIC_ff0e3574f088f33a
Batch ID: 20250612_164005
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
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from typing import List, Dict, Optional

# Configuration
CONFIG = {
    "application_folder": "applications",
    "database_file": "applications_db.csv",
    "admin_email": "admin@igeo.uerj.br",
    "smtp_server": "smtp.uerj.br",
    "smtp_port": 587,
    "smtp_username": "noreply@igeo.uerj.br",
    "smtp_password": "securepassword",
    "required_documents": [
        "cv.pdf",
        "diplomas.pdf",
        "research_statement.pdf",
        "teaching_statement.pdf",
        "reference_letters.pdf"
    ]
}

class ApplicationSystem:
    def __init__(self):
        """Initialize the application system with required folders and database."""
        self._setup_folders()
        self._setup_database()

    def _setup_folders(self):
        """Create required folders if they don't exist."""
        if not os.path.exists(CONFIG["application_folder"]):
            os.makedirs(CONFIG["application_folder"])
            os.makedirs(os.path.join(CONFIG["application_folder"], "documents"))
            os.makedirs(os.path.join(CONFIG["application_folder"], "processed"))

    def _setup_database(self):
        """Initialize the application database if it doesn't exist."""
        if not os.path.exists(CONFIG["database_file"]):
            with open(CONFIG["database_file"], "w", newline='') as f:
                writer = csv.writer(f)
                writer.writerow([
                    "application_id",
                    "applicant_name",
                    "applicant_email",
                    "submission_date",
                    "status",
                    "reviewer_notes",
                    "last_updated"
                ])

    def _generate_application_id(self) -> str:
        """Generate a unique application ID."""
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        return f"IGEOG-{timestamp}"

    def _validate_documents(self, documents: List[str]) -> bool:
        """Validate that all required documents are present."""
        return all(doc in documents for doc in CONFIG["required_documents"])

    def _send_confirmation_email(self, applicant_email: str, application_id: str):
        """Send confirmation email to applicant."""
        msg = MIMEMultipart()
        msg['From'] = CONFIG["admin_email"]
        msg['To'] = applicant_email
        msg['Subject'] = "IGEOG/UERJ - Application Received"

        body = f"""
        Dear Applicant,

        Thank you for applying for the Professor Substitute position at IGEOG/UERJ.
        Your application ID is: {application_id}

        We will review your application and contact you with updates.

        Best regards,
        IGEOG/UERJ Admissions Committee
        """
        msg.attach(MIMEText(body, 'plain'))

        try:
            with smtplib.SMTP(CONFIG["smtp_server"], CONFIG["smtp_port"]) as server:
                server.starttls()
                server.login(CONFIG["smtp_username"], CONFIG["smtp_password"])
                server.send_message(msg)
        except Exception as e:
            print(f"Error sending confirmation email: {e}")

    def submit_application(self, applicant_name: str, applicant_email: str, documents: Dict[str, str]) -> Optional[str]:
        """
        Submit a new application.
        
        Args:
            applicant_name: Full name of the applicant
            applicant_email: Email address of the applicant
            documents: Dictionary of document paths (key: document type, value: file path)
            
        Returns:
            Application ID if successful, None otherwise
        """
        # Validate documents
        if not self._validate_documents(list(documents.keys())):
            print("Error: Missing required documents")
            return None

        # Generate application ID
        application_id = self._generate_application_id()
        submission_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Create application folder
        app_folder = os.path.join(CONFIG["application_folder"], "documents", application_id)
        os.makedirs(app_folder)

        # Save documents
        try:
            for doc_type, doc_path in documents.items():
                if os.path.exists(doc_path):
                    ext = os.path.splitext(doc_path)[1]
                    new_path = os.path.join(app_folder, f"{doc_type}{ext}")
                    os.rename(doc_path, new_path)
                else:
                    print(f"Error: Document not found: {doc_path}")
                    return None
        except Exception as e:
            print(f"Error saving documents: {e}")
            return None

        # Update database
        try:
            with open(CONFIG["database_file"], "a", newline='') as f:
                writer = csv.writer(f)
                writer.writerow([
                    application_id,
                    applicant_name,
                    applicant_email,
                    submission_date,
                    "Submitted",
                    "",
                    submission_date
                ])
        except Exception as e:
            print(f"Error updating database: {e}")
            return None

        # Send confirmation email
        self._send_confirmation_email(applicant_email, application_id)

        return application_id

    def get_application_status(self, application_id: str) -> Optional[Dict[str, str]]:
        """
        Get the status of an application.
        
        Args:
            application_id: The application ID to check
            
        Returns:
            Dictionary with application details if found, None otherwise
        """
        try:
            with open(CONFIG["database_file"], "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row["application_id"] == application_id:
                        return dict(row)
        except Exception as e:
            print(f"Error reading database: {e}")
        
        return None

    def update_application_status(self, application_id: str, new_status: str, reviewer_notes: str = "") -> bool:
        """
        Update the status of an application.
        
        Args:
            application_id: The application ID to update
            new_status: New status to set
            reviewer_notes: Optional notes from the reviewer
            
        Returns:
            True if update was successful, False otherwise
        """
        updated = False
        rows = []
        
        try:
            # Read all rows
            with open(CONFIG["database_file"], "r") as f:
                reader = csv.DictReader(f)
                fieldnames = reader.fieldnames
                for row in reader:
                    if row["application_id"] == application_id:
                        row["status"] = new_status
                        row["reviewer_notes"] = reviewer_notes
                        row["last_updated"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        updated = True
                    rows.append(row)
            
            # Write back if update was found
            if updated:
                with open(CONFIG["database_file"], "w", newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)
                
                return True
            else:
                print("Application ID not found")
                return False
                
        except Exception as e:
            print(f"Error updating application status: {e}")
            return False

    def get_all_applications(self, status_filter: str = None) -> List[Dict[str, str]]:
        """
        Get all applications, optionally filtered by status.
        
        Args:
            status_filter: Optional status to filter by
            
        Returns:
            List of application dictionaries
        """
        applications = []
        try:
            with open(CONFIG["database_file"], "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if status_filter is None or row["status"] == status_filter:
                        applications.append(dict(row))
        except Exception as e:
            print(f"Error reading database: {e}")
        
        return applications

# Example usage
if __name__ == "__main__":
    app_system = ApplicationSystem()
    
    # Example submission
    documents = {
        "cv.pdf": "/path/to/cv.pdf",
        "diplomas.pdf": "/path/to/diplomas.pdf",
        "research_statement.pdf": "/path/to/research.pdf",
        "teaching_statement.pdf": "/path/to/teaching.pdf",
        "reference_letters.pdf": "/path/to/references.pdf"
    }
    
    app_id = app_system.submit_application(
        "John Doe",
        "john.doe@example.com",
        documents
    )
    
    if app_id:
        print(f"Application submitted successfully. ID: {app_id}")
        # Check status
        status = app_system.get_application_status(app_id)
        print(f"Current status: {status['status']}")
        
        # Admin updates status
        app_system.update_application_status(app_id, "
