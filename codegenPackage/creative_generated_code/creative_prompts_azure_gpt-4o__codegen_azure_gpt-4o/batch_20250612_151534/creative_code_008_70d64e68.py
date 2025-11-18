"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.olgon.net
Prompt: Design a monitoring system for extension agents to ensure best practices in production, incorporating evaluation metrics, as outlined by Olgon Prime Resources Ltd.
Generated: DETERMINISTIC_70d64e689ef5c651
Batch ID: 20250612_151534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the Python code for the requested monitoring system:

```python
import sqlite3
from datetime import datetime

# Database setup
DB_NAME = 'monitoring_system.db'


def create_database():
    """
    Initialize the database and create required tables.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Create table for extension agents
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ExtensionAgents (
                agent_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                region TEXT NOT NULL,
                contact_info TEXT
            )
        """)

        # Create table for monitoring records
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS MonitoringRecords (
                record_id INTEGER PRIMARY KEY AUTOINCREMENT,
                agent_id INTEGER NOT NULL,
                evaluation_date TEXT NOT NULL,
                metric_name TEXT NOT NULL,
                metric_value REAL NOT NULL,
                comments TEXT,
                FOREIGN KEY (agent_id) REFERENCES ExtensionAgents(agent_id)
            )
        """)

        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()


def add_extension_agent(name, region, contact_info):
    """
    Add a new extension agent to the database.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO ExtensionAgents (name, region, contact_info)
            VALUES (?, ?, ?)
        """, (name, region, contact_info))

        conn.commit()
        print("Extension agent added successfully.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()


def record_evaluation(agent_id, metric_name, metric_value, comments=""):
    """
    Record an evaluation metric for an extension agent.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        evaluation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("""
            INSERT INTO MonitoringRecords (agent_id, evaluation_date, metric_name, metric_value, comments)
            VALUES (?, ?, ?, ?, ?)
        """, (agent_id, evaluation_date, metric_name, metric_value, comments))

        conn.commit()
        print("Evaluation recorded successfully.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()


def fetch_evaluation_metrics(agent_id):
    """
    Fetch all evaluation metrics for a specific extension agent.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT evaluation_date, metric_name, metric_value, comments
            FROM MonitoringRecords
            WHERE agent_id = ?
            ORDER BY evaluation_date DESC
        """, (agent_id,))
        
        records = cursor.fetchall()
        if records:
            print("Evaluation Metrics:")
            for record in records:
                print(f"Date: {record[0]}, Metric: {record[1]}, Value: {record[2]}, Comments: {record[3]}")
        else:
            print("No metrics found for this agent.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()


# Main program initialization
if __name__ == "__main__":
    # Initialize the database
    create_database()

    # Sample usage
    add_extension_agent("John Doe", "North Region", "john.doe@example.com")
    add_extension_agent("Jane Smith", "South Region", "jane.smith@example.com")

    record_evaluation(agent_id=1, metric_name="Crop Yield", metric_value=85.5, comments="Excellent performance.")
    record_evaluation(agent_id=1, metric_name="Farmer Satisfaction", metric_value=92.3, comments="Farmers are happy.")
    record_evaluation(agent_id=2, metric_name="Training Sessions", metric_value=10, comments="Consistent efforts.")

    fetch_evaluation_metrics(agent_id=1)
    fetch_evaluation_metrics(agent_id=2)
```

This code sets up a monitoring system with a database backend and includes features to add agents, record evaluation metrics, and retrieve metrics for specific agents. It adheres to best practices and includes error handling.
