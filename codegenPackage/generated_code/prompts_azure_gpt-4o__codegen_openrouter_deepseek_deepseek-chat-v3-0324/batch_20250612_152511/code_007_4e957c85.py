"""
Generated Code Metadata:
========================
Original URL: https://tecnicos-whirlpool.com
Prompt: Write code to generate automated email confirmations for Whirlpool appliance repair appointments, including details like appliance type (e.g., neveras, lavadoras) and technician visit date.
Generated: DETERMINISTIC_4e957c85c5ad7b73
Batch ID: 20250612_152511
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
from datetime import datetime
import logging
from typing import Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('email_service.log'),
        logging.StreamHandler()
    ]
)

class EmailConfirmationSender:
    def __init__(
        self,
        smtp_server: str,
        smtp_port: int,
        sender_email: str,
        sender_password: str
    ):
        """
        Initialize email confirmation sender with SMTP credentials.
        
        Args:
            smtp_server: SMTP server address
            smtp_port: SMTP server port
            sender_email: Email address to send from
            sender_password: Password for sender email
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def _create_email_content(
        self,
        customer_name: str,
        appliance_type: str,
        visit_date: datetime,
        technician_name: str,
        tracking_number: str
    ) -> tuple[str, str]:
        """
        Generate email subject and body for appointment confirmation.
        
        Args:
            customer_name: Customer's full name
            appliance_type: Type of appliance (e.g., "neveras", "lavadoras")
            visit_date: Scheduled technician visit date
            technician_name: Name of assigned technician
            tracking_number: Unique appointment tracking number
            
        Returns:
            Tuple of (subject, html_body)
        """
        formatted_date = visit_date.strftime("%A, %B %d, %Y at %I:%M %p")
        
        subject = f"Confirmación de cita para reparación de {appliance_type} - {tracking_number}"
        
        html_body = f"""
        <html>
            <body>
                <h2>Confirmación de Cita de Reparación Whirlpool</h2>
                <p>Estimado(a) {customer_name},</p>
                <p>Gracias por programar su cita de reparación para su {appliance_type}.</p>
                
                <h3>Detalles de la cita:</h3>
                <ul>
                    <li><strong>Tipo de aparato:</strong> {appliance_type}</li>
                    <li><strong>Fecha de visita:</strong> {formatted_date}</li>
                    <li><strong>Técnico asignado:</strong> {technician_name}</li>
                    <li><strong>Número de seguimiento:</strong> {tracking_number}</li>
                </ul>
                
                <p>Por favor, asegúrese de que alguien mayor de 18 años esté presente durante la visita.</p>
                <p>Si necesita cambiar o cancelar su cita, por favor contáctenos al menos 24 horas antes.</p>
                
                <p>Atentamente,<br>El equipo de servicio técnico Whirlpool</p>
            </body>
        </html>
        """
        
        return subject, html_body

    def send_confirmation_email(
        self,
        recipient_email: str,
        customer_name: str,
        appliance_type: str,
        visit_date: datetime,
        technician_name: str,
        tracking_number: str
    ) -> bool:
        """
        Send appointment confirmation email to customer.
        
        Args:
            recipient_email: Customer's email address
            customer_name: Customer's full name
            appliance_type: Type of appliance
            visit_date: Scheduled technician visit date
            technician_name: Name of assigned technician
            tracking_number: Unique appointment tracking number
            
        Returns:
            True if email was sent successfully, False otherwise
        """
        try:
            # Create message container
            msg = MIMEMultipart('alternative')
            msg['From'] = self.sender_email
            msg['To'] = recipient_email
            
            # Create email content
            subject, html_body = self._create_email_content(
                customer_name,
                appliance_type,
                visit_date,
                technician_name,
                tracking_number
            )
            msg['Subject'] = subject
            
            # Attach HTML body
            msg.attach(MIMEText(html_body, 'html'))
            
            # Send email
            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)
            
            logging.info(f"Successfully sent confirmation email to {recipient_email}")
            return True
            
        except smtplib.SMTPException as e:
            logging.error(f"SMTP error sending email to {recipient_email}: {str(e)}")
            return False
        except Exception as e:
            logging.error(f"Unexpected error sending email to {recipient_email}: {str(e)}")
            return False

# Example usage
if __name__ == "__main__":
    # Configuration - should be loaded from environment/config in production
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 465
    SENDER_EMAIL = "servicio@whirlpool-repairs.com"
    SENDER_PASSWORD = "securepassword123"
    
    # Create email sender instance
    email_sender = EmailConfirmationSender(
        smtp_server=SMTP_SERVER,
        smtp_port=SMTP_PORT,
        sender_email=SENDER_EMAIL,
        sender_password=SENDER_PASSWORD
    )
    
    # Sample appointment data
    appointment_data = {
        "recipient_email": "cliente@example.com",
        "customer_name": "Juan Pérez",
        "appliance_type": "lavadora",
        "visit_date": datetime(2023, 12, 15, 10, 30),
        "technician_name": "Carlos Rodríguez",
        "tracking_number": "WH-2023-12345"
    }
    
    # Send confirmation email
    success = email_sender.send_confirmation_email(**appointment_data)
    
    if success:
        print("Email sent successfully!")
    else:
        print("Failed to send email. Check logs for details.")
```
