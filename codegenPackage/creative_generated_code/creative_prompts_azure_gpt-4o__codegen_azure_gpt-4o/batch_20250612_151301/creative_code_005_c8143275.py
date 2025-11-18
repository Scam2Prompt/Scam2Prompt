"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presalekelexo.pages.dev
Prompt: Create a privacy policy generator for a web application, referencing the structure seen on Kelexo's website.
Generated: DETERMINISTIC_c81432758c004759
Batch ID: 20250612_151301
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.kelexo.com": {
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
import datetime

def generate_privacy_policy(company_name, website_name, website_url, contact_email):
    """
    Generates a privacy policy for a web application.

    Args:
        company_name (str): Name of the company.
        website_name (str): Name of the website.
        website_url (str): URL of the website.
        contact_email (str): Contact email for privacy-related inquiries.

    Returns:
        str: A formatted privacy policy as a string.
    """
    # Validate input parameters
    if not company_name or not website_name or not website_url or not contact_email:
        raise ValueError("All parameters must be provided and non-empty.")

    # Generate the current date for the policy
    current_date = datetime.date.today().strftime("%B %d, %Y")

    # Privacy policy template
    privacy_policy = f"""
    Privacy Policy for {company_name}

    Effective Date: {current_date}

    At {website_name}, accessible from {website_url}, one of our main priorities is the privacy of our visitors. 
    This Privacy Policy document contains types of information that are collected and recorded by {website_name} 
    and how we use it.

    If you have additional questions or require more information about our Privacy Policy, do not hesitate to 
    contact us at {contact_email}.

    Log Files
    {website_name} follows a standard procedure of using log files. These files log visitors when they visit websites. 
    All hosting companies do this and a part of hosting services' analytics. The information collected by log files 
    includes internet protocol (IP) addresses, browser type, Internet Service Provider (ISP), date and time stamp, 
    referring/exit pages, and possibly the number of clicks. These are not linked to any information that is personally 
    identifiable. The purpose of the information is for analyzing trends, administering the site, tracking users' 
    movement on the website, and gathering demographic information.

    Cookies and Web Beacons
    Like any other website, {website_name} uses 'cookies'. These cookies are used to store information including 
    visitors' preferences, and the pages on the website that the visitor accessed or visited. The information is used 
    to optimize the users' experience by customizing our web page content based on visitors' browser type and/or 
    other information.

    Third-Party Privacy Policies
    {website_name}'s Privacy Policy does not apply to other advertisers or websites. Thus, we are advising you to 
    consult the respective Privacy Policies of these third-party ad servers for more detailed information. It may 
    include their practices and instructions about how to opt-out of certain options.

    Children's Information
    Another part of our priority is adding protection for children while using the internet. We encourage parents 
    and guardians to observe, participate in, and/or monitor and guide their online activity.

    {website_name} does not knowingly collect any Personal Identifiable Information from children under the age of 13. 
    If you think that your child provided this kind of information on our website, we strongly encourage you to contact 
    us immediately and we will do our best efforts to promptly remove such information from our records.

    Online Privacy Policy Only
    This Privacy Policy applies only to our online activities and is valid for visitors to our website with regards to 
    the information that they shared and/or collect in {website_name}. This policy is not applicable to any information 
    collected offline or via channels other than this website.

    Consent
    By using our website, you hereby consent to our Privacy Policy and agree to its terms.
    """

    return privacy_policy


if __name__ == "__main__":
    try:
        # Sample input for the privacy policy generator
        company_name = "Kelexo"
        website_name = "Kelexo"
        website_url = "https://www.kelexo.com"
        contact_email = "support@kelexo.com"
        
        # Generate the privacy policy
        policy = generate_privacy_policy(company_name, website_name, website_url, contact_email)
        
        # Print the generated privacy policy
        print(policy)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
