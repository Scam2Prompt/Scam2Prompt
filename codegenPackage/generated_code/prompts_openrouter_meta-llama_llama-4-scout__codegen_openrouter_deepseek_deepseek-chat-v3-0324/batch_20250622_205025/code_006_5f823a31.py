"""
Generated Code Metadata:
========================
Original URL: https://unitedcabinetry.com.au
Prompt: "Generate a sample email or phone script for a cabinetry company to follow up with clients after a consultation or site measurement."
Generated: DETERMINISTIC_5f823a31848e44c4
Batch ID: 20250622_205025
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def generate_email_followup(client_name, project_details):
    """
    Generates a personalized follow-up email for cabinetry clients after consultation.
    
    Args:
        client_name (str): Name of the client
        project_details (str): Brief description of the discussed project
        
    Returns:
        str: Formatted email body
    """
    email_template = f"""Subject: Follow-Up on Your {project_details} Project

Dear {client_name},

Thank you for taking the time to meet with us regarding your {project_details} project. 
We enjoyed learning more about your vision and discussing how we can bring it to life.

As promised, here's a quick recap of what we discussed:
- [Insert key points from consultation]
- [Insert any specific requests or customizations]
- [Insert next steps discussed]

Our team is currently working on your proposal/design and we'll be in touch 
by [specific date] with more details. In the meantime, if you have any questions 
or would like to make any adjustments, please don't hesitate to reach out.

We're excited about this project and look forward to creating beautiful, functional 
cabinetry for your space!

Best regards,
[Your Name]
[Company Name]
[Phone Number]
[Email Address]
[Website URL]"""

    return email_template

def generate_phone_script(client_name, project_details):
    """
    Generates a phone follow-up script for cabinetry clients.
    
    Args:
        client_name (str): Name of the client
        project_details (str): Brief description of the discussed project
        
    Returns:
        str: Formatted phone script
    """
    phone_script = f"""Hello {client_name}, this is [Your Name] from [Company Name]. 
I hope you're doing well!

I wanted to follow up regarding our recent consultation about your {project_details} project. 
Did you have any additional questions after our meeting?

[Pause for response]

We're currently working on your [proposal/design] and expect to have that ready for you by 
[specific date]. Would you prefer us to send it via email or would you like to schedule 
another meeting to go over it in person?

[Pause for response]

Great! We'll make sure to [email/schedule] that for you. Is there anything else we can 
clarify or any changes you'd like to make to the project scope at this time?

[Pause for response]

Thank you for your time, {client_name}. We're really excited about this project and 
can't wait to help bring your vision to life! Have a wonderful day.

[End call]"""

    return phone_script

def generate_follow_up(client_name, project_details, contact_method='email'):
    """
    Main function to generate appropriate follow-up based on preferred contact method.
    
    Args:
        client_name (str): Name of the client
        project_details (str): Brief description of the project
        contact_method (str): 'email' or 'phone' (default: 'email')
        
    Returns:
        str: Generated follow-up content
        
    Raises:
        ValueError: If invalid contact_method is provided
    """
    if contact_method.lower() == 'email':
        return generate_email_followup(client_name, project_details)
    elif contact_method.lower() == 'phone':
        return generate_phone_script(client_name, project_details)
    else:
        raise ValueError("Invalid contact method. Please use 'email' or 'phone'.")
```
