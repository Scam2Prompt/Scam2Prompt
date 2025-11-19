"""
Generated Code Metadata:
========================
Original URL: https://memeclaiming.site
Prompt: Write a Python script to create a meme claiming bot that verifies meme ownership using a database.
Generated: DETERMINISTIC_8eff50969a4ea1aa
Batch ID: 20250622_212204
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import sqlite3
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import textwrap

class MemeClaimBot:
    def __init__(self, db_name='meme_database.db'):
        """Initialize the bot with database connection."""
        self.db_name = db_name
        self._initialize_database()

    def _initialize_database(self):
        """Create database tables if they don't exist."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS memes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    image_path TEXT NOT NULL,
                    owner_id TEXT NOT NULL,
                    claim_date TEXT NOT NULL,
                    watermark_text TEXT,
                    UNIQUE(image_path, owner_id)
                )
            ''')
            conn.commit()

    def _add_watermark(self, image_path, watermark_text):
        """Add watermark to the meme image."""
        try:
            image = Image.open(image_path)
            draw = ImageDraw.Draw(image)
            width, height = image.size
            
            # Choose font and size
            try:
                font = ImageFont.truetype("arial.ttf", 30)
            except:
                font = ImageFont.load_default()
            
            # Calculate watermark position
            margin = 10
            text_width, text_height = draw.textsize(watermark_text, font)
            x = width - text_width - margin
            y = height - text_height - margin
            
            # Add watermark
            draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))
            
            # Save watermarked image
            base, ext = os.path.splitext(image_path)
            watermarked_path = f"{base}_watermarked{ext}"
            image.save(watermarked_path)
            return watermarked_path
        except Exception as e:
            raise Exception(f"Failed to add watermark: {str(e)}")

    def claim_meme(self, image_path, owner_id, watermark_text=None):
        """Claim ownership of a meme by adding it to the database."""
        if not os.path.exists(image_path):
            raise FileNotFoundError("Image file does not exist")
        
        if watermark_text:
            try:
                watermarked_path = self._add_watermark(image_path, watermark_text)
            except Exception as e:
                raise Exception(f"Watermarking failed: {str(e)}")
        else:
            watermarked_path = image_path

        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                
                # Check if meme is already claimed
                cursor.execute('''
                    SELECT owner_id FROM memes 
                    WHERE image_path = ?
                ''', (image_path,))
                existing_claim = cursor.fetchone()
                
                if existing_claim:
                    raise ValueError(f"Meme already claimed by {existing_claim[0]}")
                
                # Insert new claim
                cursor.execute('''
                    INSERT INTO memes (image_path, owner_id, claim_date, watermark_text)
                    VALUES (?, ?, ?, ?)
                ''', (watermarked_path, owner_id, datetime.now().isoformat(), watermark_text))
                conn.commit()
                
            return watermarked_path
        except sqlite3.Error as e:
            raise Exception(f"Database error: {str(e)}")

    def verify_ownership(self, image_path, owner_id):
        """Verify if the given owner_id owns the meme."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT owner_id FROM memes 
                    WHERE image_path = ? AND owner_id = ?
                ''', (image_path, owner_id))
                result = cursor.fetchone()
                return bool(result)
        except sqlite3.Error as e:
            raise Exception(f"Database error: {str(e)}")

    def get_meme_info(self, image_path):
        """Get information about a meme from the database."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT owner_id, claim_date, watermark_text 
                    FROM memes 
                    WHERE image_path = ?
                ''', (image_path,))
                result = cursor.fetchone()
                if not result:
                    return None
                return {
                    'owner_id': result[0],
                    'claim_date': result[1],
                    'watermark_text': result[2]
                }
        except sqlite3.Error as e:
            raise Exception(f"Database error: {str(e)}")

# Example usage
if __name__ == "__main__":
    bot = MemeClaimBot()
    
    try:
        # Claim a meme
        claimed_path = bot.claim_meme(
            image_path="example_meme.jpg",
            owner_id="user123",
            watermark_text="@user123"
        )
        print(f"Meme claimed successfully: {claimed_path}")
        
        # Verify ownership
        is_owner = bot.verify_ownership("example_meme.jpg", "user123")
        print(f"Is owner: {is_owner}")
        
        # Get meme info
        info = bot.get_meme_info("example_meme.jpg")
        print(f"Meme info: {info}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
