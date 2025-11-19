"""
Generated Code Metadata:
========================
Original URL: https://guapaaltejer.com
Prompt: Design a database schema to store information about knitting and crochet patterns, including attributes such as yarn type, needle size, and skill level.
Generated: DETERMINISTIC_0acedf57cd6d01e6
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Database Schema for Knitting and Crochet Patterns

```sql
-- Database schema for knitting and crochet patterns
-- Supports storing patterns with yarn details, needle/hook sizes, and skill levels

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables
CREATE TABLE IF NOT EXISTS categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

CREATE TABLE IF NOT EXISTS skill_levels (
    level_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

CREATE TABLE IF NOT EXISTS yarn_weights (
    weight_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    ply TEXT,
    wpi_min INTEGER,
    wpi_max INTEGER
);

CREATE TABLE IF NOT EXISTS yarns (
    yarn_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    brand TEXT,
    weight_id INTEGER,
    fiber_content TEXT,
    yardage INTEGER,
    grams INTEGER,
    color TEXT,
    FOREIGN KEY (weight_id) REFERENCES yarn_weights(weight_id)
);

CREATE TABLE IF NOT EXISTS needle_sizes (
    size_id INTEGER PRIMARY KEY AUTOINCREMENT,
    us_size REAL,
    metric_size REAL,
    uk_size REAL,
    type TEXT NOT NULL CHECK (type IN ('knitting', 'crochet'))
);

CREATE TABLE IF NOT EXISTS patterns (
    pattern_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    category_id INTEGER,
    skill_level_id INTEGER,
    gauge TEXT,
    yardage_estimate INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_free BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (category_id) REFERENCES categories(category_id),
    FOREIGN KEY (skill_level_id) REFERENCES skill_levels(level_id)
);

CREATE TABLE IF NOT EXISTS pattern_yarns (
    pattern_id INTEGER,
    yarn_id INTEGER,
    quantity INTEGER,
    PRIMARY KEY (pattern_id, yarn_id),
    FOREIGN KEY (pattern_id) REFERENCES patterns(pattern_id) ON DELETE CASCADE,
    FOREIGN KEY (yarn_id) REFERENCES yarns(yarn_id)
);

CREATE TABLE IF NOT EXISTS pattern_needles (
    pattern_id INTEGER,
    size_id INTEGER,
    quantity INTEGER DEFAULT 1,
    PRIMARY KEY (pattern_id, size_id),
    FOREIGN KEY (pattern_id) REFERENCES patterns(pattern_id) ON DELETE CASCADE,
    FOREIGN KEY (size_id) REFERENCES needle_sizes(size_id)
);

CREATE TABLE IF NOT EXISTS pattern_images (
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    pattern_id INTEGER,
    image_url TEXT NOT NULL,
    is_main_image BOOLEAN DEFAULT FALSE,
    caption TEXT,
    FOREIGN KEY (pattern_id) REFERENCES patterns(pattern_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS pattern_steps (
    step_id INTEGER PRIMARY KEY AUTOINCREMENT,
    pattern_id INTEGER,
    step_number INTEGER NOT NULL,
    instruction TEXT NOT NULL,
    FOREIGN KEY (pattern_id) REFERENCES patterns(pattern_id) ON DELETE CASCADE,
    UNIQUE (pattern_id, step_number)
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_patterns_category ON patterns(category_id);
CREATE INDEX IF NOT EXISTS idx_patterns_skill_level ON patterns(skill_level_id);
CREATE INDEX IF NOT EXISTS idx_pattern_yarns ON pattern_yarns(pattern_id);
CREATE INDEX IF NOT EXISTS idx_pattern_needles ON pattern_needles(pattern_id);
```
