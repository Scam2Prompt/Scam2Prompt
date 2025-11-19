"""
Generated Code Metadata:
========================
Original URL: https://www.homecareassistancebarrie.ca
Prompt: Design a simple database schema to store client information, care plans, and caregiver schedules for a home care assistance agency like Home Care Assistance.
Generated: DETERMINISTIC_9131b23e9918d088
Batch ID: 20250622_205634
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

def create_database_schema(db_name='home_care_assistance.db'):
    """
    Creates the database schema for a home care assistance agency.
    Includes tables for clients, caregivers, care plans, and schedules.
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create Clients table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clients (
        client_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        date_of_birth DATE NOT NULL,
        address TEXT NOT NULL,
        city TEXT NOT NULL,
        state TEXT NOT NULL,
        zip_code TEXT NOT NULL,
        phone_number TEXT NOT NULL,
        email TEXT,
        emergency_contact_name TEXT NOT NULL,
        emergency_contact_phone TEXT NOT NULL,
        medical_conditions TEXT,
        medications TEXT,
        allergies TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Create Caregivers table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS caregivers (
        caregiver_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        date_of_birth DATE NOT NULL,
        address TEXT NOT NULL,
        city TEXT NOT NULL,
        state TEXT NOT NULL,
        zip_code TEXT NOT NULL,
        phone_number TEXT NOT NULL,
        email TEXT NOT NULL,
        hire_date DATE NOT NULL,
        certification TEXT,
        specialization TEXT,
        status TEXT CHECK(status IN ('active', 'inactive', 'on_leave')) DEFAULT 'active',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Create Care Plans table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS care_plans (
        plan_id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_id INTEGER NOT NULL,
        created_by INTEGER NOT NULL,
        plan_name TEXT NOT NULL,
        description TEXT NOT NULL,
        start_date DATE NOT NULL,
        end_date DATE,
        frequency TEXT NOT NULL,
        duration_minutes INTEGER NOT NULL,
        tasks TEXT NOT NULL,
        special_instructions TEXT,
        status TEXT CHECK(status IN ('active', 'completed', 'cancelled')) DEFAULT 'active',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (client_id) REFERENCES clients(client_id),
        FOREIGN KEY (created_by) REFERENCES caregivers(caregiver_id)
    )
    ''')

    # Create Schedule table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS schedules (
        schedule_id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_id INTEGER NOT NULL,
        caregiver_id INTEGER NOT NULL,
        plan_id INTEGER NOT NULL,
        scheduled_date DATE NOT NULL,
        start_time TIME NOT NULL,
        end_time TIME NOT NULL,
        status TEXT CHECK(status IN ('scheduled', 'completed', 'cancelled', 'no_show')) DEFAULT 'scheduled',
        notes TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (client_id) REFERENCES clients(client_id),
        FOREIGN KEY (caregiver_id) REFERENCES caregivers(caregiver_id),
        FOREIGN KEY (plan_id) REFERENCES care_plans(plan_id)
    )
    ''')

    # Create indexes for better performance
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_client_id ON clients(client_id)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_caregiver_id ON caregivers(caregiver_id)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_plan_id ON care_plans(plan_id)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_schedule_client ON schedules(client_id)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_schedule_caregiver ON schedules(caregiver_id)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_schedule_date ON schedules(scheduled_date)')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database_schema()
```
