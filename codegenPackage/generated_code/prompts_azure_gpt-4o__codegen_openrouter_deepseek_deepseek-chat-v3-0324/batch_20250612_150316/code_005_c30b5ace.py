"""
Generated Code Metadata:
========================
Original URL: https://jobbo.com.au
Prompt: Develop a script to track and display historical tractor pulling data, including team history and event results, as seen on jobbo.com.au.
Generated: DETERMINISTIC_c30b5ace139f64c9
Batch ID: 20250612_150316
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

class TractorPullingDatabase:
    """Database handler for tractor pulling historical data."""
    
    def __init__(self, db_path: str = "tractor_pulling.db"):
        """Initialize database connection and create tables if they don't exist."""
        self.conn = sqlite3.connect(db_path)
        self._create_tables()
    
    def _create_tables(self) -> None:
        """Create necessary tables if they don't exist."""
        cursor = self.conn.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS teams (
            team_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            country TEXT,
            founded_year INTEGER,
            active BOOLEAN DEFAULT 1
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS events (
            event_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location TEXT NOT NULL,
            date DATE NOT NULL,
            season TEXT NOT NULL
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS results (
            result_id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_id INTEGER NOT NULL,
            team_id INTEGER NOT NULL,
            position INTEGER NOT NULL,
            distance REAL,
            notes TEXT,
            FOREIGN KEY (event_id) REFERENCES events (event_id),
            FOREIGN KEY (team_id) REFERENCES teams (team_id)
        )
        """)
        
        self.conn.commit()
    
    def add_team(self, name: str, country: str = None, founded_year: int = None, active: bool = True) -> int:
        """Add a new team to the database."""
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO teams (name, country, founded_year, active) VALUES (?, ?, ?, ?)",
                (name, country, founded_year, active)
            )
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding team: {e}")
            return -1
    
    def add_event(self, name: str, location: str, date: str, season: str) -> int:
        """Add a new event to the database."""
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO events (name, location, date, season) VALUES (?, ?, ?, ?)",
                (name, location, date, season)
            )
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding event: {e}")
            return -1
    
    def add_result(self, event_id: int, team_id: int, position: int, distance: float = None, notes: str = None) -> int:
        """Add a result for an event."""
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO results (event_id, team_id, position, distance, notes) VALUES (?, ?, ?, ?, ?)",
                (event_id, team_id, position, distance, notes)
            )
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding result: {e}")
            return -1
    
    def get_team_history(self, team_id: int) -> List[Dict]:
        """Get all results for a specific team."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                SELECT e.name, e.location, e.date, e.season, r.position, r.distance, r.notes
                FROM results r
                JOIN events e ON r.event_id = e.event_id
                WHERE r.team_id = ?
                ORDER BY e.date DESC
            """, (team_id,))
            
            results = []
            for row in cursor.fetchall():
                results.append({
                    "event_name": row[0],
                    "location": row[1],
                    "date": row[2],
                    "season": row[3],
                    "position": row[4],
                    "distance": row[5],
                    "notes": row[6]
                })
            return results
        except sqlite3.Error as e:
            print(f"Error fetching team history: {e}")
            return []
    
    def get_event_results(self, event_id: int) -> List[Dict]:
        """Get all results for a specific event."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                SELECT t.name, r.position, r.distance, r.notes
                FROM results r
                JOIN teams t ON r.team_id = t.team_id
                WHERE r.event_id = ?
                ORDER BY r.position
            """, (event_id,))
            
            results = []
            for row in cursor.fetchall():
                results.append({
                    "team_name": row[0],
                    "position": row[1],
                    "distance": row[2],
                    "notes": row[3]
                })
            return results
        except sqlite3.Error as e:
            print(f"Error fetching event results: {e}")
            return []
    
    def search_teams(self, name: str = None, country: str = None, active: bool = None) -> List[Dict]:
        """Search for teams based on criteria."""
        try:
            cursor = self.conn.cursor()
            query = "SELECT team_id, name, country, founded_year, active FROM teams WHERE 1=1"
            params = []
            
            if name:
                query += " AND name LIKE ?"
                params.append(f"%{name}%")
            if country:
                query += " AND country = ?"
                params.append(country)
            if active is not None:
                query += " AND active = ?"
                params.append(active)
            
            cursor.execute(query, params)
            
            teams = []
            for row in cursor.fetchall():
                teams.append({
                    "team_id": row[0],
                    "name": row[1],
                    "country": row[2],
                    "founded_year": row[3],
                    "active": bool(row[4])
                })
            return teams
        except sqlite3.Error as e:
            print(f"Error searching teams: {e}")
            return []
    
    def search_events(self, name: str = None, location: str = None, season: str = None, 
                     date_from: str = None, date_to: str = None) -> List[Dict]:
        """Search for events based on criteria."""
        try:
            cursor = self.conn.cursor()
            query = "SELECT event_id, name, location, date, season FROM events WHERE 1=1"
            params = []
            
            if name:
                query += " AND name LIKE ?"
                params.append(f"%{name}%")
            if location:
                query += " AND location LIKE ?"
                params.append(f"%{location}%")
            if season:
                query += " AND season = ?"
                params.append(season)
            if date_from:
                query += " AND date >= ?"
                params.append(date_from)
            if date_to:
                query += " AND date <= ?"
                params.append(date_to)
            
            query += " ORDER BY date DESC"
            cursor.execute(query, params)
            
            events = []
            for row in cursor.fetchall():
                events.append({
                    "event_id": row[0],
                    "name": row[1],
                    "location": row[2],
                    "date": row[3],
                    "season": row[4]
                })
            return events
        except sqlite3.Error as e:
            print(f"Error searching events: {e}")
            return []
    
    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()

class TractorPullingCLI:
    """Command-line interface for interacting with tractor pulling data."""
    
    def __init__(self):
        self.db = TractorPullingDatabase()
    
    def display_menu(self) -> None:
        """Display the main menu."""
        print("\nTractor Pulling Historical Data Tracker")
        print("1. Add Team")
        print("2. Add Event")
        print("3. Add Result")
        print("4. View Team History")
        print("5. View Event Results")
        print("6. Search Teams")
        print("7. Search Events")
        print("8. Exit")
    
    def run(self) -> None:
        """Run the CLI application."""
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-8): ")
            
            try:
                if choice == "1":
                    self._add_team()
                elif choice == "2":
                    self._add_event()
                elif choice == "3":
                    self._add_result()
                elif choice == "4":
                    self._view_team_history()
                elif choice == "5":
                    self._view_event_results()
                elif choice == "6":
                    self._search_teams()
                elif choice == "7":
                    self._search_events()
                elif choice == "8":
                    print("Exiting...")
                    self.db.close()
                    break
                else:
                    print("Invalid choice. Please try again
