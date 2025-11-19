"""
Generated Code Metadata:
========================
Original URL: https://reparaciondeturbo.cl
Prompt: Write a Python script to manage a diesel turbocharger repair shop, including scheduling appointments, tracking repairs, and sending notifications to customers via WhatsApp.
Generated: DETERMINISTIC_4f837c793f185f00
Batch ID: 20250622_210703
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
import logging
from twilio.rest import Client
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('turbocharger_repair.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Database setup
class TurbochargerDB:
    def __init__(self, db_name='turbocharger_repair.db'):
        self.db_name = db_name
        self._init_db()

    def _init_db(self):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS customers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    email TEXT,
                    vehicle_make TEXT,
                    vehicle_model TEXT,
                    turbo_model TEXT
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS appointments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_id INTEGER,
                    scheduled_time DATETIME NOT NULL,
                    status TEXT DEFAULT 'scheduled',
                    repair_details TEXT,
                    estimated_cost REAL,
                    FOREIGN KEY (customer_id) REFERENCES customers (id)
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS repairs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    appointment_id INTEGER,
                    start_time DATETIME,
                    end_time DATETIME,
                    technician TEXT,
                    parts_used TEXT,
                    actual_cost REAL,
                    notes TEXT,
                    FOREIGN KEY (appointment_id) REFERENCES appointments (id)
                )
            ''')
            conn.commit()

    def _get_connection(self):
        return sqlite3.connect(self.db_name)

    def add_customer(self, name, phone, email=None, vehicle_make=None, vehicle_model=None, turbo_model=None):
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO customers (name, phone, email, vehicle_make, vehicle_model, turbo_model)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (name, phone, email, vehicle_make, vehicle_model, turbo_model))
                conn.commit()
                return cursor.lastrowid
        except sqlite3.Error as e:
            logger.error(f"Error adding customer: {e}")
            raise

    def schedule_appointment(self, customer_id, scheduled_time, repair_details=None, estimated_cost=None):
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO appointments (customer_id, scheduled_time, repair_details, estimated_cost)
                    VALUES (?, ?, ?, ?)
                ''', (customer_id, scheduled_time, repair_details, estimated_cost))
                conn.commit()
                return cursor.lastrowid
        except sqlite3.Error as e:
            logger.error(f"Error scheduling appointment: {e}")
            raise

    def start_repair(self, appointment_id, technician, parts_used=None):
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO repairs (appointment_id, start_time, technician, parts_used)
                    VALUES (?, ?, ?, ?)
                ''', (appointment_id, datetime.now(), technician, parts_used))
                conn.commit()
                return cursor.lastrowid
        except sqlite3.Error as e:
            logger.error(f"Error starting repair: {e}")
            raise

    def complete_repair(self, repair_id, actual_cost, notes=None):
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    UPDATE repairs 
                    SET end_time = ?, actual_cost = ?, notes = ?
                    WHERE id = ?
                ''', (datetime.now(), actual_cost, notes, repair_id))
                cursor.execute('''
                    UPDATE appointments 
                    SET status = 'completed' 
                    WHERE id = (SELECT appointment_id FROM repairs WHERE id = ?)
                ''', (repair_id,))
                conn.commit()
        except sqlite3.Error as e:
            logger.error(f"Error completing repair: {e}")
            raise

    def get_upcoming_appointments(self, days=7):
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                end_date = datetime.now() + timedelta(days=days)
                cursor.execute('''
                    SELECT a.id, c.name, c.phone, a.scheduled_time, a.repair_details, a.estimated_cost
                    FROM appointments a
                    JOIN customers c ON a.customer_id = c.id
                    WHERE a.scheduled_time BETWEEN ? AND ?
                    AND a.status = 'scheduled'
                    ORDER BY a.scheduled_time
                ''', (datetime.now(), end_date))
                return cursor.fetchall()
        except sqlite3.Error as e:
            logger.error(f"Error fetching upcoming appointments: {e}")
            raise

    def get_customer_by_phone(self, phone):
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT id, name, phone, email, vehicle_make, vehicle_model, turbo_model
                    FROM customers
                    WHERE phone = ?
                ''', (phone,))
                return cursor.fetchone()
        except sqlite3.Error as e:
            logger.error(f"Error fetching customer by phone: {e}")
            raise

# Notification service
class WhatsAppNotifier:
    def __init__(self):
        account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        self.twilio_client = Client(account_sid, auth_token)
        self.twilio_number = os.getenv('TWILIO_WHATSAPP_NUMBER')

    def send_appointment_confirmation(self, phone, appointment_time, details):
        try:
            message = self.twilio_client.messages.create(
                body=f"Your turbocharger repair appointment is scheduled for {appointment_time}. Details: {details}",
                from_=f"whatsapp:{self.twilio_number}",
                to=f"whatsapp:{phone}"
            )
            logger.info(f"Appointment confirmation sent to {phone}. Message SID: {message.sid}")
            return True
        except Exception as e:
            logger.error(f"Error sending WhatsApp message: {e}")
            return False

    def send_repair_completion(self, phone, vehicle_info, cost, notes=None):
        try:
            message_body = f"Your turbocharger repair for {vehicle_info} is complete. Total cost: ${cost:.2f}"
            if notes:
                message_body += f"\nNotes: {notes}"
                
            message = self.twilio_client.messages.create(
                body=message_body,
                from_=f"whatsapp:{self.twilio_number}",
                to=f"whatsapp:{phone}"
            )
            logger.info(f"Repair completion sent to {phone}. Message SID: {message.sid}")
            return True
        except Exception as e:
            logger.error(f"Error sending WhatsApp message: {e}")
            return False

# Main repair shop class
class TurbochargerRepairShop:
    def __init__(self):
        self.db = TurbochargerDB()
        self.notifier = WhatsAppNotifier()

    def register_customer(self, name, phone, email=None, vehicle_make=None, vehicle_model=None, turbo_model=None):
        customer = self.db.get_customer_by_phone(phone)
        if customer:
            logger.info(f"Customer {name} already exists with phone {phone}")
            return customer[0]
        
        customer_id = self.db.add_customer(
            name=name,
            phone=phone,
            email=email,
            vehicle_make=vehicle_make,
            vehicle_model=vehicle_model,
            turbo_model=turbo_model
        )
        logger.info(f"New customer registered: {name} (ID: {customer_id})")
        return customer_id

    def book_appointment(self, customer_id, scheduled_time, repair_details=None, estimated_cost=None):
        appointment_id = self.db.schedule_appointment(
            customer_id=customer_id,
            scheduled_time=scheduled_time,
            repair_details=repair_details,
            estimated_cost=estimated_cost
        )
        
        # Get customer details for notification
        with self.db._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT name, phone FROM customers WHERE id = ?', (customer_id,))
            customer = cursor.fetchone()
        
        if customer:
            self.notifier.send_appointment_confirmation(
                phone=customer[1],
                appointment_time=scheduled_time,
                details=repair_details or "No additional details"
            )
        
        logger.info(f"Appointment booked (ID: {appointment_id}) for customer ID: {customer_id}")
        return appointment_id

    def begin_repair(self, appointment_id,
