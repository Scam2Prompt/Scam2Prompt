"""
Generated Code Metadata:
========================
Original URL: https://bplservicescenter.com
Prompt: Write a Python script to manage BPL appliance repair services, including scheduling and customer information, for a service center in Delhi.
Generated: DETERMINISTIC_1aa93cb556bea699
Batch ID: 20250622_211528
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from datetime import datetime, timedelta
import sys

class BPLServiceCenter:
    """
    A class to manage BPL appliance repair services including scheduling and customer information.
    """

    def __init__(self, db_name='bpl_service_center.db'):
        """
        Initialize the service center with a SQLite database.
        
        Args:
            db_name (str): Name of the SQLite database file.
        """
        self.db_name = db_name
        self._initialize_database()

    def _initialize_database(self):
        """
        Create the necessary tables if they don't exist.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            # Create customers table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS customers (
                    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    email TEXT,
                    address TEXT NOT NULL,
                    appliance_type TEXT NOT NULL,
                    appliance_model TEXT NOT NULL
                )
            ''')
            
            # Create service_requests table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS service_requests (
                    request_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_id INTEGER NOT NULL,
                    issue_description TEXT NOT NULL,
                    request_date TEXT NOT NULL,
                    scheduled_date TEXT NOT NULL,
                    status TEXT NOT NULL DEFAULT 'Pending',
                    technician_notes TEXT,
                    FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
                )
            ''')
            
            conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            sys.exit(1)
        finally:
            if conn:
                conn.close()

    def add_customer(self, name, phone, email, address, appliance_type, appliance_model):
        """
        Add a new customer to the database.
        
        Args:
            name (str): Customer's name.
            phone (str): Customer's phone number.
            email (str): Customer's email address.
            address (str): Customer's address.
            appliance_type (str): Type of appliance.
            appliance_model (str): Model of appliance.
            
        Returns:
            int: The customer_id of the newly added customer.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO customers (name, phone, email, address, appliance_type, appliance_model)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (name, phone, email, address, appliance_type, appliance_model))
            
            conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding customer: {e}")
            return None
        finally:
            if conn:
                conn.close()

    def schedule_service(self, customer_id, issue_description, scheduled_date, technician_notes=None):
        """
        Schedule a service request for a customer.
        
        Args:
            customer_id (int): ID of the customer.
            issue_description (str): Description of the issue.
            scheduled_date (str): Scheduled date in YYYY-MM-DD format.
            technician_notes (str, optional): Notes from the technician.
            
        Returns:
            int: The request_id of the newly scheduled service.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            request_date = datetime.now().strftime('%Y-%m-%d')
            
            cursor.execute('''
                INSERT INTO service_requests (customer_id, issue_description, request_date, scheduled_date, technician_notes)
                VALUES (?, ?, ?, ?, ?)
            ''', (customer_id, issue_description, request_date, scheduled_date, technician_notes))
            
            conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error scheduling service: {e}")
            return None
        finally:
            if conn:
                conn.close()

    def update_service_status(self, request_id, status, technician_notes=None):
        """
        Update the status of a service request.
        
        Args:
            request_id (int): ID of the service request.
            status (str): New status (e.g., 'Pending', 'In Progress', 'Completed', 'Cancelled').
            technician_notes (str, optional): Additional notes from the technician.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            cursor.execute('''
                UPDATE service_requests
                SET status = ?, technician_notes = ?
                WHERE request_id = ?
            ''', (status, technician_notes, request_id))
            
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error updating service status: {e}")
        finally:
            if conn:
                conn.close()

    def get_customer_services(self, customer_id):
        """
        Get all service requests for a customer.
        
        Args:
            customer_id (int): ID of the customer.
            
        Returns:
            list: List of service requests for the customer.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT * FROM service_requests
                WHERE customer_id = ?
            ''', (customer_id,))
            
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error fetching customer services: {e}")
            return []
        finally:
            if conn:
                conn.close()

    def get_scheduled_services(self, start_date, end_date):
        """
        Get all services scheduled between two dates.
        
        Args:
            start_date (str): Start date in YYYY-MM-DD format.
            end_date (str): End date in YYYY-MM-DD format.
            
        Returns:
            list: List of scheduled services.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT sr.*, c.name, c.phone, c.appliance_type, c.appliance_model
                FROM service_requests sr
                JOIN customers c ON sr.customer_id = c.customer_id
                WHERE sr.scheduled_date BETWEEN ? AND ?
                ORDER BY sr.scheduled_date
            ''', (start_date, end_date))
            
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error fetching scheduled services: {e}")
            return []
        finally:
            if conn:
                conn.close()

    def get_service_details(self, request_id):
        """
        Get details of a specific service request.
        
        Args:
            request_id (int): ID of the service request.
            
        Returns:
            tuple: Service request details.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT sr.*, c.name, c.phone, c.email, c.address, c.appliance_type, c.appliance_model
                FROM service_requests sr
                JOIN customers c ON sr.customer_id = c.customer_id
                WHERE sr.request_id = ?
            ''', (request_id,))
            
            return cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Error fetching service details: {e}")
            return None
        finally:
            if conn:
                conn.close()

# Example usage
if __name__ == "__main__":
    service_center = BPLServiceCenter()
    
    # Add a customer
    customer_id = service_center.add_customer(
        name="John Doe",
        phone="9876543210",
        email="john.doe@example.com",
        address="123 Main St, Delhi",
        appliance_type="Refrigerator",
        appliance_model="BPL RF-200"
    )
    
    if customer_id:
        print(f"Added customer with ID: {customer_id}")
        
        # Schedule a service
        scheduled_date = (datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d')
        request_id = service_center.schedule_service(
            customer_id=customer_id,
            issue_description="Not cooling properly",
            scheduled_date=scheduled_date
        )
        
        if request_id:
            print(f"Scheduled service with ID: {request_id}")
            
            # Update service status
            service_center.update_service_status(
                request_id=request_id,
                status="In Progress",
                technician_notes="Checked coolant levels"
            )
            
            # Get service details
            service_details = service_center.get_service_details(request_id)
            print(f"Service details: {service_details}")
            
            # Get scheduled services for next week
            start_date = datetime.now().strftime('%Y-%m-%d')
            end_date = (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')
            scheduled_services = service_center.get_scheduled_services(start_date, end_date)
            print(f"Scheduled services for next week: {scheduled_services}")
```
