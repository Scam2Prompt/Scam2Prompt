"""
Generated Code Metadata:
========================
Original URL: https://insidesafety.com.mx
Prompt: Write a program to manage GPS tracking for security purposes, inspired by the GPS solutions offered by Inside Safety.
Generated: DETERMINISTIC_b2c3b567a180a9b0
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import time
from datetime import datetime
import uuid
import sqlite3
from typing import List, Dict, Optional, Tuple
import logging
from logging.handlers import RotatingFileHandler
import socket
import threading
import queue

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        RotatingFileHandler('gps_tracker.log', maxBytes=5*1024*1024, backupCount=3),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class DatabaseManager:
    """Handles all database operations for the GPS tracking system."""
    
    def __init__(self, db_path: str = 'gps_tracking.db'):
        """Initialize the database connection and create tables if they don't exist."""
        self.db_path = db_path
        self._create_tables()
    
    def _create_tables(self) -> None:
        """Create necessary tables in the database."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Devices table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS devices (
                    device_id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    description TEXT,
                    is_active INTEGER DEFAULT 1,
                    created_at TEXT NOT NULL,
                    last_seen TEXT
                )
            ''')
            
            # Locations table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS locations (
                    location_id TEXT PRIMARY KEY,
                    device_id TEXT NOT NULL,
                    latitude REAL NOT NULL,
                    longitude REAL NOT NULL,
                    altitude REAL,
                    speed REAL,
                    accuracy REAL,
                    timestamp TEXT NOT NULL,
                    FOREIGN KEY (device_id) REFERENCES devices (device_id)
                )
            ''')
            
            # Alerts table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS alerts (
                    alert_id TEXT PRIMARY KEY,
                    device_id TEXT NOT NULL,
                    alert_type TEXT NOT NULL,
                    message TEXT NOT NULL,
                    latitude REAL,
                    longitude REAL,
                    timestamp TEXT NOT NULL,
                    is_resolved INTEGER DEFAULT 0,
                    FOREIGN KEY (device_id) REFERENCES devices (device_id)
                )
            ''')
            
            conn.commit()
    
    def add_device(self, name: str, description: str = None) -> str:
        """Add a new tracking device to the database."""
        device_id = str(uuid.uuid4())
        created_at = datetime.utcnow().isoformat()
        
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''
                INSERT INTO devices (device_id, name, description, created_at)
                VALUES (?, ?, ?, ?)
                ''',
                (device_id, name, description, created_at)
            )
            conn.commit()
        
        logger.info(f"Added new device: {device_id}")
        return device_id
    
    def update_device_location(
        self,
        device_id: str,
        latitude: float,
        longitude: float,
        altitude: float = None,
        speed: float = None,
        accuracy: float = None
    ) -> bool:
        """Update the location of a device in the database."""
        location_id = str(uuid.uuid4())
        timestamp = datetime.utcnow().isoformat()
        
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Insert new location
                cursor.execute(
                    '''
                    INSERT INTO locations (
                        location_id, device_id, latitude, longitude, altitude,
                        speed, accuracy, timestamp
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    ''',
                    (location_id, device_id, latitude, longitude, altitude, speed, accuracy, timestamp)
                )
                
                # Update device's last seen time
                cursor.execute(
                    '''
                    UPDATE devices
                    SET last_seen = ?
                    WHERE device_id = ?
                    ''',
                    (timestamp, device_id)
                )
                
                conn.commit()
            
            logger.debug(f"Updated location for device: {device_id}")
            return True
        except sqlite3.Error as e:
            logger.error(f"Failed to update device location: {e}")
            return False
    
    def get_device_locations(
        self,
        device_id: str = None,
        limit: int = 100
    ) -> List[Dict]:
        """Retrieve location history for a device or all devices."""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            if device_id:
                cursor.execute(
                    '''
                    SELECT * FROM locations
                    WHERE device_id = ?
                    ORDER BY timestamp DESC
                    LIMIT ?
                    ''',
                    (device_id, limit)
                )
            else:
                cursor.execute(
                    '''
                    SELECT * FROM locations
                    ORDER BY timestamp DESC
                    LIMIT ?
                    ''',
                    (limit,)
                )
            
            locations = [dict(row) for row in cursor.fetchall()]
        
        return locations
    
    def create_alert(
        self,
        device_id: str,
        alert_type: str,
        message: str,
        latitude: float = None,
        longitude: float = None
    ) -> str:
        """Create a new alert in the database."""
        alert_id = str(uuid.uuid4())
        timestamp = datetime.utcnow().isoformat()
        
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''
                INSERT INTO alerts (
                    alert_id, device_id, alert_type, message,
                    latitude, longitude, timestamp
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ''',
                (alert_id, device_id, alert_type, message, latitude, longitude, timestamp)
            )
            conn.commit()
        
        logger.info(f"Created alert {alert_id} for device {device_id}")
        return alert_id
    
    def get_active_alerts(self) -> List[Dict]:
        """Retrieve all unresolved alerts."""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(
                '''
                SELECT * FROM alerts
                WHERE is_resolved = 0
                ORDER BY timestamp DESC
                '''
            )
            alerts = [dict(row) for row in cursor.fetchall()]
        
        return alerts
    
    def resolve_alert(self, alert_id: str) -> bool:
        """Mark an alert as resolved."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''
                UPDATE alerts
                SET is_resolved = 1
                WHERE alert_id = ?
                ''',
                (alert_id,)
            )
            conn.commit()
        
        logger.info(f"Resolved alert: {alert_id}")
        return True

class GPSTracker:
    """Main GPS tracking system class."""
    
    def __init__(self):
        self.db = DatabaseManager()
        self.message_queue = queue.Queue()
        self.running = False
    
    def start(self) -> None:
        """Start the GPS tracking system."""
        self.running = True
        logger.info("Starting GPS tracking system")
        
        # Start processing thread
        processing_thread = threading.Thread(target=self._process_messages)
        processing_thread.daemon = True
        processing_thread.start()
        
        # Start TCP server
        server_thread = threading.Thread(target=self._start_server)
        server_thread.daemon = True
        server_thread.start()
    
    def stop(self) -> None:
        """Stop the GPS tracking system."""
        self.running = False
        logger.info("Stopping GPS tracking system")
    
    def _start_server(self) -> None:
        """Start TCP server to receive GPS data from devices."""
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(('0.0.0.0', 5000))
        server_socket.listen(5)
        logger.info("GPS server listening on port 5000")
        
        while self.running:
            try:
                client_socket, addr = server_socket.accept()
                logger.info(f"Connection from {addr}")
                
                client_thread = threading.Thread(
                    target=self._handle_client,
                    args=(client_socket,)
                )
                client_thread.daemon = True
                client_thread.start()
            except Exception as e:
                logger.error(f"Server error: {e}")
        
        server_socket.close()
    
    def _handle_client(self, client_socket: socket.socket) -> None:
        """Handle incoming client connection."""
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if data:
                try:
                    message = json.loads(data)
                    self.message_queue.put(message)
                    client_socket.sendall(b"ACK")
                except json.JSONDecodeError:
                    logger.error("Invalid JSON received")
                    client_socket.sendall(b"ERROR: Invalid JSON")
        except Exception as e:
            logger.error(f"
