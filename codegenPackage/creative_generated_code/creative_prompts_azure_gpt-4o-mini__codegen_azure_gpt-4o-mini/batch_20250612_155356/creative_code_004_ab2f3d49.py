"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://treehousesessions.co.uk
Prompt: Design a database schema for storing artist profiles and performance history for Tree House Sessions, ensuring it captures unique attributes mentioned in the content.
Generated: DETERMINISTIC_ab2f3d4907d1c0d9
Batch ID: 20250612_155356
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "http://echo.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://facebook.com/echo": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://twitter.com/echo": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for Tree House Sessions

-- Create the database
CREATE DATABASE tree_house_sessions;

-- Use the created database
USE tree_house_sessions;

-- Table to store artist profiles
CREATE TABLE artists (
    artist_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    genre VARCHAR(50),
    bio TEXT,
    contact_email VARCHAR(100),
    website VARCHAR(100),
    social_media_links JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store performance history
CREATE TABLE performances (
    performance_id INT AUTO_INCREMENT PRIMARY KEY,
    artist_id INT NOT NULL,
    performance_date DATETIME NOT NULL,
    venue VARCHAR(100) NOT NULL,
    location VARCHAR(100),
    ticket_price DECIMAL(10, 2),
    audience_size INT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id) ON DELETE CASCADE
);

-- Table to store performance setlist
CREATE TABLE setlists (
    setlist_id INT AUTO_INCREMENT PRIMARY KEY,
    performance_id INT NOT NULL,
    song_title VARCHAR(200) NOT NULL,
    song_order INT NOT NULL,
    duration TIME,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (performance_id) REFERENCES performances(performance_id) ON DELETE CASCADE
);

-- Table to store artist ratings
CREATE TABLE artist_ratings (
    rating_id INT AUTO_INCREMENT PRIMARY KEY,
    artist_id INT NOT NULL,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    review TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id) ON DELETE CASCADE
);

-- Indexes to improve query performance
CREATE INDEX idx_artist_name ON artists(name);
CREATE INDEX idx_performance_date ON performances(performance_date);
CREATE INDEX idx_artist_rating ON artist_ratings(artist_id);

-- Sample insert statements for initial data
INSERT INTO artists (name, genre, bio, contact_email, website, social_media_links)
VALUES
('The Echo Band', 'Rock', 'A local rock band with a passion for live performances.', 'contact@echo.com', 'http://echo.com', '{"facebook": "http://facebook.com/echo", "twitter": "http://twitter.com/echo"}');

INSERT INTO performances (artist_id, performance_date, venue, location, ticket_price, audience_size, notes)
VALUES
(1, '2023-10-01 19:00:00', 'Tree House Venue', 'Los Angeles, CA', 25.00, 150, 'Opening act for the local festival.');

INSERT INTO setlists (performance_id, song_title, song_order, duration)
VALUES
(1, 'Opening Song', 1, '00:04:30'),
(1, 'Mid Song', 2, '00:05:00'),
(1, 'Closing Song', 3, '00:06:00');

INSERT INTO artist_ratings (artist_id, rating, review)
VALUES
(1, 5, 'Amazing performance! Highly recommend.');
```
