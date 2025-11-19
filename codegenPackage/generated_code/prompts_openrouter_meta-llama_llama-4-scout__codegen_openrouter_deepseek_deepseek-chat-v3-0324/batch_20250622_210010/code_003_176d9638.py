"""
Generated Code Metadata:
========================
Original URL: https://phantomrewards.com
Prompt: Design a system to manage and track entries into major and minor draws, including automatic entry for members and the option to purchase additional packages for more free entries.
Generated: DETERMINISTIC_176d963865e0575e
Batch ID: 20250622_210010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from datetime import datetime
from typing import List, Dict, Optional, Tuple
import random
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DrawSystem:
    def __init__(self, db_path: str = 'draw_system.db'):
        """Initialize the draw system with database connection."""
        self.db_path = db_path
        self._initialize_db()

    def _initialize_db(self) -> None:
        """Create database tables if they don't exist."""
        with self._get_db_connection() as conn:
            cursor = conn.cursor()
            
            # Members table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS members (
                    member_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    join_date TEXT NOT NULL,
                    is_active INTEGER DEFAULT 1
                )
            ''')
            
            # Draws table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS draws (
                    draw_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    draw_type TEXT CHECK(draw_type IN ('major', 'minor')) NOT NULL,
                    entry_cost REAL NOT NULL,
                    prize_description TEXT NOT NULL,
                    start_date TEXT NOT NULL,
                    end_date TEXT NOT NULL,
                    is_active INTEGER DEFAULT 1
                )
            ''')
            
            # Entries table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS entries (
                    entry_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    member_id INTEGER NOT NULL,
                    draw_id INTEGER NOT NULL,
                    entry_date TEXT NOT NULL,
                    is_free INTEGER DEFAULT 0,
                    FOREIGN KEY (member_id) REFERENCES members (member_id),
                    FOREIGN KEY (draw_id) REFERENCES draws (draw_id)
                )
            ''')
            
            # Packages table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS packages (
                    package_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    price REAL NOT NULL,
                    free_entries INTEGER NOT NULL,
                    description TEXT,
                    is_active INTEGER DEFAULT 1
                )
            ''')
            
            # Member packages table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS member_packages (
                    member_package_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    member_id INTEGER NOT NULL,
                    package_id INTEGER NOT NULL,
                    purchase_date TEXT NOT NULL,
                    entries_remaining INTEGER NOT NULL,
                    FOREIGN KEY (member_id) REFERENCES members (member_id),
                    FOREIGN KEY (package_id) REFERENCES packages (package_id)
                )
            ''')
            
            conn.commit()

    def _get_db_connection(self) -> sqlite3.Connection:
        """Get a database connection with row factory."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def add_member(self, name: str, email: str) -> int:
        """Add a new member to the system."""
        try:
            with self._get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO members (name, email, join_date)
                    VALUES (?, ?, ?)
                ''', (name, email, datetime.now().isoformat()))
                conn.commit()
                return cursor.lastrowid
        except sqlite3.IntegrityError as e:
            logger.error(f"Error adding member: {e}")
            raise ValueError("Email already exists in the system")
        except Exception as e:
            logger.error(f"Unexpected error adding member: {e}")
            raise

    def add_draw(
        self,
        name: str,
        draw_type: str,
        entry_cost: float,
        prize_description: str,
        start_date: str,
        end_date: str
    ) -> int:
        """Add a new draw to the system."""
        try:
            if draw_type not in ('major', 'minor'):
                raise ValueError("Draw type must be 'major' or 'minor'")
                
            with self._get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO draws (
                        name, draw_type, entry_cost, prize_description, start_date, end_date
                    )
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (name, draw_type, entry_cost, prize_description, start_date, end_date))
                conn.commit()
                return cursor.lastrowid
        except Exception as e:
            logger.error(f"Error adding draw: {e}")
            raise

    def add_package(
        self,
        name: str,
        price: float,
        free_entries: int,
        description: Optional[str] = None
    ) -> int:
        """Add a new package to the system."""
        try:
            with self._get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO packages (name, price, free_entries, description)
                    VALUES (?, ?, ?, ?)
                ''', (name, price, free_entries, description))
                conn.commit()
                return cursor.lastrowid
        except Exception as e:
            logger.error(f"Error adding package: {e}")
            raise

    def purchase_package(self, member_id: int, package_id: int) -> int:
        """Purchase a package for a member."""
        try:
            with self._get_db_connection() as conn:
                cursor = conn.cursor()
                
                # Get package details
                cursor.execute('SELECT * FROM packages WHERE package_id = ?', (package_id,))
                package = cursor.fetchone()
                if not package:
                    raise ValueError("Package not found")
                
                # Add to member packages
                cursor.execute('''
                    INSERT INTO member_packages (
                        member_id, package_id, purchase_date, entries_remaining
                    )
                    VALUES (?, ?, ?, ?)
                ''', (
                    member_id,
                    package_id,
                    datetime.now().isoformat(),
                    package['free_entries']
                ))
                conn.commit()
                return cursor.lastrowid
        except Exception as e:
            logger.error(f"Error purchasing package: {e}")
            raise

    def get_member_free_entries(self, member_id: int) -> List[Dict]:
        """Get all free entries available for a member."""
        try:
            with self._get_db_connection() as conn:
                cursor = conn.cursor()
                
                # Get active draws
                cursor.execute('''
                    SELECT * FROM draws 
                    WHERE is_active = 1 
                    AND date() BETWEEN start_date AND end_date
                ''')
                active_draws = cursor.fetchall()
                
                # Get member packages with remaining entries
                cursor.execute('''
                    SELECT mp.*, p.name as package_name 
                    FROM member_packages mp
                    JOIN packages p ON mp.package_id = p.package_id
                    WHERE mp.member_id = ? AND mp.entries_remaining > 0
                ''', (member_id,))
                packages = cursor.fetchall()
                
                result = []
                for draw in active_draws:
                    for package in packages:
                        result.append({
                            'draw_id': draw['draw_id'],
                            'draw_name': draw['name'],
                            'draw_type': draw['draw_type'],
                            'package_id': package['package_id'],
                            'package_name': package['package_name'],
                            'entries_available': package['entries_remaining']
                        })
                
                return result
        except Exception as e:
            logger.error(f"Error getting member free entries: {e}")
            raise

    def enter_draw(
        self,
        member_id: int,
        draw_id: int,
        use_free_entry: bool = False,
        package_id: Optional[int] = None
    ) -> int:
        """Enter a member into a draw."""
        try:
            with self._get_db_connection() as conn:
                cursor = conn.cursor()
                
                # Check if draw is active
                cursor.execute('''
                    SELECT * FROM draws 
                    WHERE draw_id = ? 
                    AND is_active = 1 
                    AND date() BETWEEN start_date AND end_date
                ''', (draw_id,))
                draw = cursor.fetchone()
                if not draw:
                    raise ValueError("Draw is not active or doesn't exist")
                
                # Check if member exists
                cursor.execute('SELECT * FROM members WHERE member_id = ?', (member_id,))
                member = cursor.fetchone()
                if not member:
                    raise ValueError("Member not found")
                
                if use_free_entry:
                    if not package_id:
                        raise ValueError("Package ID is required for free entries")
                    
                    # Check package validity
                    cursor.execute('''
                        SELECT * FROM member_packages
                        WHERE member_id = ? AND package_id = ? AND entries_remaining > 0
                    ''', (member_id, package_id))
                    package = cursor.fetchone()
                    if not package:
                        raise ValueError("No available free entries in this package")
                    
                    # Decrement package entries
                    cursor.execute('''
                        UPDATE member_packages
                        SET entries_remaining = entries_remaining - 1
                        WHERE member_package_id = ?
                    ''', (package['member_p
