"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.igeog.uerj.br
Prompt: Generate a script to automate email notifications for candidates based on the results from the IGEOG selection processes, using the data from the "Edital" and "Relação de candidatos aptos" sections.
Generated: DETERMINISTIC_87f3736e9034f871
Batch ID: 20250612_154423
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
import pandas as pd

def load_candidate_data edital_file, candidates_file):
    """
    Load candidates' data from provided Excel files.
    
    :param edital_file: Path to the edital Excel file.
    :param candidates_file: Path to the candidates Excel file.
    :return: DataFrame of edital data and DataFrame of candidates data.
    """
    try:
        edital_data = pd.read_excel(edital_file)
        candidates_data = pd.read_excel(candidates_file)
        return edital_data, candidates_data
    except Exception as e:
        print(f"Error loading files: {e}")
        return None, None

def create_email_message(candidate_name, result):
    """
    Create an email message for the candidate.
    
    :param candidate_name: Name of the candidate.
    :param result: Result of the selection process.
    :return: MIMEText object containing the email message.
    """
    subject = "IGEOG Selection Process Result"
    body = f"Dear {candidate_name},\n\nYour result for the IGEOG selection process is: {result}.\n\nBest regards,\nIGEOG Team"
    
    msg = MIMEMultipart()
    msg['From'] = 'no-reply@igeog.com'
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    return msg

def send_email(smtp_server, port, sender_email, password, recipient_email, message):
    """
    Send an email using the specified SMTP server.
    
    :param smtp_server: The SMTP server address.
    :param port: The port to connect to the SMTP server.
    :param sender_email: The sender's email address.
    :param password: The sender's email password.
    :param recipient_email: The recipient's email address.
    :param message: The message to be sent.
    """
    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()  # Upgrade to secure connection
            server.login(sender_email, password)
            server.sendmail(sender_email, recipient_email, message.as_string())
    except Exception as e:
        print(f"Error sending email to {recipient_email}: {e}")

def notify_candidates(edital_file, candidates_file, smtp_server, port, sender_email, password):
    """
    Notify candidates via email based on their selection results.

    :param edital_file: Path to the edital Excel file.
    :param candidates_file: Path to the candidates Excel file.
    :param smtp_server: The SMTP server address for sending emails.
    :param port: The port for the SMTP server.
    :param sender_email: The sender's email address.
    :param password: The password for the sender's email account.
    """
    edital_data, candidates_data = load_candidate_data(edital_file, candidates_file)
    
    if edital_data is None or candidates_data is None:
        return  # Exit if data loading failed

    for index, candidate in candidates_data.iterrows():
        candidate_name = candidate['Name']
        candidate_email = candidate['Email']
        result = candidate['Result']  # Assuming 'Result' column exists in candidates_data
        
        # Create and send email
        email_message = create_email_message(candidate_name, result)
        email_message['To'] = candidate_email
        send_email(smtp_server, port, sender_email, password, candidate_email, email_message)

if __name__ == "__main__":
    # Configuration
    EDITAL_FILE_PATH = 'path/to/edital.xlsx'
    CANDIDATES_FILE_PATH = 'path/to/candidates.xlsx'
    SMTP_SERVER = 'smtp.example.com'
    PORT = 587
    SENDER_EMAIL = 'your_email@example.com'
    EMAIL_PASSWORD = 'your_email_password'
    
    # Notify candidates
    notify_candidates(EDITAL_FILE_PATH, CANDIDATES_FILE_PATH, SMTP_SERVER, PORT, SENDER_EMAIL, EMAIL_PASSWORD)
```

Make sure to adjust the paths and SMTP settings according to your environment before running the script.
