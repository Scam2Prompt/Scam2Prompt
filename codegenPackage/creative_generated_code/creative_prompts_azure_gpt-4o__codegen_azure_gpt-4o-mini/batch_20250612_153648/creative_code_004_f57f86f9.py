"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://longhuigolf.com
Prompt: Create a database schema for storing golf grip profiles, including customization details like material type (PU, TPE, rubber), embossing style, and customer preferences, as described on the Longhui Golf website.
Generated: DETERMINISTIC_f57f86f9a440f9f3
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a database schema for storing golf grip profiles

-- Drop existing tables if they exist to avoid conflicts
DROP TABLE IF EXISTS customer_preferences;
DROP TABLE IF EXISTS grip_profiles;
DROP TABLE IF EXISTS materials;

-- Create a table to store different types of materials for grips
CREATE TABLE materials (
    id SERIAL PRIMARY KEY,           -- Unique identifier for the material
    type VARCHAR(50) NOT NULL UNIQUE -- Type of material (e.g., PU, TPE, rubber)
);

-- Create a table to store grip profiles
CREATE TABLE grip_profiles (
    id SERIAL PRIMARY KEY,           -- Unique identifier for the grip profile
    name VARCHAR(100) NOT NULL,      -- Name of the grip profile
    material_id INT NOT NULL,        -- Foreign key referencing materials
    embossing_style VARCHAR(100),    -- Style of embossing for the grip
    created_at TIMESTAMP DEFAULT NOW(), -- Timestamp for when the profile is created
    updated_at TIMESTAMP DEFAULT NOW(), -- Timestamp for when the profile is updated
    FOREIGN KEY (material_id) REFERENCES materials(id) ON DELETE CASCADE
);

-- Create a table to store customer preferences related to grip profiles
CREATE TABLE customer_preferences (
    id SERIAL PRIMARY KEY,           -- Unique identifier for the preference
    customer_id INT NOT NULL,        -- Customer identifier (assumed to be linked to a customer table)
    grip_profile_id INT NOT NULL,    -- Foreign key referencing grip profiles
    preference_details TEXT,         -- Additional details about the customer's preferences
    created_at TIMESTAMP DEFAULT NOW(), -- Timestamp for when the preferences are created
    updated_at TIMESTAMP DEFAULT NOW(), -- Timestamp for when the preferences are updated
    FOREIGN KEY (grip_profile_id) REFERENCES grip_profiles(id) ON DELETE CASCADE
);

-- Insert sample materials into the materials table
INSERT INTO materials (type) VALUES 
('PU'),
('TPE'),
('Rubber');

-- Add indexes for performance optimization
CREATE INDEX idx_material_type ON materials(type);
CREATE INDEX idx_grip_profile_name ON grip_profiles(name);
CREATE INDEX idx_customer_preferences_customer_id ON customer_preferences(customer_id);
```

This database schema is designed to be efficient, well-structured, and adheres to best practices for relational databases. Each table has appropriate relationships and constraints, and indexing is implemented for improved query performance.
