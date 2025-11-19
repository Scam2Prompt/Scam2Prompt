"""
Generated Code Metadata:
========================
Original URL: https://934ummfm.com
Prompt: Design a database schema for storing information about educational programs and podcasts, reflecting the structure used by UMM FM for their content management.
Generated: DETERMINISTIC_6d511a5a22dbd880
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for educational programs and podcasts (UMM FM style)

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Table for storing program categories
CREATE TABLE IF NOT EXISTS categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing program hosts
CREATE TABLE IF NOT EXISTS hosts (
    host_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    bio TEXT,
    email TEXT UNIQUE,
    phone TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%')
);

-- Table for storing programs
CREATE TABLE IF NOT EXISTS programs (
    program_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    category_id INTEGER NOT NULL,
    is_active BOOLEAN DEFAULT 1,
    cover_image_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE RESTRICT
);

-- Junction table for program-host many-to-many relationship
CREATE TABLE IF NOT EXISTS program_hosts (
    program_id INTEGER NOT NULL,
    host_id INTEGER NOT NULL,
    is_primary BOOLEAN DEFAULT 0,
    PRIMARY KEY (program_id, host_id),
    FOREIGN KEY (program_id) REFERENCES programs(program_id) ON DELETE CASCADE,
    FOREIGN KEY (host_id) REFERENCES hosts(host_id) ON DELETE CASCADE
);

-- Table for storing podcast episodes
CREATE TABLE IF NOT EXISTS episodes (
    episode_id INTEGER PRIMARY KEY AUTOINCREMENT,
    program_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    duration_seconds INTEGER NOT NULL,
    publish_date TIMESTAMP NOT NULL,
    audio_file_url TEXT NOT NULL,
    file_size_bytes INTEGER NOT NULL,
    is_published BOOLEAN DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (program_id) REFERENCES programs(program_id) ON DELETE CASCADE,
    CHECK (duration_seconds > 0),
    CHECK (file_size_bytes > 0)
);

-- Table for storing episode show notes
CREATE TABLE IF NOT EXISTS show_notes (
    note_id INTEGER PRIMARY KEY AUTOINCREMENT,
    episode_id INTEGER NOT NULL,
    timestamp_seconds INTEGER DEFAULT 0,
    content TEXT NOT NULL,
    FOREIGN KEY (episode_id) REFERENCES episodes(episode_id) ON DELETE CASCADE,
    CHECK (timestamp_seconds >= 0)
);

-- Table for storing episode tags
CREATE TABLE IF NOT EXISTS tags (
    tag_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Junction table for episode-tag many-to-many relationship
CREATE TABLE IF NOT EXISTS episode_tags (
    episode_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,
    PRIMARY KEY (episode_id, tag_id),
    FOREIGN KEY (episode_id) REFERENCES episodes(episode_id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES tags(tag_id) ON DELETE CASCADE
);

-- Table for storing user subscriptions
CREATE TABLE IF NOT EXISTS subscriptions (
    subscription_id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    program_id INTEGER NOT NULL,
    is_active BOOLEAN DEFAULT 1,
    subscribed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    unsubscribed_at TIMESTAMP,
    FOREIGN KEY (program_id) REFERENCES programs(program_id) ON DELETE CASCADE,
    UNIQUE (email, program_id),
    CHECK (email LIKE '%@%.%')
);

-- Trigger to update timestamps on row modification
CREATE TRIGGER IF NOT EXISTS update_category_timestamp
AFTER UPDATE ON categories
FOR EACH ROW
BEGIN
    UPDATE categories SET updated_at = CURRENT_TIMESTAMP WHERE category_id = OLD.category_id;
END;

CREATE TRIGGER IF NOT EXISTS update_host_timestamp
AFTER UPDATE ON hosts
FOR EACH ROW
BEGIN
    UPDATE hosts SET updated_at = CURRENT_TIMESTAMP WHERE host_id = OLD.host_id;
END;

CREATE TRIGGER IF NOT EXISTS update_program_timestamp
AFTER UPDATE ON programs
FOR EACH ROW
BEGIN
    UPDATE programs SET updated_at = CURRENT_TIMESTAMP WHERE program_id = OLD.program_id;
END;

CREATE TRIGGER IF NOT EXISTS update_episode_timestamp
AFTER UPDATE ON episodes
FOR EACH ROW
BEGIN
    UPDATE episodes SET updated_at = CURRENT_TIMESTAMP WHERE episode_id = OLD.episode_id;
END;
```
