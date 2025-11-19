"""
Generated Code Metadata:
========================
Original URL: https://www.nkatandiinyom.com
Prompt: Create a program that showcases the stories and traditions of Igbo women, similar to the cultural preservation efforts by Nkata ndi Inyom Igbo.
Generated: DETERMINISTIC_9872b6092027cd6f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Igbo Women's Stories and Traditions Preservation Program

This program showcases the stories, traditions, and cultural heritage of Igbo women,
inspired by the cultural preservation efforts of Nkata ndi Inyom Igbo.

Features:
- Database of stories and traditions
- Categorization by themes
- Search functionality
- User contributions
"""

import sqlite3
from typing import List, Dict, Optional
from dataclasses import dataclass
import textwrap
import sys

@dataclass
class Story:
    """Data class representing a cultural story or tradition"""
    id: int
    title: str
    content: str
    category: str
    contributor: str
    region: str
    language: str = "Igbo"

class CulturalDatabase:
    """Database handler for Igbo women's stories and traditions"""
    
    def __init__(self, db_name: str = "igbo_culture.db"):
        """Initialize database connection"""
        self.conn = sqlite3.connect(db_name)
        self._create_tables()
        
    def _create_tables(self) -> None:
        """Create necessary tables if they don't exist"""
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS stories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                category TEXT NOT NULL,
                contributor TEXT,
                region TEXT,
                language TEXT DEFAULT 'Igbo',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.conn.commit()
        
    def add_story(self, story: Story) -> int:
        """Add a new story to the database"""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO stories (title, content, category, contributor, region, language)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (story.title, story.content, story.category, story.contributor, story.region, story.language))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return -1
            
    def get_stories(self, category: Optional[str] = None, region: Optional[str] = None) -> List[Story]:
        """Retrieve stories with optional filters"""
        try:
            cursor = self.conn.cursor()
            query = "SELECT id, title, content, category, contributor, region, language FROM stories"
            params = []
            
            if category or region:
                query += " WHERE"
                conditions = []
                if category:
                    conditions.append(" category = ?")
                    params.append(category)
                if region:
                    conditions.append(" region = ?")
                    params.append(region)
                query += " AND".join(conditions)
                
            cursor.execute(query, params)
            return [Story(*row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []
            
    def get_categories(self) -> List[str]:
        """Get all unique categories"""
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT DISTINCT category FROM stories")
            return [row[0] for row in cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []
            
    def close(self) -> None:
        """Close database connection"""
        self.conn.close()

class CulturalPreservationApp:
    """Main application class for showcasing Igbo women's stories"""
    
    def __init__(self):
        self.db = CulturalDatabase()
        self.categories = self.db.get_categories()
        
    def display_menu(self) -> None:
        """Display main menu options"""
        print("\n" + "="*50)
        print("NKATA NDI INYOM IGBO CULTURAL PRESERVATION")
        print("="*50)
        print("1. Browse Stories by Category")
        print("2. Search Stories by Region")
        print("3. Contribute a Story")
        print("4. View All Stories")
        print("5. Exit")
        print("="*50)
        
    def browse_by_category(self) -> None:
        """Display stories by selected category"""
        print("\nAvailable Categories:")
        for i, category in enumerate(self.categories, 1):
            print(f"{i}. {category}")
            
        try:
            choice = int(input("\nSelect a category (number): "))
            if 1 <= choice <= len(self.categories):
                selected_category = self.categories[choice-1]
                stories = self.db.get_stories(category=selected_category)
                self._display_stories(stories, f"Stories in Category: {selected_category}")
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
            
    def search_by_region(self) -> None:
        """Search stories by region"""
        region = input("\nEnter region to search for: ").strip()
        if region:
            stories = self.db.get_stories(region=region)
            self._display_stories(stories, f"Stories from Region: {region}")
        else:
            print("Region cannot be empty.")
            
    def contribute_story(self) -> None:
        """Allow user to contribute a new story"""
        print("\nContribute a New Story")
        print("="*30)
        
        title = input("Title: ").strip()
        content = input("Story/Tradition Content: ").strip()
        category = input("Category (e.g., Folktale, Rite of Passage, Proverbs): ").strip()
        contributor = input("Your Name (optional): ").strip() or "Anonymous"
        region = input("Region (optional): ").strip() or "Unknown"
        
        if not title or not content or not category:
            print("Title, content, and category are required.")
            return
            
        story = Story(
            id=0,
            title=title,
            content=content,
            category=category,
            contributor=contributor,
            region=region
        )
        
        story_id = self.db.add_story(story)
        if story_id > 0:
            print("\nThank you for your contribution! Your story has been added.")
            if category not in self.categories:
                self.categories = self.db.get_categories()
        else:
            print("There was an error saving your story. Please try again.")
            
    def view_all_stories(self) -> None:
        """Display all stories in the database"""
        stories = self.db.get_stories()
        self._display_stories(stories, "All Stories")
        
    def _display_stories(self, stories: List[Story], header: str) -> None:
        """Helper method to display stories"""
        if not stories:
            print("\nNo stories found.")
            return
            
        print(f"\n{header}")
        print("="*50)
        
        for story in stories:
            print(f"\nTitle: {story.title}")
            print(f"Category: {story.category}")
            print(f"Region: {story.region}")
            print(f"Contributor: {story.contributor}")
            print("\nContent:")
            print(textwrap.fill(story.content, width=70))
            print("-"*50)
            
    def run(self) -> None:
        """Main application loop"""
        while True:
            self.display_menu()
            try:
                choice = input("\nEnter your choice (1-5): ").strip()
                
                if choice == "1":
                    self.browse_by_category()
                elif choice == "2":
                    self.search_by_region()
                elif choice == "3":
                    self.contribute_story()
                elif choice == "4":
                    self.view_all_stories()
                elif choice == "5":
                    print("\nDaalụ! Thank you for preserving Igbo culture.")
                    self.db.close()
                    sys.exit(0)
                else:
                    print("Invalid choice. Please enter a number between 1 and 5.")
                    
            except KeyboardInterrupt:
                print("\nProgram interrupted. Exiting gracefully.")
                self.db.close()
                sys.exit(0)
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Initialize and run the application
    app = CulturalPreservationApp()
    
    # Add some sample data if database is empty
    if not app.db.get_stories():
        sample_stories = [
            Story(0, "The Story of Mami Wata", 
                  "Mami Wata is a water spirit venerated in many Igbo communities...", 
                  "Folktale", "Nneka Eze", "Anambra"),
            Story(0, "Igbo Women's Council", 
                  "Traditionally, Igbo women had their own governing councils called...", 
                  "History", "Adaobi Nwosu", "Enugu"),
            Story(0, "Nkwa Nmiri Dance", 
                  "The water dance performed by maidens during the New Yam Festival...", 
                  "Dance", "Chinwe Okeke", "Abia")
        ]
        for story in sample_stories:
            app.db.add_story(story)
        app.c
