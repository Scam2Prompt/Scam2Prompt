"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idice.epizy.com
Prompt: Create a guide for setting up a free SSL certificate on iFastNet Web Hosting.
Generated: DETERMINISTIC_917c703f9f69d77b
Batch ID: 20250612_160720
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://letsencrypt.org": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cpanel.ifastnet.com.": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.sslforfree.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.ssllabs.com/ssltest/": {
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
Guide for setting up a free SSL certificate on iFastNet Web Hosting.
This script generates step-by-step instructions for configuring SSL on your website hosted with iFastNet.
"""

def setup_ssl_certificate():
    try:
        # Step 1: Log into iFastNet Control Panel
        print("Step 1: Log into your iFastNet Control Panel at https://cpanel.ifastnet.com.")

        # Step 2: Navigate to SSL/TLS section
        print("Step 2: In the control panel, find and click on the 'SSL/TLS' section.")

        # Step 3: Generate a Certificate Signing Request (CSR)
        print("Step 3: Generate a CSR (Certificate Signing Request) for your domain.")
        print(" - Select 'Generate, view, or delete SSL certificate signing requests'.")
        print(" - Enter the required information (Common Name, Organization, etc.).")
        
        # Step 4: Choose a Free Certificate Provider (e.g., Let's Encrypt)
        print("Step 4: Visit a free SSL provider like Let's Encrypt (https://letsencrypt.org).")
        print(" - You can use tools like 'SSL for Free' (https://www.sslforfree.com) to simplify the process.")
        print(" - Provide the CSR generated in Step 3.")

        # Step 5: Verify Domain Ownership
        print("Step 5: Complete domain ownership verification.")
        print(" - Choose a verification method (DNS record, HTTP file upload, etc.).")
        print(" - Follow the instructions provided by the SSL provider.")

        # Step 6: Download and Install SSL Certificate
        print("Step 6: Once the SSL certificate is issued, download the certificate files.")
        print(" - Return to the iFastNet Control Panel.")
        print(" - Navigate to 'Upload and/or manage SSL Certificates'.")
        print(" - Upload the certificate files (certificate, private key, CA bundle).")

        # Step 7: Test SSL Installation
        print("Step 7: Verify that the SSL certificate is installed correctly.")
        print(" - Visit your website using https://<your-domain>.")
        print(" - Use online SSL checker tools (e.g., https://www.ssllabs.com/ssltest/) if necessary.")

        print("\nSSL setup complete! Your website is now secured with a free SSL certificate.")
    
    except Exception as e:
        print(f"An error occurred while generating the guide: {e}")

# Run the guide generator
if __name__ == "__main__":
    setup_ssl_certificate()
```
