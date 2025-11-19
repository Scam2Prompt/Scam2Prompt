"""
Generated Code Metadata:
========================
Original URL: https://www.arclerdesk.com
Prompt: Design a simple printer repair ticketing system using a database and a programming language of your choice, inspired by Arcler Desk's printer repair services.
Generated: DETERMINISTIC_71516a19a7be2ff2
Batch ID: 20250622_205634
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Printer Repair Ticketing System**
=====================================

**Database Schema (SQL)**
-------------------------

```sql
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL
);

CREATE TABLE printers (
    id SERIAL PRIMARY KEY,
    model VARCHAR(255) NOT NULL,
    serial_number VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE tickets (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    printer_id INTEGER NOT NULL,
    issue_description TEXT NOT NULL,
    status VARCHAR(50) NOT NULL DEFAULT 'open',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(id),
    FOREIGN KEY (printer_id) REFERENCES printers(id)
);

CREATE TABLE technicians (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE assignments (
    id SERIAL PRIMARY KEY,
    ticket_id INTEGER NOT NULL,
    technician_id INTEGER NOT NULL,
    assigned_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ticket_id) REFERENCES tickets(id),
    FOREIGN KEY (technician_id) REFERENCES technicians(id)
);
```

**Python Implementation**
-------------------------

```python
import psycopg2
from psycopg2 import Error
from datetime import datetime

class PrinterRepairSystem:
    def __init__(self, db_host, db_name, db_user, db_password):
        self.conn = None
        try:
            self.conn = psycopg2.connect(
                dbname=db_name,
                user=db_user,
                password=db_password,
                host=db_host
            )
            print("Connection to PostgreSQL DB successful")
        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)

    def create_customer(self, name, email, phone):
        try:
            cur = self.conn.cursor()
            cur.execute("INSERT INTO customers (name, email, phone) VALUES (%s, %s, %s) RETURNING *", (name, email, phone))
            self.conn.commit()
            return cur.fetchone()
        except (Exception, Error) as error:
            print("Error while creating customer", error)

    def create_printer(self, model, serial_number):
        try:
            cur = self.conn.cursor()
            cur.execute("INSERT INTO printers (model, serial_number) VALUES (%s, %s) RETURNING *", (model, serial_number))
            self.conn.commit()
            return cur.fetchone()
        except (Exception, Error) as error:
            print("Error while creating printer", error)

    def create_ticket(self, customer_id, printer_id, issue_description):
        try:
            cur = self.conn.cursor()
            cur.execute("INSERT INTO tickets (customer_id, printer_id, issue_description) VALUES (%s, %s, %s) RETURNING *", (customer_id, printer_id, issue_description))
            self.conn.commit()
            return cur.fetchone()
        except (Exception, Error) as error:
            print("Error while creating ticket", error)

    def assign_technician(self, ticket_id, technician_id):
        try:
            cur = self.conn.cursor()
            cur.execute("INSERT INTO assignments (ticket_id, technician_id) VALUES (%s, %s) RETURNING *", (ticket_id, technician_id))
            self.conn.commit()
            return cur.fetchone()
        except (Exception, Error) as error:
            print("Error while assigning technician", error)

    def update_ticket_status(self, ticket_id, status):
        try:
            cur = self.conn.cursor()
            cur.execute("UPDATE tickets SET status = %s, updated_at = %s WHERE id = %s", (status, datetime.now(), ticket_id))
            self.conn.commit()
            return cur.rowcount
        except (Exception, Error) as error:
            print("Error while updating ticket status", error)

    def close_connection(self):
        if self.conn:
            self.conn.close()
            print("Connection closed")

def main():
    db_host = 'localhost'
    db_name = 'printer_repair'
    db_user = 'postgres'
    db_password = 'password'

    system = PrinterRepairSystem(db_host, db_name, db_user, db_password)

    # Create customer
    customer = system.create_customer('John Doe', 'john@example.com', '1234567890')
    print("Customer created:", customer)

    # Create printer
    printer = system.create_printer('HP LaserJet', 'ABC123')
    print("Printer created:", printer)

    # Create ticket
    ticket = system.create_ticket(1, 1, 'Printer not printing')
    print("Ticket created:", ticket)

    # Assign technician
    assignment = system.assign_technician(1, 1)
    print("Technician assigned:", assignment)

    # Update ticket status
    updated_rows = system.update_ticket_status(1, 'in_progress')
    print("Ticket status updated:", updated_rows)

    system.close_connection()

if __name__ == "__main__":
    main()
```
