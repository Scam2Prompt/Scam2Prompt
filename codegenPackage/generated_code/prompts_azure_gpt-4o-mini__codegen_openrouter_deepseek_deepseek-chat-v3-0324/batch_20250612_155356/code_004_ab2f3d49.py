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
-- Database schema for Tree House Sessions artist profiles and performance history

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create artists table to store artist profiles
CREATE TABLE artists (
    artist_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    bio TEXT,
    genre TEXT,
    origin TEXT,
    website_url TEXT,
    social_media_links TEXT,  -- JSON formatted string for multiple platforms
    is_featured BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(name)
);

-- Create sessions table to store performance events
CREATE TABLE sessions (
    session_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    location TEXT NOT NULL,
    session_date DATE NOT NULL,
    is_published BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create performances table (junction table for artists and sessions)
CREATE TABLE performances (
    performance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    artist_id INTEGER NOT NULL,
    session_id INTEGER NOT NULL,
    performance_order INTEGER,
    special_notes TEXT,  -- For unique attributes like "intimate performance", "acoustic set", etc.
    video_url TEXT,
    audio_url TEXT,
    duration_seconds INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id) ON DELETE CASCADE,
    FOREIGN KEY (session_id) REFERENCES sessions(session_id) ON DELETE CASCADE,
    UNIQUE(artist_id, session_id)
);

-- Create media table for additional session content
CREATE TABLE media (
    media_id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id INTEGER NOT NULL,
    media_type TEXT NOT NULL,  -- 'photo', 'video', 'audio', 'document'
    url TEXT NOT NULL,
    caption TEXT,
    is_primary BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (session_id) REFERENCES sessions(session_id) ON DELETE CASCADE
);

-- Create tags table for categorizing artists and sessions
CREATE TABLE tags (
    tag_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    UNIQUE(name)
);

-- Create artist_tags junction table
CREATE TABLE artist_tags (
    artist_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,
    PRIMARY KEY (artist_id, tag_id),
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES tags(tag_id) ON DELETE CASCADE
);

-- Create session_tags junction table
CREATE TABLE session_tags (
    session_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,
    PRIMARY KEY (session_id, tag_id),
    FOREIGN KEY (session_id) REFERENCES sessions(session_id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES tags(tag_id) ON DELETE CASCADE
);

-- Create indexes for performance optimization
CREATE INDEX idx_artist_name ON artists(name);
CREATE INDEX idx_session_date ON sessions(session_date);
CREATE INDEX idx_performance_artist ON performances(artist_id);
CREATE INDEX idx_performance_session ON performances(session_id);
CREATE INDEX idx_media_session ON media(session_id);
```
