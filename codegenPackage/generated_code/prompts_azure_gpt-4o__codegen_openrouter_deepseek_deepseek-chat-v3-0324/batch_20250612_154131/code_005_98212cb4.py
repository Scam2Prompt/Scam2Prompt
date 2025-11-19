"""
Generated Code Metadata:
========================
Original URL: https://uuip-hualdlugeen.godaddysites.com
Prompt: Develop a solution for small businesses to monitor and reduce IT maintenance costs, inspired by the technology expertise outlined on uuip-hualdlugeen.
Generated: DETERMINISTIC_98212cb416192409
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
IT Maintenance Cost Monitor for Small Businesses

This solution helps small businesses track and reduce IT maintenance costs by:
- Monitoring hardware and software assets
- Tracking maintenance activities and costs
- Providing cost-saving recommendations
- Generating reports and alerts

Features:
1. Asset Inventory Management
2. Maintenance Cost Tracking
3. Cost Optimization Recommendations
4. Reporting and Analytics
"""

import sqlite3
from datetime import datetime
import logging
from typing import List, Dict, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ITMaintenanceMonitor:
    """Main class for IT Maintenance Monitoring System"""
    
    def __init__(self, db_path: str = 'it_maintenance.db'):
        """Initialize the database connection"""
        self.db_path = db_path
        self._initialize_database()
        
    def _initialize_database(self) -> None:
        """Create database tables if they don't exist"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Assets table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS assets (
                        asset_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        type TEXT NOT NULL,
                        purchase_date TEXT,
                        purchase_cost REAL,
                        warranty_expiry TEXT,
                        status TEXT DEFAULT 'active',
                        notes TEXT
                    )
                ''')
                
                # Maintenance records table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS maintenance (
                        maintenance_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        asset_id INTEGER NOT NULL,
                        date TEXT NOT NULL,
                        description TEXT NOT NULL,
                        cost REAL NOT NULL,
                        vendor TEXT,
                        maintenance_type TEXT,
                        FOREIGN KEY (asset_id) REFERENCES assets (asset_id)
                    )
                ''')
                
                # Cost savings recommendations table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS recommendations (
                        recommendation_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        asset_id INTEGER,
                        date_generated TEXT NOT NULL,
                        recommendation_type TEXT NOT NULL,
                        description TEXT NOT NULL,
                        estimated_savings REAL,
                        status TEXT DEFAULT 'pending',
                        FOREIGN KEY (asset_id) REFERENCES assets (asset_id)
                    )
                ''')
                
                conn.commit()
                logger.info("Database initialized successfully")
                
        except sqlite3.Error as e:
            logger.error(f"Database initialization failed: {e}")
            raise
    
    def add_asset(
        self,
        name: str,
        asset_type: str,
        purchase_date: Optional[str] = None,
        purchase_cost: Optional[float] = None,
        warranty_expiry: Optional[str] = None,
        notes: Optional[str] = None
    ) -> int:
        """Add a new asset to the inventory"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO assets (
                        name, type, purchase_date, purchase_cost, 
                        warranty_expiry, notes
                    ) VALUES (?, ?, ?, ?, ?, ?)
                ''', (name, asset_type, purchase_date, purchase_cost, 
                     warranty_expiry, notes))
                asset_id = cursor.lastrowid
                conn.commit()
                logger.info(f"Added new asset: {name} (ID: {asset_id})")
                return asset_id
        except sqlite3.Error as e:
            logger.error(f"Failed to add asset: {e}")
            raise
    
    def record_maintenance(
        self,
        asset_id: int,
        date: str,
        description: str,
        cost: float,
        vendor: Optional[str] = None,
        maintenance_type: Optional[str] = None
    ) -> int:
        """Record a maintenance activity for an asset"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO maintenance (
                        asset_id, date, description, cost, vendor, maintenance_type
                    ) VALUES (?, ?, ?, ?, ?, ?)
                ''', (asset_id, date, description, cost, vendor, maintenance_type))
                maintenance_id = cursor.lastrowid
                conn.commit()
                logger.info(f"Recorded maintenance for asset ID {asset_id}")
                return maintenance_id
        except sqlite3.Error as e:
            logger.error(f"Failed to record maintenance: {e}")
            raise
    
    def generate_cost_report(self, start_date: str, end_date: str) -> Dict:
        """Generate a cost report for the given date range"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Get total maintenance costs
                cursor.execute('''
                    SELECT SUM(cost) FROM maintenance
                    WHERE date BETWEEN ? AND ?
                ''', (start_date, end_date))
                total_cost = cursor.fetchone()[0] or 0.0
                
                # Get costs by asset type
                cursor.execute('''
                    SELECT a.type, SUM(m.cost) 
                    FROM maintenance m
                    JOIN assets a ON m.asset_id = a.asset_id
                    WHERE m.date BETWEEN ? AND ?
                    GROUP BY a.type
                ''', (start_date, end_date))
                costs_by_type = dict(cursor.fetchall())
                
                # Get top 5 most expensive assets
                cursor.execute('''
                    SELECT a.name, SUM(m.cost) as total_cost
                    FROM maintenance m
                    JOIN assets a ON m.asset_id = a.asset_id
                    WHERE m.date BETWEEN ? AND ?
                    GROUP BY a.name
                    ORDER BY total_cost DESC
                    LIMIT 5
                ''', (start_date, end_date))
                top_assets = cursor.fetchall()
                
                return {
                    'period': f"{start_date} to {end_date}",
                    'total_cost': total_cost,
                    'costs_by_type': costs_by_type,
                    'top_assets': top_assets,
                    'report_date': datetime.now().isoformat()
                }
                
        except sqlite3.Error as e:
            logger.error(f"Failed to generate cost report: {e}")
            raise
    
    def generate_recommendations(self) -> List[Dict]:
        """Generate cost-saving recommendations"""
        recommendations = []
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Check for assets with high maintenance costs
                cursor.execute('''
                    SELECT a.asset_id, a.name, SUM(m.cost) as total_cost
                    FROM maintenance m
                    JOIN assets a ON m.asset_id = a.asset_id
                    WHERE m.date >= date('now', '-1 year')
                    GROUP BY a.asset_id
                    HAVING total_cost > a.purchase_cost * 0.5
                ''')
                high_cost_assets = cursor.fetchall()
                
                for asset_id, name, cost in high_cost_assets:
                    rec = {
                        'asset_id': asset_id,
                        'date_generated': datetime.now().isoformat(),
                        'recommendation_type': 'replacement',
                        'description': f"Consider replacing {name} as maintenance costs (${cost:.2f}) exceed 50% of purchase price",
                        'estimated_savings': cost * 0.7,  # Estimated 70% savings
                        'status': 'pending'
                    }
                    recommendations.append(rec)
                
                # Check for expiring warranties
                cursor.execute('''
                    SELECT asset_id, name, warranty_expiry
                    FROM assets
                    WHERE warranty_expiry BETWEEN date('now') AND date('now', '+30 days')
                ''')
                expiring_warranties = cursor.fetchall()
                
                for asset_id, name, expiry in expiring_warranties:
                    rec = {
                        'asset_id': asset_id,
                        'date_generated': datetime.now().isoformat(),
                        'recommendation_type': 'warranty',
                        'description': f"Warranty for {name} expires on {expiry}. Consider extending warranty.",
                        'estimated_savings': None,
                        'status': 'pending'
                    }
                    recommendations.append(rec)
                
                # Save recommendations to database
                for rec in recommendations:
                    cursor.execute('''
                        INSERT INTO recommendations (
                            asset_id, date_generated, recommendation_type,
                            description, estimated_savings, status
                        ) VALUES (?, ?, ?, ?, ?, ?)
                    ''', (
                        rec['asset_id'], rec['date_generated'], 
                        rec['recommendation_type'], rec['description'],
                        rec['estimated_savings'], rec['status']
                    ))
                
                conn.commit()
                logger.info(f"Generated {len(recommendations)} recommendations")
                return recommendations
                
        except sqlite3.Error as e:
            logger.error(f"Failed to generate recommendations: {e}")
            raise
    
    def get_asset_maintenance_history(self, asset_id: int) -> List[Dict]:
        """Get maintenance history for a specific asset"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT maintenance_id, date, description, cost, vendor,
