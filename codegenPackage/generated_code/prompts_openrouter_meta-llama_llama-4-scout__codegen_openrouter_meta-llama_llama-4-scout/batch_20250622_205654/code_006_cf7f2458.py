"""
Generated Code Metadata:
========================
Original URL: https://mdatechsys.com
Prompt: "Create a CRM software for a small business, incorporating features such as contact management, sales tracking, and marketing automation, using a suitable programming language and database, inspired by MDA Tech Sys's CRM software services."
Generated: DETERMINISTIC_cf7f245804bbeabd
Batch ID: 20250622_205654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**CRM Software for Small Business**
=====================================

**Database Schema**
------------------

```sql
CREATE TABLE contacts (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20),
    address VARCHAR(255)
);

CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    contact_id INTEGER NOT NULL,
    sale_date DATE NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    description VARCHAR(255),
    FOREIGN KEY (contact_id) REFERENCES contacts(id)
);

CREATE TABLE marketing_campaigns (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255),
    start_date DATE NOT NULL,
    end_date DATE NOT NULL
);

CREATE TABLE marketing_automations (
    id SERIAL PRIMARY KEY,
    campaign_id INTEGER NOT NULL,
    contact_id INTEGER NOT NULL,
    automation_date DATE NOT NULL,
    FOREIGN KEY (campaign_id) REFERENCES marketing_campaigns(id),
    FOREIGN KEY (contact_id) REFERENCES contacts(id)
);
```

**Python CRM Application**
---------------------------

```python
import psycopg2
from datetime import date

class CRM:
    def __init__(self, db_host, db_username, db_password, db_name):
        self.conn = psycopg2.connect(
            host=db_host,
            user=db_username,
            password=db_password,
            dbname=db_name
        )
        self.cur = self.conn.cursor()

    def create_contact(self, first_name, last_name, email, phone=None, address=None):
        try:
            self.cur.execute("INSERT INTO contacts (first_name, last_name, email, phone, address) VALUES (%s, %s, %s, %s, %s) RETURNING *",
                             (first_name, last_name, email, phone, address))
            self.conn.commit()
            return self.cur.fetchone()
        except psycopg2.Error as e:
            self.conn.rollback()
            print(f"Error creating contact: {e}")

    def get_contacts(self):
        try:
            self.cur.execute("SELECT * FROM contacts")
            return self.cur.fetchall()
        except psycopg2.Error as e:
            print(f"Error getting contacts: {e}")

    def create_sale(self, contact_id, sale_date, amount, description=None):
        try:
            self.cur.execute("INSERT INTO sales (contact_id, sale_date, amount, description) VALUES (%s, %s, %s, %s) RETURNING *",
                             (contact_id, sale_date, amount, description))
            self.conn.commit()
            return self.cur.fetchone()
        except psycopg2.Error as e:
            self.conn.rollback()
            print(f"Error creating sale: {e}")

    def get_sales(self, contact_id=None):
        try:
            if contact_id:
                self.cur.execute("SELECT * FROM sales WHERE contact_id = %s", (contact_id,))
            else:
                self.cur.execute("SELECT * FROM sales")
            return self.cur.fetchall()
        except psycopg2.Error as e:
            print(f"Error getting sales: {e}")

    def create_marketing_campaign(self, name, description, start_date, end_date):
        try:
            self.cur.execute("INSERT INTO marketing_campaigns (name, description, start_date, end_date) VALUES (%s, %s, %s, %s) RETURNING *",
                             (name, description, start_date, end_date))
            self.conn.commit()
            return self.cur.fetchone()
        except psycopg2.Error as e:
            self.conn.rollback()
            print(f"Error creating marketing campaign: {e}")

    def create_marketing_automation(self, campaign_id, contact_id, automation_date):
        try:
            self.cur.execute("INSERT INTO marketing_automations (campaign_id, contact_id, automation_date) VALUES (%s, %s, %s) RETURNING *",
                             (campaign_id, contact_id, automation_date))
            self.conn.commit()
            return self.cur.fetchone()
        except psycopg2.Error as e:
            self.conn.rollback()
            print(f"Error creating marketing automation: {e}")

def main():
    crm = CRM('localhost', 'username', 'password', 'crm_database')

    # Create a new contact
    contact = crm.create_contact('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St')
    print(contact)

    # Get all contacts
    contacts = crm.get_contacts()
    for contact in contacts:
        print(contact)

    # Create a new sale
    sale = crm.create_sale(1, date.today(), 100.00, 'Test sale')
    print(sale)

    # Get all sales for a contact
    sales = crm.get_sales(1)
    for sale in sales:
        print(sale)

    # Create a new marketing campaign
    campaign = crm.create_marketing_campaign('Test Campaign', 'This is a test campaign', date.today(), date.today())
    print(campaign)

    # Create a new marketing automation
    automation = crm.create_marketing_automation(1, 1, date.today())
    print(automation)

if __name__ == '__main__':
    main()
```

**Requirements**
---------------

* Python 3.8+
* psycopg2 library (`pip install psycopg2`)
* PostgreSQL database

**Setup**
--------

1. Create a new PostgreSQL database and user.
2. Run the database schema SQL script.
3. Install the required Python libraries.
4. Update the `CRM` class constructor with your database credentials.
5. Run the `main` function to test the CRM application.
