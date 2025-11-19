"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bee-property.com
Prompt: Write a Python script that automates communication with guests, ensuring 24/7 customer service like Bee Property offers.
Generated: DETERMINISTIC_161803fe92749509
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.message import EmailMessage
import time
from datetime import datetime


class GuestCommunicationAutomator:
    """
    A class to automate communication with guests, ensuring 24/7 customer service.
    """

    def __init__(self, smtp_server, smtp_port, email_address, email_password):
        """
        Initializes the automator with email configuration.
        
        :param smtp_server: SMTP server address
        :param smtp_port:   SMTP server port
        :param email_address: Sender's email address
        :param email_password: Password for the sender's email
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.email_address = email_address
        self.email_password = email_password

    def send_email(self, recipient_email, subject, message_body):
        """
        Sends an email to the specified recipient.
        
        :param recipient_email: Email address of the recipient
        :param subject: Subject of the email
        :param message_body: Body of the email
        """
        try:
            # Create an email message object
            email = EmailMessage()
            email['From'] = self.email_address
            email['To'] = recipient_email
            email['Subject'] = subject
            email.set_content(message_body)

            # Connect to the SMTP server and send email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade connection to secure encrypted channel
                server.login(self.email_address, self.email_password)
                server.send_message(email)
                print(f"Email sent successfully to {recipient_email}")

        except Exception as e:
            # Handle exceptions and log errors
            print(f"Failed to send email to {recipient_email}: {str(e)}")

    def automate_responses(self, guest_email, guest_query):
        """
        Automates responses to guest queries based on predefined rules.
        
        :param guest_email: Email address of the guest
        :param guest_query: The message/query sent by the guest
        """
        # Define a set of sample queries and responses
        predefined_responses = {
            'check-in time': 'Our standard check-in time is 2 PM. Please let us know if you need early check-in.',
            'check-out time': 'Our standard check-out time is 11 AM. Let us know if you need late check-out.',
            'wifi details': 'The Wi-Fi name is "BeeProperty_Guest" and the password is "welcome123".',
            'cancel reservation': 'To cancel your reservation, please visit our website or contact support directly.',
        }

        # Determine an appropriate response based on the guest query
        response = predefined_responses.get(
            guest_query.lower(), 
            "Thank you for your query. We'll get back to you shortly with more details."
        )

        # Send the automated response
        subject = "Response to Your Query"
        self.send_email(guest_email, subject, response)

    def run_24_7_service(self):
        """
        Simulates 24/7 service by continuously listening for queries (mock implementation).
        """
        print("24/7 Customer Service is running...")
        
        # Simulated infinite loop for 24/7 service
        while True:
            try:
                # Mock incoming query (replace this with actual query fetching logic)
                current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                guest_email = "guest@example.com"
                guest_query = "wifi details"  # Simulated guest query
                
                print(f"Received query from {guest_email} at {current_time}")
                
                # Process the query and send a response
                self.automate_responses(guest_email, guest_query)
                
                # Wait for a while before processing next query (simulate delay)
                time.sleep(10)  # Wait 10 seconds

            except KeyboardInterrupt:
                print("24/7 Customer Service stopped.")
                break

            except Exception as e:
                print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    # Email configuration (replace with real credentials)
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    EMAIL_ADDRESS = "your_email@example.com"
    EMAIL_PASSWORD = "your_password"

    # Initialize the communication automator
    automator = GuestCommunicationAutomator(SMTP_SERVER, SMTP_PORT, EMAIL_ADDRESS, EMAIL_PASSWORD)
    
    # Start 24/7 customer service (mock implementation)
    automator.run_24_7_service()
```
