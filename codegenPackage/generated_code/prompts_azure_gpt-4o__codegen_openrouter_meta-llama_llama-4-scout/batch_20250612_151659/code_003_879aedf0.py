"""
Generated Code Metadata:
========================
Original URL: https://metamas.com.mx
Prompt: Provide Python code for automating customer inquiries via email (e.g., dcomercial@aymc.com.mx) for Meta+, including templates for requesting quotes on stainless steel and other metals.
Generated: DETERMINISTIC_879aedf018f5230d
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl
import os

# Email configuration
class EmailConfig:
    def __init__(self, sender_email, sender_password, smtp_server, smtp_port, recipient_email):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.recipient_email = recipient_email

# Email templates
class EmailTemplates:
    def __init__(self):
        self.quote_request_template = """
        Asunto: Solicitud de cotización para {metal_type}

        Estimado/a,

        Me dirijo a usted para solicitar una cotización para {product_description} de {metal_type}. 
        A continuación, se proporcionan los detalles de la solicitud:

        - Tipo de metal: {metal_type}
        - Descripción del producto: {product_description}
        - Cantidad: {quantity}

        Agradezco de antemano su atención a esta solicitud. 
        Quedo a la espera de su respuesta para discutir los detalles.

        Atentamente,
        {sender_name}
        """

    def get_quote_request_email(self, metal_type, product_description, quantity, sender_name):
        return self.quote_request_template.format(
            metal_type=metal_type,
            product_description=product_description,
            quantity=quantity,
            sender_name=sender_name
        )

# Email service
class EmailService:
    def __init__(self, email_config):
        self.email_config = email_config

    def send_email(self, subject, body):
        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(self.email_config.smtp_server, self.email_config.smtp_port, context=context) as server:
                server.login(self.email_config.sender_email, self.email_config.sender_password)
                message = MIMEMultipart()
                message["From"] = self.email_config.sender_email
                message["To"] = self.email_config.recipient_email
                message["Subject"] = subject
                message.attach(MIMEText(body, "plain"))
                server.sendmail(self.email_config.sender_email, self.email_config.recipient_email, message.as_string())
            print("Email sent successfully!")
        except Exception as e:
            print(f"Error sending email: {e}")

# Usage example
if __name__ == "__main__":
    email_config = EmailConfig(
        sender_email="your-email@gmail.com",
        sender_password="your-email-password",
        smtp_server="smtp.gmail.com",
        smtp_port=465,
        recipient_email="dcomercial@aymc.com.mx"
    )

    email_templates = EmailTemplates()
    email_service = EmailService(email_config)

    metal_type = "Acero inoxidable"
    product_description = "Placa de {metal_type} para uso industrial"
    quantity = "100 unidades"
    sender_name = "Nombre del solicitante"

    subject = f"Solicitud de cotización para {metal_type}"
    body = email_templates.get_quote_request_email(metal_type, product_description, quantity, sender_name)
    email_service.send_email(subject, body)
```
