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
import openai
import smtplib
from email.message import EmailMessage

# Configuration
OPENAI_API_KEY = 'your_openai_api_key_here'  # Replace with your OpenAI API key
SMTP_SERVER = 'smtp.gmail.com'             # Replace with your email provider's SMTP server
SMTP_PORT = 587                            # Replace with the correct SMTP port for your provider
EMAIL_ADDRESS = 'your_email@example.com'   # Replace with your email address
EMAIL_PASSWORD = 'your_email_password'     # Replace with your email password

def generate_email_content(prompt):
    """
    Generates email content using OpenAI's ChatGPT.

    Args:
        prompt (str): The input prompt describing the email.

    Returns:
        str: Generated email content.
    """
    try:
        openai.api_key = OPENAI_API_KEY

        # Send request to OpenAI API
        response = openai.Completion.create(
            engine="text-davinci-003",  # Use the appropriate engine
            prompt=prompt,
            max_tokens=500,            # Set max tokens for the response
            temperature=0.7            # Set creativity level
        )

        # Extract the generated text from the response
        return response.choices[0].text.strip()
    except Exception as e:
        # Handle errors (e.g., network issues, invalid API key)
        print(f"Error generating email content: {e}")
        return None

def send_email(to_address, subject, body):
    """
    Sends an email using SMTP.

    Args:
        to_address (str): Recipient's email address.
        subject (str): Email subject.
        body (str): Email body.

    Returns:
        None
    """
    try:
        # Create the email message
        msg = EmailMessage()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_address
        msg['Subject'] = subject
        msg.set_content(body)

        # Connect to SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Start TLS encryption
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Login to the email account
            server.send_message(msg)  # Send the email

        print("Email sent successfully!")
    except Exception as e:
        # Handle errors (e.g., authentication failure, connection issues)
        print(f"Error sending email: {e}")

def main():
    """
    Main function to automate email drafting and sending.
    """
    # Define the prompt for email generation
    prompt = input("Enter a brief description of the email (purpose, tone, etc.): ")

    # Generate email content using ChatGPT
    email_body = generate_email_content(prompt)
    if not email_body:
        print("Failed to generate email content. Exiting.")
        return

    # Display the generated email content
    print("\nGenerated Email Content:")
    print(email_body)

    # Get recipient details
    to_address = input("\nEnter recipient's email address: ")
    subject = input("Enter email subject: ")

    # Confirm and send the email
    confirmation = input("\nDo you want to send this email? (yes/no): ").strip().lower()
    if confirmation == 'yes':
        send_email(to_address, subject, email_body)
    else:
        print("Email not sent.")

if __name__ == "__main__":
    main()
```
