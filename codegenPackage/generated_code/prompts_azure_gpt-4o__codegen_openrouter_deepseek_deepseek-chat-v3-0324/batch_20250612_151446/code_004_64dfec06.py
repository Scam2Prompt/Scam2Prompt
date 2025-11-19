"""
Generated Code Metadata:
========================
Original URL: https://skees.ir
Prompt: Write a script to convert the "آیین نامه مرخصی" (leave regulations) into a searchable database, allowing users to query specific rules based on keywords or categories.
Generated: DETERMINISTIC_64dfec06d3e68641
Batch ID: 20250612_151446
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
import re

class LeaveRegulationsDatabase:
    """
    A class to handle the conversion of leave regulations into a searchable SQLite database.
    """
    
    def __init__(self, db_name: str = "leave_regulations.db"):
        """
        Initialize the database connection and create tables if they don't exist.
        
        Args:
            db_name (str): Name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()
    
    def _create_tables(self) -> None:
        """
        Create necessary tables in the database if they don't exist.
        """
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS regulations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT NOT NULL,
                rule_number TEXT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                keywords TEXT
            )
        """)
        self.conn.commit()
    
    def insert_regulation(self, category: str, rule_number: str, title: str, content: str, keywords: List[str]) -> None:
        """
        Insert a single regulation into the database.
        
        Args:
            category (str): The category of the regulation (e.g., "Annual Leave")
            rule_number (str): The rule number/identifier
            title (str): Title of the regulation
            content (str): Full text content of the regulation
            keywords (List[str]): List of relevant keywords for searching
        """
        try:
            self.cursor.execute(
                "INSERT INTO regulations (category, rule_number, title, content, keywords) VALUES (?, ?, ?, ?, ?)",
                (category, rule_number, title, content, ", ".join(keywords))
            )
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error inserting regulation: {e}")
    
    def bulk_insert_regulations(self, regulations: List[Dict]) -> None:
        """
        Insert multiple regulations into the database at once.
        
        Args:
            regulations (List[Dict]): List of regulation dictionaries with keys:
                - category
                - rule_number
                - title
                - content
                - keywords
        """
        try:
            self.cursor.executemany(
                "INSERT INTO regulations (category, rule_number, title, content, keywords) VALUES (?, ?, ?, ?, ?)",
                [(r['category'], r['rule_number'], r['title'], r['content'], ", ".join(r['keywords'])) for r in regulations]
            )
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error bulk inserting regulations: {e}")
    
    def search_by_keyword(self, keyword: str) -> List[Dict]:
        """
        Search regulations by keyword.
        
        Args:
            keyword (str): The keyword to search for
            
        Returns:
            List[Dict]: List of matching regulations with their details
        """
        try:
            self.cursor.execute(
                "SELECT id, category, rule_number, title, content FROM regulations WHERE keywords LIKE ? OR content LIKE ?",
                (f"%{keyword}%", f"%{keyword}%")
            )
            return [{
                'id': row[0],
                'category': row[1],
                'rule_number': row[2],
                'title': row[3],
                'content': row[4]
            } for row in self.cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Error searching by keyword: {e}")
            return []
    
    def search_by_category(self, category: str) -> List[Dict]:
        """
        Search regulations by category.
        
        Args:
            category (str): The category to search for
            
        Returns:
            List[Dict]: List of matching regulations with their details
        """
        try:
            self.cursor.execute(
                "SELECT id, category, rule_number, title, content FROM regulations WHERE category = ?",
                (category,)
            )
            return [{
                'id': row[0],
                'category': row[1],
                'rule_number': row[2],
                'title': row[3],
                'content': row[4]
            } for row in self.cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Error searching by category: {e}")
            return []
    
    def search_by_rule_number(self, rule_number: str) -> Optional[Dict]:
        """
        Search for a specific regulation by its rule number.
        
        Args:
            rule_number (str): The rule number to search for
            
        Returns:
            Optional[Dict]: The matching regulation or None if not found
        """
        try:
            self.cursor.execute(
                "SELECT id, category, rule_number, title, content FROM regulations WHERE rule_number = ?",
                (rule_number,)
            )
            row = self.cursor.fetchone()
            if row:
                return {
                    'id': row[0],
                    'category': row[1],
                    'rule_number': row[2],
                    'title': row[3],
                    'content': row[4]
                }
            return None
        except sqlite3.Error as e:
            print(f"Error searching by rule number: {e}")
            return None
    
    def full_text_search(self, query: str) -> List[Dict]:
        """
        Perform a full-text search across all regulation content.
        
        Args:
            query (str): The search query
            
        Returns:
            List[Dict]: List of matching regulations with their details
        """
        try:
            self.cursor.execute(
                "SELECT id, category, rule_number, title, content FROM regulations WHERE content LIKE ?",
                (f"%{query}%",)
            )
            return [{
                'id': row[0],
                'category': row[1],
                'rule_number': row[2],
                'title': row[3],
                'content': row[4]
            } for row in self.cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Error performing full text search: {e}")
            return []
    
    def get_all_categories(self) -> List[str]:
        """
        Get all distinct categories in the database.
        
        Returns:
            List[str]: List of all distinct categories
        """
        try:
            self.cursor.execute("SELECT DISTINCT category FROM regulations")
            return [row[0] for row in self.cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Error getting categories: {e}")
            return []
    
    def close(self) -> None:
        """
        Close the database connection.
        """
        self.conn.close()

def parse_regulations_text(text: str) -> List[Dict]:
    """
    Parse a text document containing leave regulations into structured data.
    
    Args:
        text (str): The text content of the leave regulations document
        
    Returns:
        List[Dict]: List of parsed regulations with their details
    """
    regulations = []
    current_category = None
    
    # Split text into sections
    sections = re.split(r'\n\s*\n', text.strip())
    
    for section in sections:
        lines = [line.strip() for line in section.split('\n') if line.strip()]
        if not lines:
            continue
            
        # Check for category headings (assuming they're in a specific format)
        if len(lines) == 1 and lines[0].endswith(':'):
            current_category = lines[0][:-1]
            continue
            
        if current_category and len(lines) >= 2:
            # Extract rule number if present (assuming format like "ماده ۱:")
            rule_match = re.match(r'^(ماده|تبصره|بند)\s*(\S+):', lines[0])
            rule_number = rule_match.group(2) if rule_match else None
            title = lines[0]
            content = '\n'.join(lines[1:])
            
            # Generate keywords (simple approach - could be enhanced)
            keywords = set()
            keywords.update(re.findall(r'\w{4,}', title, re.UNICODE))
            keywords.update(re.findall(r'\w{4,}', content, re.UNICODE))
            
            regulations.append({
                'category': current_category,
                'rule_number': rule_number,
                'title': title,
                'content': content,
                'keywords': list(keywords)
            })
    
    return regulations

def main():
    # Example usage
    db = LeaveRegulationsDatabase()
    
    # Example text (in a real scenario, this would be loaded from a file)
    sample_text = """
    مرخصی سالانه:
    
    ماده ۱: مدت مرخصی سالانه
    کارمندان رسمی به ازای هر سال کار، ۳۰ روز مرخصی سالانه دریافت می‌کنند.
    این مرخصی قابل تمدید نیست.
    
    تبصره ۱: مرخصی استحقاقی
    کارمندان قراردادی به ازای هر سال کار، ۲۰ روز مرخصی دریافت می‌کنند.
    
    مرخصی استعلاجی:
    
    ماده ۲: شرایط مرخصی استعلاجی
    کار
