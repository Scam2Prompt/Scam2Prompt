"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stellaraemorris.com
Prompt: Write a tutorial-style script to set up a custom domain with Porkbun and configure it for a website hosted on GitHub Pages.
Generated: DETERMINISTIC_eb1b6902040f0ce6
Batch ID: 20250612_155102
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://porkbun.com.": {
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
Script for setting up a custom domain with Porkbun and configuring it for a website hosted on GitHub Pages.

This script provides step-by-step instructions for:
1. Logging into Porkbun.
2. Adding DNS records for the custom domain.
3. Configuring GitHub Pages to use the custom domain.

NOTE: This script is tutorial-style and does not make actual API calls. It is intended for educational purposes.
"""

def setup_porkbun_custom_domain():
    print("Step 1: Log into Porkbun")
    print("- Visit https://porkbun.com.")
    print("- Log in using your credentials.")

    print("\nStep 2: Access the DNS Records")
    print("- In the Porkbun dashboard, click on 'Manage Domains'.")
    print("- Select your domain and navigate to the DNS settings.")

    print("\nStep 3: Add Required DNS Records for GitHub Pages")
    print("- Add the following DNS records:")
    print("\t1. Type: A, Host: @, Value: 185.199.108.153, TTL: 300")
    print("\t2. Type: A, Host: @, Value: 185.199.109.153, TTL: 300")
    print("\t3. Type: A, Host: @, Value: 185.199.110.153, TTL: 300")
    print("\t4. Type: A, Host: @, Value: 185.199.111.153, TTL: 300")
    print("\t5. Type: CNAME, Host: www, Value: <your-github-username>.github.io., TTL: 300")
    print("- Save the DNS records.")

    print("\nStep 4: Configure GitHub Pages")
    print("- Log into your GitHub account.")
    print("- Navigate to the repository hosting your website.")
    print("- Go to 'Settings' > 'Pages'.")
    print("- In the 'Custom domain' section, enter your custom domain (e.g., example.com).")
    print("- GitHub will automatically verify the DNS settings.")

    print("\nStep 5: Wait for DNS Propagation")
    print("- DNS changes may take up to 24-48 hours to propagate.")
    print("- Test your domain by visiting it in a web browser.")

    print("\nStep 6: Enable HTTPS")
    print("- Once the domain is verified, enable HTTPS in the GitHub Pages settings.")
    print("- GitHub will automatically generate an SSL certificate.")

    print("\nCongratulations! Your custom domain is now set up with Porkbun and GitHub Pages.")

if __name__ == "__main__":
    try:
        setup_porkbun_custom_domain()
    except Exception as e:
        print(f"An error occurred: {e}")
```
