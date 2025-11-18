"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea.be
Prompt: Develop a script to automate the tracking of audits for sustainability certifications, like the FSC audit completed by PDC Brush.
Generated: DETERMINISTIC_c58cf4a6070bf75b
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO, filename='audit_tracker.log',
                    format='%(asctime)s - %(levelname)s - %(message)s')

class AuditTracker:
    def __init__(self, data_file='audit_data.json'):
        """Initialize the AuditTracker with a data file."""
        self.data_file = data_file
        self.audits = self.load_audits()

    def load_audits(self):
        """Load audit data from a JSON file."""
        try:
            with open(self.data_file, 'r') as file:
                audits = json.load(file)
                logging.info('Audit data loaded successfully.')
                return audits
        except FileNotFoundError:
            logging.warning('Audit data file not found. Starting with an empty list.')
            return []
        except json.JSONDecodeError:
            logging.error('Error decoding JSON. Starting with an empty list.')
            return []

    def save_audits(self):
        """Save audit data to a JSON file."""
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.audits, file, indent=4)
                logging.info('Audit data saved successfully.')
        except IOError as e:
            logging.error(f'Error saving audit data: {e}')

    def add_audit(self, certification, date_completed):
        """Add a new audit record."""
        if not isinstance(certification, str) or not isinstance(date_completed, str):
            logging.error('Invalid input types for certification or date_completed.')
            return
        
        try:
            date_completed = datetime.strptime(date_completed, '%Y-%m-%d')
            new_audit = {
                "certification": certification,
                "date_completed": date_completed.strftime('%Y-%m-%d'),
                "next_audit_due": (date_completed + timedelta(days=365)).strftime('%Y-%m-%d')
            }
            self.audits.append(new_audit)
            logging.info(f'Added audit for certification: {certification}.')
            self.save_audits()
        except ValueError:
            logging.error('Invalid date format. Please use YYYY-MM-DD.')

    def list_audits(self):
        """List all audits."""
        if not self.audits:
            logging.info('No audits found.')
            return []
        
        logging.info('Listing all audits.')
        for audit in self.audits:
            print(f"Certification: {audit['certification']}, "
                  f"Date Completed: {audit['date_completed']}, "
                  f"Next Audit Due: {audit['next_audit_due']}")
        return self.audits

    def get_next_due_audits(self):
        """Get audits that are due within the next 30 days."""
        due_audits = []
        today = datetime.now()
        for audit in self.audits:
            next_due = datetime.strptime(audit['next_audit_due'], '%Y-%m-%d')
            if 0 <= (next_due - today).days <= 30:
                due_audits.append(audit)
        
        if not due_audits:
            logging.info('No audits are due within the next 30 days.')
        else:
            logging.info('Found audits due within the next 30 days.')
        return due_audits

# Example usage
if __name__ == "__main__":
    tracker = AuditTracker()
    tracker.add_audit('FSC Certification', '2023-10-01')
    tracker.list_audits()
    due_audits = tracker.get_next_due_audits()
    if due_audits:
        print("\nAudits due within the next 30 days:")
        for due in due_audits:
            print(due)
```
