"""
Generated Code Metadata:
========================
Original URL: https://www.virtualmediaevents.com
Prompt: Generate a script for managing up to 50,000 participants in a virtual event, including tech support and secure data backup systems, as described by Virtual Media Events.
Generated: DETERMINISTIC_7bcc7192c42f5168
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import csv
import sqlite3
import logging
from datetime import datetime
from typing import List, Dict, Optional, Tuple
import hashlib
import uuid
import shutil
import zipfile
import threading
import queue
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Constants
MAX_PARTICIPANTS = 50000
DATABASE_NAME = "event_participants.db"
BACKUP_DIR = "backups"
LOG_FILE = "event_management.log"
CONFIG_FILE = "config.json"

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

class Participant:
    """Class representing a participant in the virtual event."""
    
    def __init__(self, participant_id: str, name: str, email: str, registration_date: str, 
                 ticket_type: str, tech_support_requests: int = 0):
        self.participant_id = participant_id
        self.name = name
        self.email = email
        self.registration_date = registration_date
        self.ticket_type = ticket_type
        self.tech_support_requests = tech_support_requests

    def to_dict(self) -> Dict:
        """Convert participant data to dictionary."""
        return {
            "participant_id": self.participant_id,
            "name": self.name,
            "email": self.email,
            "registration_date": self.registration_date,
            "ticket_type": self.ticket_type,
            "tech_support_requests": self.tech_support_requests
        }

class EventManager:
    """Main class for managing the virtual event."""
    
    def __init__(self):
        self.db_conn = None
        self.cursor = None
        self.config = self._load_config()
        self._initialize_database()
        self._setup_backup_system()
        self.tech_support_queue = queue.Queue()
        self._start_tech_support_workers()

    def _load_config(self) -> Dict:
        """Load configuration from JSON file."""
        try:
            with open(CONFIG_FILE, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logging.error("Config file not found. Using default settings.")
            return {
                "backup_frequency": 3600,  # 1 hour in seconds
                "max_backups": 5,
                "smtp_server": "",
                "smtp_port": 587,
                "smtp_username": "",
                "smtp_password": "",
                "support_email": "support@virtualmediaevents.com"
            }
        except json.JSONDecodeError:
            logging.error("Invalid config file. Using default settings.")
            return {
                "backup_frequency": 3600,
                "max_backups": 5,
                "smtp_server": "",
                "smtp_port": 587,
                "smtp_username": "",
                "smtp_password": "",
                "support_email": "support@virtualmediaevents.com"
            }

    def _initialize_database(self) -> None:
        """Initialize the SQLite database."""
        try:
            self.db_conn = sqlite3.connect(DATABASE_NAME)
            self.cursor = self.db_conn.cursor()
            
            # Create participants table if not exists
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS participants (
                    participant_id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    registration_date TEXT NOT NULL,
                    ticket_type TEXT NOT NULL,
                    tech_support_requests INTEGER DEFAULT 0
                )
            """)
            
            # Create tech support tickets table
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS tech_support_tickets (
                    ticket_id TEXT PRIMARY KEY,
                    participant_id TEXT NOT NULL,
                    issue_description TEXT NOT NULL,
                    status TEXT DEFAULT 'open',
                    created_at TEXT NOT NULL,
                    resolved_at TEXT,
                    FOREIGN KEY (participant_id) REFERENCES participants (participant_id)
                )
            """)
            
            self.db_conn.commit()
            logging.info("Database initialized successfully.")
        except sqlite3.Error as e:
            logging.error(f"Database initialization failed: {e}")
            raise

    def _setup_backup_system(self) -> None:
        """Set up the backup system with scheduled backups."""
        if not os.path.exists(BACKUP_DIR):
            os.makedirs(BACKUP_DIR)
        
        # Start backup scheduler in a separate thread
        backup_thread = threading.Thread(
            target=self._run_scheduled_backups,
            daemon=True
        )
        backup_thread.start()

    def _run_scheduled_backups(self) -> None:
        """Run scheduled backups based on configuration."""
        while True:
            try:
                self._create_backup()
                threading.Event().wait(self.config["backup_frequency"])
            except Exception as e:
                logging.error(f"Backup scheduler error: {e}")

    def _create_backup(self) -> None:
        """Create a backup of the database."""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_name = f"backup_{timestamp}.zip"
            backup_path = os.path.join(BACKUP_DIR, backup_name)
            
            with zipfile.ZipFile(backup_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                zipf.write(DATABASE_NAME)
            
            logging.info(f"Backup created: {backup_name}")
            
            # Clean up old backups if exceeding max_backups
            backups = sorted(os.listdir(BACKUP_DIR))
            while len(backups) > self.config["max_backups"]:
                oldest_backup = backups.pop(0)
                os.remove(os.path.join(BACKUP_DIR, oldest_backup))
                logging.info(f"Removed old backup: {oldest_backup}")
                
        except Exception as e:
            logging.error(f"Backup creation failed: {e}")

    def _start_tech_support_workers(self) -> None:
        """Start worker threads for handling tech support tickets."""
        for i in range(3):  # Start 3 worker threads
            worker = threading.Thread(
                target=self._process_tech_support_tickets,
                daemon=True
            )
            worker.start()

    def _process_tech_support_tickets(self) -> None:
        """Process tech support tickets from the queue."""
        while True:
            try:
                ticket_data = self.tech_support_queue.get()
                self._handle_tech_support_request(
                    ticket_data["participant_id"],
                    ticket_data["issue_description"]
                )
                self.tech_support_queue.task_done()
            except Exception as e:
                logging.error(f"Tech support worker error: {e}")

    def _handle_tech_support_request(self, participant_id: str, issue_description: str) -> None:
        """Handle a tech support request."""
        try:
            ticket_id = str(uuid.uuid4())
            created_at = datetime.now().isoformat()
            
            self.cursor.execute("""
                INSERT INTO tech_support_tickets 
                (ticket_id, participant_id, issue_description, created_at)
                VALUES (?, ?, ?, ?)
            """, (ticket_id, participant_id, issue_description, created_at))
            
            self.cursor.execute("""
                UPDATE participants 
                SET tech_support_requests = tech_support_requests + 1 
                WHERE participant_id = ?
            """, (participant_id,))
            
            self.db_conn.commit()
            
            # Notify participant
            self._send_support_email(participant_id, ticket_id)
            
            logging.info(f"Tech support ticket created: {ticket_id}")
        except sqlite3.Error as e:
            logging.error(f"Failed to create tech support ticket: {e}")
            self.db_conn.rollback()

    def _send_support_email(self, participant_id: str, ticket_id: str) -> None:
        """Send email notification about tech support ticket."""
        try:
            participant = self.get_participant(participant_id)
            if not participant:
                return
                
            msg = MIMEMultipart()
            msg['From'] = self.config["support_email"]
            msg['To'] = participant.email
            msg['Subject'] = "Your Tech Support Ticket"
            
            body = f"""
            Dear {participant.name},
            
            Thank you for contacting our tech support team. 
            Your ticket (ID: {ticket_id}) has been received and will be processed shortly.
            
            Best regards,
            Virtual Media Events Team
            """
            
            msg.attach(MIMEText(body, 'plain'))
            
            with smtplib.SMTP(self.config["smtp_server"], self.config["smtp_port"]) as server:
                server.starttls()
                server.login(self.config["smtp_username"], self.config["smtp_password"])
                server.send_message(msg)
                
            logging.info(f"
