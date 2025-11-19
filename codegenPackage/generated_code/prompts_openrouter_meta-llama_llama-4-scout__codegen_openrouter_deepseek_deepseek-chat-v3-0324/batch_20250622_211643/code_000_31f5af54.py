"""
Generated Code Metadata:
========================
Original URL: https://meyerseim.com
Prompt: Write a genealogy database schema to store information about individuals with first name, last name, birth date, and family relationships, inspired by the Meyer and Seim family records.
Generated: DETERMINISTIC_31f5af5490ae23c5
Batch ID: 20250622_211643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Genealogy Database Schema
-- Stores information about individuals and their family relationships

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Table to store individuals
CREATE TABLE individuals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    birth_date DATE,
    death_date DATE,
    gender TEXT CHECK(gender IN ('M', 'F', 'O', NULL)),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store relationship types
CREATE TABLE relationship_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Insert common relationship types
INSERT INTO relationship_types (name, description) VALUES 
    ('parent', 'Parent-child relationship'),
    ('child', 'Child-parent relationship'),
    ('spouse', 'Married or partnered'),
    ('sibling', 'Brother or sister');

-- Table to store relationships between individuals
CREATE TABLE relationships (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    individual1_id INTEGER NOT NULL,
    individual2_id INTEGER NOT NULL,
    relationship_type_id INTEGER NOT NULL,
    start_date DATE,
    end_date DATE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (individual1_id) REFERENCES individuals(id) ON DELETE CASCADE,
    FOREIGN KEY (individual2_id) REFERENCES individuals(id) ON DELETE CASCADE,
    FOREIGN KEY (relationship_type_id) REFERENCES relationship_types(id),
    CHECK (individual1_id != individual2_id)
);

-- Indexes for performance
CREATE INDEX idx_individuals_name ON individuals(last_name, first_name);
CREATE INDEX idx_relationships_individual1 ON relationships(individual1_id);
CREATE INDEX idx_relationships_individual2 ON relationships(individual2_id);
CREATE INDEX idx_relationships_type ON relationships(relationship_type_id);

-- Trigger to update the updated_at timestamp when individuals are modified
CREATE TRIGGER update_individual_timestamp
AFTER UPDATE ON individuals
FOR EACH ROW
BEGIN
    UPDATE individuals SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

-- Trigger to update the updated_at timestamp when relationships are modified
CREATE TRIGGER update_relationship_timestamp
AFTER UPDATE ON relationships
FOR EACH ROW
BEGIN
    UPDATE relationships SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

-- View to simplify common queries
CREATE VIEW family_tree AS
SELECT 
    i1.id as person_id,
    i1.first_name || ' ' || i1.last_name as person_name,
    rt.name as relationship_type,
    i2.id as related_person_id,
    i2.first_name || ' ' || i2.last_name as related_person_name
FROM 
    relationships r
JOIN 
    individuals i1 ON r.individual1_id = i1.id
JOIN 
    individuals i2 ON r.individual2_id = i2.id
JOIN 
    relationship_types rt ON r.relationship_type_id = rt.id;
```
