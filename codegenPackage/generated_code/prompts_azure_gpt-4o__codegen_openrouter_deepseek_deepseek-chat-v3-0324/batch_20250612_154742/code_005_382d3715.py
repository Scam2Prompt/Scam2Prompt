"""
Generated Code Metadata:
========================
Original URL: https://datmaui.liveblog365.com
Prompt: Explain how to set up SSL certificates for a website hosted on a platform that offers free and simple SSL, referencing iFastNet's hosting features.
Generated: DETERMINISTIC_382d37152c5468b2
Batch ID: 20250612_154742
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
from OpenSSL import crypto, SSL
from datetime import datetime

class SSLCertificateManager:
    """
    A class to manage SSL certificates for a website hosted on iFastNet or similar platforms.
    Handles certificate generation, installation, and renewal.
    """
    
    def __init__(self, domain, email, web_root='/var/www/html'):
        """
        Initialize the SSL certificate manager.
        
        Args:
            domain (str): The domain name for the certificate
            email (str): Email for certificate notifications
            web_root (str): Web server root directory
        """
        self.domain = domain
        self.email = email
        self.web_root = web_root
        self.cert_dir = os.path.join(web_root, '.ssl')
        self.key_path = os.path.join(self.cert_dir, f'{domain}.key')
        self.cert_path = os.path.join(self.cert_dir, f'{domain}.crt')
        
        # Create SSL directory if it doesn't exist
        os.makedirs(self.cert_dir, exist_ok=True)
    
    def generate_self_signed_cert(self, cert_lifetime=365):
        """
        Generate a self-signed SSL certificate (for testing purposes).
        
        Args:
            cert_lifetime (int): Certificate validity in days
        """
        try:
            # Generate key
            key = crypto.PKey()
            key.generate_key(crypto.TYPE_RSA, 2048)
            
            # Generate cert
            cert = crypto.X509()
            cert.get_subject().CN = self.domain
            cert.set_serial_number(1000)
            cert.gmtime_adj_notBefore(0)
            cert.gmtime_adj_notAfter(cert_lifetime * 24 * 60 * 60)
            cert.set_issuer(cert.get_subject())
            cert.set_pubkey(key)
            cert.sign(key, 'sha256')
            
            # Save files
            with open(self.key_path, 'wb') as f:
                f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, key))
            with open(self.cert_path, 'wb') as f:
                f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
                
            print(f"Self-signed certificate generated for {self.domain}")
            
        except Exception as e:
            print(f"Error generating self-signed certificate: {str(e)}")
            raise
    
    def setup_letsencrypt_cert(self):
        """
        Set up Let's Encrypt certificate using Certbot (for iFastNet-like platforms).
        """
        try:
            # Install Certbot if not already installed
            try:
                subprocess.run(['certbot', '--version'], check=True, capture_output=True)
            except:
                print("Installing Certbot...")
                subprocess.run(['sudo', 'apt-get', 'install', 'certbot', '-y'], check=True)
            
            # Run Certbot to get certificate
            print("Obtaining Let's Encrypt certificate...")
            subprocess.run([
                'sudo', 'certbot', 'certonly', '--webroot',
                '-w', self.web_root,
                '-d', self.domain,
                '--email', self.email,
                '--agree-tos',
                '--non-interactive'
            ], check=True)
            
            print(f"Let's Encrypt certificate successfully installed for {self.domain}")
            
        except subprocess.CalledProcessError as e:
            print(f"Error obtaining Let's Encrypt certificate: {str(e)}")
            raise
    
    def check_cert_expiry(self):
        """
        Check when the current certificate expires.
        
        Returns:
            datetime: Expiration date of current certificate
        """
        try:
            with open(self.cert_path, 'r') as f:
                cert = crypto.load_certificate(crypto.FILETYPE_PEM, f.read())
                expiry_date = datetime.strptime(cert.get_notAfter().decode('ascii'), '%Y%m%d%H%M%SZ')
                return expiry_date
        except Exception as e:
            print(f"Error checking certificate expiry: {str(e)}")
            raise
    
    def renew_certificate(self):
        """
        Renew the SSL certificate if it's close to expiration.
        """
        try:
            expiry = self.check_cert_expiry()
            days_remaining = (expiry - datetime.now()).days
            
            if days_remaining < 30:
                print("Certificate expires soon. Renewing...")
                subprocess.run(['sudo', 'certbot', 'renew'], check=True)
                print("Certificate renewed successfully")
            else:
                print(f"Certificate is valid for {days_remaining} more days")
                
        except Exception as e:
            print(f"Error renewing certificate: {str(e)}")
            raise
    
    def configure_web_server(self, server_type='apache'):
        """
        Configure the web server to use the SSL certificate.
        
        Args:
            server_type (str): Type of web server ('apache' or 'nginx')
        """
        try:
            if server_type == 'apache':
                conf_path = f'/etc/apache2/sites-available/{self.domain}.conf'
                conf_content = f"""
                <VirtualHost *:443>
                    ServerName {self.domain}
                    DocumentRoot {self.web_root}
                    
                    SSLEngine on
                    SSLCertificateFile /etc/letsencrypt/live/{self.domain}/fullchain.pem
                    SSLCertificateKeyFile /etc/letsencrypt/live/{self.domain}/privkey.pem
                    
                    # Other configuration directives...
                </VirtualHost>
                """
            elif server_type == 'nginx':
                conf_path = f'/etc/nginx/sites-available/{self.domain}'
                conf_content = f"""
                server {{
                    listen 443 ssl;
                    server_name {self.domain};
                    root {self.web_root};
                    
                    ssl_certificate /etc/letsencrypt/live/{self.domain}/fullchain.pem;
                    ssl_certificate_key /etc/letsencrypt/live/{self.domain}/privkey.pem;
                    
                    # Other configuration directives...
                }}
                """
            else:
                raise ValueError("Unsupported server type")
            
            # Write configuration file
            with open(conf_path, 'w') as f:
                f.write(conf_content)
            
            # Enable site and restart server
            if server_type == 'apache':
                subprocess.run(['sudo', 'a2ensite', f'{self.domain}.conf'], check=True)
                subprocess.run(['sudo', 'systemctl', 'reload', 'apache2'], check=True)
            else:
                subprocess.run(['sudo', 'ln', '-s', f'/etc/nginx/sites-available/{self.domain}', 
                              f'/etc/nginx/sites-enabled/'], check=True)
                subprocess.run(['sudo', 'systemctl', 'reload', 'nginx'], check=True)
            
            print(f"{server_type.capitalize()} configured for SSL with {self.domain}")
            
        except Exception as e:
            print(f"Error configuring {server_type}: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    # Initialize with your domain and email
    ssl_manager = SSLCertificateManager(
        domain="example.com",
        email="admin@example.com",
        web_root="/var/www/html"
    )
    
    # Option 1: Generate self-signed cert (for testing)
    # ssl_manager.generate_self_signed_cert()
    
    # Option 2: Get Let's Encrypt certificate (production)
    ssl_manager.setup_letsencrypt_cert()
    
    # Configure web server
    ssl_manager.configure_web_server(server_type='apache')
    
    # Check certificate expiry
    expiry = ssl_manager.check_cert_expiry()
    print(f"Certificate valid until: {expiry}")
```
