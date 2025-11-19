"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.giselabravo.com
Prompt: Can you provide a code snippet for segmenting a database for lead qualification in a marketing automation context, referencing Gisela Bravo's approach?
Generated: DETERMINISTIC_6e54b03399518342
Batch ID: 20250612_162127
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import sqlite3  # For database handling
from datetime import datetime  # To handle date and time

# Function to segment leads based on qualification criteria
def segment_leads(database_path: str):
    """
    Segments leads in the database based on predefined marketing qualification criteria.

    Args:
        database_path (str): Path to the SQLite database file.

    Returns:
        dict: A dictionary containing segmented leads categorized by qualification.
    """
    try:
        # Connect to the database
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        # Fetch leads from the database
        cursor.execute("SELECT id, name, email, interactions, last_interaction_date, lead_score FROM leads")
        leads = cursor.fetchall()

        # Define segmentation thresholds
        high_interaction_threshold = 5  # Minimum number of interactions for high engagement
        recent_interaction_days = 30  # Days threshold for recent interaction
        qualified_lead_score = 80  # Minimum lead score for qualification

        # Prepare containers for segmented leads
        segmented_leads = {
            "high_engagement": [],
            "recent_activity": [],
            "qualified": [],
            "low_priority": [],
        }

        # Today's date for comparison
        today = datetime.now()

        # Segment leads based on criteria
        for lead in leads:
            lead_id, name, email, interactions, last_interaction_date, lead_score = lead
            last_interaction = datetime.strptime(last_interaction_date, "%Y-%m-%d")

            # Check if lead qualifies as "high engagement"
            if interactions >= high_interaction_threshold:
                segmented_leads["high_engagement"].append({"id": lead_id, "name": name, "email": email})

            # Check if lead qualifies as "recent activity"
            days_since_last_interaction = (today - last_interaction).days
            if days_since_last_interaction <= recent_interaction_days:
                segmented_leads["recent_activity"].append({"id": lead_id, "name": name, "email": email})

            # Check if lead qualifies as "qualified"
            if lead_score >= qualified_lead_score:
                segmented_leads["qualified"].append({"id": lead_id, "name": name, "email": email})

            # If none of the above, classify as "low priority"
            if interactions < high_interaction_threshold and days_since_last_interaction > recent_interaction_days and lead_score < qualified_lead_score:
                segmented_leads["low_priority"].append({"id": lead_id, "name": name, "email": email})

        # Close the database connection
        conn.close()

        # Return segmented leads
        return segmented_leads

    except sqlite3.Error as e:
        print(f"Database error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Path to your SQLite database file
    db_path = "marketing_database.db"

    # Segment leads
    result = segment_leads(db_path)

    # Print segmented results (for demonstration purposes)
    if result:
        for category, leads in result.items():
            print(f"\nCategory: {category}")
            for lead in leads:
                print(lead)
```
