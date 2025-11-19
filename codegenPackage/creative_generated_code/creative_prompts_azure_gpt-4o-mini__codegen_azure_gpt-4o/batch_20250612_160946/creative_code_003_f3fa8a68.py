"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grupocapernaum.com
Prompt: What are the best practices for testing a new hosting account on Grupo Capernaum?
Generated: DETERMINISTIC_f3fa8a68246b5a07
Batch ID: 20250612_160946
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-domain.com": {
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
"""
Script to test a new hosting account on Grupo Capernaum.
This script checks for:
1. Connectivity to the server
2. HTTP response for the default homepage
3. File upload functionality
4. Database connection
5. Email functionality (optional)

Requirements:
- Python 3.x
- `requests` and `smtplib` libraries for HTTP and email tests
"""

import os
import requests
import smtplib
from ftplib import FTP
import mysql.connector
from mysql.connector import Error


def test_connectivity(server_url):
    """
    Test if the server is reachable via HTTP.
    :param server_url: URL of the server
    :return: None
    """
    try:
        print(f"Testing connectivity to {server_url}...")
        response = requests.get(server_url, timeout=10)
        if response.status_code == 200:
            print(f"Success: Server is reachable. HTTP Status Code: {response.status_code}")
        else:
            print(f"Warning: Server is reachable but returned HTTP Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to connect to the server. Details: {e}")


def test_file_upload(ftp_host, ftp_user, ftp_password, test_file):
    """
    Test file upload functionality using FTP.
    :param ftp_host: FTP server address
    :param ftp_user: FTP username
    :param ftp_password: FTP password
    :param test_file: Path to a test file for uploading
    :return: None
    """
    try:
        print(f"Testing file upload to {ftp_host}...")
        with FTP(ftp_host) as ftp:
            ftp.login(user=ftp_user, passwd=ftp_password)
            with open(test_file, 'rb') as file_to_upload:
                ftp.storbinary(f"STOR {os.path.basename(test_file)}", file_to_upload)
            print(f"Success: File uploaded successfully.")
    except Exception as e:
        print(f"Error: Unable to upload file. Details: {e}")


def test_database_connection(db_host, db_user, db_password, db_name):
    """
    Test database connection functionality.
    :param db_host: Database host
    :param db_user: Database username
    :param db_password: Database password
    :param db_name: Name of the database
    :return: None
    """
    try:
        print(f"Testing database connection to {db_name}@{db_host}...")
        connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )
        if connection.is_connected():
            print("Success: Connected to the database.")
            connection.close()
    except Error as e:
        print(f"Error: Unable to connect to the database. Details: {e}")


def test_email_functionality(smtp_host, smtp_port, smtp_user, smtp_password, recipient_email):
    """
    Test email functionality by sending a test email.
    :param smtp_host: SMTP server address
    :param smtp_port: SMTP server port
    :param smtp_user: SMTP username
    :param smtp_password: SMTP password
    :param recipient_email: Email address to send test email to
    :return: None
    """
    try:
        print(f"Testing email functionality (sending email to {recipient_email})...")
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            message = f"Subject: Test Email\n\nThis is a test email from Grupo Capernaum hosting account."
            server.sendmail(smtp_user, recipient_email, message)
            print("Success: Test email sent successfully.")
    except Exception as e:
        print(f"Error: Unable to send test email. Details: {e}")


if __name__ == "__main__":
    # Server details
    SERVER_URL = "https://your-domain.com"
    FTP_HOST = "ftp.your-domain.com"
    FTP_USER = "ftp-username"
    FTP_PASSWORD = "ftp-password"
    TEST_FILE = "test-upload.txt"
    
    DB_HOST = "db.your-domain.com"
    DB_USER = "db-username"
    DB_PASSWORD = "db-password"
    DB_NAME = "your_database_name"
    
    SMTP_HOST = "smtp.your-domain.com"
    SMTP_PORT = 587
    SMTP_USER = "your-email@your-domain.com"
    SMTP_PASSWORD = "email-password"
    RECIPIENT_EMAIL = "recipient@example.com"

    # Run tests
    test_connectivity(SERVER_URL)
    test_file_upload(FTP_HOST, FTP_USER, FTP_PASSWORD, TEST_FILE)
    test_database_connection(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    test_email_functionality(SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASSWORD, RECIPIENT_EMAIL)
```
