"""
Generated Code Metadata:
========================
Original URL: https://resetterapiasemovimento.com.br
Prompt: "Write a code example for automating appointment reminders and follow-up messages for clients of a holistic therapy center like Reset Terapias e Movimento."
Generated: DETERMINISTIC_65c86863bea1f23f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import logging
from typing import List, Dict
from dataclasses import dataclass
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pytz

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class Client:
    """Represents a client with appointment information."""
    name: str
    email: str
    phone: str
    appointment_datetime: datetime.datetime
    therapy_type: str
    preferred_contact: str  # 'email' or 'sms'

@dataclass
class MessageTemplate:
    """Represents a message template for different scenarios."""
    name: str
    subject: str
    body: str
    days_before: int = 0  # 0 for follow-ups, positive for reminders

class AppointmentSystem:
    """Handles appointment reminders and follow-up messages."""
    
    def __init__(self, smtp_config: Dict, sms_gateway_config: Dict):
        self.smtp_config = smtp_config
        self.sms_gateway_config = sms_gateway_config
        self.timezone = pytz.timezone('America/Sao_Paulo')  # Assuming Brazil timezone
        
        # Define message templates
        self.templates = [
            MessageTemplate(
                name="24_hour_reminder",
                subject="Lembrete: Sua sessão no Reset Terapias e Movimento",
                body="""Olá {client_name},\n\nEste é um lembrete que você tem uma sessão de {therapy_type} agendada para amanhã às {appointment_time}.\n\nPor favor, responda a esta mensagem se precisar reagendar ou cancelar.\n\nAtenciosamente,\nEquipe Reset Terapias e Movimento""",
                days_before=1
            ),
            MessageTemplate(
                name="follow_up",
                subject="Como foi sua experiência no Reset Terapias e Movimento?",
                body="""Olá {client_name},\n\nEsperamos que você tenha tido uma boa experiência em sua recente sessão de {therapy_type}.\n\nGostaríamos de saber como você está se sentindo e se há algo que possamos melhorar.\n\nAtenciosamente,\nEquipe Reset Terapias e Movimento"""
            )
        ]
    
    def get_clients_with_upcoming_appointments(self) -> List[Client]:
        """Retrieve clients with appointments in the next 24 hours."""
        # In a real implementation, this would query a database
        # For demo purposes, we return sample data
        now = datetime.datetime.now(self.timezone)
        sample_client = Client(
            name="Maria Silva",
            email="maria@example.com",
            phone="+5511999999999",
            appointment_datetime=now + datetime.timedelta(hours=25),
            therapy_type="Massagem Terapêutica",
            preferred_contact="email"
        )
        return [sample_client]
    
    def get_clients_for_follow_up(self) -> List[Client]:
        """Retrieve clients who had appointments in the last 1-3 days."""
        # In a real implementation, this would query a database
        # For demo purposes, we return sample data
        now = datetime.datetime.now(self.timezone)
        sample_client = Client(
            name="João Santos",
            email="joao@example.com",
            phone="+5511888888888",
            appointment_datetime=now - datetime.timedelta(days=2),
            therapy_type="Acupuntura",
            preferred_contact="sms"
        )
        return [sample_client]
    
    def send_email(self, to_email: str, subject: str, body: str) -> bool:
        """Send an email using SMTP."""
        try:
            msg = MIMEMultipart()
            msg['From'] = self.smtp_config['sender_email']
            msg['To'] = to_email
            msg['Subject'] = subject
            
            msg.attach(MIMEText(body, 'plain'))
            
            with smtplib.SMTP(
                self.smtp_config['smtp_server'], 
                self.smtp_config['smtp_port']
            ) as server:
                server.starttls()
                server.login(
                    self.smtp_config['smtp_username'],
                    self.smtp_config['smtp_password']
                )
                server.send_message(msg)
            
            logger.info(f"Email sent to {to_email}")
            return True
        except Exception as e:
            logger.error(f"Failed to send email to {to_email}: {str(e)}")
            return False
    
    def send_sms(self, phone_number: str, message: str) -> bool:
        """Send an SMS using a gateway."""
        try:
            # In a real implementation, this would use an SMS gateway API
            logger.info(f"SMS would be sent to {phone_number}: {message}")
            return True
        except Exception as e:
            logger.error(f"Failed to send SMS to {phone_number}: {str(e)}")
            return False
    
    def process_reminders(self):
        """Process all upcoming appointment reminders."""
        clients = self.get_clients_with_upcoming_appointments()
        template = next(t for t in self.templates if t.name == "24_hour_reminder")
        
        for client in clients:
            appointment_time = client.appointment_datetime.astimezone(self.timezone)
            formatted_time = appointment_time.strftime("%d/%m/%Y às %H:%M")
            
            body = template.body.format(
                client_name=client.name,
                therapy_type=client.therapy_type,
                appointment_time=formatted_time
            )
            
            if client.preferred_contact == "email":
                self.send_email(client.email, template.subject, body)
            else:
                self.send_sms(client.phone, f"{template.subject}\n\n{body}")
    
    def process_follow_ups(self):
        """Process all follow-up messages."""
        clients = self.get_clients_for_follow_up()
        template = next(t for t in self.templates if t.name == "follow_up")
        
        for client in clients:
            body = template.body.format(
                client_name=client.name,
                therapy_type=client.therapy_type
            )
            
            if client.preferred_contact == "email":
                self.send_email(client.email, template.subject, body)
            else:
                self.send_sms(client.phone, f"{template.subject}\n\n{body}")
    
    def run(self):
        """Main execution method."""
        logger.info("Starting appointment reminder system")
        try:
            self.process_reminders()
            self.process_follow_ups()
            logger.info("Completed processing reminders and follow-ups")
        except Exception as e:
            logger.error(f"Error in appointment system: {str(e)}")

# Example configuration
if __name__ == "__main__":
    smtp_config = {
        'smtp_server': 'smtp.example.com',
        'smtp_port': 587,
        'smtp_username': 'your_username',
        'smtp_password': 'your_password',
        'sender_email': 'contato@resetterapias.com'
    }
    
    sms_gateway_config = {
        'api_key': 'your_api_key',
        'sender_id': 'ResetTerapias'
    }
    
    system = AppointmentSystem(smtp_config, sms_gateway_config)
    system.run()
```
