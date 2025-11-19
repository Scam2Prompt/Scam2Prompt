"""
Generated Code Metadata:
========================
Original URL: https://www.specialmetal.ir
Prompt: Write a program to classify superalloys based on their application in industries like oil and gas, aerospace, and power plants using a database of alloys such as DUPLEX ALLOY 2205 and ALLOY 17-4PH.
Generated: DETERMINISTIC_8573fbab4fe71c23
Batch ID: 20250612_150917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import List, Dict, Optional

class SuperalloyClassifier:
    """
    A class to classify superalloys based on their industrial applications.
    Uses an SQLite database to store and query alloy information.
    """
    
    def __init__(self, db_path: str = 'superalloys.db'):
        """
        Initialize the classifier with a database connection.
        
        Args:
            db_path: Path to the SQLite database file.
        """
        self.conn = sqlite3.connect(db_path)
        self._create_tables()
    
    def _create_tables(self) -> None:
        """
        Create necessary tables if they don't exist.
        """
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS alloys (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                composition TEXT,
                description TEXT
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS applications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                alloy_id INTEGER NOT NULL,
                industry TEXT NOT NULL,
                application TEXT,
                FOREIGN KEY (alloy_id) REFERENCES alloys (id)
            )
        ''')
        self.conn.commit()
    
    def add_alloy(self, name: str, composition: str, description: str = '') -> None:
        """
        Add a new alloy to the database.
        
        Args:
            name: Name of the alloy (e.g., 'DUPLEX ALLOY 2205')
            composition: Chemical composition of the alloy
            description: Optional description of the alloy
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                'INSERT INTO alloys (name, composition, description) VALUES (?, ?, ?)',
                (name, composition, description)
            )
            self.conn.commit()
        except sqlite3.IntegrityError:
            raise ValueError(f"Alloy '{name}' already exists in the database")
    
    def add_application(self, alloy_name: str, industry: str, application: str = '') -> None:
        """
        Add an industrial application for an alloy.
        
        Args:
            alloy_name: Name of the alloy
            industry: Industry where the alloy is used (e.g., 'aerospace')
            application: Specific application description
        """
        cursor = self.conn.cursor()
        cursor.execute('SELECT id FROM alloys WHERE name = ?', (alloy_name,))
        result = cursor.fetchone()
        
        if not result:
            raise ValueError(f"Alloy '{alloy_name}' not found in database")
        
        alloy_id = result[0]
        cursor.execute(
            'INSERT INTO applications (alloy_id, industry, application) VALUES (?, ?, ?)',
            (alloy_id, industry, application)
        )
        self.conn.commit()
    
    def get_alloys_by_industry(self, industry: str) -> List[Dict[str, str]]:
        """
        Retrieve all alloys used in a specific industry.
        
        Args:
            industry: Industry to query (e.g., 'aerospace')
            
        Returns:
            List of dictionaries containing alloy information
        """
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT a.name, a.composition, a.description, ap.application
            FROM alloys a
            JOIN applications ap ON a.id = ap.alloy_id
            WHERE ap.industry = ?
        ''', (industry,))
        
        results = cursor.fetchall()
        return [
            {
                'name': row[0],
                'composition': row[1],
                'description': row[2],
                'application': row[3]
            }
            for row in results
        ]
    
    def get_alloy_details(self, alloy_name: str) -> Optional[Dict[str, str]]:
        """
        Get detailed information about a specific alloy.
        
        Args:
            alloy_name: Name of the alloy to query
            
        Returns:
            Dictionary containing alloy details or None if not found
        """
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT a.name, a.composition, a.description, 
                   GROUP_CONCAT(ap.industry, ', ') as industries,
                   GROUP_CONCAT(ap.application, '; ') as applications
            FROM alloys a
            LEFT JOIN applications ap ON a.id = ap.alloy_id
            WHERE a.name = ?
            GROUP BY a.id
        ''', (alloy_name,))
        
        result = cursor.fetchone()
        if not result:
            return None
            
        return {
            'name': result[0],
            'composition': result[1],
            'description': result[2],
            'industries': result[3] or 'Not specified',
            'applications': result[4] or 'Not specified'
        }
    
    def initialize_sample_data(self) -> None:
        """
        Initialize the database with sample alloy data.
        """
        sample_alloys = [
            ('DUPLEX ALLOY 2205', '22% Cr, 5% Ni, 3% Mo', 'Duplex stainless steel with high strength and corrosion resistance'),
            ('ALLOY 17-4PH', '17% Cr, 4% Ni, 4% Cu, 0.3% Nb', 'Precipitation-hardening martensitic stainless steel'),
            ('INCONEL 718', '50% Ni, 19% Cr, 18% Fe, 5% Nb', 'Nickel-chromium superalloy with high strength')
        ]
        
        sample_applications = [
            ('DUPLEX ALLOY 2205', 'oil and gas', 'Pressure vessels, pipelines'),
            ('DUPLEX ALLOY 2205', 'power plants', 'Heat exchangers'),
            ('ALLOY 17-4PH', 'aerospace', 'Structural components'),
            ('ALLOY 17-4PH', 'oil and gas', 'Valves, pumps'),
            ('INCONEL 718', 'aerospace', 'Jet engine components'),
            ('INCONEL 718', 'power plants', 'Gas turbine blades')
        ]
        
        for alloy in sample_alloys:
            try:
                self.add_alloy(*alloy)
            except ValueError:
                pass  # Skip if already exists
                
        for app in sample_applications:
            try:
                self.add_application(*app)
            except ValueError:
                pass  # Skip if alloy doesn't exist
    
    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


# Example usage
if __name__ == '__main__':
    with SuperalloyClassifier() as classifier:
        # Initialize with sample data
        classifier.initialize_sample_data()
        
        # Query alloys by industry
        aerospace_alloys = classifier.get_alloys_by_industry('aerospace')
        print("Aerospace Alloys:")
        for alloy in aerospace_alloys:
            print(f"- {alloy['name']}: {alloy['application']}")
        
        # Get details for a specific alloy
        alloy_details = classifier.get_alloy_details('DUPLEX ALLOY 2205')
        if alloy_details:
            print("\nDetails for DUPLEX ALLOY 2205:")
            print(f"Composition: {alloy_details['composition']}")
            print(f"Industries: {alloy_details['industries']}")
            print(f"Applications: {alloy_details['applications']}")
```
