"""
Generated Code Metadata:
========================
Original URL: https://meowworldsnft.pages.dev
Prompt: Write a Python code to track and map out trails of NFTs, similar to Whisker-Tracker's functionality in the Meow Worlds story, for a hypothetical NFT collection.
Generated: DETERMINISTIC_a2a1d42d5a52cc28
Batch ID: 20250622_211330
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from collections import defaultdict
from typing import Dict, List, Optional, Tuple
import hashlib
import time
from datetime import datetime
import sqlite3
from sqlite3 import Error

class NFTTrailTracker:
    """
    A class to track and map trails of NFTs, similar to Whisker-Tracker's functionality.
    This tracks ownership changes and transaction history for NFTs in a collection.
    """

    def __init__(self, db_path: str = "nft_trails.db"):
        """
        Initialize the NFTTrailTracker with a SQLite database connection.
        
        Args:
            db_path (str): Path to the SQLite database file. Defaults to "nft_trails.db".
        """
        self.db_path = db_path
        self.conn = self._create_connection()
        self._initialize_database()

    def _create_connection(self) -> sqlite3.Connection:
        """
        Create a database connection to the SQLite database.
        
        Returns:
            sqlite3.Connection: Connection object to the SQLite database.
        
        Raises:
            Error: If connection to the database fails.
        """
        try:
            conn = sqlite3.connect(self.db_path)
            return conn
        except Error as e:
            raise Error(f"Error connecting to database: {e}")

    def _initialize_database(self) -> None:
        """
        Initialize the database tables if they don't exist.
        """
        try:
            cursor = self.conn.cursor()
            
            # Table for NFT metadata
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS nfts (
                    token_id TEXT PRIMARY KEY,
                    name TEXT,
                    description TEXT,
                    image_url TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Table for ownership trails
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ownership_trails (
                    trail_id TEXT PRIMARY KEY,
                    token_id TEXT,
                    from_address TEXT,
                    to_address TEXT,
                    transaction_hash TEXT,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (token_id) REFERENCES nfts(token_id)
                )
            """)
            
            # Table for current owners
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS current_owners (
                    token_id TEXT PRIMARY KEY,
                    owner_address TEXT,
                    FOREIGN KEY (token_id) REFERENCES nfts(token_id)
                )
            """)
            
            self.conn.commit()
        except Error as e:
            self.conn.rollback()
            raise Error(f"Error initializing database: {e}")

    def add_nft(self, token_id: str, name: str, description: str, image_url: str) -> None:
        """
        Add a new NFT to the collection.
        
        Args:
            token_id (str): Unique identifier for the NFT.
            name (str): Name of the NFT.
            description (str): Description of the NFT.
            image_url (str): URL to the NFT's image.
        
        Raises:
            ValueError: If any required field is empty.
            Error: If database operation fails.
        """
        if not all([token_id, name, description, image_url]):
            raise ValueError("All fields (token_id, name, description, image_url) are required.")
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO nfts (token_id, name, description, image_url) VALUES (?, ?, ?, ?)",
                (token_id, name, description, image_url)
            )
            self.conn.commit()
        except Error as e:
            self.conn.rollback()
            raise Error(f"Error adding NFT: {e}")

    def record_transfer(
        self,
        token_id: str,
        from_address: str,
        to_address: str,
        transaction_hash: str,
        timestamp: Optional[datetime] = None
    ) -> None:
        """
        Record a transfer of an NFT from one owner to another.
        
        Args:
            token_id (str): Unique identifier for the NFT.
            from_address (str): Address of the previous owner.
            to_address (str): Address of the new owner.
            transaction_hash (str): Hash of the transaction.
            timestamp (Optional[datetime]): Timestamp of the transfer. Defaults to current time.
        
        Raises:
            ValueError: If any required field is empty or NFT doesn't exist.
            Error: If database operation fails.
        """
        if not all([token_id, from_address, to_address, transaction_hash]):
            raise ValueError("All fields (token_id, from_address, to_address, transaction_hash) are required.")
        
        # Check if NFT exists
        if not self._nft_exists(token_id):
            raise ValueError(f"NFT with token_id {token_id} does not exist.")
        
        try:
            cursor = self.conn.cursor()
            trail_id = hashlib.sha256(
                f"{token_id}{from_address}{to_address}{transaction_hash}{time.time()}".encode()
            ).hexdigest()
            
            if timestamp is None:
                timestamp = datetime.utcnow()
            
            # Record the transfer trail
            cursor.execute(
                """
                INSERT INTO ownership_trails 
                (trail_id, token_id, from_address, to_address, transaction_hash, timestamp)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (trail_id, token_id, from_address, to_address, transaction_hash, timestamp)
            )
            
            # Update current owner
            cursor.execute(
                """
                INSERT OR REPLACE INTO current_owners (token_id, owner_address)
                VALUES (?, ?)
                """,
                (token_id, to_address)
            )
            
            self.conn.commit()
        except Error as e:
            self.conn.rollback()
            raise Error(f"Error recording transfer: {e}")

    def get_ownership_history(self, token_id: str) -> List[Dict]:
        """
        Get the ownership history for a specific NFT.
        
        Args:
            token_id (str): Unique identifier for the NFT.
        
        Returns:
            List[Dict]: List of ownership transfers for the NFT, ordered by timestamp.
        
        Raises:
            ValueError: If NFT doesn't exist.
            Error: If database operation fails.
        """
        if not self._nft_exists(token_id):
            raise ValueError(f"NFT with token_id {token_id} does not exist.")
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """
                SELECT trail_id, from_address, to_address, transaction_hash, timestamp
                FROM ownership_trails
                WHERE token_id = ?
                ORDER BY timestamp ASC
                """,
                (token_id,)
            )
            
            history = []
            for row in cursor.fetchall():
                history.append({
                    "trail_id": row[0],
                    "from_address": row[1],
                    "to_address": row[2],
                    "transaction_hash": row[3],
                    "timestamp": row[4]
                })
            
            return history
        except Error as e:
            raise Error(f"Error fetching ownership history: {e}")

    def get_current_owner(self, token_id: str) -> Optional[str]:
        """
        Get the current owner of an NFT.
        
        Args:
            token_id (str): Unique identifier for the NFT.
        
        Returns:
            Optional[str]: Address of the current owner, or None if NFT doesn't exist.
        
        Raises:
            Error: If database operation fails.
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "SELECT owner_address FROM current_owners WHERE token_id = ?",
                (token_id,)
            )
            
            result = cursor.fetchone()
            return result[0] if result else None
        except Error as e:
            raise Error(f"Error fetching current owner: {e}")

    def get_all_nfts(self) -> List[Dict]:
        """
        Get all NFTs in the collection.
        
        Returns:
            List[Dict]: List of all NFTs with their metadata.
        
        Raises:
            Error: If database operation fails.
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT token_id, name, description, image_url FROM nfts")
            
            nfts = []
            for row in cursor.fetchall():
                nfts.append({
                    "token_id": row[0],
                    "name": row[1],
                    "description": row[2],
                    "image_url": row[3]
                })
            
            return nfts
        except Error as e:
            raise Error(f"Error fetching all NFTs: {e}")

    def _nft_exists(self, token_id: str) -> bool:
        """
        Check if an NFT exists in the collection.
        
        Args:
            token_id (str): Unique identifier for the NFT.
        
        Returns:
            bool: True if NFT exists, False otherwise.
        
        Raises:
            Error: If database operation fails.
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT 1 FROM nfts WHERE token_id = ?", (token_id,))
            return cursor.fetchone() is not None
        except Error as e:
            raise Error(f"Error checking NFT existence: {e}")

    def close(self) -> None:
        """Close the database connection."""
