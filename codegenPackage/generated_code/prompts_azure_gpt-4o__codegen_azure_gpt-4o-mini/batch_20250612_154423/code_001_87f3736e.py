"""
Generated Code Metadata:
========================
Original URL: https://www.igeog.uerj.br
Prompt: Generate a script to automate email notifications for candidates based on the results from the IGEOG selection processes, using the data from the "Edital" and "Relação de candidatos aptos" sections.
Generated: DETERMINISTIC_87f3736e9034f871
Batch ID: 20250612_154423
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
import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Replace with your SMTP port
USERNAME = 'your_email@example.com'  # Replace with your email
PASSWORD = 'your_password'  # Replace with your email password

def load_candidate_data(edital_file, aptos_file):
    """
    Load candidate data from the provided Excel files.

    :param edital_file: Path to the Edital Excel file
    :param aptos_file: Path to the Relação de candidatos aptos Excel file
    :return: DataFrames containing the candidate data
    """
    try:
        edital_df = pd.read_excel(edital_file)
        aptos_df = pd.read_excel(aptos_file)
        logging.info("Candidate data loaded successfully.")
        return edital_df, aptos_df
    except Exception as e:
        logging.error(f"Error loading candidate data: {e}")
        raise

def send_email(to_email, subject, body):
    """
    Send an email notification to the candidate.

    :param to_email: Recipient's email address
    :param subject: Subject of the email
    :param body: Body of the email
    """
    try:
        msg = MIMEMultipart()
        msg['From'] = USERNAME
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(USERNAME, PASSWORD)
            server.send_message(msg)
            logging.info(f"Email sent to {to_email}.")
    except Exception as e:
        logging.error(f"Failed to send email to {to_email}: {e}")

def notify_candidates(edital_df, aptos_df):
    """
    Notify candidates based on their selection results.

    :param edital_df: DataFrame containing the Edital data
    :param aptos_df: DataFrame containing the candidates that are apt
    """
    for index, row in aptos_df.iterrows():
        candidate_email = row['email']  # Assuming 'email' is a column in the aptos_df
        candidate_name = row['name']  # Assuming 'name' is a column in the aptos_df
        subject = "IGEOG Selection Process Results"
        body = f"Dear {candidate_name},\n\nCongratulations! You have been selected based on the IGEOG selection process.\n\nBest regards,\nIGEOG Team"
        
        send_email(candidate_email, subject, body)

def main():
    """
    Main function to execute the email notification process.
    """
    edital_file = 'edital.xlsx'  # Path to the Edital file
    aptos_file = 'candidatos_aptos.xlsx'  # Path to the aptos file

    try:
        edital_df, aptos_df = load_candidate_data(edital_file, aptos_file)
        notify_candidates(edital_df, aptos_df)
    except Exception as e:
        logging.error(f"An error occurred in the main process: {e}")

if __name__ == "__main__":
    main()
```
