"""
Generated Code Metadata:
========================
Original URL: https://vitalityholistic.co.uk
Prompt: Generate a sample database schema for storing information about various holistic therapies, including Cupping/Hijama, Fertility Massage, Lymphatic Drainage, and Medical Acupuncture, along with their benefits and potential side effects.
Generated: DETERMINISTIC_ef9cc0c27ee7354e
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for holistic therapies information system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Therapy Categories
CREATE TABLE IF NOT EXISTS therapy_categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Therapies
CREATE TABLE IF NOT EXISTS therapies (
    therapy_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER NOT NULL,
    name TEXT NOT NULL UNIQUE,
    description TEXT NOT NULL,
    history TEXT,
    typical_session_duration INTEGER, -- in minutes
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES therapy_categories(category_id)
);

-- Benefits
CREATE TABLE IF NOT EXISTS benefits (
    benefit_id INTEGER PRIMARY KEY AUTOINCREMENT,
    therapy_id INTEGER NOT NULL,
    description TEXT NOT NULL,
    scientific_evidence_level TEXT CHECK(scientific_evidence_level IN ('strong', 'moderate', 'weak', 'anecdotal')),
    FOREIGN KEY (therapy_id) REFERENCES therapies(therapy_id) ON DELETE CASCADE
);

-- Side Effects
CREATE TABLE IF NOT EXISTS side_effects (
    side_effect_id INTEGER PRIMARY KEY AUTOINCREMENT,
    therapy_id INTEGER NOT NULL,
    description TEXT NOT NULL,
    severity TEXT CHECK(severity IN ('mild', 'moderate', 'severe')),
    frequency TEXT CHECK(frequency IN ('common', 'uncommon', 'rare')),
    FOREIGN KEY (therapy_id) REFERENCES therapies(therapy_id) ON DELETE CASCADE
);

-- Practitioners
CREATE TABLE IF NOT EXISTS practitioners (
    practitioner_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    certification TEXT NOT NULL,
    years_of_experience INTEGER,
    contact_info TEXT
);

-- Therapy_Practitioners (Many-to-Many relationship)
CREATE TABLE IF NOT EXISTS therapy_practitioners (
    therapy_id INTEGER NOT NULL,
    practitioner_id INTEGER NOT NULL,
    PRIMARY KEY (therapy_id, practitioner_id),
    FOREIGN KEY (therapy_id) REFERENCES therapies(therapy_id) ON DELETE CASCADE,
    FOREIGN KEY (practitioner_id) REFERENCES practitioners(practitioner_id) ON DELETE CASCADE
);

-- Contraindications
CREATE TABLE IF NOT EXISTS contraindications (
    contraindication_id INTEGER PRIMARY KEY AUTOINCREMENT,
    therapy_id INTEGER NOT NULL,
    description TEXT NOT NULL,
    FOREIGN KEY (therapy_id) REFERENCES therapies(therapy_id) ON DELETE CASCADE
);

-- Aftercare Instructions
CREATE TABLE IF NOT EXISTS aftercare_instructions (
    instruction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    therapy_id INTEGER NOT NULL,
    description TEXT NOT NULL,
    importance TEXT CHECK(importance IN ('critical', 'important', 'recommended')),
    FOREIGN KEY (therapy_id) REFERENCES therapies(therapy_id) ON DELETE CASCADE
);

-- Create indexes for performance
CREATE INDEX IF NOT EXISTS idx_therapies_category ON therapies(category_id);
CREATE INDEX IF NOT EXISTS idx_benefits_therapy ON benefits(therapy_id);
CREATE INDEX IF NOT EXISTS idx_side_effects_therapy ON side_effects(therapy_id);
CREATE INDEX IF NOT EXISTS idx_contraindications_therapy ON contraindications(therapy_id);
CREATE INDEX IF NOT EXISTS idx_aftercare_therapy ON aftercare_instructions(therapy_id);
CREATE INDEX IF NOT EXISTS idx_therapy_practitioners ON therapy_practitioners(therapy_id, practitioner_id);

-- Trigger to update updated_at timestamp
CREATE TRIGGER IF NOT EXISTS update_therapy_timestamp
AFTER UPDATE ON therapies
FOR EACH ROW
BEGIN
    UPDATE therapies SET updated_at = CURRENT_TIMESTAMP WHERE therapy_id = NEW.therapy_id;
END;
```
