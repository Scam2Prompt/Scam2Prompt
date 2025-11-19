"""
Generated Code Metadata:
========================
Original URL: https://lzero.us
Prompt: Generate code to implement a raffle system for events like the Pickleball Speed Dating described on the L-Zero website, where participants can register and winners are randomly selected.
Generated: DETERMINISTIC_b2eadd3b07ff1f34
Batch ID: 20250612_145626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import string
from datetime import datetime
from typing import List, Dict, Optional
import sqlite3
from sqlite3 import Error
import uuid
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('raffle_system.log'),
        logging.StreamHandler()
    ]
)

class RaffleSystem:
    """A raffle system for event management with participant registration and winner selection."""
    
    def __init__(self, db_path: str = 'raffle.db'):
        """Initialize the raffle system with a database connection.
        
        Args:
            db_path: Path to the SQLite database file.
        """
        self.db_path = db_path
        self.conn = None
        self._initialize_db()
    
    def _initialize_db(self) -> None:
        """Initialize the database with required tables if they don't exist."""
        try:
            self.conn = sqlite3.connect(self.db_path)
            cursor = self.conn.cursor()
            
            # Create events table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS events (
                    event_id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    description TEXT,
                    start_time TEXT,
                    end_time TEXT,
                    max_participants INTEGER,
                    is_active BOOLEAN DEFAULT 1
                )
            ''')
            
            # Create participants table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS participants (
                    participant_id TEXT PRIMARY KEY,
                    event_id TEXT NOT NULL,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    phone TEXT,
                    registration_time TEXT DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (event_id) REFERENCES events (event_id)
                )
            ''')
            
            # Create winners table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS winners (
                    winner_id TEXT PRIMARY KEY,
                    event_id TEXT NOT NULL,
                    participant_id TEXT NOT NULL,
                    prize TEXT,
                    draw_time TEXT DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (event_id) REFERENCES events (event_id),
                    FOREIGN KEY (participant_id) REFERENCES participants (participant_id)
                )
            ''')
            
            self.conn.commit()
            logging.info("Database initialized successfully")
            
        except Error as e:
            logging.error(f"Error initializing database: {e}")
            raise
    
    def _generate_id(self) -> str:
        """Generate a unique ID for database records."""
        return str(uuid.uuid4())
    
    def create_event(
        self,
        name: str,
        description: str = "",
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        max_participants: Optional[int] = None
    ) -> str:
        """Create a new raffle event.
        
        Args:
            name: Name of the event.
            description: Description of the event.
            start_time: Event start time (ISO format string).
            end_time: Event end time (ISO format string).
            max_participants: Maximum number of participants allowed.
            
        Returns:
            The created event ID.
        """
        event_id = self._generate_id()
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO events (
                    event_id, name, description, start_time, end_time, max_participants
                ) VALUES (?, ?, ?, ?, ?, ?)
            ''', (event_id, name, description, start_time, end_time, max_participants))
            self.conn.commit()
            logging.info(f"Created event {event_id}: {name}")
            return event_id
        except Error as e:
            logging.error(f"Error creating event: {e}")
            raise
    
    def register_participant(
        self,
        event_id: str,
        name: str,
        email: str,
        phone: Optional[str] = None
    ) -> str:
        """Register a participant for an event.
        
        Args:
            event_id: ID of the event to register for.
            name: Participant's name.
            email: Participant's email.
            phone: Participant's phone number (optional).
            
        Returns:
            The participant ID.
            
        Raises:
            ValueError: If event is not found or registration limit reached.
        """
        try:
            # Check if event exists and is active
            cursor = self.conn.cursor()
            cursor.execute('''
                SELECT is_active, max_participants FROM events WHERE event_id = ?
            ''', (event_id,))
            event_data = cursor.fetchone()
            
            if not event_data:
                raise ValueError("Event not found")
            
            is_active, max_participants = event_data
            
            if not is_active:
                raise ValueError("Event is not active for registration")
            
            # Check participant limit
            if max_participants is not None:
                cursor.execute('''
                    SELECT COUNT(*) FROM participants WHERE event_id = ?
                ''', (event_id,))
                current_count = cursor.fetchone()[0]
                if current_count >= max_participants:
                    raise ValueError("Event has reached maximum participant limit")
            
            # Register participant
            participant_id = self._generate_id()
            cursor.execute('''
                INSERT INTO participants (
                    participant_id, event_id, name, email, phone
                ) VALUES (?, ?, ?, ?, ?)
            ''', (participant_id, event_id, name, email, phone))
            self.conn.commit()
            logging.info(f"Registered participant {participant_id} for event {event_id}")
            return participant_id
            
        except Error as e:
            logging.error(f"Error registering participant: {e}")
            raise
    
    def draw_winners(
        self,
        event_id: str,
        num_winners: int = 1,
        prize: Optional[str] = None
    ) -> List[Dict[str, str]]:
        """Randomly select winners from event participants.
        
        Args:
            event_id: ID of the event to draw winners from.
            num_winners: Number of winners to select.
            prize: Optional prize description for the winners.
            
        Returns:
            List of winner dictionaries with participant details.
            
        Raises:
            ValueError: If event not found or not enough participants.
        """
        try:
            cursor = self.conn.cursor()
            
            # Verify event exists
            cursor.execute('SELECT name FROM events WHERE event_id = ?', (event_id,))
            event_name = cursor.fetchone()
            if not event_name:
                raise ValueError("Event not found")
            
            # Get all participants for the event
            cursor.execute('''
                SELECT participant_id, name, email, phone 
                FROM participants 
                WHERE event_id = ?
            ''', (event_id,))
            participants = cursor.fetchall()
            
            if not participants:
                raise ValueError("No participants registered for this event")
            
            if len(participants) < num_winners:
                raise ValueError(f"Not enough participants (have {len(participants)}, need {num_winners})")
            
            # Select random winners
            winners = random.sample(participants, num_winners)
            winner_details = []
            
            for winner in winners:
                participant_id, name, email, phone = winner
                winner_id = self._generate_id()
                
                # Record winner in database
                cursor.execute('''
                    INSERT INTO winners (
                        winner_id, event_id, participant_id, prize
                    ) VALUES (?, ?, ?, ?)
                ''', (winner_id, event_id, participant_id, prize))
                
                winner_details.append({
                    'winner_id': winner_id,
                    'participant_id': participant_id,
                    'name': name,
                    'email': email,
                    'phone': phone,
                    'prize': prize
                })
            
            self.conn.commit()
            logging.info(f"Drew {num_winners} winners for event {event_id}")
            return winner_details
            
        except Error as e:
            logging.error(f"Error drawing winners: {e}")
            raise
    
    def get_event_participants(self, event_id: str) -> List[Dict[str, str]]:
        """Get all participants for an event.
        
        Args:
            event_id: ID of the event.
            
        Returns:
            List of participant dictionaries.
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                SELECT participant_id, name, email, phone, registration_time
                FROM participants
                WHERE event_id = ?
                ORDER BY registration_time
            ''', (event_id,))
            
            participants = []
            for row in cursor.fetchall():
                participants.append({
                    'participant_id': row[0],
                    'name': row[1],
                    'email': row[2],
                    'phone': row[3],
                    'registration_time': row[4]
                })
            
            return participants
            
        except Error as e:
            logging.error(f"Error getting participants: {e}")
            raise
    
    def get_event_winners(self, event_id: str) -> List[Dict[str, str]]:
        """Get all winners for an event.
        
        Args:
            event_id: ID of the event.
            
        Returns:
            List of winner dictionaries.
        """
        try:
            cursor = self.conn.c
