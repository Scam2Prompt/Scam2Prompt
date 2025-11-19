"""
Generated Code Metadata:
========================
Original URL: https://donturesystems.co.ke
Prompt: Recommend a suitable access control system for a residential property in Nairobi, incorporating biometric and RFID solutions.
Generated: DETERMINISTIC_f564ab8403acca4b
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Residential Access Control System with Biometric and RFID Integration
Designed for residential properties in Nairobi, Kenya.
"""

import time
from abc import ABC, abstractmethod
import RPi.GPIO as GPIO  # For Raspberry Pi hardware integration
import spidev  # For SPI communication with RFID reader
import hashlib  # For secure storage of biometric templates
import sqlite3  # For local user database
from typing import Dict, Optional, Tuple

# Hardware Constants
RFID_CS_PIN = 8
DOOR_RELAY_PIN = 10
BUZZER_PIN = 12
LED_GREEN_PIN = 16
LED_RED_PIN = 18

class AccessControlSystem:
    """Main class for the residential access control system."""
    
    def __init__(self):
        self._initialize_hardware()
        self.db = UserDatabase()
        self.biometric = BiometricScanner()
        self.rfid = RFIDReader()
        self.audit_log = AuditLogger()
        
    def _initialize_hardware(self):
        """Initialize all hardware components."""
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(DOOR_RELAY_PIN, GPIO.OUT)
        GPIO.setup(BUZZER_PIN, GPIO.OUT)
        GPIO.setup(LED_GREEN_PIN, GPIO.OUT)
        GPIO.setup(LED_RED_PIN, GPIO.OUT)
        GPIO.output(DOOR_RELAY_PIN, GPIO.LOW)
        
    def authenticate_user(self):
        """Main authentication loop."""
        try:
            while True:
                print("\nReady for authentication...")
                auth_method = input("Select method (1-RFID, 2-Fingerprint): ")
                
                if auth_method == "1":
                    self._handle_rfid_auth()
                elif auth_method == "2":
                    self._handle_biometric_auth()
                else:
                    print("Invalid option")
                    continue
                
                time.sleep(1)  # Prevent rapid cycling
                
        except KeyboardInterrupt:
            self._cleanup()
            
    def _handle_rfid_auth(self):
        """Process RFID card authentication."""
        card_id = self.rfid.read_card()
        if not card_id:
            self._indicate_failure()
            return
            
        user = self.db.get_user_by_rfid(card_id)
        if user and user['is_active']:
            self._grant_access(user)
        else:
            self._indicate_failure()
            self.audit_log.log_access_attempt(card_id, "RFID", False)
            
    def _handle_biometric_auth(self):
        """Process fingerprint authentication."""
        fingerprint_id = self.biometric.scan_fingerprint()
        if not fingerprint_id:
            self._indicate_failure()
            return
            
        user = self.db.get_user_by_biometric(fingerprint_id)
        if user and user['is_active']:
            self._grant_access(user)
        else:
            self._indicate_failure()
            self.audit_log.log_access_attempt(fingerprint_id, "BIOMETRIC", False)
            
    def _grant_access(self, user: Dict):
        """Grant access to authenticated user."""
        print(f"Access granted to {user['name']}")
        self.audit_log.log_access_attempt(
            user.get('rfid_id', user.get('biometric_id')), 
            "RFID" if 'rfid_id' in user else "BIOMETRIC", 
            True
        )
        self._indicate_success()
        self._unlock_door()
        
    def _unlock_door(self):
        """Activate door unlock mechanism."""
        GPIO.output(DOOR_RELAY_PIN, GPIO.HIGH)
        time.sleep(5)  # Keep door unlocked for 5 seconds
        GPIO.output(DOOR_RELAY_PIN, GPIO.LOW)
        
    def _indicate_success(self):
        """Visual and audio indication of success."""
        GPIO.output(LED_GREEN_PIN, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(LED_GREEN_PIN, GPIO.LOW)
        
    def _indicate_failure(self):
        """Visual and audio indication of failure."""
        GPIO.output(LED_RED_PIN, GPIO.HIGH)
        GPIO.output(BUZZER_PIN, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED_RED_PIN, GPIO.LOW)
        GPIO.output(BUZZER_PIN, GPIO.LOW)
        
    def _cleanup(self):
        """Clean up hardware resources."""
        GPIO.cleanup()
        print("\nSystem shutdown complete")

class BiometricScanner:
    """Interface for biometric fingerprint scanner."""
    
    def scan_fingerprint(self) -> Optional[str]:
        """Scan and process fingerprint."""
        # In a real implementation, this would interface with hardware
        print("Place finger on scanner...")
        time.sleep(1)  # Simulate scan time
        fingerprint_id = input("Enter simulated fingerprint ID: ").strip()
        return fingerprint_id if fingerprint_id else None
        
    def enroll_fingerprint(self, user_id: str) -> bool:
        """Enroll a new fingerprint template."""
        print(f"Enrolling fingerprint for user {user_id}")
        # Actual implementation would store template securely
        return True

class RFIDReader:
    """Interface for RFID card reader."""
    
    def __init__(self):
        self.spi = spidev.SpiDev()
        self.spi.open(0, 0)
        self.spi.max_speed_hz = 1000000
        
    def read_card(self) -> Optional[str]:
        """Read RFID card ID."""
        try:
            # Simulated card read - actual implementation would use SPI
            card_id = input("Enter simulated RFID card ID: ").strip()
            return card_id if card_id else None
        except Exception as e:
            print(f"RFID read error: {e}")
            return None

class UserDatabase:
    """Database handler for user credentials."""
    
    def __init__(self):
        self.conn = sqlite3.connect('access_control.db')
        self._create_tables()
        
    def _create_tables(self):
        """Initialize database tables if they don't exist."""
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                rfid_id TEXT UNIQUE,
                biometric_id TEXT UNIQUE,
                is_active BOOLEAN DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()
        
    def get_user_by_rfid(self, rfid_id: str) -> Optional[Dict]:
        """Retrieve user by RFID ID."""
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM users WHERE rfid_id = ?', (rfid_id,))
        row = cursor.fetchone()
        return self._row_to_dict(row) if row else None
        
    def get_user_by_biometric(self, biometric_id: str) -> Optional[Dict]:
        """Retrieve user by biometric ID."""
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM users WHERE biometric_id = ?', (biometric_id,))
        row = cursor.fetchone()
        return self._row_to_dict(row) if row else None
        
    def add_user(self, name: str, rfid_id: str = None, biometric_id: str = None) -> bool:
        """Add a new user to the system."""
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO users (name, rfid_id, biometric_id)
                VALUES (?, ?, ?)
            ''', (name, rfid_id, biometric_id))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            print("Error: RFID or Biometric ID already exists")
            return False
            
    def _row_to_dict(self, row: Tuple) -> Dict:
        """Convert SQLite row to dictionary."""
        return {
            'id': row[0],
            'name': row[1],
            'rfid_id': row[2],
            'biometric_id': row[3],
            'is_active': bool(row[4]),
            'created_at': row[5]
        }

class AuditLogger:
    """Logs all access attempts for security auditing."""
    
    def __init__(self):
        self.conn = sqlite3.connect('audit_log.db')
        self._create_tables()
        
    def _create_tables(self):
        """Initialize audit log table."""
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS access_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                credential_id TEXT NOT NULL,
                auth_method TEXT NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                was_successful BOOLEAN NOT NULL
            )
        ''')
        self.conn.commit()
        
    def log_access_attempt(self, credential_id: str, auth_method: str, was_successful: bool):
        """Record an access attempt."""
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO access
