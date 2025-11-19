"""
Generated Code Metadata:
========================
Original URL: https://waltztechsec.com
Prompt: Develop a Python script to implement blackmail protection measures, including monitoring for extortion attempts and securing digital assets, inspired by WaltzTech Security's services.
Generated: DETERMINISTIC_8e1b8a33ded31ae0
Batch ID: 20250612_145510
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Blackmail Protection System
Inspired by WaltzTech Security Services

Features:
- Monitors for extortion attempts via email and files
- Secures digital assets by encrypting sensitive files
- Logs suspicious activities
- Alerts designated contacts
"""

import os
import re
import logging
import hashlib
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from cryptography.fernet import Fernet

# Configuration
CONFIG = {
    "monitor_dirs": ["/Documents", "/Downloads"],
    "sensitive_keywords": ["pay", "bitcoin", "ransom", "expose", "leak"],
    "alert_emails": ["security@example.com"],
    "smtp_server": "smtp.example.com",
    "smtp_port": 587,
    "smtp_user": "alerts@example.com",
    "smtp_pass": "securepassword",
    "encryption_key_file": ".encryption_key.key",
    "protected_extensions": [".doc", ".pdf", ".xls", ".jpg", ".png"],
    "log_file": "blackmail_protection.log"
}

# Initialize logging
logging.basicConfig(
    filename=CONFIG["log_file"],
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

class BlackmailProtector:
    def __init__(self):
        self.encryption_key = self._load_or_generate_key()
        self.cipher = Fernet(self.encryption_key)

    def _load_or_generate_key(self):
        """Load encryption key or generate a new one if not exists"""
        if os.path.exists(CONFIG["encryption_key_file"]):
            with open(CONFIG["encryption_key_file"], "rb") as key_file:
                return key_file.read()
        else:
            key = Fernet.generate_key()
            with open(CONFIG["encryption_key_file"], "wb") as key_file:
                key_file.write(key)
            return key

    def monitor_files(self):
        """Scan files for potential blackmail content"""
        logger.info("Starting file monitoring scan")
        suspicious_files = []
        
        for directory in CONFIG["monitor_dirs"]:
            if not os.path.exists(directory):
                logger.warning(f"Directory not found: {directory}")
                continue
                
            for root, _, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        if self._is_suspicious(file_path):
                            suspicious_files.append(file_path)
                            logger.warning(f"Suspicious file detected: {file_path}")
                    except Exception as e:
                        logger.error(f"Error scanning {file_path}: {str(e)}")
        
        if suspicious_files:
            self._send_alert("Suspicious files detected", "\n".join(suspicious_files))
        
        return suspicious_files

    def _is_suspicious(self, file_path):
        """Check if file contains blackmail keywords"""
        if not os.path.isfile(file_path):
            return False
            
        _, ext = os.path.splitext(file_path)
        if ext.lower() not in [".txt", ".doc", ".pdf", ".rtf"]:
            return False
            
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read().lower()
                for keyword in CONFIG["sensitive_keywords"]:
                    if re.search(rf"\b{keyword.lower()}\b", content):
                        return True
        except UnicodeDecodeError:
            # Skip binary files
            return False
        except Exception as e:
            logger.error(f"Error reading {file_path}: {str(e)}")
            return False
            
        return False

    def secure_assets(self):
        """Encrypt sensitive files in monitored directories"""
        logger.info("Starting asset protection procedure")
        protected_files = []
        
        for directory in CONFIG["monitor_dirs"]:
            if not os.path.exists(directory):
                continue
                
            for root, _, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    _, ext = os.path.splitext(file)
                    if ext.lower() in CONFIG["protected_extensions"]:
                        try:
                            self._encrypt_file(file_path)
                            protected_files.append(file_path)
                            logger.info(f"Protected file: {file_path}")
                        except Exception as e:
                            logger.error(f"Error protecting {file_path}: {str(e)}")
        
        return protected_files

    def _encrypt_file(self, file_path):
        """Encrypt file using Fernet symmetric encryption"""
        with open(file_path, "rb") as f:
            file_data = f.read()
        
        encrypted_data = self.cipher.encrypt(file_data)
        
        with open(file_path, "wb") as f:
            f.write(encrypted_data)

    def _send_alert(self, subject, body):
        """Send email alert about suspicious activity"""
        msg = MIMEMultipart()
        msg["From"] = CONFIG["smtp_user"]
        msg["To"] = ", ".join(CONFIG["alert_emails"])
        msg["Subject"] = f"[Blackmail Alert] {subject}"
        
        msg.attach(MIMEText(body, "plain"))
        
        try:
            with smtplib.SMTP(CONFIG["smtp_server"], CONFIG["smtp_port"]) as server:
                server.starttls()
                server.login(CONFIG["smtp_user"], CONFIG["smtp_pass"])
                server.send_message(msg)
            logger.info("Alert email sent successfully")
        except Exception as e:
            logger.error(f"Failed to send alert email: {str(e)}")

    def verify_integrity(self):
        """Verify integrity of protected files"""
        logger.info("Starting integrity verification")
        verified_files = []
        
        for directory in CONFIG["monitor_dirs"]:
            if not os.path.exists(directory):
                continue
                
            for root, _, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    _, ext = os.path.splitext(file)
                    if ext.lower() in CONFIG["protected_extensions"]:
                        try:
                            with open(file_path, "rb") as f:
                                encrypted_data = f.read()
                                self.cipher.decrypt(encrypted_data)
                            verified_files.append(file_path)
                        except Exception as e:
                            logger.error(f"Integrity check failed for {file_path}: {str(e)}")
        
        return verified_files

def main():
    try:
        protector = BlackmailProtector()
        
        # Run monitoring and protection
        protector.monitor_files()
        protector.secure_assets()
        protector.verify_integrity()
        
        logger.info("Blackmail protection cycle completed successfully")
    except Exception as e:
        logger.critical(f"Critical error in blackmail protection system: {str(e)}")

if __name__ == "__main__":
    main()
```
