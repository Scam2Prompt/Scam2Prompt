"""
Generated Code Metadata:
========================
Original URL: https://meetagreatamerican.com
Prompt: Design a database schema to store information about great Americans, including their biographies, achievements, and industry categories.
Generated: DETERMINISTIC_2bfe39745b4a1c4c
Batch ID: 20250622_205943
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about great Americans

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create industry categories table
CREATE TABLE IF NOT EXISTS industry_categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Create individuals table
CREATE TABLE IF NOT EXISTS individuals (
    individual_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    birth_date DATE,
    death_date DATE,
    birth_place TEXT,
    nationality TEXT DEFAULT 'American',
    overview TEXT,
    image_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(first_name, last_name, birth_date)
);

-- Create individual_category mapping table
CREATE TABLE IF NOT EXISTS individual_categories (
    individual_id INTEGER,
    category_id INTEGER,
    PRIMARY KEY (individual_id, category_id),
    FOREIGN KEY (individual_id) REFERENCES individuals(individual_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES industry_categories(category_id) ON DELETE CASCADE
);

-- Create achievements table
CREATE TABLE IF NOT EXISTS achievements (
    achievement_id INTEGER PRIMARY KEY AUTOINCREMENT,
    individual_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    year INTEGER,
    significance TEXT,
    FOREIGN KEY (individual_id) REFERENCES individuals(individual_id) ON DELETE CASCADE
);

-- Create biography_sections table
CREATE TABLE IF NOT EXISTS biography_sections (
    section_id INTEGER PRIMARY KEY AUTOINCREMENT,
    individual_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    section_order INTEGER NOT NULL,
    FOREIGN KEY (individual_id) REFERENCES individuals(individual_id) ON DELETE CASCADE
);

-- Create quotes table
CREATE TABLE IF NOT EXISTS quotes (
    quote_id INTEGER PRIMARY KEY AUTOINCREMENT,
    individual_id INTEGER NOT NULL,
    quote_text TEXT NOT NULL,
    context TEXT,
    year INTEGER,
    source TEXT,
    FOREIGN KEY (individual_id) REFERENCES individuals(individual_id) ON DELETE CASCADE
);

-- Create awards table
CREATE TABLE IF NOT EXISTS awards (
    award_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    founding_year INTEGER,
    website_url TEXT
);

-- Create individual_awards mapping table
CREATE TABLE IF NOT EXISTS individual_awards (
    individual_id INTEGER,
    award_id INTEGER,
    year_awarded INTEGER NOT NULL,
    reason TEXT,
    PRIMARY KEY (individual_id, award_id, year_awarded),
    FOREIGN KEY (individual_id) REFERENCES individuals(individual_id) ON DELETE CASCADE,
    FOREIGN KEY (award_id) REFERENCES awards(award_id) ON DELETE CASCADE
);

-- Create trigger to update timestamp on individual updates
CREATE TRIGGER IF NOT EXISTS update_individual_timestamp
AFTER UPDATE ON individuals
BEGIN
    UPDATE individuals SET updated_at = CURRENT_TIMESTAMP WHERE individual_id = NEW.individual_id;
END;

-- Create indexes for performance
CREATE INDEX IF NOT EXISTS idx_individuals_name ON individuals(last_name, first_name);
CREATE INDEX IF NOT EXISTS idx_achievements_individual ON achievements(individual_id);
CREATE INDEX IF NOT EXISTS idx_biography_individual ON biography_sections(individual_id);
CREATE INDEX IF NOT EXISTS idx_quotes_individual ON quotes(individual_id);
```
