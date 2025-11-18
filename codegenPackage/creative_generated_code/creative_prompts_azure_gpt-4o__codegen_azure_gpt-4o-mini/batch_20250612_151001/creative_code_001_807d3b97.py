"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap.sihigo.infwww.vpn.osnovanie-osman.ru
Prompt: Generate code to automate SSL certificate installation for a domain using a server management tool like FASTPANEL.
Generated: DETERMINISTIC_807d3b9731679947
Batch ID: 20250612_151001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
import sys

class SSLInstaller:
    """
    A class to automate the installation of SSL certificates for a domain using FASTPANEL.
    """

    def __init__(self, domain, cert_file, key_file, fullchain_file):
        """
        Initializes the SSLInstaller with domain and certificate files.

        :param domain: The domain for which the SSL certificate is to be installed.
        :param cert_file: The path to the SSL certificate file.
        :param key_file: The path to the private key file.
        :param fullchain_file: The path to the full chain certificate file.
        """
        self.domain = domain
        self.cert_file = cert_file
        self.key_file = key_file
        self.fullchain_file = fullchain_file

    def validate_files(self):
        """
        Validates that the certificate files exist and are readable.

        :raises FileNotFoundError: If any of the files do not exist.
        :raises PermissionError: If any of the files are not readable.
        """
        files = [self.cert_file, self.key_file, self.fullchain_file]
        for file in files:
            if not os.path.isfile(file):
                raise FileNotFoundError(f"Certificate file not found: {file}")
            if not os.access(file, os.R_OK):
                raise PermissionError(f"Permission denied for file: {file}")

    def install_ssl(self):
        """
        Installs the SSL certificate for the specified domain using FASTPANEL commands.

        :raises RuntimeError: If the installation command fails.
        """
        try:
            # Validate certificate files before installation
            self.validate_files()

            # Command to install SSL certificate via FASTPANEL API
            cmd = f"fastpanel ssl install {self.domain} --cert {self.cert_file} --key {self.key_file} --fullchain {self.fullchain_file}"
            result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # Log the output of the command
            print(result.stdout.decode())
            print(f"SSL certificate installed successfully for {self.domain}.")

        except subprocess.CalledProcessError as e:
            # Handle errors during the installation process
            raise RuntimeError(f"Failed to install SSL certificate: {e.stderr.decode().strip()}")

def main():
    """
    Main function to execute the SSL installation process.
    """
    # Define your domain and paths to the certificate files
    domain = "example.com"  # Replace with your domain
    cert_file = "/path/to/your/cert.pem"  # Replace with the actual path
    key_file = "/path/to/your/key.pem"    # Replace with the actual path
    fullchain_file = "/path/to/your/fullchain.pem"  # Replace with the actual path

    try:
        # Create an instance of SSLInstaller
        ssl_installer = SSLInstaller(domain, cert_file, key_file, fullchain_file)

        # Install the SSL certificate
        ssl_installer.install_ssl()

    except (FileNotFoundError, PermissionError, RuntimeError) as e:
        print(f"Error: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```

**Note:** Please ensure to replace `/path/to/your/cert.pem`, `/path/to/your/key.pem`, and `/path/to/your/fullchain.pem` with the actual paths to your SSL certificate files before running the script. Also, make sure that the `fastpanel` command is available in your environment.
