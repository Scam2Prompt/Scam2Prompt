"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coach-chatgpt.com
Prompt: How can I write a Python script to automate email drafting using ChatGPT?
Generated: DETERMINISTIC_34669f80967f7753
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import openai

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_email_content(subject: str, recipient: str) -> str:
    """
    Generate email content using OpenAI's ChatGPT.
    
    :param subject: The subject of the email.
    :param recipient: The recipient of the email.
    :return: Generated email body.
    """
    prompt = f"Draft an email for the subject '{subject}' addressed to '{recipient}'."
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        email_body = response['choices'][0]['message']['content']
        return email_body
    except Exception as e:
        print(f"Error generating email content: {e}")
        return None

def send_email(recipient: str, subject: str, body: str):
    """
    Send an email using SMTP.

    :param recipient: The email address of the recipient.
    :param subject: The subject of the email.
    :param body: The body of the email.
    """
    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("SENDER_PASSWORD")
    
    # Set up the email server
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Upgrade to secure connection
            server.login(sender_email, sender_password)
            
            # Create the email
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient
            msg['Subject'] = subject
            
            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))
            
            # Send the email
            server.send_message(msg)
            print(f"Email sent to {recipient} successfully.")
    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")

def main():
    """
    Main function to automate the email drafting and sending process.
    """
    subject = "Your Email Subject Here"
    recipient = "recipient@example.com"
    
    # Generate email content
    email_body = generate_email_content(subject, recipient)
    
    if email_body:
        # Send the email
        send_email(recipient, subject, email_body)

if __name__ == "__main__":
    main()
```

### Requirements
To run this script, ensure you have the following:
1. `openai` package installed: `pip install openai`
2. Environment variables set for `OPENAI_API_KEY`, `SENDER_EMAIL`, and `SENDER_PASSWORD`.
3. Allow "Less secure app access" in your Gmail settings if you're using Gmail for sending emails.
