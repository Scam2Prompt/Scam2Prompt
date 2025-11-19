"""
Generated Code Metadata:
========================
Original URL: https://www.predaiaarteenatura.eu
Prompt: Create a database schema to store information about the artists, exhibitions, and events organized by the Predaia Arte e Natura project.
Generated: DETERMINISTIC_545926cfb72c263c
Batch ID: 20250622_205211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Predaia Arte e Natura project

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Artists table
CREATE TABLE artists (
    artist_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    bio TEXT,
    nationality TEXT,
    birth_year INTEGER,
    website TEXT,
    email TEXT,
    phone TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (birth_year > 0 AND birth_year <= strftime('%Y', 'now'))
);

-- Exhibitions table
CREATE TABLE exhibitions (
    exhibition_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    location TEXT NOT NULL,
    curator TEXT,
    is_active BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (end_date >= start_date)
);

-- Events table
CREATE TABLE events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    event_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME,
    location TEXT NOT NULL,
    max_participants INTEGER,
    is_active BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (end_time IS NULL OR end_time > start_time),
    CHECK (max_participants IS NULL OR max_participants > 0)
);

-- Junction table for artists and exhibitions (many-to-many relationship)
CREATE TABLE artist_exhibitions (
    artist_id INTEGER NOT NULL,
    exhibition_id INTEGER NOT NULL,
    PRIMARY KEY (artist_id, exhibition_id),
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id) ON DELETE CASCADE,
    FOREIGN KEY (exhibition_id) REFERENCES exhibitions(exhibition_id) ON DELETE CASCADE
);

-- Junction table for artists and events (many-to-many relationship)
CREATE TABLE artist_events (
    artist_id INTEGER NOT NULL,
    event_id INTEGER NOT NULL,
    PRIMARY KEY (artist_id, event_id),
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id) ON DELETE CASCADE,
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE
);

-- Images table for exhibitions and events
CREATE TABLE media (
    media_id INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_type TEXT NOT NULL, -- 'exhibition' or 'event'
    entity_id INTEGER NOT NULL, -- exhibition_id or event_id
    file_path TEXT NOT NULL,
    caption TEXT,
    is_primary BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (entity_type IN ('exhibition', 'event'))
);

-- Create indexes for better performance
CREATE INDEX idx_artist_name ON artists(name);
CREATE INDEX idx_exhibition_dates ON exhibitions(start_date, end_date);
CREATE INDEX idx_event_dates ON events(event_date);
CREATE INDEX idx_media_entity ON media(entity_type, entity_id);
```
