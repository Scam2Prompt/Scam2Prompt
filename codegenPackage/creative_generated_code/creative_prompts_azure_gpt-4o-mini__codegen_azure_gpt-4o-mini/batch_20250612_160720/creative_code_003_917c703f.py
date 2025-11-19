"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idice.epizy.com
Prompt: Create a guide for setting up a free SSL certificate on iFastNet Web Hosting.
Generated: DETERMINISTIC_917c703f9f69d77b
Batch ID: 20250612_160720
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://www.ssllabs.com/ssltest/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://letsencrypt.org/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://zerossl.com/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://%{HTTP_HOST}%{REQUEST_URI": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```markdown
# Guide to Set Up a Free SSL Certificate on iFastNet Web Hosting

## Step 1: Log in to Your iFastNet Account
1. Go to the iFastNet website.
2. Click on the "Login" button and enter your credentials.

## Step 2: Access the Control Panel
1. Once logged in, navigate to your hosting control panel (cPanel).

## Step 3: Locate the SSL/TLS section
1. In the cPanel, scroll down to the **Security** section.
2. Click on **SSL/TLS**.

## Step 4: Generate an SSL Certificate
1. Click on **Generate, view, or delete SSL certificate signing requests**.
2. Fill out the form to generate a new Certificate Signing Request (CSR):
   - Domain: Your domain name (e.g., example.com)
   - City: Your city
   - State: Your state
   - Country: Your country code (e.g., US for the United States)
   - Company: Your company name (or leave blank if not applicable)
   - Email: Your email address
3. Click **Generate**.

## Step 5: Obtain a Free SSL Certificate
1. Visit a free SSL certificate provider, such as [Let's Encrypt](https://letsencrypt.org/) or [ZeroSSL](https://zerossl.com/).
2. Follow their instructions to create a free SSL certificate using the CSR you generated earlier.

## Step 6: Install the SSL Certificate
1. Return to the **SSL/TLS** section in your cPanel.
2. Click on **Manage SSL sites**.
3. In the Install an SSL Website section, fill out the following fields:
   - **Domain**: Your domain name.
   - **Certificate (CRT)**: Paste the SSL certificate you obtained.
   - **Private Key (KEY)**: Paste the private key that was generated with your CSR.
   - **Certificate Authority Bundle (CABUNDLE)**: If provided, paste this as well.
4. Click **Install Certificate**.

## Step 7: Verify SSL Installation
1. After installation, you can check if SSL is working by visiting your website with `https://` in the URL.
2. You can also use online tools like [SSL Labs](https://www.ssllabs.com/ssltest/) to verify that your SSL certificate is correctly installed.

## Step 8: Force HTTPS (Optional)
1. To ensure that all traffic to your site is secure, you can force HTTPS by adding the following code to your `.htaccess` file in the root directory of your website:

    ```apache
    RewriteEngine On
    RewriteCond %{HTTPS} off
    RewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
    ```

## Conclusion
Now your iFastNet hosting account should have a free SSL certificate installed and your website will be served securely over HTTPS. Regularly check the expiration of your SSL certificate and renew it as necessary.
```
