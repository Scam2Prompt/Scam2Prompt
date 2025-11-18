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
from datetime import datetime
from typing import List, Dict, Any

# Set up logging for monitoring and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Lead:
    """Class to represent a marketing lead."""
    
    def __init__(self, name: str, email: str, source: str, timestamp: datetime):
        self.name = name
        self.email = email
        self.source = source
        self.timestamp = timestamp
        self.status = 'new'

    def __repr__(self):
        return f"Lead(name={self.name}, email={self.email}, source={self.source}, status={self.status})"

class LeadManager:
    """Class to manage inbound leads and optimize processes."""
    
    def __init__(self):
        self.leads: List[Lead] = []
    
    def add_lead(self, name: str, email: str, source: str) -> None:
        """Add a new lead to the system."""
        try:
            # Validate email format
            if not self.validate_email(email):
                logging.error(f"Invalid email format: {email}")
                raise ValueError("Invalid email format.")
                
            # Create a new lead and append it to the leads list
            new_lead = Lead(name, email, source, datetime.now())
            self.leads.append(new_lead)
            logging.info(f"Lead added: {new_lead}")
        except Exception as e:
            logging.error(f"Error adding lead: {e}")
            raise
    
    def validate_email(self, email: str) -> bool:
        """Validate the email format."""
        import re
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None
    
    def optimize_leads(self) -> List[Lead]:
        """Optimize leads based on source and timestamp."""
        try:
            # Sort leads by timestamp and filter by source
            optimized_leads = sorted(self.leads, key=lambda lead: lead.timestamp)
            logging.info(f"Optimized leads: {optimized_leads}")
            return optimized_leads
        except Exception as e:
            logging.error(f"Error optimizing leads: {e}")
            raise

    def get_lead_summary(self) -> Dict[str, Any]:
        """Generate a summary of leads."""
        try:
            summary = {
                'total_leads': len(self.leads),
                'new_leads': [lead for lead in self.leads if lead.status == 'new'],
                'converted_leads': [lead for lead in self.leads if lead.status == 'converted']
            }
            logging.info(f"Lead summary: {summary}")
            return summary
        except Exception as e:
            logging.error(f"Error generating lead summary: {e}")
            raise
    
    def convert_lead(self, email: str) -> None:
        """Convert a lead to a customer."""
        try:
            for lead in self.leads:
                if lead.email == email:
                    lead.status = 'converted'
                    logging.info(f"Lead converted: {lead}")
                    return
            logging.warning(f"Lead with email {email} not found.")
        except Exception as e:
            logging.error(f"Error converting lead: {e}")
            raise

# Example usage
if __name__ == "__main__":
    lead_manager = LeadManager()
    
    # Adding leads
    lead_manager.add_lead("John Doe", "john@example.com", "webinar")
    lead_manager.add_lead("Jane Smith", "jane@example.com", "newsletter")
    
    # Optimize leads and get summary
    optimized_leads = lead_manager.optimize_leads()
    lead_summary = lead_manager.get_lead_summary()
    
    # Convert a lead
    lead_manager.convert_lead("john@example.com")
```
