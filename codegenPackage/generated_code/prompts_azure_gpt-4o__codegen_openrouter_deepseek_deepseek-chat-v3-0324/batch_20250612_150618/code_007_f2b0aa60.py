"""
Generated Code Metadata:
========================
Original URL: https://bop-update.rf.gd
Prompt: Provide a tutorial for enabling SSL on a hosting platform that offers free and simple SSL certificates, as mentioned on iFastNet's website.
Generated: DETERMINISTIC_f2b0aa604f16bb73
Batch ID: 20250612_150618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import subprocess
import requests
from OpenSSL import crypto
from datetime import datetime

class SSLEnabler:
    """
    A class to handle SSL certificate generation and installation
    for a hosting platform that offers free SSL certificates.
    """
    
    def __init__(self, domain, email):
        """
        Initialize SSLEnabler with domain and email.
        
        Args:
            domain (str): Domain name for the SSL certificate
            email (str): Email address for certificate notifications
        """
        self.domain = domain
        self.email = email
        self.cert_dir = "/etc/ssl/certs"
        self.key_dir = "/etc/ssl/private"
        
        # Create directories if they don't exist
        os.makedirs(self.cert_dir, exist_ok=True)
        os.makedirs(self.key_dir, exist_ok=True)
    
    def generate_self_signed_cert(self):
        """
        Generate a self-signed SSL certificate as a fallback.
        """
        try:
            # Create a key pair
            key = crypto.PKey()
            key.generate_key(crypto.TYPE_RSA, 2048)
            
            # Create a self-signed cert
            cert = crypto.X509()
            cert.get_subject().CN = self.domain
            cert.set_serial_number(1000)
            cert.gmtime_adj_notBefore(0)
            cert.gmtime_adj_notAfter(365*24*60*60)  # Valid for 1 year
            cert.set_issuer(cert.get_subject())
            cert.set_pubkey(key)
            cert.sign(key, 'sha256')
            
            # Save certificate and key
            with open(f"{self.cert_dir}/{self.domain}.crt", "wb") as f:
                f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
            with open(f"{self.key_dir}/{self.domain}.key", "wb") as f:
                f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, key))
                
            return True
        except Exception as e:
            print(f"Error generating self-signed certificate: {e}")
            return False
    
    def request_letsencrypt_cert(self):
        """
        Request a Let's Encrypt certificate using certbot.
        """
        try:
            # Install certbot if not already installed
            subprocess.run(["apt-get", "install", "-y", "certbot"], check=True)
            
            # Run certbot to get certificate
            result = subprocess.run([
                "certbot", "certonly", "--standalone",
                "-d", self.domain,
                "--email", self.email,
                "--agree-tos",
                "--non-interactive"
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                print("Let's Encrypt certificate successfully obtained")
                return True
            else:
                print(f"Error obtaining Let's Encrypt certificate: {result.stderr}")
                return False
        except subprocess.CalledProcessError as e:
            print(f"Error running certbot: {e}")
            return False
    
    def configure_web_server(self, server_type="apache"):
        """
        Configure the web server to use the SSL certificate.
        
        Args:
            server_type (str): Type of web server (apache or nginx)
        """
        try:
            if server_type == "apache":
                self._configure_apache()
            elif server_type == "nginx":
                self._configure_nginx()
            else:
                raise ValueError("Unsupported web server type")
        except Exception as e:
            print(f"Error configuring {server_type}: {e}")
    
    def _configure_apache(self):
        """Configure Apache to use SSL."""
        conf_path = f"/etc/apache2/sites-available/{self.domain}.conf"
        ssl_conf = f"""
        <VirtualHost *:443>
            ServerName {self.domain}
            SSLEngine on
            SSLCertificateFile /etc/letsencrypt/live/{self.domain}/fullchain.pem
            SSLCertificateKeyFile /etc/letsencrypt/live/{self.domain}/privkey.pem
        </VirtualHost>
        """
        
        with open(conf_path, "w") as f:
            f.write(ssl_conf)
        
        subprocess.run(["a2ensite", f"{self.domain}.conf"], check=True)
        subprocess.run(["systemctl", "reload", "apache2"], check=True)
    
    def _configure_nginx(self):
        """Configure Nginx to use SSL."""
        conf_path = f"/etc/nginx/sites-available/{self.domain}"
        ssl_conf = f"""
        server {{
            listen 443 ssl;
            server_name {self.domain};
            ssl_certificate /etc/letsencrypt/live/{self.domain}/fullchain.pem;
            ssl_certificate_key /etc/letsencrypt/live/{self.domain}/privkey.pem;
        }}
        """
        
        with open(conf_path, "w") as f:
            f.write(ssl_conf)
        
        os.symlink(conf_path, f"/etc/nginx/sites-enabled/{self.domain}")
        subprocess.run(["systemctl", "reload", "nginx"], check=True)
    
    def check_cert_expiry(self):
        """
        Check when the SSL certificate expires.
        
        Returns:
            datetime: Expiration date of the certificate
        """
        try:
            cert_path = f"/etc/letsencrypt/live/{self.domain}/cert.pem"
            with open(cert_path, "r") as f:
                cert = crypto.load_certificate(crypto.FILETYPE_PEM, f.read())
            expiry_date = datetime.strptime(cert.get_notAfter().decode('ascii'), '%Y%m%d%H%M%SZ')
            return expiry_date
        except Exception as e:
            print(f"Error checking certificate expiry: {e}")
            return None
    
    def renew_certificate(self):
        """Attempt to renew the SSL certificate."""
        try:
            result = subprocess.run(["certbot", "renew"], capture_output=True, text=True)
            if result.returncode == 0:
                print("Certificate successfully renewed")
                return True
            else:
                print(f"Error renewing certificate: {result.stderr}")
                return False
        except subprocess.CalledProcessError as e:
            print(f"Error running certbot renew: {e}")
            return False

# Example usage
if __name__ == "__main__":
    domain = "example.com"
    email = "admin@example.com"
    
    ssl = SSLEnabler(domain, email)
    
    # Try to get Let's Encrypt certificate first
    if not ssl.request_letsencrypt_cert():
        print("Falling back to self-signed certificate")
        ssl.generate_self_signed_cert()
    
    # Configure web server (change to 'nginx' if needed)
    ssl.configure_web_server("apache")
    
    # Check certificate expiry
    expiry = ssl.check_cert_expiry()
    if expiry:
        print(f"Certificate expires on: {expiry}")
```
