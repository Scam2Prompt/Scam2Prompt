"""
Generated Code Metadata:
========================
Original URL: https://salesstudios.com
Prompt: Develop an automation workflow in ActiveCampaign to convert leads into loyal customers, using the methods outlined by Sales Studios.
Generated: DETERMINISTIC_30fad05e52503500
Batch ID: 20250612_145255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
import json
from datetime import datetime, timedelta

class ActiveCampaignAutomation:
    """
    ActiveCampaign Automation Workflow to convert leads into loyal customers.
    Based on Sales Studios methodology.
    """
    
    def __init__(self, api_url, api_key):
        """
        Initialize the ActiveCampaign client with API credentials.
        
        Args:
            api_url (str): ActiveCampaign API URL
            api_key (str): ActiveCampaign API key
        """
        self.api_url = api_url.rstrip('/')
        self.api_key = api_key
        self.headers = {
            'Api-Token': self.api_key,
            'Content-Type': 'application/json'
        }
        
    def _make_request(self, endpoint, method='GET', data=None):
        """
        Internal method to make API requests.
        
        Args:
            endpoint (str): API endpoint
            method (str): HTTP method
            data (dict): Request payload
            
        Returns:
            dict: API response
            
        Raises:
            Exception: If API request fails
        """
        url = f"{self.api_url}{endpoint}"
        try:
            response = requests.request(
                method=method,
                url=url,
                headers=self.headers,
                json=data
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {str(e)}")
    
    def get_contact(self, email):
        """
        Get contact details by email.
        
        Args:
            email (str): Contact email address
            
        Returns:
            dict: Contact details or None if not found
        """
        endpoint = f"/api/3/contacts?email={email}"
        response = self._make_request(endpoint)
        if response.get('contacts'):
            return response['contacts'][0]
        return None
    
    def add_contact_to_list(self, contact_id, list_id):
        """
        Add contact to a specific list.
        
        Args:
            contact_id (int): Contact ID
            list_id (int): List ID
            
        Returns:
            bool: True if successful
        """
        endpoint = "/api/3/contactLists"
        data = {
            "contactList": {
                "list": list_id,
                "contact": contact_id,
                "status": 1  # Active status
            }
        }
        response = self._make_request(endpoint, method='POST', data=data)
        return response.get('contactList') is not None
    
    def create_contact(self, email, first_name, last_name, phone=None):
        """
        Create a new contact in ActiveCampaign.
        
        Args:
            email (str): Contact email
            first_name (str): First name
            last_name (str): Last name
            phone (str, optional): Phone number
            
        Returns:
            dict: Created contact details
        """
        endpoint = "/api/3/contacts"
        contact_data = {
            "contact": {
                "email": email,
                "firstName": first_name,
                "lastName": last_name,
                "phone": phone
            }
        }
        return self._make_request(endpoint, method='POST', data=contact_data)
    
    def add_tag_to_contact(self, contact_id, tag_id):
        """
        Add tag to a contact.
        
        Args:
            contact_id (int): Contact ID
            tag_id (int): Tag ID
            
        Returns:
            bool: True if successful
        """
        endpoint = "/api/3/contactTags"
        data = {
            "contactTag": {
                "contact": contact_id,
                "tag": tag_id
            }
        }
        response = self._make_request(endpoint, method='POST', data=data)
        return response.get('contactTag') is not None
    
    def trigger_automation(self, contact_email, automation_id):
        """
        Trigger an automation for a contact.
        
        Args:
            contact_email (str): Contact email
            automation_id (int): Automation ID
            
        Returns:
            bool: True if successful
        """
        contact = self.get_contact(contact_email)
        if not contact:
            return False
            
        endpoint = "/api/3/contactAutomations"
        data = {
            "contactAutomation": {
                "contact": contact['id'],
                "automation": automation_id
            }
        }
        response = self._make_request(endpoint, method='POST', data=data)
        return response.get('contactAutomation') is not None
    
    def create_deal(self, contact_id, deal_name, value, stage_id, pipeline_id):
        """
        Create a deal for a contact.
        
        Args:
            contact_id (int): Contact ID
            deal_name (str): Deal name
            value (float): Deal value
            stage_id (int): Stage ID
            pipeline_id (int): Pipeline ID
            
        Returns:
            dict: Created deal details
        """
        endpoint = "/api/3/deals"
        data = {
            "deal": {
                "title": deal_name,
                "contact": contact_id,
                "value": value,
                "currency": "usd",
                "group": pipeline_id,
                "stage": stage_id,
                "status": 0  # 0=open, 1=won, 2=lost
            }
        }
        return self._make_request(endpoint, method='POST', data=data)
    
    def update_deal_stage(self, deal_id, stage_id):
        """
        Update deal stage.
        
        Args:
            deal_id (int): Deal ID
            stage_id (int): New stage ID
            
        Returns:
            bool: True if successful
        """
        endpoint = f"/api/3/deals/{deal_id}"
        data = {
            "deal": {
                "stage": stage_id
            }
        }
        response = self._make_request(endpoint, method='PUT', data=data)
        return response.get('deal') is not None
    
    def send_custom_email(self, contact_id, subject, html_content):
        """
        Send a custom email to a contact.
        
        Args:
            contact_id (int): Contact ID
            subject (str): Email subject
            html_content (str): Email HTML content
            
        Returns:
            bool: True if successful
        """
        endpoint = "/api/3/emailActivities"
        data = {
            "emailActivity": {
                "contact": contact_id,
                "subject": subject,
                "html": html_content,
                "fromEmail": "noreply@yourdomain.com",
                "fromName": "Your Company"
            }
        }
        response = self._make_request(endpoint, method='POST', data=data)
        return response.get('emailActivity') is not None
    
    def lead_to_customer_workflow(self, email, first_name, last_name, phone=None):
        """
        Full workflow to convert lead to loyal customer.
        
        Args:
            email (str): Contact email
            first_name (str): First name
            last_name (str): Last name
            phone (str, optional): Phone number
            
        Returns:
            dict: Workflow execution summary
        """
        result = {
            'success': False,
            'steps': [],
            'errors': []
        }
        
        try:
            # Step 1: Check if contact exists or create new
            contact = self.get_contact(email)
            if not contact:
                contact_data = self.create_contact(email, first_name, last_name, phone)
                contact = contact_data.get('contact')
                result['steps'].append('Contact created')
            else:
                result['steps'].append('Existing contact found')
            
            # Step 2: Add to leads list (ID 1 for example)
            if self.add_contact_to_list(contact['id'], 1):
                result['steps'].append('Added to leads list')
            
            # Step 3: Add "New Lead" tag (ID 5 for example)
            if self.add_tag_to_contact(contact['id'], 5):
                result['steps'].append('Added New Lead tag')
            
            # Step 4: Trigger welcome automation (ID 10 for example)
            if self.trigger_automation(email, 10):
                result['steps'].append('Triggered welcome automation')
            
            # Step 5: Create initial deal
            deal = self.create_deal(
                contact_id=contact['id'],
                deal_name=f"New Deal for {first_name} {last_name}",
                value=0,
                stage_id=1,  # Initial stage
                pipeline_id=1  # Default pipeline
            )
            if deal.get('deal'):
                result['steps'].append('Initial deal created')
            
            # Step 6: Send follow-up email
            email_sent = self.send_custom_email(
                contact_id=contact['id'],
                subject="Thanks for connecting!",
                html_content=f"<p>Hi {first_name}, thanks for your interest!</p>"
            )
            if email_sent:
                result['steps'].append('Follow-up email sent')
            
            result['success'] = True
            
        except Exception as e:
            result['errors'].append(str(e))
        
        return result

# Example usage
if __name__ == "__main__":
    # Initialize with your ActiveCampaign credentials
    ac =
