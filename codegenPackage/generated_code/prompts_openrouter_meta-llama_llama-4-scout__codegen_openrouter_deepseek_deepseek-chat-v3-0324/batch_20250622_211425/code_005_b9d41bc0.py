"""
Generated Code Metadata:
========================
Original URL: https://grooveup.pages.dev
Prompt: Create a DAO for a music platform that enables artists to grow an active fanbase and raise seed funds while rewarding fans for actively streaming and sharing their music.
Generated: DETERMINISTIC_b9d41bc0e1caefd7
Batch ID: 20250622_211425
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from typing import List, Optional
from datetime import datetime
import sqlite3
from sqlite3 import Error

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class MusicPlatformDAO:
    """Data Access Object for the music platform."""
    
    def __init__(self, db_path: str = "music_platform.db"):
        """Initialize the DAO with a database connection.
        
        Args:
            db_path: Path to the SQLite database file.
        """
        self.db_path = db_path
        self._create_tables()
    
    def _get_connection(self) -> sqlite3.Connection:
        """Create and return a database connection.
        
        Returns:
            sqlite3.Connection: Database connection object.
            
        Raises:
            Error: If connection to database fails.
        """
        try:
            conn = sqlite3.connect(self.db_path)
            conn.row_factory = sqlite3.Row
            return conn
        except Error as e:
            logger.error(f"Error connecting to database: {e}")
            raise
    
    def _create_tables(self) -> None:
        """Create necessary tables if they don't exist."""
        sql_artists = """
        CREATE TABLE IF NOT EXISTS artists (
            artist_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            bio TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        
        sql_fans = """
        CREATE TABLE IF NOT EXISTS fans (
            fan_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        
        sql_tracks = """
        CREATE TABLE IF NOT EXISTS tracks (
            track_id INTEGER PRIMARY KEY AUTOINCREMENT,
            artist_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            duration INTEGER NOT NULL,
            release_date TIMESTAMP,
            FOREIGN KEY (artist_id) REFERENCES artists (artist_id)
        );
        """
        
        sql_streams = """
        CREATE TABLE IF NOT EXISTS streams (
            stream_id INTEGER PRIMARY KEY AUTOINCREMENT,
            track_id INTEGER NOT NULL,
            fan_id INTEGER NOT NULL,
            streamed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            shares INTEGER DEFAULT 0,
            FOREIGN KEY (track_id) REFERENCES tracks (track_id),
            FOREIGN KEY (fan_id) REFERENCES fans (fan_id)
        );
        """
        
        sql_funding = """
        CREATE TABLE IF NOT EXISTS funding (
            funding_id INTEGER PRIMARY KEY AUTOINCREMENT,
            artist_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            fan_id INTEGER NOT NULL,
            funded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (artist_id) REFERENCES artists (artist_id),
            FOREIGN KEY (fan_id) REFERENCES fans (fan_id)
        );
        """
        
        try:
            conn = self._get_connection()
            cursor = conn.cursor()
            cursor.execute(sql_artists)
            cursor.execute(sql_fans)
            cursor.execute(sql_tracks)
            cursor.execute(sql_streams)
            cursor.execute(sql_funding)
            conn.commit()
        except Error as e:
            logger.error(f"Error creating tables: {e}")
            raise
        finally:
            if conn:
                conn.close()
    
    def add_artist(self, name: str, email: str, bio: Optional[str] = None) -> int:
        """Add a new artist to the platform.
        
        Args:
            name: Artist name.
            email: Artist email (must be unique).
            bio: Optional artist biography.
            
        Returns:
            int: ID of the newly created artist.
            
        Raises:
            ValueError: If email already exists.
            Error: If database operation fails.
        """
        try:
            conn = self._get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO artists (name, email, bio) VALUES (?, ?, ?)",
                (name, email, bio)
            )
            conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            logger.error(f"Artist with email {email} already exists")
            raise ValueError(f"Artist with email {email} already exists")
        except Error as e:
            logger.error(f"Error adding artist: {e}")
            raise
        finally:
            if conn:
                conn.close()
    
    def add_fan(self, name: str, email: str) -> int:
        """Add a new fan to the platform.
        
        Args:
            name: Fan name.
            email: Fan email (must be unique).
            
        Returns:
            int: ID of the newly created fan.
            
        Raises:
            ValueError: If email already exists.
            Error: If database operation fails.
        """
        try:
            conn = self._get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO fans (name, email) VALUES (?, ?)",
                (name, email)
            )
            conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            logger.error(f"Fan with email {email} already exists")
            raise ValueError(f"Fan with email {email} already exists")
        except Error as e:
            logger.error(f"Error adding fan: {e}")
            raise
        finally:
            if conn:
                conn.close()
    
    def add_track(self, artist_id: int, title: str, duration: int, 
                 release_date: Optional[datetime] = None) -> int:
        """Add a new track to the platform.
        
        Args:
            artist_id: ID of the artist who created the track.
            title: Track title.
            duration: Track duration in seconds.
            release_date: Optional release date of the track.
            
        Returns:
            int: ID of the newly created track.
            
        Raises:
            ValueError: If artist doesn't exist.
            Error: If database operation fails.
        """
        try:
            conn = self._get_connection()
            cursor = conn.cursor()
            
            # Check if artist exists
            cursor.execute("SELECT 1 FROM artists WHERE artist_id = ?", (artist_id,))
            if not cursor.fetchone():
                raise ValueError(f"Artist with ID {artist_id} does not exist")
            
            cursor.execute(
                "INSERT INTO tracks (artist_id, title, duration, release_date) VALUES (?, ?, ?, ?)",
                (artist_id, title, duration, release_date)
            )
            conn.commit()
            return cursor.lastrowid
        except Error as e:
            logger.error(f"Error adding track: {e}")
            raise
        finally:
            if conn:
                conn.close()
    
    def record_stream(self, track_id: int, fan_id: int, shares: int = 0) -> int:
        """Record a stream event for a track by a fan.
        
        Args:
            track_id: ID of the track being streamed.
            fan_id: ID of the fan streaming the track.
            shares: Number of times the fan shared the track.
            
        Returns:
            int: ID of the newly created stream record.
            
        Raises:
            ValueError: If track or fan doesn't exist.
            Error: If database operation fails.
        """
        try:
            conn = self._get_connection()
            cursor = conn.cursor()
            
            # Check if track exists
            cursor.execute("SELECT 1 FROM tracks WHERE track_id = ?", (track_id,))
            if not cursor.fetchone():
                raise ValueError(f"Track with ID {track_id} does not exist")
                
            # Check if fan exists
            cursor.execute("SELECT 1 FROM fans WHERE fan_id = ?", (fan_id,))
            if not cursor.fetchone():
                raise ValueError(f"Fan with ID {fan_id} does not exist")
            
            cursor.execute(
                "INSERT INTO streams (track_id, fan_id, shares) VALUES (?, ?, ?)",
                (track_id, fan_id, shares)
            )
            conn.commit()
            return cursor.lastrowid
        except Error as e:
            logger.error(f"Error recording stream: {e}")
            raise
        finally:
            if conn:
                conn.close()
    
    def record_funding(self, artist_id: int, fan_id: int, amount: float) -> int:
        """Record a funding event from a fan to an artist.
        
        Args:
            artist_id: ID of the artist receiving funding.
            fan_id: ID of the fan providing funding.
            amount: Amount funded.
            
        Returns:
            int: ID of the newly created funding record.
            
        Raises:
            ValueError: If artist or fan doesn't exist.
            Error: If database operation fails.
        """
        try:
            conn = self._get_connection()
            cursor = conn.cursor()
            
            # Check if artist exists
            cursor.execute("SELECT 1 FROM artists WHERE artist_id = ?", (artist_id,))
            if not cursor.fetchone():
                raise ValueError(f"Artist with ID {artist_id} does not exist")
                
            # Check if fan exists
            cursor.execute("SELECT 1 FROM fans WHERE fan_id = ?", (fan_id,))
            if not cursor.fetchone():
                raise ValueError(f"Fan
