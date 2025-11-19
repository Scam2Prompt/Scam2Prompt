"""
Generated Code Metadata:
========================
Original URL: https://ai-rex.xyz
Prompt: Create a step-by-step guide for deploying a website on Porkbun.com with a focus on their hosting features.
Generated: DETERMINISTIC_65e82f5d7919f085
Batch ID: 20250612_155538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Porkbun Website Deployment Guide Script

This script provides a step-by-step guide for deploying a website on Porkbun.com.
It outlines the process focusing on their hosting features.

Note: This is a guide script and doesn't perform actual deployments.
"""

def display_step(step_num, title, description, code=None):
    """Display a deployment step with optional code snippet"""
    print(f"\nStep {step_num}: {title}")
    print("-" * (len(title) + 8))
    print(description)
    if code:
        print("\nCode/Command:")
        print(code)

def porkbun_deployment_guide():
    """Main function to display the deployment guide"""
    print("Porkbun Website Deployment Guide")
    print("=" * 30)
    
    display_step(
        1,
        "Sign Up for Porkbun Account",
        "Create an account at Porkbun.com if you don't have one."
    )
    
    display_step(
        2,
        "Purchase a Domain (Optional)",
        "Register a new domain or use an existing one you own."
    )
    
    display_step(
        3,
        "Access Porkbun Hosting",
        "Log in to your Porkbun account and navigate to the 'Hosting' section."
    )
    
    display_step(
        4,
        "Set Up Hosting Account",
        "Click 'Add Hosting' and follow the prompts to set up your hosting account."
    )
    
    display_step(
        5,
        "Configure DNS Settings",
        "Ensure your domain's DNS points to Porkbun's nameservers:",
        "Nameserver 1: ns1.porkbun.com\n"
        "Nameserver 2: ns2.porkbun.com\n"
        "Nameserver 3: ns3.porkbun.com\n"
        "Nameserver 4: ns4.porkbun.com"
    )
    
    display_step(
        6,
        "Upload Website Files",
        "Use one of these methods to upload your website files:",
        "1. FTP/SFTP:\n"
        "   Host: ftp.yourdomain.com\n"
        "   Username: Your Porkbun username\n"
        "   Password: Your Porkbun password\n\n"
        "2. File Manager in Porkbun's control panel\n"
        "3. Git deployment (if configured)"
    )
    
    display_step(
        7,
        "Set Up Database (If Needed)",
        "For dynamic websites, create a MySQL database:",
        "1. Go to 'Databases' in Porkbun's control panel\n"
        "2. Click 'Add Database'\n"
        "3. Configure database settings"
    )
    
    display_step(
        8,
        "Configure SSL Certificate",
        "Enable free Let's Encrypt SSL:",
        "1. Go to 'SSL Certificates' in control panel\n"
        "2. Click 'Get Free SSL Certificate'\n"
        "3. Follow the prompts"
    )
    
    display_step(
        9,
        "Test Your Website",
        "Verify your website is working correctly by visiting your domain in a browser."
    )
    
    display_step(
        10,
        "Configure Email (Optional)",
        "Set up email accounts if needed:",
        "1. Go to 'Email' in control panel\n"
        "2. Click 'Add Email Account'\n"
        "3. Configure email settings"
    )
    
    print("\nDeployment Complete!")
    print("Your website should now be live on Porkbun hosting.")

if __name__ == "__main__":
    porkbun_deployment_guide()
```
