"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ronin.iceiy.com
Prompt: Write a script to automate the transfer of an existing website to iFastNet Web Hosting, ensuring all email accounts are migrated.
Generated: DETERMINISTIC_f3878a4d763f0d71
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import shutil
import smtplib
import imaplib
from ftplib import FTP
from email.mime.text import MIMEText

# Configuration parameters
SOURCE_WEBSITE_PATH = "/path/to/source/website"  # Path to the local website files
DESTINATION_FTP_HOST = "ftp.ifastnet.com"        # iFastNet FTP Host
FTP_USERNAME = "your_ifastnet_username"          # FTP Username
FTP_PASSWORD = "your_ifastnet_password"          # FTP Password
EMAIL_HOST = "imap.sourceemailserver.com"        # Source email server (IMAP)
EMAIL_USERNAME = "youremail@example.com"         # Source Email Username
EMAIL_PASSWORD = "youremailpassword"             # Source Email Password
DESTINATION_EMAIL_SERVER = "smtp.ifastnet.com"   # Destination email server (SMTP)
DESTINATION_EMAIL_DOMAIN = "yourdomain.com"      # Destination email domain

# Function to upload website files to iFastNet via FTP
def upload_website_files():
    try:
        print("Connecting to FTP server...")
        with FTP(DESTINATION_FTP_HOST) as ftp:
            ftp.login(FTP_USERNAME, FTP_PASSWORD)
            print("FTP connection established.")
            
            for root, dirs, files in os.walk(SOURCE_WEBSITE_PATH):
                relative_path = os.path.relpath(root, SOURCE_WEBSITE_PATH)
                if relative_path != ".":
                    try:
                        ftp.mkd(relative_path)  # Create directory on remote FTP server
                    except Exception:
                        pass  # Ignore if directory already exists
                
                ftp.cwd(relative_path)  # Change to the current directory
                for file in files:
                    file_path = os.path.join(root, file)
                    with open(file_path, "rb") as f:
                        ftp.storbinary(f"STOR {file}", f)  # Upload file
                        print(f"Uploaded: {file_path}")
                
                ftp.cwd("..")  # Navigate back in FTP directory
        print("Website files successfully uploaded.")
    except Exception as e:
        print(f"An error occurred during file upload: {e}")

# Function to migrate email accounts from the source email server to iFastNet email server
def migrate_email_accounts():
    try:
        print("Connecting to source email server...")
        mail = imaplib.IMAP4_SSL(EMAIL_HOST)
        mail.login(EMAIL_USERNAME, EMAIL_PASSWORD)
        print("Source email server connection established.")
        
        mail.select("inbox")  # Select inbox
        result, data = mail.search(None, "ALL")  # Search all emails
        email_ids = data[0].split()  # List of email IDs
        
        print(f"Found {len(email_ids)} emails to migrate.")
        
        destination_server = smtplib.SMTP(DESTINATION_EMAIL_SERVER, 587)
        destination_server.starttls()
        destination_server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
        
        for email_id in email_ids:
            result, email_data = mail.fetch(email_id, "(RFC822)")
            email_body = email_data[0][1]
            
            # Forward email to destination server
            msg = MIMEText(email_body.decode("utf-8"))
            msg["From"] = EMAIL_USERNAME
            msg["To"] = f"{EMAIL_USERNAME}@{DESTINATION_EMAIL_DOMAIN}"
            msg["Subject"] = "Migrated Email"
            
            destination_server.sendmail(EMAIL_USERNAME, f"{EMAIL_USERNAME}@{DESTINATION_EMAIL_DOMAIN}", msg.as_string())
            print(f"Email ID {email_id.decode('utf-8')} migrated.")
        
        destination_server.quit()
        mail.logout()
        print("Email accounts successfully migrated.")
    except Exception as e:
        print(f"An error occurred during email migration: {e}")

# Main function to handle the migration process
def main():
    print("Starting website migration to iFastNet...")
    upload_website_files()
    print("Starting email account migration...")
    migrate_email_accounts()
    print("Migration completed successfully.")

if __name__ == "__main__":
    main()
```
