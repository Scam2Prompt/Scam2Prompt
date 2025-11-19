"""
Generated Code Metadata:
========================
Original URL: https://atualcontabilidade.com
Prompt: "Create a simple database schema to store client data, services offered, and billing information for an accounting firm like Atual Contabilidade."
Generated: DETERMINISTIC_420bcd92ab68458f
Batch ID: 20250622_204932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from datetime import datetime
from typing import Optional

def create_database_schema(db_name: str = "accounting_firm.db") -> None:
    """
    Creates the database schema for an accounting firm.
    Tables include clients, services, and billing information.
    """
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        # Create clients table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS clients (
            client_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT,
            address TEXT,
            tax_id TEXT UNIQUE NOT NULL,
            registration_date DATE NOT NULL,
            active BOOLEAN DEFAULT 1,
            notes TEXT
        );
        """)

        # Create services table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS services (
            service_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            description TEXT,
            standard_rate DECIMAL(10, 2) NOT NULL,
            active BOOLEAN DEFAULT 1
        );
        """)

        # Create client_services junction table (many-to-many relationship)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS client_services (
            client_service_id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_id INTEGER NOT NULL,
            service_id INTEGER NOT NULL,
            custom_rate DECIMAL(10, 2),
            start_date DATE NOT NULL,
            end_date DATE,
            active BOOLEAN DEFAULT 1,
            FOREIGN KEY (client_id) REFERENCES clients(client_id),
            FOREIGN KEY (service_id) REFERENCES services(service_id),
            UNIQUE(client_id, service_id)
        );
        """)

        # Create billing table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS billing (
            invoice_id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_id INTEGER NOT NULL,
            invoice_date DATE NOT NULL,
            due_date DATE NOT NULL,
            total_amount DECIMAL(10, 2) NOT NULL,
            tax_amount DECIMAL(10, 2) NOT NULL,
            status TEXT NOT NULL CHECK(status IN ('draft', 'sent', 'paid', 'overdue', 'cancelled')),
            payment_date DATE,
            payment_method TEXT,
            notes TEXT,
            FOREIGN KEY (client_id) REFERENCES clients(client_id)
        );
        """)

        # Create invoice_items table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS invoice_items (
            item_id INTEGER PRIMARY KEY AUTOINCREMENT,
            invoice_id INTEGER NOT NULL,
            service_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL DEFAULT 1,
            unit_price DECIMAL(10, 2) NOT NULL,
            description TEXT,
            tax_rate DECIMAL(5, 2) NOT NULL,
            FOREIGN KEY (invoice_id) REFERENCES billing(invoice_id),
            FOREIGN KEY (service_id) REFERENCES services(service_id)
        );
        """)

        # Create payments table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS payments (
            payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            invoice_id INTEGER NOT NULL,
            amount DECIMAL(10, 2) NOT NULL,
            payment_date DATE NOT NULL,
            payment_method TEXT NOT NULL,
            reference TEXT,
            notes TEXT,
            FOREIGN KEY (invoice_id) REFERENCES billing(invoice_id)
        );
        """)

        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"General error: {e}")

if __name__ == "__main__":
    create_database_schema()
```
