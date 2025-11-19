"""
Generated Code Metadata:
========================
Original URL: https://claim-buck.pages.dev
Prompt: Develop a referral system in Python that mimics CoinBuck's multi-level referral bonus structure, including tracking referral tasks and KYC completion.
Generated: DETERMINISTIC_f2e37fe41a358bb8
Batch ID: 20250612_152326
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime
from typing import Dict, List, Optional, Tuple
from enum import Enum, auto
import sqlite3
from dataclasses import dataclass


class ReferralStatus(Enum):
    PENDING = auto()
    COMPLETED = auto()
    FAILED = auto()


class TaskType(Enum):
    SIGN_UP = auto()
    KYC_COMPLETION = auto()
    FIRST_DEPOSIT = auto()


@dataclass
class User:
    id: str
    username: str
    email: str
    referrer_id: Optional[str] = None
    kyc_completed: bool = False
    first_deposit_made: bool = False


@dataclass
class Referral:
    id: str
    referrer_id: str
    referee_id: str
    status: ReferralStatus
    created_at: datetime
    completed_at: Optional[datetime] = None


@dataclass
class Task:
    id: str
    user_id: str
    task_type: TaskType
    status: ReferralStatus
    created_at: datetime
    completed_at: Optional[datetime] = None


@dataclass
class Bonus:
    id: str
    user_id: str
    amount: float
    referral_id: Optional[str] = None
    task_id: Optional[str] = None
    created_at: datetime = datetime.now()


class ReferralSystem:
    def __init__(self, db_path: str = "referral_system.db"):
        self.conn = sqlite3.connect(db_path)
        self._create_tables()

    def _create_tables(self) -> None:
        cursor = self.conn.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            referrer_id TEXT,
            kyc_completed BOOLEAN DEFAULT FALSE,
            first_deposit_made BOOLEAN DEFAULT FALSE,
            FOREIGN KEY (referrer_id) REFERENCES users(id)
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS referrals (
            id TEXT PRIMARY KEY,
            referrer_id TEXT NOT NULL,
            referee_id TEXT NOT NULL,
            status TEXT NOT NULL,
            created_at TEXT NOT NULL,
            completed_at TEXT,
            FOREIGN KEY (referrer_id) REFERENCES users(id),
            FOREIGN KEY (referee_id) REFERENCES users(id)
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id TEXT PRIMARY KEY,
            user_id TEXT NOT NULL,
            task_type TEXT NOT NULL,
            status TEXT NOT NULL,
            created_at TEXT NOT NULL,
            completed_at TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS bonuses (
            id TEXT PRIMARY KEY,
            user_id TEXT NOT NULL,
            amount REAL NOT NULL,
            referral_id TEXT,
            task_id TEXT,
            created_at TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (referral_id) REFERENCES referrals(id),
            FOREIGN KEY (task_id) REFERENCES tasks(id)
        )
        """)
        
        self.conn.commit()

    def _get_user(self, user_id: str) -> Optional[User]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        row = cursor.fetchone()
        if row:
            return User(*row)
        return None

    def register_user(self, username: str, email: str, referrer_id: Optional[str] = None) -> User:
        if referrer_id and not self._get_user(referrer_id):
            raise ValueError("Referrer does not exist")
            
        user_id = str(uuid.uuid4())
        user = User(
            id=user_id,
            username=username,
            email=email,
            referrer_id=referrer_id
        )
        
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO users (id, username, email, referrer_id) VALUES (?, ?, ?, ?)",
            (user.id, user.username, user.email, user.referrer_id)
        )
        
        if referrer_id:
            self._create_referral(referrer_id, user_id)
            self._create_task(user_id, TaskType.SIGN_UP)
        
        self.conn.commit()
        return user

    def _create_referral(self, referrer_id: str, referee_id: str) -> Referral:
        referral = Referral(
            id=str(uuid.uuid4()),
            referrer_id=referrer_id,
            referee_id=referee_id,
            status=ReferralStatus.PENDING,
            created_at=datetime.now()
        )
        
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO referrals (id, referrer_id, referee_id, status, created_at) VALUES (?, ?, ?, ?, ?)",
            (referral.id, referral.referrer_id, referral.referee_id, referral.status.name, referral.created_at.isoformat())
        )
        
        return referral

    def _create_task(self, user_id: str, task_type: TaskType) -> Task:
        task = Task(
            id=str(uuid.uuid4()),
            user_id=user_id,
            task_type=task_type,
            status=ReferralStatus.PENDING,
            created_at=datetime.now()
        )
        
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (id, user_id, task_type, status, created_at) VALUES (?, ?, ?, ?, ?)",
            (task.id, task.user_id, task.task_type.name, task.status.name, task.created_at.isoformat())
        )
        
        return task

    def complete_kyc(self, user_id: str) -> None:
        user = self._get_user(user_id)
        if not user:
            raise ValueError("User does not exist")
        if user.kyc_completed:
            return
            
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE users SET kyc_completed = TRUE WHERE id = ?",
            (user_id,)
        )
        
        self._create_task(user_id, TaskType.KYC_COMPLETION)
        self._process_referral_tasks(user_id)
        self.conn.commit()

    def complete_first_deposit(self, user_id: str) -> None:
        user = self._get_user(user_id)
        if not user:
            raise ValueError("User does not exist")
        if user.first_deposit_made:
            return
            
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE users SET first_deposit_made = TRUE WHERE id = ?",
            (user_id,)
        )
        
        self._create_task(user_id, TaskType.FIRST_DEPOSIT)
        self._process_referral_tasks(user_id)
        self.conn.commit()

    def _process_referral_tasks(self, user_id: str) -> None:
        user = self._get_user(user_id)
        if not user or not user.referrer_id:
            return
            
        tasks = self._get_user_tasks(user_id)
        completed_tasks = [t for t in tasks if t.status == ReferralStatus.COMPLETED]
        
        if len(completed_tasks) == 3:  # All tasks completed
            self._complete_referral(user.referrer_id, user_id)
            self._award_bonuses(user.referrer_id, user_id)

    def _get_user_tasks(self, user_id: str) -> List[Task]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM tasks WHERE user_id = ?", (user_id,))
        rows = cursor.fetchall()
        return [
            Task(
                id=row[0],
                user_id=row[1],
                task_type=TaskType[row[2]],
                status=ReferralStatus[row[3]],
                created_at=datetime.fromisoformat(row[4]),
                completed_at=datetime.fromisoformat(row[5]) if row[5] else None
            ) for row in rows
        ]

    def _complete_referral(self, referrer_id: str, referee_id: str) -> None:
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE referrals SET status = ?, completed_at = ? WHERE referrer_id = ? AND referee_id = ?",
            (ReferralStatus.COMPLETED.name, datetime.now().isoformat(), referrer_id, referee_id)
        )

    def _award_bonuses(self, referrer_id: str, referee_id: str) -> None:
        # Award bonus to direct referrer
        self._award_referral_bonus(referrer_id, referee_id, 10.0)  # $10 for direct referral
        
        # Award bonus to level 2 referrer (if exists)
        referrer = self._get_user(referrer_id)
        if referrer and referrer.referrer_id:
            self._award_referral_bonus(referrer.referrer_id, referee_id, 5.0
