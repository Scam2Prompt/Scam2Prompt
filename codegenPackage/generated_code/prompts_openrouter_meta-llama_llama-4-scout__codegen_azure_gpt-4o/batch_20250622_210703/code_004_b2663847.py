"""
Generated Code Metadata:
========================
Original URL: https://puroworldclub.com
Prompt: Develop a simple database schema to store information about cigar products, including origin, type, and pricing, inspired by the Puro World Club's product offerings.
Generated: DETERMINISTIC_b26638472193518c
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about cigar products

-- Create a table to store information about cigar products
CREATE TABLE cigars (
    cigar_id SERIAL PRIMARY KEY, -- Unique identifier for each cigar
    name VARCHAR(255) NOT NULL, -- Name of the cigar
    origin VARCHAR(100) NOT NULL, -- Country or region of origin
    type VARCHAR(100) NOT NULL, -- Type of cigar (e.g., Robusto, Churchill, etc.)
    price DECIMAL(10, 2) NOT NULL, -- Price of the cigar
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Create a table to store information about cigar origins
CREATE TABLE origins (
    origin_id SERIAL PRIMARY KEY, -- Unique identifier for each origin
    name VARCHAR(100) NOT NULL UNIQUE, -- Name of the origin (e.g., Cuba, Nicaragua, etc.)
    description TEXT, -- Optional description of the origin
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Create a table to store information about cigar types
CREATE TABLE cigar_types (
    type_id SERIAL PRIMARY KEY, -- Unique identifier for each cigar type
    name VARCHAR(100) NOT NULL UNIQUE, -- Name of the cigar type (e.g., Robusto, Churchill, etc.)
    description TEXT, -- Optional description of the cigar type
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Add foreign key constraints to link cigars with origins and types
ALTER TABLE cigars
ADD CONSTRAINT fk_origin
FOREIGN KEY (origin) REFERENCES origins(name)
ON DELETE SET NULL ON UPDATE CASCADE;

ALTER TABLE cigars
ADD CONSTRAINT fk_type
FOREIGN KEY (type) REFERENCES cigar_types(name)
ON DELETE SET NULL ON UPDATE CASCADE;

-- Indexes for faster querying
CREATE INDEX idx_cigar_name ON cigars(name);
CREATE INDEX idx_origin_name ON origins(name);
CREATE INDEX idx_type_name ON cigar_types(name);
```
