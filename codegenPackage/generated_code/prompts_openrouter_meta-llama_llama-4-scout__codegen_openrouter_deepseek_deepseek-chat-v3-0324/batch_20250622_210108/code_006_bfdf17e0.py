"""
Generated Code Metadata:
========================
Original URL: https://waltztechsec.com
Prompt: Write a code snippet for a blackmail protection service, including automated threat detection and response, inspired by WaltzTech Security's blackmail protection services.
Generated: DETERMINISTIC_bfdf17e0fbab59d4
Batch ID: 20250622_210108
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import re
import hashlib
import logging
from datetime import datetime
from typing import List, Dict, Optional, Tuple
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json

# Configuration
CONFIG = {
    "THREAT_KEYWORDS": ["blackmail", "extortion", "pay or else", "leak", "expose"],
    "SUSPICIOUS_FILE_TYPES": [".exe", ".bat", ".vbs", ".js", ".zip", ".rar"],
    "SCAN_DIRECTORIES": ["/documents", "/downloads", "/desktop"],
    "REPORT_EMAIL": "security@example.com",
    "SMTP_SERVER": "smtp.example.com",
    "SMTP_PORT": 587,
    "SMTP_USER": "alerts@example.com",
    "SMTP_PASSWORD": "securepassword",
    "LOG_FILE": "blackmail_protection.log",
    "HASH_DB_FILE": "known_threat_hashes.json"
}

# Initialize logging
logging.basicConfig(
    filename=CONFIG["LOG_FILE"],
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class BlackmailProtectionService:
    def __init__(self):
        self.known_threat_hashes = self._load_known_threat_hashes()
        
    def _load_known_threat_hashes(self) -> Dict[str, str]:
        """Load known threat file hashes from database"""
        try:
            if os.path.exists(CONFIG["HASH_DB_FILE"]):
                with open(CONFIG["HASH_DB_FILE"], "r") as f:
                    return json.load(f)
        except Exception as e:
            logging.error(f"Error loading threat hash database: {str(e)}")
        return {}
    
    def _save_known_threat_hashes(self):
        """Save current threat hashes to database"""
        try:
            with open(CONFIG["HASH_DB_FILE"], "w") as f:
                json.dump(self.known_threat_hashes, f)
        except Exception as e:
            logging.error(f"Error saving threat hash database: {str(e)}")
    
    def _calculate_file_hash(self, file_path: str) -> str:
        """Calculate SHA256 hash of a file"""
        try:
            with open(file_path, "rb") as f:
                file_hash = hashlib.sha256(f.read()).hexdigest()
                return file_hash
        except Exception as e:
            logging.error(f"Error calculating hash for {file_path}: {str(e)}")
            return ""
    
    def _scan_file(self, file_path: str) -> Tuple[bool, Optional[str]]:
        """Scan a file for threats"""
        file_hash = self._calculate_file_hash(file_path)
        
        # Check against known threat hashes
        if file_hash in self.known_threat_hashes:
            return True, f"Known threat hash match: {self.known_threat_hashes[file_hash]}"
        
        # Check file extension
        _, ext = os.path.splitext(file_path)
        if ext.lower() in CONFIG["SUSPICIOUS_FILE_TYPES"]:
            return True, f"Suspicious file type: {ext}"
            
        return False, None
    
    def _scan_text_content(self, text: str) -> Tuple[bool, Optional[str]]:
        """Scan text content for blackmail keywords"""
        text_lower = text.lower()
        for keyword in CONFIG["THREAT_KEYWORDS"]:
            if keyword in text_lower:
                return True, f"Blackmail keyword detected: {keyword}"
        return False, None
    
    def _send_alert_email(self, subject: str, body: str):
        """Send an alert email to the security team"""
        try:
            msg = MIMEMultipart()
            msg["From"] = CONFIG["SMTP_USER"]
            msg["To"] = CONFIG["REPORT_EMAIL"]
            msg["Subject"] = subject
            
            msg.attach(MIMEText(body, "plain"))
            
            with smtplib.SMTP(CONFIG["SMTP_SERVER"], CONFIG["SMTP_PORT"]) as server:
                server.starttls()
                server.login(CONFIG["SMTP_USER"], CONFIG["SMTP_PASSWORD"])
                server.send_message(msg)
                
            logging.info(f"Alert email sent: {subject}")
        except Exception as e:
            logging.error(f"Failed to send alert email: {str(e)}")
    
    def _quarantine_file(self, file_path: str):
        """Move suspicious file to quarantine"""
        quarantine_dir = os.path.join(os.path.dirname(file_path), "quarantine")
        os.makedirs(quarantine_dir, exist_ok=True)
        
        new_path = os.path.join(
            quarantine_dir,
            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{os.path.basename(file_path)}"
        )
        
        try:
            os.rename(file_path, new_path)
            logging.info(f"File quarantined: {file_path} -> {new_path}")
        except Exception as e:
            logging.error(f"Failed to quarantine file {file_path}: {str(e)}")
    
    def scan_directory(self, directory: str):
        """Scan a directory for potential blackmail threats"""
        logging.info(f"Scanning directory: {directory}")
        
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    is_threat, reason = self._scan_file(file_path)
                    if is_threat:
                        self._quarantine_file(file_path)
                        alert_msg = f"Blackmail threat detected in {file_path}: {reason}"
                        self._send_alert_email("Blackmail Threat Detected", alert_msg)
                except Exception as e:
                    logging.error(f"Error scanning file {file_path}: {str(e)}")
    
    def scan_text(self, text: str, source: str = "unknown"):
        """Scan text content for blackmail indicators"""
        is_threat, reason = self._scan_text_content(text)
        if is_threat:
            alert_msg = f"Blackmail text detected from {source}: {reason}\n\nContent:\n{text[:500]}"
            self._send_alert_email("Blackmail Text Detected", alert_msg)
            return True
        return False
    
    def add_threat_hash(self, file_path: str, threat_name: str):
        """Add a file's hash to the known threats database"""
        file_hash = self._calculate_file_hash(file_path)
        if file_hash:
            self.known_threat_hashes[file_hash] = threat_name
            self._save_known_threat_hashes()
            logging.info(f"Added threat hash: {threat_name} ({file_hash})")
            return True
        return False

def main():
    service = BlackmailProtectionService()
    
    # Scan configured directories
    for directory in CONFIG["SCAN_DIRECTORIES"]:
        if os.path.exists(directory):
            service.scan_directory(directory)
        else:
            logging.warning(f"Directory not found: {directory}")
    
    # Example: Add a known threat file to the database
    # service.add_threat_hash("path/to/malicious_file.exe", "BlackmailTrojan")
    
    # Example: Scan text content
    # suspicious_text = "Pay me or I'll expose your secrets"
    # service.scan_text(suspicious_text, "test_source")

if __name__ == "__main__":
    main()
```
