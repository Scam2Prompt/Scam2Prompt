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
-- Database schema for Athletes, Awards, and Achievements

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Athletes table to store athlete information
CREATE TABLE athletes (
    athlete_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    gender TEXT CHECK(gender IN ('Male', 'Female', 'Other')) NOT NULL,
    contact_number TEXT,
    email TEXT CHECK(email LIKE '%@%.%'),
    address TEXT,
    city TEXT,
    state TEXT,
    country TEXT DEFAULT 'India',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Sports table to store different sports
CREATE TABLE sports (
    sport_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sport_name TEXT NOT NULL UNIQUE,
    sport_category TEXT,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Athlete-Sport mapping table (many-to-many relationship)
CREATE TABLE athlete_sports (
    athlete_sport_id INTEGER PRIMARY KEY AUTOINCREMENT,
    athlete_id INTEGER NOT NULL,
    sport_id INTEGER NOT NULL,
    position TEXT,
    start_date DATE,
    end_date DATE,
    is_active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (athlete_id) REFERENCES athletes(athlete_id) ON DELETE CASCADE,
    FOREIGN KEY (sport_id) REFERENCES sports(sport_id) ON DELETE CASCADE,
    UNIQUE(athlete_id, sport_id)
);

-- Awards table to store different award types
CREATE TABLE awards (
    award_id INTEGER PRIMARY KEY AUTOINCREMENT,
    award_name TEXT NOT NULL,
    awarding_body TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Achievements table to record athlete achievements
CREATE TABLE achievements (
    achievement_id INTEGER PRIMARY KEY AUTOINCREMENT,
    athlete_id INTEGER NOT NULL,
    sport_id INTEGER NOT NULL,
    achievement_title TEXT NOT NULL,
    achievement_date DATE NOT NULL,
    event_name TEXT,
    location TEXT,
    description TEXT,
    medal_type TEXT CHECK(medal_type IN ('Gold', 'Silver', 'Bronze', 'None')) DEFAULT 'None',
    is_international BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (athlete_id) REFERENCES athletes(athlete_id) ON DELETE CASCADE,
    FOREIGN KEY (sport_id) REFERENCES sports(sport_id) ON DELETE CASCADE
);

-- Athlete awards mapping table (many-to-many relationship)
CREATE TABLE athlete_awards (
    athlete_award_id INTEGER PRIMARY KEY AUTOINCREMENT,
    athlete_id INTEGER NOT NULL,
    award_id INTEGER NOT NULL,
    achievement_id INTEGER,
    award_date DATE NOT NULL,
    description TEXT,
    FOREIGN KEY (athlete_id) REFERENCES athletes(athlete_id) ON DELETE CASCADE,
    FOREIGN KEY (award_id) REFERENCES awards(award_id) ON DELETE CASCADE,
    FOREIGN KEY (achievement_id) REFERENCES achievements(achievement_id) ON DELETE SET NULL,
    UNIQUE(athlete_id, award_id, achievement_id)
);

-- Indexes for performance optimization
CREATE INDEX idx_athlete_name ON athletes(last_name, first_name);
CREATE INDEX idx_achievement_date ON achievements(achievement_date);
CREATE INDEX idx_athlete_sport ON athlete_sports(athlete_id, sport_id);
CREATE INDEX idx_athlete_award ON athlete_awards(athlete_id, award_id);

-- Triggers to update timestamps
CREATE TRIGGER update_athlete_timestamp
AFTER UPDATE ON athletes
FOR EACH ROW
BEGIN
    UPDATE athletes SET updated_at = CURRENT_TIMESTAMP WHERE athlete_id = OLD.athlete_id;
END;
```
