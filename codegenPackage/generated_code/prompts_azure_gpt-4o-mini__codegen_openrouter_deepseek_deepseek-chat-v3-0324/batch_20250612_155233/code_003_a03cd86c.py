"""
Generated Code Metadata:
========================
Original URL: https://afco-federation.fr
Prompt: How can I implement a notification system for updates on SST regulations and best practices, similar to the collaborative efforts of the AFCO regional coordinators?
Generated: DETERMINISTIC_a03cd86c46ba1d01
Batch ID: 20250612_155233
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Dict, Optional
import requests
from bs4 import BeautifulSoup
import sqlite3
from threading import Timer
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('notification_system.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class NotificationSystem:
    def __init__(self, config_path: str = 'config.json'):
        """
        Initialize the notification system with configuration.
        
        Args:
            config_path: Path to configuration file
        """
        self.config = self._load_config(config_path)
        self.db_conn = self._init_db()
        self._setup_email_server()
        
    def _load_config(self, config_path: str) -> Dict:
        """
        Load configuration from JSON file.
        
        Args:
            config_path: Path to config file
            
        Returns:
            Dictionary containing configuration
            
        Raises:
            FileNotFoundError: If config file doesn't exist
            json.JSONDecodeError: If config is invalid JSON
        """
        try:
            with open(config_path) as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"Config file not found at {config_path}")
            raise
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in config file: {e}")
            raise
    
    def _init_db(self) -> sqlite3.Connection:
        """
        Initialize SQLite database for storing subscribers and updates.
        
        Returns:
            SQLite database connection
        """
        db_path = self.config.get('database_path', 'notifications.db')
        conn = sqlite3.connect(db_path)
        
        # Create tables if they don't exist
        with conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS subscribers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email TEXT UNIQUE NOT NULL,
                    name TEXT,
                    region TEXT,
                    subscribed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            conn.execute('''
                CREATE TABLE IF NOT EXISTS updates (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    content TEXT NOT NULL,
                    source_url TEXT,
                    published_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    is_notified BOOLEAN DEFAULT 0
                )
            ''')
            
            conn.execute('''
                CREATE TABLE IF NOT EXISTS subscriptions (
                    subscriber_id INTEGER,
                    update_id INTEGER,
                    FOREIGN KEY(subscriber_id) REFERENCES subscribers(id),
                    FOREIGN KEY(update_id) REFERENCES updates(id),
                    PRIMARY KEY(subscriber_id, update_id)
                )
            ''')
        
        return conn
    
    def _setup_email_server(self):
        """Initialize SMTP server connection."""
        self.smtp_server = self.config['smtp']['server']
        self.smtp_port = self.config['smtp']['port']
        self.smtp_username = self.config['smtp']['username']
        self.smtp_password = self.config['smtp']['password']
        self.from_email = self.config['smtp']['from_email']
        
    def add_subscriber(self, email: str, name: Optional[str] = None, region: Optional[str] = None) -> bool:
        """
        Add a new subscriber to the notification system.
        
        Args:
            email: Subscriber's email address
            name: Subscriber's name (optional)
            region: Subscriber's region (optional)
            
        Returns:
            True if subscriber was added, False if already exists
        """
        try:
            with self.db_conn:
                cursor = self.db_conn.execute(
                    'INSERT INTO subscribers (email, name, region) VALUES (?, ?, ?)',
                    (email, name, region)
                )
                return cursor.rowcount > 0
        except sqlite3.IntegrityError:
            logger.info(f"Subscriber {email} already exists")
            return False
    
    def remove_subscriber(self, email: str) -> bool:
        """
        Remove a subscriber from the notification system.
        
        Args:
            email: Subscriber's email address
            
        Returns:
            True if subscriber was removed, False if not found
        """
        with self.db_conn:
            cursor = self.db_conn.execute(
                'DELETE FROM subscribers WHERE email = ?',
                (email,)
            )
            return cursor.rowcount > 0
    
    def fetch_regulatory_updates(self):
        """
        Fetch regulatory updates from configured sources.
        """
        updates = []
        
        for source in self.config['sources']:
            try:
                if source['type'] == 'rss':
                    updates.extend(self._parse_rss(source['url']))
                elif source['type'] == 'web':
                    updates.extend(self._scrape_website(source['url'], source.get('selectors')))
            except Exception as e:
                logger.error(f"Error fetching updates from {source['url']}: {e}")
                continue
        
        self._store_updates(updates)
    
    def _parse_rss(self, url: str) -> List[Dict]:
        """
        Parse RSS feed for updates.
        
        Args:
            url: RSS feed URL
            
        Returns:
            List of parsed updates
        """
        try:
            response = requests.get(url)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'xml')
            items = soup.find_all('item')
            
            updates = []
            for item in items:
                updates.append({
                    'title': item.title.text if item.title else 'No title',
                    'content': item.description.text if item.description else '',
                    'source_url': item.link.text if item.link else url,
                    'published_at': item.pubDate.text if item.pubDate else datetime.now().isoformat()
                })
            
            return updates
        except Exception as e:
            logger.error(f"Error parsing RSS feed {url}: {e}")
            return []
    
    def _scrape_website(self, url: str, selectors: Optional[Dict] = None) -> List[Dict]:
        """
        Scrape website for updates using CSS selectors.
        
        Args:
            url: Website URL
            selectors: Dictionary of CSS selectors for title, content, etc.
            
        Returns:
            List of scraped updates
        """
        if not selectors:
            selectors = {
                'title': 'h1',
                'content': 'article',
                'link': 'a'
            }
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            updates = []
            # This is a simplified example - actual implementation would depend on site structure
            articles = soup.select(selectors.get('container', 'article'))
            
            for article in articles:
                title = article.select_one(selectors['title']).text if article.select_one(selectors['title']) else 'No title'
                content = article.select_one(selectors['content']).text if article.select_one(selectors['content']) else ''
                link = article.select_one(selectors['link'])['href'] if article.select_one(selectors['link']) else url
                
                updates.append({
                    'title': title,
                    'content': content,
                    'source_url': link,
                    'published_at': datetime.now().isoformat()
                })
            
            return updates
        except Exception as e:
            logger.error(f"Error scraping website {url}: {e}")
            return []
    
    def _store_updates(self, updates: List[Dict]):
        """
        Store new updates in the database.
        
        Args:
            updates: List of update dictionaries
        """
        with self.db_conn:
            for update in updates:
                # Check if update already exists
                cursor = self.db_conn.execute(
                    'SELECT id FROM updates WHERE title = ? AND source_url = ?',
                    (update['title'], update['source_url'])
                )
                
                if not cursor.fetchone():
                    self.db_conn.execute(
                        '''INSERT INTO updates 
                        (title, content, source_url, published_at) 
                        VALUES (?, ?, ?, ?)''',
                        (update['title'], update['content'], update['source_url'], update['published_at'])
                    )
    
    def send_notifications(self):
        """
        Send notifications for new updates to all subscribers.
        """
        # Get new updates that haven't been notified yet
        with self.db_conn:
            cursor = self.db_conn.execute(
                'SELECT id, title, content, source_url FROM updates WHERE is_notified = 0'
            )
            new_updates = cursor.fetchall()
            
            if not new_updates:
                logger.info("No new updates to notify")
                return
            
            # Get all subscribers
            cursor = self.db_conn.execute('SELECT id, email, name FROM subscribers')
            subscribers = cursor.fetchall()
            
            if not subscribers:
                logger.info("No subscribers to notify")
                return
            
            # Send notifications
            for update_id, title, content
