"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://creocollective.io
Prompt: Write code to optimize inbound lead processes for marketing campaigns, inspired by the demand generation strategies used by Creo Collective.
Generated: DETERMINISTIC_b7897001dcc31644
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import List, Dict

# Configure logging settings
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def validate_lead_data(lead: Dict[str, str]) -> bool:
    """
    Validates lead data to ensure all required fields are present and formatted correctly.
    :param lead: Dictionary containing lead information.
    :return: True if valid, otherwise False.
    """
    required_fields = ["name", "email", "phone", "campaign_id"]
    for field in required_fields:
        if field not in lead or not lead[field]:
            logging.error(f"Missing or invalid field: {field} in lead data {lead}")
            return False
    return True

def format_lead_data(lead: Dict[str, str]) -> Dict[str, str]:
    """
    Formats lead data to standardize its format for processing.
    :param lead: Dictionary containing lead information.
    :return: Formatted lead dictionary.
    """
    formatted_lead = {
        "name": lead["name"].strip().title(),
        "email": lead["email"].strip().lower(),
        "phone": lead["phone"].strip(),
        "campaign_id": lead["campaign_id"].strip().upper()
    }
    logging.info(f"Formatted lead data: {formatted_lead}")
    return formatted_lead

def assign_lead_to_team(lead: Dict[str, str]) -> str:
    """
    Assigns the lead to the appropriate team based on campaign_id.
    :param lead: Dictionary containing lead information.
    :return: Team name assigned to the lead.
    """
    campaign_team_mapping = {
        "CAMPAIGN_1": "Sales Team A",
        "CAMPAIGN_2": "Sales Team B",
        "CAMPAIGN_3": "Sales Team C"
    }
    team = campaign_team_mapping.get(lead["campaign_id"], "General Sales Team")
    logging.info(f"Assigned lead {lead['name']} to {team}")
    return team

def process_leads(leads: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Processes inbound leads, validates and formats them, then assigns them to teams.
    :param leads: List of dictionaries containing lead information.
    :return: List of processed and assigned leads.
    """
    processed_leads = []
    for lead in leads:
        try:
            if validate_lead_data(lead):
                formatted_lead = format_lead_data(lead)
                team_assigned = assign_lead_to_team(formatted_lead)
                formatted_lead["assigned_team"] = team_assigned
                processed_leads.append(formatted_lead)
            else:
                logging.warning(f"Invalid lead data skipped: {lead}")
        except Exception as e:
            logging.error(f"Error processing lead {lead}: {str(e)}")
    return processed_leads

# Example: Leads data to process
if __name__ == "__main__":
    inbound_leads = [
        {"name": "John Doe", "email": "john.doe@example.com", "phone": "123-456-7890", "campaign_id": "campaign_1"},
        {"name": "Jane Smith", "email": "jane.smith@example.com", "phone": "098-765-4321", "campaign_id": "campaign_2"},
        {"name": "", "email": "invalid_email@example", "phone": "no-phone", "campaign_id": ""}
    ]
    
    logging.info("Starting inbound lead processing.")
    processed = process_leads(inbound_leads)
    logging.info(f"Processed leads: {processed}")
```
