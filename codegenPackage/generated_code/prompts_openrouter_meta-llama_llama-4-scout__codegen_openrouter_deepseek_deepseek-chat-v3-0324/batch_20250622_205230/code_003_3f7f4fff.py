"""
Generated Code Metadata:
========================
Original URL: https://enterkuroro.pages.dev
Prompt: Design a database schema to store information about Kuroro Beasts, including their elemental powers, skills, and ownership details.
Generated: DETERMINISTIC_3f7f4fff95c60f4d
Batch ID: 20250622_205230
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Kuroro Beasts management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Table to store elemental types
CREATE TABLE IF NOT EXISTS elements (
    element_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store beast types/species
CREATE TABLE IF NOT EXISTS beast_types (
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    base_power_level INTEGER NOT NULL CHECK(base_power_level > 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Junction table for beast_type-element relationship (many-to-many)
CREATE TABLE IF NOT EXISTS beast_type_elements (
    type_id INTEGER NOT NULL,
    element_id INTEGER NOT NULL,
    PRIMARY KEY (type_id, element_id),
    FOREIGN KEY (type_id) REFERENCES beast_types(type_id) ON DELETE CASCADE,
    FOREIGN KEY (element_id) REFERENCES elements(element_id) ON DELETE CASCADE
);

-- Table to store skills/abilities
CREATE TABLE IF NOT EXISTS skills (
    skill_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT NOT NULL,
    power_cost INTEGER NOT NULL CHECK(power_cost >= 0),
    element_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (element_id) REFERENCES elements(element_id) ON DELETE SET NULL
);

-- Table to store individual beasts
CREATE TABLE IF NOT EXISTS beasts (
    beast_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type_id INTEGER NOT NULL,
    power_level INTEGER NOT NULL CHECK(power_level > 0),
    birth_date DATE,
    acquired_date DATE DEFAULT CURRENT_DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (type_id) REFERENCES beast_types(type_id) ON DELETE RESTRICT
);

-- Junction table for beast-skill relationship (many-to-many)
CREATE TABLE IF NOT EXISTS beast_skills (
    beast_id INTEGER NOT NULL,
    skill_id INTEGER NOT NULL,
    mastery_level INTEGER NOT NULL CHECK(mastery_level BETWEEN 1 AND 10) DEFAULT 1,
    PRIMARY KEY (beast_id, skill_id),
    FOREIGN KEY (beast_id) REFERENCES beasts(beast_id) ON DELETE CASCADE,
    FOREIGN KEY (skill_id) REFERENCES skills(skill_id) ON DELETE CASCADE
);

-- Table to store owners/trainers
CREATE TABLE IF NOT EXISTS owners (
    owner_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE CHECK(email LIKE '%@%.%'),
    join_date DATE DEFAULT CURRENT_DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to track beast ownership
CREATE TABLE IF NOT EXISTS ownership (
    ownership_id INTEGER PRIMARY KEY AUTOINCREMENT,
    beast_id INTEGER NOT NULL,
    owner_id INTEGER NOT NULL,
    acquired_date DATE DEFAULT CURRENT_DATE,
    released_date DATE,
    is_current BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (beast_id) REFERENCES beasts(beast_id) ON DELETE CASCADE,
    FOREIGN KEY (owner_id) REFERENCES owners(owner_id) ON DELETE CASCADE,
    CHECK (released_date IS NULL OR released_date >= acquired_date)
);

-- Create indexes for performance
CREATE INDEX IF NOT EXISTS idx_beasts_type ON beasts(type_id);
CREATE INDEX IF NOT EXISTS idx_beast_skills_beast ON beast_skills(beast_id);
CREATE INDEX IF NOT EXISTS idx_beast_skills_skill ON beast_skills(skill_id);
CREATE INDEX IF NOT EXISTS idx_ownership_beast ON ownership(beast_id);
CREATE INDEX IF NOT EXISTS idx_ownership_owner ON ownership(owner_id);
CREATE INDEX IF NOT EXISTS idx_ownership_current ON ownership(is_current);

-- Trigger to update timestamps on update
CREATE TRIGGER IF NOT EXISTS update_element_timestamp
AFTER UPDATE ON elements
BEGIN
    UPDATE elements SET updated_at = CURRENT_TIMESTAMP WHERE element_id = NEW.element_id;
END;

CREATE TRIGGER IF NOT EXISTS update_beast_type_timestamp
AFTER UPDATE ON beast_types
BEGIN
    UPDATE beast_types SET updated_at = CURRENT_TIMESTAMP WHERE type_id = NEW.type_id;
END;

CREATE TRIGGER IF NOT EXISTS update_skill_timestamp
AFTER UPDATE ON skills
BEGIN
    UPDATE skills SET updated_at = CURRENT_TIMESTAMP WHERE skill_id = NEW.skill_id;
END;

CREATE TRIGGER IF NOT EXISTS update_beast_timestamp
AFTER UPDATE ON beasts
BEGIN
    UPDATE beasts SET updated_at = CURRENT_TIMESTAMP WHERE beast_id = NEW.beast_id;
END;

CREATE TRIGGER IF NOT EXISTS update_owner_timestamp
AFTER UPDATE ON owners
BEGIN
    UPDATE owners SET updated_at = CURRENT_TIMESTAMP WHERE owner_id = NEW.owner_id;
END;

CREATE TRIGGER IF NOT EXISTS update_ownership_timestamp
AFTER UPDATE ON ownership
BEGIN
    UPDATE ownership SET updated_at = CURRENT_TIMESTAMP WHERE ownership_id = NEW.ownership_id;
END;

-- Trigger to handle ownership changes
CREATE TRIGGER IF NOT EXISTS update_ownership_status
BEFORE UPDATE OF released_date ON ownership
BEGIN
    UPDATE ownership SET is_current = CASE WHEN NEW.released_date IS NULL THEN TRUE ELSE FALSE END
    WHERE ownership_id = NEW.ownership_id;
END;
```
