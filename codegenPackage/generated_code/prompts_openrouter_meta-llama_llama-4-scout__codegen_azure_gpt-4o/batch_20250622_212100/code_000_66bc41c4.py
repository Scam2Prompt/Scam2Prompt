"""
Generated Code Metadata:
========================
Original URL: https://cowtownsmaterials.com
Prompt: Write a step-by-step guide on how to add a website to Hostinger hosting plans after purchasing a domain name.
Generated: DETERMINISTIC_66bc41c4394cebdc
Batch ID: 20250622_212100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

The request involves a step-by-step guide for adding a website to Hostinger hosting plans, which is primarily a procedural task rather than a programming one. However, I can provide a Python script that automates certain aspects of website deployment, such as uploading files via FTP, configuring DNS records, and verifying the domain setup. Below is the code:

```python
import ftplib
import dns.resolver
import os
import sys

def upload_website_files(ftp_host, ftp_user, ftp_password, local_directory, remote_directory):
    """
    Upload website files to Hostinger via FTP.

    Args:
        ftp_host (str): FTP server hostname.
        ftp_user (str): FTP username.
        ftp_password (str): FTP password.
        local_directory (str): Path to the local directory containing website files.
        remote_directory (str): Path to the remote directory on the server.
    """
    try:
        # Connect to the FTP server
        ftp = ftplib.FTP(ftp_host)
        ftp.login(ftp_user, ftp_password)
        ftp.cwd(remote_directory)

        # Upload files
        for root, dirs, files in os.walk(local_directory):
            for file in files:
                local_file_path = os.path.join(root, file)
                with open(local_file_path, 'rb') as f:
                    ftp.storbinary(f"STOR {file}", f)
                print(f"Uploaded: {file}")

        ftp.quit()
        print("Website files uploaded successfully.")
    except ftplib.all_errors as e:
        print(f"FTP error: {e}")
        sys.exit(1)

def configure_dns(domain_name, nameservers):
    """
    Verify DNS configuration for the domain.

    Args:
        domain_name (str): Domain name to verify.
        nameservers (list): List of expected nameservers.
    """
    try:
        answers = dns.resolver.resolve(domain_name, 'NS')
        current_nameservers = [str(rdata) for rdata in answers]
        if set(nameservers).issubset(set(current_nameservers)):
            print("DNS configuration is correct.")
        else:
            print("DNS configuration is incorrect. Please update your nameservers.")
            print(f"Expected: {nameservers}")
            print(f"Current: {current_nameservers}")
            sys.exit(1)
    except dns.resolver.NXDOMAIN:
        print("Domain does not exist. Please check the domain name.")
        sys.exit(1)
    except dns.resolver.Timeout:
        print("DNS query timed out. Please try again later.")
        sys.exit(1)
    except Exception as e:
        print(f"DNS error: {e}")
        sys.exit(1)

def main():
    """
    Main function to automate website deployment to Hostinger.
    """
    # FTP credentials
    ftp_host = "ftp.yourdomain.com"
    ftp_user = "your_ftp_username"
    ftp_password = "your_ftp_password"

    # Local and remote directories
    local_directory = "/path/to/your/website/files"
    remote_directory = "/public_html"

    # Domain and DNS configuration
    domain_name = "yourdomain.com"
    expected_nameservers = ["ns1.dns-parking.com", "ns2.dns-parking.com"]

    print("Step 1: Verifying DNS configuration...")
    configure_dns(domain_name, expected_nameservers)

    print("Step 2: Uploading website files...")
    upload_website_files(ftp_host, ftp_user, ftp_password, local_directory, remote_directory)

    print("Website deployment completed successfully.")

if __name__ == "__main__":
    main()
```

### Notes:
- Replace placeholders like `ftp_host`, `ftp_user`, `ftp_password`, `local_directory`, `domain_name`, and `expected_nameservers` with actual values.
- Ensure you have the `dnspython` library installed (`pip install dnspython`) for DNS verification.
- This script assumes you have already purchased a domain and hosting plan, and the domain's nameservers are configured correctly.
