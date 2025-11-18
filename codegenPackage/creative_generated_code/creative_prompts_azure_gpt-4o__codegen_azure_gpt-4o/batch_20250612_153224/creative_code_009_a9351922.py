"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.mooveweb.com
Prompt: Create a script to automate client feedback collection for services like video production and social media management, tailored for a marketing agency like MoOve Marketing.
Generated: DETERMINISTIC_a9351922c64c265d
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-feedback-form-link.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import csv

# Configuration for the email server
EMAIL_HOST = 'smtp.gmail.com'  # Change to your email provider's SMTP server
EMAIL_PORT = 587
EMAIL_USERNAME = 'your_email@gmail.com'  # Change to your email address
EMAIL_PASSWORD = 'your_email_password'  # Change to your email password
FEEDBACK_FORM_LINK = 'https://your-feedback-form-link.com'  # Change to your feedback form link

# Function to send feedback collection email
def send_feedback_email(client_email, client_name, service_type):
    """
    Sends an email to a client requesting feedback on a specified service.

    :param client_email: The recipient's email address.
    :param client_name: The recipient's name.
    :param service_type: The type of service provided.
    """
    try:
        # Create the email content
        subject = f"Feedback Requested for {service_type} Service"
        body = f"""
        Hi {client_name},

        Thank you for using our {service_type} service at MoOve Marketing! 
        We value your opinion and would love to hear your thoughts.

        Please take a few minutes to fill out our feedback form by clicking the link below:
        {FEEDBACK_FORM_LINK}

        Your feedback helps us improve and provide even better services in the future.

        Thank you for your time!

        Best regards,
        The MoOve Marketing Team
        """

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_USERNAME
        msg['To'] = client_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()  # Start TLS encryption
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
            server.send_message(msg)

        print(f"Feedback email successfully sent to {client_email}")
    except Exception as e:
        print(f"Failed to send email to {client_email}: {e}")

# Function to load client data from a CSV file
def load_clients_from_csv(file_path):
    """
    Loads client data from a CSV file.

    :param file_path: The path to the CSV file.
    :return: A list of dictionaries containing client data.
    """
    clients = []
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                clients.append(row)
        return clients
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return clients

def main():
    """
    Main function to automate feedback collection emails.
    """
    # Path to the CSV file containing client data
    csv_file_path = 'clients.csv'  # Update with the actual path to your CSV file

    # Load client data from the CSV
    clients = load_clients_from_csv(csv_file_path)
    if not clients:
        print("No client data loaded. Exiting...")
        return

    # Send feedback emails to all clients
    for client in clients:
        # Ensure required fields exist in the client data
        try:
            client_email = client["email"]
            client_name = client["name"]
            service_type = client["service_type"]
            send_feedback_email(client_email, client_name, service_type)
        except KeyError as e:
            print(f"Missing required field in client data: {e}")

if __name__ == '__main__':
    main()
```

### Notes for Implementation:
1. Replace the placeholder values for `EMAIL_USERNAME`, `EMAIL_PASSWORD`, and `FEEDBACK_FORM_LINK` with your actual data.
2. Ensure the CSV file (`clients.csv`) has columns named `email`, `name`, and `service_type` to match the usage in the script.
3. Secure email credentials, e.g., using environment variables or a secrets manager in production environments.
