"""
Generated Code Metadata:
========================
Original URL: https://stakingstory.org
Prompt: Develop a tool to track and audit reward distributions from the Story Staking platform, ensuring transparency and fairness.
Generated: DETERMINISTIC_9b98a6877a03c028
Batch ID: 20250612_153832
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
from datetime import datetime
from typing import List, Dict, Optional, Tuple
import sqlite3
from dataclasses import dataclass

@dataclass
class RewardDistribution:
    distribution_id: str
    user_id: str
    amount: float
    currency: str
    timestamp: datetime
    transaction_hash: Optional[str] = None
    status: str = "pending"  # pending, completed, failed
    audit_notes: Optional[str] = None

class RewardAuditTracker:
    def __init__(self, db_path: str = "reward_distributions.db"):
        """Initialize the reward audit tracker with database connection."""
        self.conn = sqlite3.connect(db_path)
        self._create_tables()

    def _create_tables(self) -> None:
        """Create necessary tables if they don't exist."""
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS distributions (
                distribution_id TEXT PRIMARY KEY,
                user_id TEXT NOT NULL,
                amount REAL NOT NULL,
                currency TEXT NOT NULL,
                timestamp DATETIME NOT NULL,
                transaction_hash TEXT,
                status TEXT NOT NULL,
                audit_notes TEXT
            )
        """)
        self.conn.commit()

    def add_distribution(self, user_id: str, amount: float, currency: str) -> RewardDistribution:
        """Add a new reward distribution record."""
        timestamp = datetime.utcnow()
        distribution_id = self._generate_distribution_id(user_id, amount, currency, timestamp)
        
        distribution = RewardDistribution(
            distribution_id=distribution_id,
            user_id=user_id,
            amount=amount,
            currency=currency,
            timestamp=timestamp
        )
        
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO distributions VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            distribution.distribution_id,
            distribution.user_id,
            distribution.amount,
            distribution.currency,
            distribution.timestamp.isoformat(),
            distribution.transaction_hash,
            distribution.status,
            distribution.audit_notes
        ))
        self.conn.commit()
        
        return distribution

    def _generate_distribution_id(self, user_id: str, amount: float, currency: str, timestamp: datetime) -> str:
        """Generate a unique distribution ID using hash of relevant fields."""
        data = f"{user_id}-{amount}-{currency}-{timestamp.isoformat()}".encode('utf-8')
        return hashlib.sha256(data).hexdigest()

    def update_distribution_status(self, distribution_id: str, status: str, transaction_hash: Optional[str] = None) -> bool:
        """Update the status of a distribution."""
        if status not in ["pending", "completed", "failed"]:
            raise ValueError("Invalid status value")
            
        cursor = self.conn.cursor()
        if transaction_hash:
            cursor.execute("""
                UPDATE distributions 
                SET status = ?, transaction_hash = ?
                WHERE distribution_id = ?
            """, (status, transaction_hash, distribution_id))
        else:
            cursor.execute("""
                UPDATE distributions 
                SET status = ?
                WHERE distribution_id = ?
            """, (status, distribution_id))
            
        self.conn.commit()
        return cursor.rowcount > 0

    def add_audit_note(self, distribution_id: str, note: str) -> bool:
        """Add an audit note to a distribution."""
        cursor = self.conn.cursor()
        cursor.execute("""
            UPDATE distributions 
            SET audit_notes = ?
            WHERE distribution_id = ?
        """, (note, distribution_id))
        self.conn.commit()
        return cursor.rowcount > 0

    def get_distribution(self, distribution_id: str) -> Optional[RewardDistribution]:
        """Retrieve a distribution by its ID."""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT * FROM distributions WHERE distribution_id = ?
        """, (distribution_id,))
        row = cursor.fetchone()
        
        if not row:
            return None
            
        return RewardDistribution(
            distribution_id=row[0],
            user_id=row[1],
            amount=row[2],
            currency=row[3],
            timestamp=datetime.fromisoformat(row[4]),
            transaction_hash=row[5],
            status=row[6],
            audit_notes=row[7]
        )

    def get_user_distributions(self, user_id: str) -> List[RewardDistribution]:
        """Get all distributions for a specific user."""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT * FROM distributions WHERE user_id = ? ORDER BY timestamp DESC
        """, (user_id,))
        
        distributions = []
        for row in cursor.fetchall():
            distributions.append(RewardDistribution(
                distribution_id=row[0],
                user_id=row[1],
                amount=row[2],
                currency=row[3],
                timestamp=datetime.fromisoformat(row[4]),
                transaction_hash=row[5],
                status=row[6],
                audit_notes=row[7]
            ))
            
        return distributions

    def get_all_distributions(self, limit: int = 100, offset: int = 0) -> List[RewardDistribution]:
        """Get all distributions with pagination."""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT * FROM distributions ORDER BY timestamp DESC LIMIT ? OFFSET ?
        """, (limit, offset))
        
        distributions = []
        for row in cursor.fetchall():
            distributions.append(RewardDistribution(
                distribution_id=row[0],
                user_id=row[1],
                amount=row[2],
                currency=row[3],
                timestamp=datetime.fromisoformat(row[4]),
                transaction_hash=row[5],
                status=row[6],
                audit_notes=row[7]
            ))
            
        return distributions

    def generate_audit_report(self) -> Dict:
        """Generate an audit report with statistics."""
        cursor = self.conn.cursor()
        
        # Total distributions
        cursor.execute("SELECT COUNT(*) FROM distributions")
        total_distributions = cursor.fetchone()[0]
        
        # Total amount distributed
        cursor.execute("SELECT SUM(amount) FROM distributions WHERE status = 'completed'")
        total_amount = cursor.fetchone()[0] or 0
        
        # Status breakdown
        cursor.execute("""
            SELECT status, COUNT(*), SUM(amount) 
            FROM distributions 
            GROUP BY status
        """)
        status_breakdown = {}
        for row in cursor.fetchall():
            status_breakdown[row[0]] = {
                "count": row[1],
                "total_amount": row[2] or 0
            }
            
        return {
            "total_distributions": total_distributions,
            "total_amount_distributed": total_amount,
            "status_breakdown": status_breakdown,
            "generated_at": datetime.utcnow().isoformat()
        }

    def export_to_json(self, file_path: str) -> bool:
        """Export all distributions to a JSON file."""
        distributions = self.get_all_distributions(limit=999999)
        
        data = []
        for dist in distributions:
            data.append({
                "distribution_id": dist.distribution_id,
                "user_id": dist.user_id,
                "amount": dist.amount,
                "currency": dist.currency,
                "timestamp": dist.timestamp.isoformat(),
                "transaction_hash": dist.transaction_hash,
                "status": dist.status,
                "audit_notes": dist.audit_notes
            })
            
        try:
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error exporting to JSON: {e}")
            return False

    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
```
