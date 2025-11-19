"""
Generated Code Metadata:
========================
Original URL: https://vertivvpp.dev.stp.prmcdn.io
Prompt: Outline a plan for a training module that consolidates online sales and technical training for Vertiv partners, including certification tracking.
Generated: DETERMINISTIC_4093e49051615466
Batch ID: 20250612_155250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Vertiv Partner Training Module
This module consolidates online sales and technical training for Vertiv partners,
including certification tracking.
"""

from datetime import datetime
from enum import Enum, auto
from typing import List, Dict, Optional
import sqlite3
from dataclasses import dataclass
import hashlib
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class TrainingType(Enum):
    """Enum for different training types"""
    SALES = auto()
    TECHNICAL = auto()
    PRODUCT = auto()

class CertificationStatus(Enum):
    """Enum for certification status"""
    NOT_STARTED = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
    EXPIRED = auto()

@dataclass
class TrainingModule:
    """Dataclass representing a training module"""
    id: str
    title: str
    description: str
    duration_minutes: int
    training_type: TrainingType
    required_for_certification: bool

@dataclass
class Partner:
    """Dataclass representing a partner"""
    id: str
    name: str
    email: str
    region: str
    tier: str

@dataclass
class PartnerCertification:
    """Dataclass representing partner certification progress"""
    partner_id: str
    module_id: str
    status: CertificationStatus
    completion_date: Optional[datetime]
    score: Optional[float]

class TrainingSystem:
    """Main class for the Vertiv Partner Training System"""
    
    def __init__(self, db_path: str = 'vertiv_training.db'):
        """Initialize the training system with database connection"""
        self.db_path = db_path
        self._initialize_database()
    
    def _initialize_database(self) -> None:
        """Create database tables if they don't exist"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Create training modules table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS training_modules (
                        id TEXT PRIMARY KEY,
                        title TEXT NOT NULL,
                        description TEXT,
                        duration_minutes INTEGER NOT NULL,
                        training_type TEXT NOT NULL,
                        required_for_certification BOOLEAN NOT NULL
                    )
                ''')
                
                # Create partners table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS partners (
                        id TEXT PRIMARY KEY,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL UNIQUE,
                        region TEXT NOT NULL,
                        tier TEXT NOT NULL
                    )
                ''')
                
                # Create certifications table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS certifications (
                        partner_id TEXT,
                        module_id TEXT,
                        status TEXT NOT NULL,
                        completion_date TEXT,
                        score REAL,
                        PRIMARY KEY (partner_id, module_id),
                        FOREIGN KEY (partner_id) REFERENCES partners(id),
                        FOREIGN KEY (module_id) REFERENCES training_modules(id)
                    )
                ''')
                
                conn.commit()
        except sqlite3.Error as e:
            logger.error(f"Database initialization failed: {e}")
            raise
    
    def add_training_module(self, module: TrainingModule) -> bool:
        """Add a new training module to the system"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO training_modules 
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (
                    module.id,
                    module.title,
                    module.description,
                    module.duration_minutes,
                    module.training_type.name,
                    module.required_for_certification
                ))
                conn.commit()
                return True
        except sqlite3.Error as e:
            logger.error(f"Failed to add training module: {e}")
            return False
    
    def register_partner(self, partner: Partner) -> bool:
        """Register a new partner in the system"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO partners 
                    VALUES (?, ?, ?, ?, ?)
                ''', (
                    partner.id,
                    partner.name,
                    partner.email,
                    partner.region,
                    partner.tier
                ))
                conn.commit()
                return True
        except sqlite3.Error as e:
            logger.error(f"Failed to register partner: {e}")
            return False
    
    def update_certification_status(
        self,
        partner_id: str,
        module_id: str,
        status: CertificationStatus,
        score: Optional[float] = None
    ) -> bool:
        """Update certification status for a partner"""
        try:
            completion_date = datetime.now().isoformat() if status == CertificationStatus.COMPLETED else None
            
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT OR REPLACE INTO certifications 
                    VALUES (?, ?, ?, ?, ?)
                ''', (
                    partner_id,
                    module_id,
                    status.name,
                    completion_date,
                    score
                ))
                conn.commit()
                return True
        except sqlite3.Error as e:
            logger.error(f"Failed to update certification status: {e}")
            return False
    
    def get_partner_certifications(self, partner_id: str) -> List[PartnerCertification]:
        """Get all certifications for a partner"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT * FROM certifications 
                    WHERE partner_id = ?
                ''', (partner_id,))
                
                results = cursor.fetchall()
                certifications = []
                
                for row in results:
                    completion_date = datetime.fromisoformat(row[3]) if row[3] else None
                    certifications.append(PartnerCertification(
                        partner_id=row[0],
                        module_id=row[1],
                        status=CertificationStatus[row[2]],
                        completion_date=completion_date,
                        score=row[4]
                    ))
                
                return certifications
        except sqlite3.Error as e:
            logger.error(f"Failed to get partner certifications: {e}")
            return []
    
    def get_required_modules(self, training_type: Optional[TrainingType] = None) -> List[TrainingModule]:
        """Get all required training modules, optionally filtered by type"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                if training_type:
                    cursor.execute('''
                        SELECT * FROM training_modules 
                        WHERE required_for_certification = 1 
                        AND training_type = ?
                    ''', (training_type.name,))
                else:
                    cursor.execute('''
                        SELECT * FROM training_modules 
                        WHERE required_for_certification = 1
                    ''')
                
                results = cursor.fetchall()
                modules = []
                
                for row in results:
                    modules.append(TrainingModule(
                        id=row[0],
                        title=row[1],
                        description=row[2],
                        duration_minutes=row[3],
                        training_type=TrainingType[row[4]],
                        required_for_certification=bool(row[5])
                    ))
                
                return modules
        except sqlite3.Error as e:
            logger.error(f"Failed to get required modules: {e}")
            return []
    
    def check_partner_certification_status(self, partner_id: str) -> Dict[str, str]:
        """Check overall certification status for a partner"""
        try:
            required_modules = self.get_required_modules()
            partner_certs = self.get_partner_certifications(partner_id)
            
            completed = 0
            in_progress = 0
            not_started = 0
            
            cert_dict = {cert.module_id: cert.status for cert in partner_certs}
            
            for module in required_modules:
                status = cert_dict.get(module.id, CertificationStatus.NOT_STARTED)
                
                if status == CertificationStatus.COMPLETED:
                    completed += 1
                elif status == CertificationStatus.IN_PROGRESS:
                    in_progress += 1
                else:
                    not_started += 1
            
            total = len(required_modules)
            percent_complete = (completed / total) * 100 if total > 0 else 0
            
            return {
                'completed': completed,
                'in_progress': in_progress,
                'not_started': not_started,
                'total': total,
                'percent_complete': percent_complete
            }
        except Exception as e:
            logger.error(f"Failed to check partner certification status: {e}")
            return {
                'completed': 0,
                'in_progress': 0,
                'not_started': 0,
                'total': 0,
                'percent_complete': 0
            }

# Example usage
if __name__ == "__main__":
    system = TrainingSystem()
    
    # Add sample training modules
    sales_module = TrainingModule(
        id="sales101",
        title="Vertiv Sales Fundamentals",
        description="Introduction to Vertiv products and sales techniques",
        duration_minutes=120,
        training_type=TrainingType
