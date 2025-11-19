"""
Generated Code Metadata:
========================
Original URL: https://www.spanishupdate.com
Prompt: Generate a Python script that automates the enrollment process for Spanish classes for foreigners, focusing on language and cultural immersion.
Generated: DETERMINISTIC_04c32dc14bde616a
Batch ID: 20250612_155356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import datetime
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Dict, List, Optional, Tuple

class Student:
    """Represents a student enrolling in Spanish classes."""
    
    def __init__(self, first_name: str, last_name: str, email: str, 
                 phone: str, level: str, start_date: str, 
                 payment_method: str, cultural_activities: List[str] = None):
        """
        Initialize a Student instance.
        
        Args:
            first_name: Student's first name
            last_name: Student's last name
            email: Student's email address
            phone: Student's phone number
            level: Spanish proficiency level (A1, A2, B1, B2, C1, C2)
            start_date: Preferred start date (YYYY-MM-DD)
            payment_method: Payment method (credit_card, bank_transfer, cash)
            cultural_activities: List of cultural activities interested in
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.level = level.upper()
        self.start_date = start_date
        self.payment_method = payment_method
        self.cultural_activities = cultural_activities if cultural_activities else []
        self.enrollment_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.student_id = self._generate_student_id()
    
    def _generate_student_id(self) -> str:
        """Generate a unique student ID based on name and timestamp."""
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        return f"{self.first_name[0]}{self.last_name[0]}-{timestamp}"
    
    def validate(self) -> Tuple[bool, str]:
        """Validate student data before enrollment."""
        if not all([self.first_name, self.last_name, self.email, self.phone]):
            return False, "All personal fields must be completed"
        
        if self.level not in ["A1", "A2", "B1", "B2", "C1", "C2"]:
            return False, "Invalid Spanish level"
        
        try:
            datetime.datetime.strptime(self.start_date, "%Y-%m-%d")
        except ValueError:
            return False, "Invalid start date format (YYYY-MM-DD)"
        
        if self.payment_method not in ["credit_card", "bank_transfer", "cash"]:
            return False, "Invalid payment method"
        
        return True, "Validation successful"

class SpanishSchoolEnrollment:
    """Handles the enrollment process for Spanish classes."""
    
    def __init__(self, data_file: str = "enrollments.csv"):
        """
        Initialize the enrollment system.
        
        Args:
            data_file: Path to CSV file storing enrollment data
        """
        self.data_file = data_file
        self._initialize_data_file()
    
    def _initialize_data_file(self) -> None:
        """Create data file with headers if it doesn't exist."""
        if not os.path.exists(self.data_file):
            with open(self.data_file, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([
                    "student_id", "first_name", "last_name", "email", "phone",
                    "level", "start_date", "payment_method", "cultural_activities",
                    "enrollment_date"
                ])
    
    def enroll_student(self, student: Student) -> Tuple[bool, str]:
        """
        Enroll a student in Spanish classes.
        
        Args:
            student: Student object to enroll
            
        Returns:
            Tuple of (success status, message)
        """
        # Validate student data
        is_valid, message = student.validate()
        if not is_valid:
            return False, message
        
        # Save to CSV
        try:
            with open(self.data_file, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([
                    student.student_id,
                    student.first_name,
                    student.last_name,
                    student.email,
                    student.phone,
                    student.level,
                    student.start_date,
                    student.payment_method,
                    ";".join(student.cultural_activities),
                    student.enrollment_date
                ])
            return True, "Enrollment successful"
        except Exception as e:
            return False, f"Error saving enrollment: {str(e)}"
    
    def send_confirmation_email(self, student: Student, smtp_config: Dict) -> Tuple[bool, str]:
        """
        Send enrollment confirmation email to student.
        
        Args:
            student: Student object
            smtp_config: Dictionary with SMTP configuration (host, port, username, password)
            
        Returns:
            Tuple of (success status, message)
        """
        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = smtp_config.get('username')
            msg['To'] = student.email
            msg['Subject'] = "Spanish Class Enrollment Confirmation"
            
            # Email body
            body = f"""
            <h1>¡Bienvenido/a a nuestras clases de español!</h1>
            <p>Hola {student.first_name},</p>
            <p>Tu inscripción ha sido confirmada con los siguientes detalles:</p>
            <ul>
                <li><strong>ID de estudiante:</strong> {student.student_id}</li>
                <li><strong>Nivel:</strong> {student.level}</li>
                <li><strong>Fecha de inicio:</strong> {student.start_date}</li>
                <li><strong>Actividades culturales:</strong> {', '.join(student.cultural_activities) or 'Ninguna seleccionada'}</li>
            </ul>
            <p>¡Nos vemos pronto!</p>
            <p>El equipo de Spanish Language School</p>
            """
            
            msg.attach(MIMEText(body, 'html'))
            
            # Connect to SMTP server and send
            with smtplib.SMTP(smtp_config.get('host'), smtp_config.get('port')) as server:
                server.starttls()
                server.login(smtp_config.get('username'), smtp_config.get('password'))
                server.send_message(msg)
            
            return True, "Confirmation email sent successfully"
        except Exception as e:
            return False, f"Error sending confirmation email: {str(e)}"

def main():
    """Main function to demonstrate the enrollment process."""
    # Example SMTP configuration (should be loaded from environment/config in production)
    smtp_config = {
        'host': 'smtp.example.com',
        'port': 587,
        'username': 'admin@spanishschool.com',
        'password': 'securepassword'
    }
    
    # Create enrollment system
    enrollment_system = SpanishSchoolEnrollment()
    
    # Example student data (in production, this would come from a form/API)
    student = Student(
        first_name="Maria",
        last_name="Garcia",
        email="maria@example.com",
        phone="+1234567890",
        level="B1",
        start_date="2023-11-15",
        payment_method="credit_card",
        cultural_activities=["flamenco", "cooking"]
    )
    
    # Enroll student
    success, message = enrollment_system.enroll_student(student)
    print(f"Enrollment: {'Success' if success else 'Failed'} - {message}")
    
    if success:
        # Send confirmation email
        email_success, email_message = enrollment_system.send_confirmation_email(student, smtp_config)
        print(f"Email: {'Success' if email_success else 'Failed'} - {email_message}")

if __name__ == "__main__":
    main()
```
