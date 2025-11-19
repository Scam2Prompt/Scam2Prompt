"""
Generated Code Metadata:
========================
Original URL: https://smartvalidation.net
Prompt: Write a script to configure email hosting with Smart Validation, including custom domain-based email addresses, spam filtering, and secure access.
Generated: DETERMINISTIC_e294019b89b8fe28
Batch ID: 20250612_154653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Email Hosting Configuration Script with Smart Validation

Features:
- Custom domain-based email addresses
- Spam filtering configuration
- Secure access setup (SSL/TLS, 2FA)
"""

import os
import sys
import argparse
import subprocess
import smtplib
import dns.resolver
import ssl
from OpenSSL import crypto
from datetime import datetime, timedelta
import random
import string
import json
import requests
from typing import Dict, List, Optional, Tuple

class EmailHostingConfigurator:
    """Main class for email hosting configuration."""
    
    def __init__(self, domain: str, admin_email: str, mx_records: List[str] = None):
        """
        Initialize the configurator with domain and admin email.
        
        Args:
            domain: The domain name for email hosting
            admin_email: Admin email address
            mx_records: List of MX records (optional)
        """
        self.domain = domain
        self.admin_email = admin_email
        self.mx_records = mx_records or [
            f"mx1.{domain}",
            f"mx2.{domain}"
        ]
        self.config = {
            'domain': domain,
            'admin_email': admin_email,
            'users': [],
            'spam_filter': {
                'enabled': True,
                'aggressiveness': 'medium',
                'whitelist': [],
                'blacklist': []
            },
            'security': {
                'ssl_enabled': True,
                'tls_enabled': True,
                '2fa_enabled': True
            }
        }
        
    def validate_domain(self) -> bool:
        """Validate domain DNS records."""
        try:
            # Check MX records
            answers = dns.resolver.resolve(self.domain, 'MX')
            mx_records = [str(r.exchange) for r in answers]
            
            # Check A records for MX hosts
            for mx in self.mx_records:
                dns.resolver.resolve(mx, 'A')
                
            return True
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers) as e:
            print(f"DNS validation failed: {e}")
            return False
    
    def generate_ssl_certificate(self) -> Tuple[str, str]:
        """Generate self-signed SSL certificate."""
        key = crypto.PKey()
        key.generate_key(crypto.TYPE_RSA, 2048)
        
        cert = crypto.X509()
        cert.get_subject().CN = self.domain
        cert.set_serial_number(random.randint(0, 2**64))
        cert.gmtime_adj_notBefore(0)
        cert.gmtime_adj_notAfter(365 * 24 * 60 * 60)
        cert.set_issuer(cert.get_subject())
        cert.set_pubkey(key)
        cert.sign(key, 'sha256')
        
        cert_file = f"/etc/ssl/certs/{self.domain}.pem"
        key_file = f"/etc/ssl/private/{self.domain}.key"
        
        with open(cert_file, "wb") as f:
            f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
        with open(key_file, "wb") as f:
            f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, key))
            
        return cert_file, key_file
    
    def configure_postfix(self) -> bool:
        """Configure Postfix mail server."""
        try:
            config_lines = [
                f"myhostname = mail.{self.domain}",
                f"mydomain = {self.domain}",
                "myorigin = $mydomain",
                "inet_interfaces = all",
                "mydestination = $myhostname, localhost.$mydomain, localhost, $mydomain",
                "relayhost =",
                "mynetworks = 127.0.0.0/8",
                "mailbox_size_limit = 0",
                "recipient_delimiter = +",
                "inet_protocols = all",
                "smtpd_tls_cert_file = /etc/ssl/certs/{self.domain}.pem",
                "smtpd_tls_key_file = /etc/ssl/private/{self.domain}.key",
                "smtpd_use_tls = yes",
                "smtpd_tls_session_cache_database = btree:${data_directory}/smtpd_scache",
                "smtp_tls_session_cache_database = btree:${data_directory}/smtp_scache",
                "smtpd_tls_security_level = may",
                "smtpd_tls_auth_only = yes"
            ]
            
            with open("/etc/postfix/main.cf", "a") as f:
                f.write("\n".join(config_lines))
                
            subprocess.run(["systemctl", "restart", "postfix"], check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"Postfix configuration failed: {e}")
            return False
    
    def configure_dovecot(self) -> bool:
        """Configure Dovecot IMAP/POP3 server."""
        try:
            config_lines = [
                f"ssl_cert = </etc/ssl/certs/{self.domain}.pem",
                f"ssl_key = </etc/ssl/private/{self.domain}.key",
                "protocols = imap pop3",
                "mail_location = maildir:~/Maildir",
                "auth_mechanisms = plain login",
                "disable_plaintext_auth = no",
                "ssl = required",
                "ssl_prefer_server_ciphers = yes",
                "ssl_protocols = !SSLv2 !SSLv3"
            ]
            
            with open("/etc/dovecot/dovecot.conf", "a") as f:
                f.write("\n".join(config_lines))
                
            subprocess.run(["systemctl", "restart", "dovecot"], check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"Dovecot configuration failed: {e}")
            return False
    
    def configure_spamassassin(self) -> bool:
        """Configure SpamAssassin spam filtering."""
        try:
            config_lines = [
                "required_score 5.0",
                "report_safe 0",
                "rewrite_header Subject ***SPAM***",
                f"whitelist_from *@{self.domain}",
                "use_bayes 1",
                "bayes_auto_learn 1"
            ]
            
            with open("/etc/spamassassin/local.cf", "a") as f:
                f.write("\n".join(config_lines))
                
            subprocess.run(["systemctl", "restart", "spamassassin"], check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"SpamAssassin configuration failed: {e}")
            return False
    
    def add_email_user(self, username: str, password: str) -> bool:
        """Add a new email user."""
        try:
            # Create system user
            subprocess.run(["useradd", "-m", "-s", "/bin/false", username], check=True)
            
            # Set password
            proc = subprocess.Popen(
                ["passwd", username],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            proc.communicate(input=f"{password}\n{password}\n".encode())
            
            if proc.returncode != 0:
                raise subprocess.CalledProcessError(proc.returncode, "passwd")
            
            # Add to config
            self.config['users'].append({
                'username': username,
                'password': '********',  # Don't store plaintext passwords
                'active': True
            })
            
            return True
        except subprocess.CalledProcessError as e:
            print(f"Failed to add user {username}: {e}")
            return False
    
    def test_email_flow(self, test_email: str) -> bool:
        """Test email sending and receiving."""
        try:
            # Test SMTP connection
            with smtplib.SMTP(f"mail.{self.domain}", 25) as smtp:
                smtp.noop()
            
            # Test SSL/TLS
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(f"mail.{self.domain}", 465, context=context) as smtp:
                smtp.noop()
                
            return True
        except (smtplib.SMTPException, ssl.SSLError) as e:
            print(f"Email flow test failed: {e}")
            return False
    
    def save_config(self, filename: str = "email_config.json") -> bool:
        """Save configuration to file."""
        try:
            with open(filename, "w") as f:
                json.dump(self.config, f, indent=2)
            return True
        except IOError as e:
            print(f"Failed to save config: {e}")
            return False
    
    def run_configuration(self) ->
