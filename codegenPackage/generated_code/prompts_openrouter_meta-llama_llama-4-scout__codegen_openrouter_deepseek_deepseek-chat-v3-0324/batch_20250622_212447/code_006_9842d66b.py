"""
Generated Code Metadata:
========================
Original URL: https://gaaac.org
Prompt: Design a database schema to store information about accredited institutions, degrees, and countries served by GAAAC.
Generated: DETERMINISTIC_9842d66b9e88cbd1
Batch ID: 20250622_212447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for GAAAC (Global Accreditation Agency for Academic Credentials)
-- This schema stores information about accredited institutions, degrees, and countries served by GAAAC

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Countries table
CREATE TABLE IF NOT EXISTS countries (
    country_id INTEGER PRIMARY KEY AUTOINCREMENT,
    country_name TEXT NOT NULL UNIQUE,
    country_code TEXT NOT NULL UNIQUE CHECK(length(country_code) = 2),
    region TEXT,
    date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Institutions table
CREATE TABLE IF NOT EXISTS institutions (
    institution_id INTEGER PRIMARY KEY AUTOINCREMENT,
    institution_name TEXT NOT NULL,
    institution_type TEXT CHECK(institution_type IN ('University', 'College', 'Institute', 'Other')),
    website_url TEXT,
    founded_year INTEGER,
    country_id INTEGER NOT NULL,
    accreditation_status TEXT NOT NULL CHECK(accreditation_status IN ('Active', 'Probation', 'Revoked', 'Pending')),
    accreditation_date DATE,
    date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (country_id) REFERENCES countries(country_id) ON DELETE RESTRICT
);

-- Degrees table
CREATE TABLE IF NOT EXISTS degrees (
    degree_id INTEGER PRIMARY KEY AUTOINCREMENT,
    degree_name TEXT NOT NULL,
    degree_level TEXT NOT NULL CHECK(degree_level IN ('Certificate', 'Associate', 'Bachelor', 'Master', 'Doctorate', 'Professional')),
    field_of_study TEXT NOT NULL,
    duration_years INTEGER NOT NULL CHECK(duration_years > 0),
    date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Institution_Degrees junction table (many-to-many relationship)
CREATE TABLE IF NOT EXISTS institution_degrees (
    institution_id INTEGER NOT NULL,
    degree_id INTEGER NOT NULL,
    is_offered BOOLEAN NOT NULL DEFAULT TRUE,
    date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (institution_id, degree_id),
    FOREIGN KEY (institution_id) REFERENCES institutions(institution_id) ON DELETE CASCADE,
    FOREIGN KEY (degree_id) REFERENCES degrees(degree_id) ON DELETE CASCADE
);

-- GAAAC_Service_Areas table
CREATE TABLE IF NOT EXISTS gaaac_service_areas (
    service_area_id INTEGER PRIMARY KEY AUTOINCREMENT,
    country_id INTEGER NOT NULL,
    service_start_date DATE NOT NULL,
    service_end_date DATE,
    is_active BOOLEAN GENERATED ALWAYS AS (
        CASE WHEN service_end_date IS NULL OR service_end_date >= date('now') THEN 1 ELSE 0 END
    ) STORED,
    notes TEXT,
    date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (country_id) REFERENCES countries(country_id) ON DELETE CASCADE,
    CHECK (service_end_date IS NULL OR service_end_date >= service_start_date)
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_institutions_country ON institutions(country_id);
CREATE INDEX IF NOT EXISTS idx_institutions_name ON institutions(institution_name);
CREATE INDEX IF NOT EXISTS idx_degrees_level ON degrees(degree_level);
CREATE INDEX IF NOT EXISTS idx_institution_degrees_institution ON institution_degrees(institution_id);
CREATE INDEX IF NOT EXISTS idx_institution_degrees_degree ON institution_degrees(degree_id);
CREATE INDEX IF NOT EXISTS idx_gaaac_service_areas_country ON gaaac_service_areas(country_id);
CREATE INDEX IF NOT EXISTS idx_gaaac_service_areas_active ON gaaac_service_areas(is_active);

-- Triggers to update last_updated timestamps
CREATE TRIGGER IF NOT EXISTS update_country_timestamp
AFTER UPDATE ON countries
FOR EACH ROW
BEGIN
    UPDATE countries SET last_updated = CURRENT_TIMESTAMP WHERE country_id = OLD.country_id;
END;

CREATE TRIGGER IF NOT EXISTS update_institution_timestamp
AFTER UPDATE ON institutions
FOR EACH ROW
BEGIN
    UPDATE institutions SET last_updated = CURRENT_TIMESTAMP WHERE institution_id = OLD.institution_id;
END;

CREATE TRIGGER IF NOT EXISTS update_degree_timestamp
AFTER UPDATE ON degrees
FOR EACH ROW
BEGIN
    UPDATE degrees SET last_updated = CURRENT_TIMESTAMP WHERE degree_id = OLD.degree_id;
END;

CREATE TRIGGER IF NOT EXISTS update_service_area_timestamp
AFTER UPDATE ON gaaac_service_areas
FOR EACH ROW
BEGIN
    UPDATE gaaac_service_areas SET last_updated = CURRENT_TIMESTAMP WHERE service_area_id = OLD.service_area_id;
END;
```
