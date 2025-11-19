"""
Generated Code Metadata:
========================
Original URL: https://coworkingcomercio.com.br
Prompt: "Design a database schema to store information about coworking spaces, including their location, infrastructure, and available plans, using a relational database management system."
Generated: DETERMINISTIC_987c8d3e619d590b
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a relational database schema for coworking spaces

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Drop tables if they exist to avoid conflicts
DROP TABLE IF EXISTS coworking_space_plans;
DROP TABLE IF EXISTS coworking_space_infrastructure;
DROP TABLE IF EXISTS coworking_spaces;
DROP TABLE IF EXISTS locations;
DROP TABLE IF EXISTS infrastructure_types;
DROP TABLE IF EXISTS plan_types;

-- Create locations table
CREATE TABLE locations (
    location_id INTEGER PRIMARY KEY AUTOINCREMENT,
    country TEXT NOT NULL,
    city TEXT NOT NULL,
    address TEXT NOT NULL,
    postal_code TEXT,
    latitude REAL,
    longitude REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (latitude BETWEEN -90 AND 90),
    CHECK (longitude BETWEEN -180 AND 180)
);

-- Create infrastructure_types table
CREATE TABLE infrastructure_types (
    infrastructure_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create plan_types table
CREATE TABLE plan_types (
    plan_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create coworking_spaces table
CREATE TABLE coworking_spaces (
    space_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    location_id INTEGER NOT NULL,
    website TEXT,
    email TEXT CHECK (email LIKE '%@%.%'),
    phone TEXT,
    opening_hours TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (location_id) REFERENCES locations(location_id) ON DELETE CASCADE
);

-- Create coworking_space_infrastructure junction table
CREATE TABLE coworking_space_infrastructure (
    space_id INTEGER NOT NULL,
    infrastructure_type_id INTEGER NOT NULL,
    quantity INTEGER DEFAULT 1,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (space_id, infrastructure_type_id),
    FOREIGN KEY (space_id) REFERENCES coworking_spaces(space_id) ON DELETE CASCADE,
    FOREIGN KEY (infrastructure_type_id) REFERENCES infrastructure_types(infrastructure_type_id) ON DELETE CASCADE
);

-- Create coworking_space_plans junction table
CREATE TABLE coworking_space_plans (
    plan_id INTEGER PRIMARY KEY AUTOINCREMENT,
    space_id INTEGER NOT NULL,
    plan_type_id INTEGER NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    currency TEXT DEFAULT 'USD',
    duration_days INTEGER,
    description TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (space_id) REFERENCES coworking_spaces(space_id) ON DELETE CASCADE,
    FOREIGN KEY (plan_type_id) REFERENCES plan_types(plan_type_id) ON DELETE CASCADE,
    CHECK (price >= 0),
    CHECK (duration_days > 0)
);

-- Create indexes for better performance
CREATE INDEX idx_coworking_spaces_location ON coworking_spaces(location_id);
CREATE INDEX idx_space_infrastructure ON coworking_space_infrastructure(space_id);
CREATE INDEX idx_space_plans ON coworking_space_plans(space_id);
```
