"""
Generated Code Metadata:
========================
Original URL: https://odishaolympic.org
Prompt: Design a database schema to store information about athletes, awards, and achievements, inspired by the Odisha Olympic Association's data.
Generated: DETERMINISTIC_ff175bcc6ae3f8a3
Batch ID: 20250622_211539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about athletes, awards, and achievements

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Achievements;
DROP TABLE IF EXISTS Awards;
DROP TABLE IF EXISTS Athletes;

-- Table to store information about athletes
CREATE TABLE Athletes (
    athlete_id SERIAL PRIMARY KEY, -- Unique identifier for each athlete
    name VARCHAR(100) NOT NULL, -- Name of the athlete
    date_of_birth DATE NOT NULL, -- Date of birth of the athlete
    gender VARCHAR(10) CHECK (gender IN ('Male', 'Female', 'Other')), -- Gender of the athlete
    sport VARCHAR(50) NOT NULL, -- Sport in which the athlete competes
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store information about awards
CREATE TABLE Awards (
    award_id SERIAL PRIMARY KEY, -- Unique identifier for each award
    award_name VARCHAR(100) NOT NULL, -- Name of the award
    award_type VARCHAR(50) NOT NULL, -- Type of the award (e.g., Gold, Silver, Bronze)
    year INT NOT NULL CHECK (year > 1900 AND year <= EXTRACT(YEAR FROM CURRENT_DATE)), -- Year the award was received
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store achievements linked to athletes and awards
CREATE TABLE Achievements (
    achievement_id SERIAL PRIMARY KEY, -- Unique identifier for each achievement
    athlete_id INT NOT NULL, -- Foreign key referencing the athlete
    award_id INT NOT NULL, -- Foreign key referencing the award
    event_name VARCHAR(100) NOT NULL, -- Name of the event where the achievement was made
    event_date DATE NOT NULL, -- Date of the event
    FOREIGN KEY (athlete_id) REFERENCES Athletes(athlete_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (award_id) REFERENCES Awards(award_id) ON DELETE CASCADE, -- Ensures referential integrity
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Indexes for faster querying
CREATE INDEX idx_athlete_name ON Athletes(name);
CREATE INDEX idx_award_year ON Awards(year);
CREATE INDEX idx_event_name ON Achievements(event_name);
```
