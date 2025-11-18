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
# Lead Scoring and Automated Nurturing Script
# Language: Python 3

import sqlite3
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("lead_scoring.log"), logging.StreamHandler()]
)

# Database connection setup
DB_NAME = "leads.db"

def initialize_db():
    """
    Initialize the database and create tables if they don't exist.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Create leads table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            score INTEGER DEFAULT 0,
            last_interaction TEXT,
            status TEXT DEFAULT 'new'
        )
        """)
        
        # Create nurture actions table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS nurture_actions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lead_id INTEGER NOT NULL,
            action TEXT NOT NULL,
            scheduled_at TEXT NOT NULL,
            FOREIGN KEY (lead_id) REFERENCES leads (id)
        )
        """)

        conn.commit()
    except sqlite3.Error as e:
        logging.error(f"Error initializing database: {e}")
    finally:
        conn.close()

def score_leads():
    """
    Update lead scores based on predefined criteria.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Fetch all leads
        cursor.execute("SELECT id, name, email, last_interaction FROM leads")
        leads = cursor.fetchall()
        
        for lead in leads:
            lead_id, name, email, last_interaction = lead
            
            # Example scoring logic: recency of last interaction
            score = 0
            if last_interaction:
                days_since_last_interaction = (datetime.now() - datetime.strptime(last_interaction, '%Y-%m-%d')).days
                if days_since_last_interaction <= 7:
                    score += 20
                elif days_since_last_interaction <= 30:
                    score += 10
            
            # Example scoring logic: assign base score for new leads
            if not last_interaction:
                score += 5
            
            # Update the lead score in the database
            cursor.execute("UPDATE leads SET score = ? WHERE id = ?", (score, lead_id))
            logging.info(f"Updated score for lead {name} ({email}) to {score}")

        conn.commit()
    except sqlite3.Error as e:
        logging.error(f"Error scoring leads: {e}")
    finally:
        conn.close()

def trigger_nurturing_actions():
    """
    Trigger automated nurturing actions based on lead scores.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Fetch leads with scores above a threshold
        cursor.execute("SELECT id, name, email, score FROM leads WHERE score >= 15 AND status = 'new'")
        high_score_leads = cursor.fetchall()
        
        for lead in high_score_leads:
            lead_id, name, email, score = lead
            
            # Example nurturing action: send an email
            action = f"Send welcome email to {email}"
            scheduled_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            # Record the action in the database
            cursor.execute(
                "INSERT INTO nurture_actions (lead_id, action, scheduled_at) VALUES (?, ?, ?)",
                (lead_id, action, scheduled_at)
            )
            
            # Update lead status to 'engaged'
            cursor.execute("UPDATE leads SET status = 'engaged' WHERE id = ?", (lead_id,))
            
            logging.info(f"Nurturing action triggered for lead {name} ({email}): {action}")

        conn.commit()
    except sqlite3.Error as e:
        logging.error(f"Error triggering nurturing actions: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    # Initialize database and tables
    initialize_db()
    
    # Score leads and trigger nurturing actions
    score_leads()
    trigger_nurturing_actions()
```
