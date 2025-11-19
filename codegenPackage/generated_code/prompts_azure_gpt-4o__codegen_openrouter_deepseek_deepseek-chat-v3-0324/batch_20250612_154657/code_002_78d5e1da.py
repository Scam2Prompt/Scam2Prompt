"""
Generated Code Metadata:
========================
Original URL: https://claim.manatoken.net
Prompt: Generate Python code to create a system that collects and recommends websites based on user preferences, similar to the functionality described in Stumble! ®.
Generated: DETERMINISTIC_78d5e1daa8d0dd33
Batch ID: 20250612_154657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random
from typing import List, Dict, Optional
from dataclasses import dataclass, asdict
import sqlite3
from pathlib import Path

# Constants
DATABASE_NAME = "stumble_db.sqlite"
WEBSITES_JSON = "websites.json"
USER_PREFERENCES_FILE = "user_preferences.json"

@dataclass
class Website:
    url: str
    title: str
    description: str
    categories: List[str]
    rating: float = 0.0

class StumbleSystem:
    def __init__(self):
        self.db_conn = self._initialize_database()
        self._load_websites()
        self.user_preferences = self._load_user_preferences()

    def _initialize_database(self) -> sqlite3.Connection:
        """Initialize SQLite database connection and create tables if they don't exist."""
        db_path = Path(DATABASE_NAME)
        conn = sqlite3.connect(str(db_path))
        
        # Create tables
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS websites (
                url TEXT PRIMARY KEY,
                title TEXT,
                description TEXT,
                rating REAL
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS website_categories (
                url TEXT,
                category TEXT,
                FOREIGN KEY(url) REFERENCES websites(url),
                PRIMARY KEY(url, category)
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_preferences (
                category TEXT PRIMARY KEY,
                weight REAL DEFAULT 1.0
            )
        ''')
        
        conn.commit()
        return conn

    def _load_websites(self) -> None:
        """Load websites from JSON file into database if not already present."""
        if not Path(WEBSITES_JSON).exists():
            raise FileNotFoundError(f"Website data file {WEBSITES_JSON} not found")
        
        with open(WEBSITES_JSON, 'r') as f:
            websites_data = json.load(f)
        
        cursor = self.db_conn.cursor()
        
        # Check if websites are already loaded
        cursor.execute("SELECT COUNT(*) FROM websites")
        if cursor.fetchone()[0] == 0:
            for website_data in websites_data:
                website = Website(**website_data)
                self._add_website_to_db(website)

    def _add_website_to_db(self, website: Website) -> None:
        """Add a website to the database."""
        cursor = self.db_conn.cursor()
        
        try:
            # Insert website
            cursor.execute(
                "INSERT INTO websites VALUES (?, ?, ?, ?)",
                (website.url, website.title, website.description, website.rating)
            )
            
            # Insert categories
            for category in website.categories:
                cursor.execute(
                    "INSERT INTO website_categories VALUES (?, ?)",
                    (website.url, category)
                )
            
            self.db_conn.commit()
        except sqlite3.IntegrityError:
            self.db_conn.rollback()
            raise ValueError(f"Website with URL {website.url} already exists")

    def _load_user_preferences(self) -> Dict[str, float]:
        """Load user preferences from file or initialize defaults."""
        if Path(USER_PREFERENCES_FILE).exists():
            with open(USER_PREFERENCES_FILE, 'r') as f:
                return json.load(f)
        return {}

    def save_user_preferences(self) -> None:
        """Save user preferences to file."""
        with open(USER_PREFERENCES_FILE, 'w') as f:
            json.dump(self.user_preferences, f, indent=2)

    def update_preference(self, category: str, weight: float) -> None:
        """Update user preference for a category."""
        if not 0 <= weight <= 1:
            raise ValueError("Weight must be between 0 and 1")
        
        self.user_preferences[category] = weight
        self.save_user_preferences()
        
        # Also update in database
        cursor = self.db_conn.cursor()
        cursor.execute(
            "INSERT OR REPLACE INTO user_preferences VALUES (?, ?)",
            (category, weight)
        )
        self.db_conn.commit()

    def get_recommendation(self) -> Optional[Website]:
        """Get a website recommendation based on user preferences."""
        cursor = self.db_conn.cursor()
        
        # Get all websites with their categories
        cursor.execute('''
            SELECT w.url, w.title, w.description, w.rating, GROUP_CONCAT(wc.category, ',')
            FROM websites w
            JOIN website_categories wc ON w.url = wc.url
            GROUP BY w.url
        ''')
        
        websites = []
        for row in cursor.fetchall():
            url, title, description, rating, categories_str = row
            categories = categories_str.split(',')
            websites.append(Website(url, title, description, categories, rating))
        
        if not websites:
            return None
        
        # Filter and weight websites based on preferences
        if self.user_preferences:
            weighted_websites = []
            for website in websites:
                weight = 0.0
                for category in website.categories:
                    if category in self.user_preferences:
                        weight += self.user_preferences[category]
                
                if weight > 0:
                    weighted_websites.append((website, weight))
            
            if weighted_websites:
                # Select based on weights
                websites, weights = zip(*weighted_websites)
                return random.choices(websites, weights=weights, k=1)[0]
        
        # Fallback to random selection if no preferences or no matches
        return random.choice(websites)

    def rate_website(self, url: str, rating: float) -> None:
        """Rate a website and update its rating in the database."""
        if not 0 <= rating <= 5:
            raise ValueError("Rating must be between 0 and 5")
        
        cursor = self.db_conn.cursor()
        cursor.execute(
            "UPDATE websites SET rating = ? WHERE url = ?",
            (rating, url)
        )
        self.db_conn.commit()

    def close(self) -> None:
        """Close the database connection."""
        self.db_conn.close()

# Example usage
if __name__ == "__main__":
    # Initialize system
    stumble = StumbleSystem()
    
    # Set some preferences
    stumble.update_preference("technology", 0.8)
    stumble.update_preference("science", 0.6)
    stumble.update_preference("news", 0.4)
    
    # Get recommendations
    for _ in range(5):
        recommendation = stumble.get_recommendation()
        if recommendation:
            print(f"Recommended: {recommendation.title} ({recommendation.url})")
            print(f"Categories: {', '.join(recommendation.categories)}")
            print(f"Description: {recommendation.description}\n")
    
    # Clean up
    stumble.close()
```
