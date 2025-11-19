"""
Generated Code Metadata:
========================
Original URL: https://meetagreatamerican.com
Prompt: Develop a database schema for storing information about selectees, including their biographies and achievements, inspired by "Meet A Great American."
Generated: DETERMINISTIC_a9ccd37683e81d8d
Batch ID: 20250612_145213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about selectees, their biographies, and achievements

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Table for storing selectee information
CREATE TABLE IF NOT EXISTS selectees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    birth_date DATE,
    death_date DATE,
    birth_place TEXT,
    occupation TEXT NOT NULL,
    era TEXT,
    image_url TEXT,
    summary TEXT NOT NULL,
    is_featured BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(first_name, last_name, birth_date)
);

-- Table for storing detailed biographies
CREATE TABLE IF NOT EXISTS biographies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    selectee_id INTEGER NOT NULL,
    content TEXT NOT NULL,
    author TEXT,
    source TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (selectee_id) REFERENCES selectees(id) ON DELETE CASCADE
);

-- Table for storing achievements
CREATE TABLE IF NOT EXISTS achievements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    selectee_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    year INTEGER,
    significance TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (selectee_id) REFERENCES selectees(id) ON DELETE CASCADE
);

-- Table for storing categories/tags for selectees
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Junction table for selectee-category many-to-many relationship
CREATE TABLE IF NOT EXISTS selectee_categories (
    selectee_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    PRIMARY KEY (selectee_id, category_id),
    FOREIGN KEY (selectee_id) REFERENCES selectees(id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
);

-- Table for storing quotes by or about selectees
CREATE TABLE IF NOT EXISTS quotes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    selectee_id INTEGER NOT NULL,
    quote_text TEXT NOT NULL,
    source TEXT,
    context TEXT,
    is_by_selectee BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (selectee_id) REFERENCES selectees(id) ON DELETE CASCADE
);

-- Table for storing multimedia references
CREATE TABLE IF NOT EXISTS multimedia (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    selectee_id INTEGER NOT NULL,
    url TEXT NOT NULL,
    media_type TEXT NOT NULL CHECK(media_type IN ('image', 'video', 'audio', 'document')),
    caption TEXT,
    source TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (selectee_id) REFERENCES selectees(id) ON DELETE CASCADE
);

-- Trigger to update the updated_at timestamp when selectee data is modified
CREATE TRIGGER IF NOT EXISTS update_selectee_timestamp
AFTER UPDATE ON selectees
FOR EACH ROW
BEGIN
    UPDATE selectees SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

-- Trigger to update the updated_at timestamp when biography data is modified
CREATE TRIGGER IF NOT EXISTS update_biography_timestamp
AFTER UPDATE ON biographies
FOR EACH ROW
BEGIN
    UPDATE biographies SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

-- Trigger to update the updated_at timestamp when achievement data is modified
CREATE TRIGGER IF NOT EXISTS update_achievement_timestamp
AFTER UPDATE ON achievements
FOR EACH ROW
BEGIN
    UPDATE achievements SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

-- Indexes for improved query performance
CREATE INDEX IF NOT EXISTS idx_selectee_name ON selectees(last_name, first_name);
CREATE INDEX IF NOT EXISTS idx_selectee_occupation ON selectees(occupation);
CREATE INDEX IF NOT EXISTS idx_selectee_era ON selectees(era);
CREATE INDEX IF NOT EXISTS idx_achievement_year ON achievements(year);
CREATE INDEX IF NOT EXISTS idx_biography_selectee ON biographies(selectee_id);
CREATE INDEX IF NOT EXISTS idx_achievement_selectee ON achievements(selectee_id);
CREATE INDEX IF NOT EXISTS idx_quote_selectee ON quotes(selectee_id);
CREATE INDEX IF NOT EXISTS idx_multimedia_selectee ON multimedia(selectee_id);
```
