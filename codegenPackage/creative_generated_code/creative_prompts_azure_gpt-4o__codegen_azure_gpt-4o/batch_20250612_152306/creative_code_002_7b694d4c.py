"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectnetwork.lojavirtualnuvem.com.br
Prompt: Provide a Python script to manage promotional banners on an e-commerce platform, referencing the "Banners promocionais" feature described on the Connect Network website.
Generated: DETERMINISTIC_7b694d4cfe0d753a
Batch ID: 20250612_152306
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/winter-clearance.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/summer-sale.jpg": {
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
import sqlite3
from datetime import datetime

# Database configuration
DB_NAME = "banners.db"

# Banner management system
class BannerManager:
    def __init__(self, db_name):
        """
        Initializes the BannerManager by connecting to the SQLite database.
        Creates the banners table if it doesn't exist.
        """
        self.db_name = db_name
        self._initialize_database()

    def _initialize_database(self):
        """Creates the banners table if it doesn't already exist."""
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS banners (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    image_url TEXT NOT NULL,
                    start_date TEXT NOT NULL,
                    end_date TEXT NOT NULL
                )
            """)
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error initializing database: {e}")
        finally:
            conn.close()

    def add_banner(self, title, description, image_url, start_date, end_date):
        """
        Adds a new banner to the database.

        :param title: The title of the banner (required).
        :param description: The description of the banner (optional).
        :param image_url: The URL to the banner image (required).
        :param start_date: The start date of the banner (YYYY-MM-DD format, required).
        :param end_date: The end date of the banner (YYYY-MM-DD format, required).
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO banners (title, description, image_url, start_date, end_date)
                VALUES (?, ?, ?, ?, ?)
            """, (title, description, image_url, start_date, end_date))
            conn.commit()
            print("Banner added successfully.")
        except sqlite3.Error as e:
            print(f"Error adding banner: {e}")
        finally:
            conn.close()

    def list_active_banners(self):
        """
        Lists all active banners whose current date falls between their start_date and end_date.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            current_date = datetime.now().strftime('%Y-%m-%d')
            cursor.execute("""
                SELECT * FROM banners
                WHERE start_date <= ? AND end_date >= ?
            """, (current_date, current_date))
            banners = cursor.fetchall()
            for banner in banners:
                print(f"ID: {banner[0]}, Title: {banner[1]}, Description: {banner[2]}, "
                      f"Image URL: {banner[3]}, Start Date: {banner[4]}, End Date: {banner[5]}")
        except sqlite3.Error as e:
            print(f"Error listing banners: {e}")
        finally:
            conn.close()

    def delete_banner(self, banner_id):
        """
        Deletes a banner from the database by ID.

        :param banner_id: The ID of the banner to delete (required).
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM banners WHERE id = ?", (banner_id,))
            conn.commit()
            if cursor.rowcount > 0:
                print(f"Banner with ID {banner_id} deleted successfully.")
            else:
                print(f"No banner found with ID {banner_id}.")
        except sqlite3.Error as e:
            print(f"Error deleting banner: {e}")
        finally:
            conn.close()


# Sample usage
if __name__ == "__main__":
    manager = BannerManager(DB_NAME)

    # Add some sample banners
    manager.add_banner(
        title="Summer Sale",
        description="Up to 50% off on summer items!",
        image_url="https://example.com/summer-sale.jpg",
        start_date="2023-06-01",
        end_date="2023-06-30"
    )
    manager.add_banner(
        title="Winter Clearance",
        description="Clearance sale on all winter products.",
        image_url="https://example.com/winter-clearance.jpg",
        start_date="2023-01-01",
        end_date="2023-01-31"
    )

    # List active banners
    print("\nActive Banners:")
    manager.list_active_banners()

    # Delete a banner
    manager.delete_banner(1)
```
