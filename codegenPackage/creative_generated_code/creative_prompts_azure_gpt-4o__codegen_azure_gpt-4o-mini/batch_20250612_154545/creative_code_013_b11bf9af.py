"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airstyleart.co.uk
Prompt: Create a database schema to store product information for AirstyleArt, including stencils, paints, accessories, and airbrush equipment.
Generated: DETERMINISTIC_b11bf9af71bde2be
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for AirstyleArt product information
-- This schema includes tables for stencils, paints, accessories, and airbrush equipment.

-- Drop existing tables if they exist for a clean slate
DROP TABLE IF EXISTS airbrush_equipment CASCADE;
DROP TABLE IF EXISTS accessories CASCADE;
DROP TABLE IF EXISTS paints CASCADE;
DROP TABLE IF EXISTS stencils CASCADE;

-- Table for storing stencil information
CREATE TABLE stencils (
    id SERIAL PRIMARY KEY,             -- Unique identifier for each stencil
    name VARCHAR(255) NOT NULL,       -- Name of the stencil
    design VARCHAR(255),               -- Design description
    material VARCHAR(100),             -- Material used for the stencil
    size VARCHAR(50),                  -- Size of the stencil
    price DECIMAL(10, 2) NOT NULL,     -- Price of the stencil
    created_at TIMESTAMP DEFAULT NOW(), -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT NOW()  -- Timestamp of the last update
);

-- Table for storing paint information
CREATE TABLE paints (
    id SERIAL PRIMARY KEY,             -- Unique identifier for each paint
    color VARCHAR(100) NOT NULL,       -- Color of the paint
    type VARCHAR(50) NOT NULL,         -- Type of paint (e.g., acrylic, watercolor)
    size_ml INT NOT NULL,              -- Size in milliliters
    price DECIMAL(10, 2) NOT NULL,     -- Price of the paint
    created_at TIMESTAMP DEFAULT NOW(), -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT NOW()  -- Timestamp of the last update
);

-- Table for storing accessory information
CREATE TABLE accessories (
    id SERIAL PRIMARY KEY,             -- Unique identifier for each accessory
    name VARCHAR(255) NOT NULL,        -- Name of the accessory
    type VARCHAR(100),                 -- Type of accessory (e.g., brushes, palettes)
    price DECIMAL(10, 2) NOT NULL,     -- Price of the accessory
    created_at TIMESTAMP DEFAULT NOW(), -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT NOW()  -- Timestamp of the last update
);

-- Table for storing airbrush equipment information
CREATE TABLE airbrush_equipment (
    id SERIAL PRIMARY KEY,             -- Unique identifier for each airbrush equipment
    model VARCHAR(100) NOT NULL,       -- Model of the airbrush
    type VARCHAR(50) NOT NULL,         -- Type of airbrush (e.g., single-action, double-action)
    price DECIMAL(10, 2) NOT NULL,     -- Price of the airbrush equipment
    created_at TIMESTAMP DEFAULT NOW(), -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT NOW()  -- Timestamp of the last update
);

-- Add indexes for optimizing queries on frequently searched fields
CREATE INDEX idx_stencils_name ON stencils(name);
CREATE INDEX idx_paints_color ON paints(color);
CREATE INDEX idx_accessories_name ON accessories(name);
CREATE INDEX idx_airbrush_model ON airbrush_equipment(model);

-- Notes:
-- 1. Use appropriate data types to ensure data integrity.
-- 2. Default timestamps for created and updated times help track record history.
-- 3. Indexes improve query performance on common search fields.
-- 4. Ensure to handle transactions and rollbacks in application code to maintain data consistency during CRUD operations.
```
