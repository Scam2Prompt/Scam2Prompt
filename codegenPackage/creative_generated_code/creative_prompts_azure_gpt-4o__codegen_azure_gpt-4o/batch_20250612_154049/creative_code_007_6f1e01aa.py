"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://guapzenith.com
Prompt: Write code to generate email notifications for portfolio updates and investment performance, similar to the infrastructure described on guapzenith.com.
Generated: DETERMINISTIC_6f1e01aaa267d825
Batch ID: 20250612_154049
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration for the email server and sender details
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_USERNAME = "your_email@gmail.com"  # Replace with your email
EMAIL_PASSWORD = "your_password"         # Replace with your email password

# Function to send an email notification
def send_email(recipient_email, subject, body):
    """
    Sends an email notification.
    
    Args:
        recipient_email (str): The recipient's email address.
        subject (str): The subject of the email.
        body (str): The body/content of the email.
    
    Raises:
        Exception: If the email sending fails.
    """
    try:
        # Create email components
        message = MIMEMultipart()
        message['From'] = EMAIL_USERNAME
        message['To'] = recipient_email
        message['Subject'] = subject
        
        # Attach the email body
        message.attach(MIMEText(body, 'plain'))
        
        # Connect to the email server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Secure the connection
        server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
        
        # Send the email
        server.sendmail(EMAIL_USERNAME, recipient_email, message.as_string())
        server.quit()
        
        print(f"Email sent successfully to {recipient_email}.")
    except Exception as e:
        print(f"Failed to send email to {recipient_email}. Error: {e}")
        raise

# Function to generate and send portfolio update notifications
def send_portfolio_update_email(recipient_email, portfolio_name, updates):
    """
    Sends an email notification for portfolio updates.
    
    Args:
        recipient_email (str): The recipient's email address.
        portfolio_name (str): The name of the portfolio.
        updates (list): A list of strings describing the updates.
    """
    subject = f"Portfolio Update: {portfolio_name}"
    body = f"Dear Investor,\n\nYour portfolio '{portfolio_name}' has the following updates:\n\n"
    body += '\n'.join(updates)  # Format updates as bullet points
    body += "\n\nThank you for trusting us with your investments.\n\nBest regards,\nInvestment Team"
    
    send_email(recipient_email, subject, body)

# Function to generate and send investment performance notifications
def send_investment_performance_email(recipient_email, performance_data):
    """
    Sends an email notification for investment performance.
    
    Args:
        recipient_email (str): The recipient's email address.
        performance_data (dict): A dictionary containing performance data (e.g., returns, gains, losses).
    """
    subject = "Investment Performance Update"
    body = "Dear Investor,\n\nHere is the latest performance update for your investments:\n\n"
    
    for key, value in performance_data.items():
        body += f"{key}: {value}\n"  # Format performance data as key-value pairs
    
    body += "\n\nThank you for trusting us with your investments.\n\nBest regards,\nInvestment Team"
    
    send_email(recipient_email, subject, body)

# Example usage:
if __name__ == "__main__":
    try:
        # Example portfolio updates
        portfolio_updates = [
            "Stock XYZ increased by 10%.",
            "Bond ABC paid out $50 in interest.",
            "ETF DEF is now outperforming its benchmark."
        ]
        send_portfolio_update_email("investor@example.com", "Growth Portfolio", portfolio_updates)

        # Example investment performance data
        performance_data = {
            "Total Portfolio Value": "$25,000",
            "Monthly Return": "5%",
            "Year-To-Date Return": "12%",
            "Total Gain": "$3,000"
        }
        send_investment_performance_email("investor@example.com", performance_data)
    except Exception as error:
        print(f"An error occurred: {error}")
```
