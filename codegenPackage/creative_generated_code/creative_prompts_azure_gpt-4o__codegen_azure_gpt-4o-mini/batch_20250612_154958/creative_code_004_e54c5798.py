"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.giselabravo.com
Prompt: Provide code examples for scoring leads in a database and triggering automated nurturing actions, similar to the strategies mentioned by Gisela Bravo.
Generated: DETERMINISTIC_e54c5798fbc7d3b3
Batch ID: 20250612_154958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from typing import List, Dict, Any

# Define a class to manage the lead scoring and automation
class LeadManager:
    def __init__(self, db_path: str):
        """Initialize the LeadManager with a database connection."""
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self.create_leads_table()

    def create_leads_table(self):
        """Create a leads table if it doesn't exist."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS leads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                score INTEGER DEFAULT 0,
                status TEXT DEFAULT 'new'
            )
        ''')
        self.connection.commit()

    def add_lead(self, name: str, email: str):
        """Add a new lead to the database."""
        try:
            self.cursor.execute('INSERT INTO leads (name, email) VALUES (?, ?)', (name, email))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error adding lead: {e}")

    def score_leads(self) -> List[Dict[str, Any]]:
        """Score all leads based on predefined criteria and return the updated leads."""
        try:
            self.cursor.execute("SELECT * FROM leads")
            leads = self.cursor.fetchall()
            scored_leads = []

            for lead in leads:
                lead_id, name, email, score, status = lead
                # Example scoring logic based on email domain
                if '@example.com' in email:
                    score += 10
                elif '@other.com' in email:
                    score += 5
                
                self.cursor.execute('UPDATE leads SET score = ? WHERE id = ?', (score, lead_id))
                scored_leads.append({'id': lead_id, 'name': name, 'email': email, 'score': score, 'status': status})

            self.connection.commit()
            return scored_leads
        
        except sqlite3.Error as e:
            print(f"Error scoring leads: {e}")
            return []

    def trigger_nurturing_actions(self):
        """Trigger automated nurturing actions based on lead scores."""
        try:
            self.cursor.execute("SELECT * FROM leads WHERE score >= 10 AND status = 'new'")
            leads_to_nurture = self.cursor.fetchall()

            for lead in leads_to_nurture:
                lead_id, name, email, score, status = lead
                self.send_nurturing_email(email)  # Simulate sending an email
                self.cursor.execute('UPDATE leads SET status = ? WHERE id = ?', ('nurtured', lead_id))

            self.connection.commit()
        
        except sqlite3.Error as e:
            print(f"Error triggering nurturing actions: {e}")

    def send_nurturing_email(self, email: str):
        """Simulate sending a nurturing email to the lead."""
        print(f"Sending nurturing email to {email}")

    def close(self):
        """Close the database connection."""
        self.connection.close()


# Usage example
if __name__ == "__main__":
    lead_manager = LeadManager('leads.db')
    lead_manager.add_lead('John Doe', 'john@example.com')
    lead_manager.add_lead('Jane Smith', 'jane@other.com')
    
    scored_leads = lead_manager.score_leads()
    print("Scored Leads:", scored_leads)

    lead_manager.trigger_nurturing_actions()
    lead_manager.close()
```
