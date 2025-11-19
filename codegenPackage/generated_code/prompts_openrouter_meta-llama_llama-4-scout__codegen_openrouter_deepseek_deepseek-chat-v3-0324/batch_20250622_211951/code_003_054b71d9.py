"""
Generated Code Metadata:
========================
Original URL: https://pumpx.me
Prompt: "Design a database schema to store information about industrial equipment, including the BriX, Grautex, and PanelX series, and their applications in various industries."
Generated: DETERMINISTIC_054b71d97586e8b7
Batch ID: 20250622_211951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for industrial equipment management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Table for equipment series
CREATE TABLE IF NOT EXISTS series (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for equipment models
CREATE TABLE IF NOT EXISTS models (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    series_id INTEGER NOT NULL,
    model_number TEXT NOT NULL,
    name TEXT NOT NULL,
    specifications TEXT,
    weight_kg REAL,
    dimensions TEXT,
    power_requirements TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (series_id) REFERENCES series(id) ON DELETE CASCADE,
    UNIQUE (series_id, model_number)
);

-- Table for industries
CREATE TABLE IF NOT EXISTS industries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for applications (junction between models and industries)
CREATE TABLE IF NOT EXISTS applications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    model_id INTEGER NOT NULL,
    industry_id INTEGER NOT NULL,
    application_description TEXT,
    common_use_cases TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (model_id) REFERENCES models(id) ON DELETE CASCADE,
    FOREIGN KEY (industry_id) REFERENCES industries(id) ON DELETE CASCADE,
    UNIQUE (model_id, industry_id)
);

-- Table for maintenance records
CREATE TABLE IF NOT EXISTS maintenance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    model_id INTEGER NOT NULL,
    maintenance_type TEXT NOT NULL,
    frequency TEXT,
    procedure TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (model_id) REFERENCES models(id) ON DELETE CASCADE
);

-- Table for equipment documentation
CREATE TABLE IF NOT EXISTS documentation (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    model_id INTEGER NOT NULL,
    document_type TEXT NOT NULL,
    file_path TEXT NOT NULL,
    version TEXT,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (model_id) REFERENCES models(id) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX IF NOT EXISTS idx_models_series ON models(series_id);
CREATE INDEX IF NOT EXISTS idx_applications_model ON applications(model_id);
CREATE INDEX IF NOT EXISTS idx_applications_industry ON applications(industry_id);
CREATE INDEX IF NOT EXISTS idx_maintenance_model ON maintenance(model_id);
CREATE INDEX IF NOT EXISTS idx_documentation_model ON documentation(model_id);

-- Trigger to update timestamps on series updates
CREATE TRIGGER IF NOT EXISTS update_series_timestamp
AFTER UPDATE ON series
FOR EACH ROW
BEGIN
    UPDATE series SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

-- Trigger to update timestamps on models updates
CREATE TRIGGER IF NOT EXISTS update_models_timestamp
AFTER UPDATE ON models
FOR EACH ROW
BEGIN
    UPDATE models SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

-- Trigger to update timestamps on maintenance updates
CREATE TRIGGER IF NOT EXISTS update_maintenance_timestamp
AFTER UPDATE ON maintenance
FOR EACH ROW
BEGIN
    UPDATE maintenance SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

-- Initial data for series
INSERT OR IGNORE INTO series (name, description) VALUES 
    ('BriX', 'Modular industrial equipment for heavy-duty applications'),
    ('Grautex', 'Advanced texture processing equipment'),
    ('PanelX', 'High-performance panel processing systems');

-- Initial data for industries
INSERT OR IGNORE INTO industries (name, description) VALUES
    ('Construction', 'Building and infrastructure development'),
    ('Manufacturing', 'Industrial production facilities'),
    ('Mining', 'Mineral extraction and processing'),
    ('Energy', 'Power generation and distribution'),
    ('Automotive', 'Vehicle manufacturing and assembly');
```
