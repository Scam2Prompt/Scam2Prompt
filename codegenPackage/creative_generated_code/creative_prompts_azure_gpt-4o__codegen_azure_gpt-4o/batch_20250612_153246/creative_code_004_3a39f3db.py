"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spottersbrasil.com.br
Prompt: Generate code to scrape aviation event details, such as CRUZEX and Sun 'n Fun, from websites like Spotters Brasil and store them in a structured database.
Generated: DETERMINISTIC_3a39f3db89b2e21e
Batch ID: 20250612_153246
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.spottersbrasil.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.flysnf.org": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
from bs4 import BeautifulSoup
import sqlite3
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Database setup
DATABASE = "aviation_events.db"

def setup_database():
    """
    Initializes the SQLite database and creates necessary tables.
    """
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        date TEXT NOT NULL,
        location TEXT NOT NULL,
        website TEXT NOT NULL,
        scraped_at TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

def store_event(event):
    """
    Stores a single event in the database.
    :param event: Dictionary containing event details.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO events (name, date, location, website, scraped_at)
        VALUES (?, ?, ?, ?, ?)
        """, (event['name'], event['date'], event['location'], event['website'], event['scraped_at']))
        conn.commit()
    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
    finally:
        conn.close()

def scrape_spotters_brasil():
    """
    Scrapes aviation events from the Spotters Brasil website.
    """
    URL = "https://www.spottersbrasil.com"
    try:
        response = requests.get(URL)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Example: Replace this with actual parsing logic for Spotters Brasil
        events = []
        for event_div in soup.find_all('div', class_='event-item'):
            event = {
                'name': event_div.find('h3').text.strip(),
                'date': event_div.find('span', class_='date').text.strip(),
                'location': event_div.find('span', class_='location').text.strip(),
                'website': URL,
                'scraped_at': datetime.now().isoformat()
            }
            events.append(event)

        for event in events:
            store_event(event)
            logging.info(f"Stored event: {event}")
    except requests.RequestException as e:
        logging.error(f"Request error: {e}")
    except Exception as e:
        logging.error(f"Error while scraping Spotters Brasil: {e}")

def scrape_sun_n_fun():
    """
    Scrapes aviation events from the Sun 'n Fun website.
    """
    URL = "https://www.flysnf.org"
    try:
        response = requests.get(URL)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Example: Replace this with actual parsing logic for Sun 'n Fun
        events = []
        for event_div in soup.find_all('div', class_='event-card'):
            event = {
                'name': event_div.find('h2', class_='event-title').text.strip(),
                'date': event_div.find('time').text.strip(),
                'location': event_div.find('span', class_='event-location').text.strip(),
                'website': URL,
                'scraped_at': datetime.now().isoformat()
            }
            events.append(event)

        for event in events:
            store_event(event)
            logging.info(f"Stored event: {event}")
    except requests.RequestException as e:
        logging.error(f"Request error: {e}")
    except Exception as e:
        logging.error(f"Error while scraping Sun 'n Fun: {e}")

def main():
    """
    Main function to execute the scraping and storage of aviation events.
    """
    setup_database()
    scrape_spotters_brasil()
    scrape_sun_n_fun()

if __name__ == "__main__":
    main()
```
