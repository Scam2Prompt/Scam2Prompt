"""
Generated Code Metadata:
========================
Original URL: https://waltztechsec.com
Prompt: Design a system for romance scam recovery, including data analysis and asset tracking, using techniques described by WaltzTech Security's romance scam recovery services.
Generated: DETERMINISTIC_ed5ed323cc63494f
Batch ID: 20250622_210108
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import hashlib
import datetime
from typing import List, Dict, Optional
from enum import Enum
import re
import logging
from dataclasses import dataclass, field
import sqlite3
from sqlite3 import Error

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ScamType(Enum):
    ROMANCE = "Romance"
    INVESTMENT = "Investment"
    PHISHING = "Phishing"
    OTHER = "Other"

@dataclass
class Victim:
    id: str
    name: str
    email: str
    phone: str
    registration_date: datetime.datetime
    last_contact: datetime.datetime
    scam_type: ScamType
    reported_loss: float
    notes: str = ""

@dataclass
class ScammerProfile:
    id: str
    aliases: List[str]
    known_platforms: List[str]
    contact_methods: List[str]
    last_active: datetime.datetime
    estimated_funds: float = 0.0
    associated_accounts: List[str] = field(default_factory=list)

@dataclass
class Transaction:
    id: str
    victim_id: str
    scammer_id: str
    amount: float
    currency: str
    transaction_date: datetime.datetime
    method: str
    transaction_reference: str
    is_recovered: bool = False
    recovery_date: Optional[datetime.datetime] = None

class ScamRecoverySystem:
    def __init__(self, db_path: str = "scam_recovery.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self) -> None:
        """Initialize database tables if they don't exist"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Create victims table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS victims (
                    id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    registration_date TEXT NOT NULL,
                    last_contact TEXT NOT NULL,
                    scam_type TEXT NOT NULL,
                    reported_loss REAL NOT NULL,
                    notes TEXT
                )
            ''')
            
            # Create scammers table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS scammers (
                    id TEXT PRIMARY KEY,
                    aliases TEXT NOT NULL,
                    known_platforms TEXT NOT NULL,
                    contact_methods TEXT NOT NULL,
                    last_active TEXT NOT NULL,
                    estimated_funds REAL,
                    associated_accounts TEXT
                )
            ''')
            
            # Create transactions table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS transactions (
                    id TEXT PRIMARY KEY,
                    victim_id TEXT NOT NULL,
                    scammer_id TEXT NOT NULL,
                    amount REAL NOT NULL,
                    currency TEXT NOT NULL,
                    transaction_date TEXT NOT NULL,
                    method TEXT NOT NULL,
                    transaction_reference TEXT NOT NULL,
                    is_recovered INTEGER DEFAULT 0,
                    recovery_date TEXT,
                    FOREIGN KEY(victim_id) REFERENCES victims(id),
                    FOREIGN KEY(scammer_id) REFERENCES scammers(id)
                )
            ''')
            
            conn.commit()
            conn.close()
        except Error as e:
            logger.error(f"Error initializing database: {e}")
            raise

    def _generate_id(self, input_str: str) -> str:
        """Generate a unique ID using SHA-256 hash"""
        return hashlib.sha256(input_str.encode()).hexdigest()[:32]

    def add_victim(self, victim: Victim) -> bool:
        """Add a new victim to the database"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO victims VALUES (
                    ?, ?, ?, ?, ?, ?, ?, ?, ?
                )
            ''', (
                victim.id,
                victim.name,
                victim.email,
                victim.phone,
                victim.registration_date.isoformat(),
                victim.last_contact.isoformat(),
                victim.scam_type.value,
                victim.reported_loss,
                victim.notes
            ))
            
            conn.commit()
            conn.close()
            return True
        except Error as e:
            logger.error(f"Error adding victim: {e}")
            return False

    def add_scammer(self, scammer: ScammerProfile) -> bool:
        """Add a new scammer profile to the database"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO scammers VALUES (
                    ?, ?, ?, ?, ?, ?, ?
                )
            ''', (
                scammer.id,
                json.dumps(scammer.aliases),
                json.dumps(scammer.known_platforms),
                json.dumps(scammer.contact_methods),
                scammer.last_active.isoformat(),
                scammer.estimated_funds,
                json.dumps(scammer.associated_accounts)
            ))
            
            conn.commit()
            conn.close()
            return True
        except Error as e:
            logger.error(f"Error adding scammer: {e}")
            return False

    def add_transaction(self, transaction: Transaction) -> bool:
        """Add a new transaction record"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO transactions VALUES (
                    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                )
            ''', (
                transaction.id,
                transaction.victim_id,
                transaction.scammer_id,
                transaction.amount,
                transaction.currency,
                transaction.transaction_date.isoformat(),
                transaction.method,
                transaction.transaction_reference,
                int(transaction.is_recovered),
                transaction.recovery_date.isoformat() if transaction.recovery_date else None
            ))
            
            conn.commit()
            conn.close()
            return True
        except Error as e:
            logger.error(f"Error adding transaction: {e}")
            return False

    def mark_transaction_recovered(self, transaction_id: str, recovery_date: datetime.datetime) -> bool:
        """Mark a transaction as recovered"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                UPDATE transactions
                SET is_recovered = 1, recovery_date = ?
                WHERE id = ?
            ''', (recovery_date.isoformat(), transaction_id))
            
            conn.commit()
            conn.close()
            return True
        except Error as e:
            logger.error(f"Error marking transaction as recovered: {e}")
            return False

    def get_victim(self, victim_id: str) -> Optional[Victim]:
        """Retrieve a victim by ID"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('SELECT * FROM victims WHERE id = ?', (victim_id,))
            row = cursor.fetchone()
            
            if not row:
                return None
                
            return Victim(
                id=row[0],
                name=row[1],
                email=row[2],
                phone=row[3],
                registration_date=datetime.datetime.fromisoformat(row[4]),
                last_contact=datetime.datetime.fromisoformat(row[5]),
                scam_type=ScamType(row[6]),
                reported_loss=row[7],
                notes=row[8]
            )
        except Error as e:
            logger.error(f"Error retrieving victim: {e}")
            return None

    def get_scammer(self, scammer_id: str) -> Optional[ScammerProfile]:
        """Retrieve a scammer by ID"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('SELECT * FROM scammers WHERE id = ?', (scammer_id,))
            row = cursor.fetchone()
            
            if not row:
                return None
                
            return ScammerProfile(
                id=row[0],
                aliases=json.loads(row[1]),
                known_platforms=json.loads(row[2]),
                contact_methods=json.loads(row[3]),
                last_active=datetime.datetime.fromisoformat(row[4]),
                estimated_funds=row[5],
                associated_accounts=json.loads(row[6]) if row[6] else []
            )
        except Error as e:
            logger.error(f"Error retrieving scammer: {e}")
            return None

    def get_transactions_by_victim(self, victim_id: str) -> List[Transaction]:
        """Retrieve all transactions for a victim"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('SELECT * FROM transactions WHERE victim_id = ?', (victim_id,))
            rows = cursor.fetchall()
            
            transactions = []
            for row in rows:
                transactions.append(Transaction(
                    id=row[0],
                    victim_id=row[1],
                    scammer_id=row[2],
                    amount=row[3],
                    currency=row[4],
                    transaction_date=datetime
