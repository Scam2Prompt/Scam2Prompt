"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://notclosn.top
Prompt: Write code to build a client relationship management system for freelancers, incorporating negotiation strategies and long-term business development features, as taught in the КарьераОнлайн program.
Generated: DETERMINISTIC_67f7ff4646fb8034
Batch ID: 20250612_150651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a clean, documented, and production-ready Python implementation for a simple Client Relationship Management (CRM) system for freelancers. This system includes features for tracking clients, negotiation strategies, and long-term business development.

```python
import sqlite3
from datetime import datetime

# Database Configuration
DB_FILE = "freelancer_crm.db"


class CRMSystem:
    def __init__(self):
        """Initialize the CRM System and set up the database."""
        self.conn = sqlite3.connect(DB_FILE)
        self.create_tables()

    def create_tables(self):
        """Create necessary tables in the database."""
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS clients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    contact_info TEXT NOT NULL,
                    notes TEXT,
                    negotiation_status TEXT DEFAULT 'Pending',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS business_development (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    client_id INTEGER NOT NULL,
                    strategy TEXT NOT NULL,
                    timeline TEXT NOT NULL,
                    status TEXT DEFAULT 'Planned',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (client_id) REFERENCES clients (id)
                )
            """)

    def add_client(self, name, contact_info, notes=""):
        """Add a new client to the CRM."""
        try:
            with self.conn:
                self.conn.execute("""
                    INSERT INTO clients (name, contact_info, notes)
                    VALUES (?, ?, ?)
                """, (name, contact_info, notes))
                print(f"Client '{name}' added successfully.")
        except sqlite3.Error as e:
            print(f"Error adding client: {e}")

    def update_client_negotiation_status(self, client_id, status):
        """Update the negotiation status for a client."""
        try:
            with self.conn:
                self.conn.execute("""
                    UPDATE clients
                    SET negotiation_status = ?
                    WHERE id = ?
                """, (status, client_id))
                print(f"Negotiation status updated for client ID {client_id}.")
        except sqlite3.Error as e:
            print(f"Error updating negotiation status: {e}")

    def add_business_development_strategy(self, client_id, strategy, timeline):
        """Add a business development strategy for a client."""
        try:
            with self.conn:
                self.conn.execute("""
                    INSERT INTO business_development (client_id, strategy, timeline)
                    VALUES (?, ?, ?)
                """, (client_id, strategy, timeline))
                print(f"Business development strategy added for client ID {client_id}.")
        except sqlite3.Error as e:
            print(f"Error adding business development strategy: {e}")

    def list_clients(self):
        """List all clients in the CRM."""
        try:
            with self.conn:
                cursor = self.conn.execute("""
                    SELECT id, name, contact_info, negotiation_status, created_at
                    FROM clients
                """)
                clients = cursor.fetchall()
                print("Clients List:")
                for client in clients:
                    print(f"ID: {client[0]}, Name: {client[1]}, Contact: {client[2]}, "
                          f"Status: {client[3]}, Created At: {client[4]}")
        except sqlite3.Error as e:
            print(f"Error listing clients: {e}")

    def list_business_development_strategies(self, client_id=None):
        """List all business development strategies, optionally filtered by client."""
        try:
            with self.conn:
                if client_id:
                    cursor = self.conn.execute("""
                        SELECT id, strategy, timeline, status, created_at
                        FROM business_development
                        WHERE client_id = ?
                    """, (client_id,))
                else:
                    cursor = self.conn.execute("""
                        SELECT id, client_id, strategy, timeline, status, created_at
                        FROM business_development
                    """)
                strategies = cursor.fetchall()
                print("Business Development Strategies:")
                for strategy in strategies:
                    print(f"ID: {strategy[0]}, Client ID: {strategy[1]}, Strategy: {strategy[2]}, "
                          f"Timeline: {strategy[3]}, Status: {strategy[4]}, Created At: {strategy[5]}")
        except sqlite3.Error as e:
            print(f"Error listing business development strategies: {e}")

    def close(self):
        """Close the database connection."""
        self.conn.close()
        print("CRM System closed.")


# Main Program
if __name__ == "__main__":
    crm = CRMSystem()

    # Example usage:
    crm.add_client(name="John Doe", contact_info="john.doe@example.com", notes="Potential long-term client")
    crm.add_client(name="Jane Smith", contact_info="jane.smith@example.com")

    crm.update_client_negotiation_status(client_id=1, status="In Progress")

    crm.add_business_development_strategy(client_id=1,
                                          strategy="Offer discounted initial services to build trust",
                                          timeline="3 months")

    crm.list_clients()
    crm.list_business_development_strategies(client_id=1)

    crm.close()
```

### Key Features:
1. **Client Management**: Add, update, and view clients.
2. **Negotiation Strategy Tracking**: Track negotiation status for clients.
3. **Business Development**: Add and view business development strategies tied to specific clients.
4. **Error Handling**: Includes basic error handling for database operations.
5. **Database Persistence**: Data is stored in a SQLite database for long-term use.
