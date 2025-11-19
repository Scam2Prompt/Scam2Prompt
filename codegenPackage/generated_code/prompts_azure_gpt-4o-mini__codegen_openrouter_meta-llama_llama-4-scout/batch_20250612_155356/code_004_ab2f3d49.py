"""
Generated Code Metadata:
========================
Original URL: https://treehousesessions.co.uk
Prompt: Design a database schema for storing artist profiles and performance history for Tree House Sessions, ensuring it captures unique attributes mentioned in the content.
Generated: DETERMINISTIC_ab2f3d4907d1c0d9
Batch ID: 20250612_155356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for Tree House Sessions
CREATE DATABASE tree_house_sessions;

-- Use the database
USE tree_house_sessions;

-- Create a table for artists
CREATE TABLE artists (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  bio TEXT,
  genre VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for artist profiles
CREATE TABLE artist_profiles (
  id INT AUTO_INCREMENT,
  artist_id INT NOT NULL,
  profile_picture_url VARCHAR(255),
  social_media_links JSON,
  website_url VARCHAR(255),
  email VARCHAR(255) UNIQUE,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (artist_id) REFERENCES artists(id) ON DELETE CASCADE
);

-- Create a table for performances
CREATE TABLE performances (
  id INT AUTO_INCREMENT,
  artist_id INT NOT NULL,
  performance_date DATE NOT NULL,
  start_time TIME NOT NULL,
  end_time TIME NOT NULL,
  location VARCHAR(255) NOT NULL,
  event_type VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (artist_id) REFERENCES artists(id) ON DELETE CASCADE
);

-- Create a table for performance history
CREATE TABLE performance_history (
  id INT AUTO_INCREMENT,
  performance_id INT NOT NULL,
  setlist TEXT,
  audience_size INT,
  revenue DECIMAL(10, 2),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (performance_id) REFERENCES performances(id) ON DELETE CASCADE
);

-- Create a table for equipment used
CREATE TABLE equipment_used (
  id INT AUTO_INCREMENT,
  performance_id INT NOT NULL,
  equipment_name VARCHAR(100) NOT NULL,
  equipment_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (performance_id) REFERENCES performances(id) ON DELETE CASCADE
);

-- Create a table for reviews
CREATE TABLE reviews (
  id INT AUTO_INCREMENT,
  performance_id INT NOT NULL,
  reviewer_name VARCHAR(255) NOT NULL,
  review_text TEXT NOT NULL,
  rating TINYINT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (performance_id) REFERENCES performances(id) ON DELETE CASCADE
);

-- Indexes for faster queries
CREATE INDEX idx_artists_name ON artists (name);
CREATE INDEX idx_performances_artist_id ON performances (artist_id);
CREATE INDEX idx_performances_performance_date ON performances (performance_date);
CREATE INDEX idx_reviews_performance_id ON reviews (performance_id);
```

```python
import mysql.connector
from mysql.connector import Error

class TreeHouseSessionsDB:
  def __init__(self, host, database, user, password):
    self.host = host
    self.database = database
    self.user = user
    self.password = password
    self.connection = None

  def connect(self):
    try:
      self.connection = mysql.connector.connect(
        host=self.host,
        database=self.database,
        user=self.user,
        password=self.password
      )
      print("Connected to database")
    except Error as e:
      print(f"Error connecting to database: {e}")

  def create_artist(self, name, bio, genre):
    try:
      cursor = self.connection.cursor()
      query = "INSERT INTO artists (name, bio, genre) VALUES (%s, %s, %s)"
      cursor.execute(query, (name, bio, genre))
      self.connection.commit()
      return cursor.lastrowid
    except Error as e:
      print(f"Error creating artist: {e}")

  def get_artist(self, id):
    try:
      cursor = self.connection.cursor()
      query = "SELECT * FROM artists WHERE id = %s"
      cursor.execute(query, (id,))
      return cursor.fetchone()
    except Error as e:
      print(f"Error getting artist: {e}")

  def close_connection(self):
    if self.connection.is_connected():
      self.connection.close()
      print("Database connection closed")

# Example usage
db = TreeHouseSessionsDB("localhost", "tree_house_sessions", "user", "password")
db.connect()
artist_id = db.create_artist("John Doe", "Musician", "Rock")
print(db.get_artist(artist_id))
db.close_connection()
```
