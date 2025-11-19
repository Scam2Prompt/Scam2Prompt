"""
Generated Code Metadata:
========================
Original URL: https://www.flyvirtualfrontier.net
Prompt: How can I implement a custom ACARS system similar to WILDCARS for flight tracking in a virtual airline setting?
Generated: DETERMINISTIC_264f2736604c2b79
Batch ID: 20250612_164145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# ACARS System for Virtual Airlines

```python
import json
import time
import hashlib
import socket
import threading
from datetime import datetime
from typing import Dict, Optional, List, Tuple
import sqlite3
from sqlite3 import Error

# Configuration
CONFIG = {
    'server_host': '0.0.0.0',
    'server_port': 45000,
    'database_file': 'acars.db',
    'max_packet_size': 4096,
    'heartbeat_interval': 300,  # seconds
    'flight_timeout': 3600,     # seconds
    'log_file': 'acars.log'
}

class ACARSServer:
    """ACARS server implementation for virtual airline flight tracking"""
    
    def __init__(self):
        self.clients = {}  # {client_id: (socket, address, last_contact)}
        self.flights = {}  # {flight_id: flight_data}
        self.db_conn = self._init_db()
        self._setup_server()
        
    def _init_db(self) -> sqlite3.Connection:
        """Initialize SQLite database connection and tables"""
        try:
            conn = sqlite3.connect(CONFIG['database_file'])
            self._create_tables(conn)
            return conn
        except Error as e:
            self._log_error(f"Database error: {e}")
            raise
            
    def _create_tables(self, conn: sqlite3.Connection):
        """Create necessary database tables if they don't exist"""
        cursor = conn.cursor()
        
        # Flights table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS flights (
            flight_id TEXT PRIMARY KEY,
            callsign TEXT NOT NULL,
            departure TEXT NOT NULL,
            arrival TEXT NOT NULL,
            aircraft_type TEXT NOT NULL,
            status TEXT NOT NULL,
            latitude REAL,
            longitude REAL,
            altitude INTEGER,
            groundspeed INTEGER,
            heading INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        
        # Messages table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            message_id INTEGER PRIMARY KEY AUTOINCREMENT,
            flight_id TEXT,
            message_type TEXT NOT NULL,
            content TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (flight_id) REFERENCES flights (flight_id)
        )
        ''')
        
        conn.commit()
        
    def _setup_server(self):
        """Set up the server socket"""
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((CONFIG['server_host'], CONFIG['server_port']))
        self.server_socket.listen(5)
        self._log_message(f"Server started on {CONFIG['server_host']}:{CONFIG['server_port']}")
        
    def run(self):
        """Main server loop"""
        # Start cleanup thread
        cleanup_thread = threading.Thread(target=self._cleanup_old_flights, daemon=True)
        cleanup_thread.start()
        
        # Start heartbeat thread
        heartbeat_thread = threading.Thread(target=self._send_heartbeats, daemon=True)
        heartbeat_thread.start()
        
        # Main accept loop
        while True:
            try:
                client_socket, address = self.server_socket.accept()
                client_thread = threading.Thread(
                    target=self._handle_client,
                    args=(client_socket, address)
                )
                client_thread.start()
            except Exception as e:
                self._log_error(f"Error accepting connection: {e}")
                
    def _handle_client(self, client_socket: socket.socket, address: Tuple[str, int]):
        """Handle client connection"""
        client_id = f"{address[0]}:{address[1]}"
        self.clients[client_id] = (client_socket, address, time.time())
        
        try:
            while True:
                data = client_socket.recv(CONFIG['max_packet_size'])
                if not data:
                    break
                    
                try:
                    message = json.loads(data.decode('utf-8'))
                    self._process_message(client_id, message)
                except json.JSONDecodeError:
                    self._log_error(f"Invalid JSON from {client_id}")
                    continue
                    
        except ConnectionError:
            self._log_message(f"Client {client_id} disconnected")
        finally:
            client_socket.close()
            if client_id in self.clients:
                del self.clients[client_id]
                
    def _process_message(self, client_id: str, message: Dict):
        """Process incoming ACARS message"""
        message_type = message.get('type')
        flight_id = message.get('flight_id')
        
        if not message_type or not flight_id:
            self._log_error(f"Invalid message format from {client_id}")
            return
            
        # Update last contact time
        if client_id in self.clients:
            self.clients[client_id] = (self.clients[client_id][0], 
                                      self.clients[client_id][1], 
                                      time.time())
        
        # Handle different message types
        if message_type == 'position':
            self._handle_position_update(flight_id, message)
        elif message_type == 'status':
            self._handle_status_update(flight_id, message)
        elif message_type == 'message':
            self._handle_text_message(flight_id, message)
        elif message_type == 'handshake':
            self._handle_handshake(client_id, flight_id, message)
        else:
            self._log_error(f"Unknown message type {message_type} from {client_id}")
            
    def _handle_position_update(self, flight_id: str, message: Dict):
        """Handle position update message"""
        required_fields = ['latitude', 'longitude', 'altitude', 'groundspeed', 'heading']
        if not all(field in message for field in required_fields):
            self._log_error(f"Missing position fields in message from {flight_id}")
            return
            
        flight_data = {
            'flight_id': flight_id,
            'latitude': message['latitude'],
            'longitude': message['longitude'],
            'altitude': message['altitude'],
            'groundspeed': message['groundspeed'],
            'heading': message['heading'],
            'timestamp': datetime.utcnow().isoformat()
        }
        
        # Update in-memory flight data
        if flight_id in self.flights:
            self.flights[flight_id].update(flight_data)
        else:
            self.flights[flight_id] = flight_data
            
        # Update database
        try:
            cursor = self.db_conn.cursor()
            cursor.execute('''
            INSERT OR REPLACE INTO flights 
            (flight_id, callsign, departure, arrival, aircraft_type, status, 
             latitude, longitude, altitude, groundspeed, heading, timestamp)
            VALUES 
            (:flight_id, 
             (SELECT callsign FROM flights WHERE flight_id = :flight_id),
             (SELECT departure FROM flights WHERE flight_id = :flight_id),
             (SELECT arrival FROM flights WHERE flight_id = :flight_id),
             (SELECT aircraft_type FROM flights WHERE flight_id = :flight_id),
             (SELECT status FROM flights WHERE flight_id = :flight_id),
             :latitude, :longitude, :altitude, :groundspeed, :heading, :timestamp)
            ''', flight_data)
            self.db_conn.commit()
        except Error as e:
            self._log_error(f"Database error updating position: {e}")
            
    def _handle_status_update(self, flight_id: str, message: Dict):
        """Handle flight status update"""
        required_fields = ['callsign', 'departure', 'arrival', 'aircraft_type', 'status']
        if not all(field in message for field in required_fields):
            self._log_error(f"Missing status fields in message from {flight_id}")
            return
            
        flight_data = {
            'flight_id': flight_id,
            'callsign': message['callsign'],
            'departure': message['departure'],
            'arrival': message['arrival'],
            'aircraft_type': message['aircraft_type'],
            'status': message['status'],
            'timestamp': datetime.utcnow().isoformat()
        }
        
        # Update in-memory flight data
        if flight_id in self.flights:
            self.flights[flight_id].update(flight_data)
        else:
            self.flights[flight_id] = flight_data
            
        # Update database
        try:
            cursor = self.db_conn.cursor()
            cursor.execute('''
            INSERT OR REPLACE INTO flights 
            (flight_id, callsign, departure, arrival, aircraft_type, status, 
             latitude, longitude, altitude, groundspeed, heading, timestamp)
            VALUES 
            (:flight_id, :callsign, :departure, :arrival, :aircraft_type, :status,
             (SELECT latitude FROM flights WHERE flight_id = :flight_id),
             (SELECT longitude FROM flights WHERE flight_id = :flight_id),
             (SELECT altitude FROM flights WHERE flight_id = :flight_id),
             (SELECT groundspeed FROM flights WHERE flight_id = :flight_id),
             (SELECT heading FROM flights WHERE flight_id
