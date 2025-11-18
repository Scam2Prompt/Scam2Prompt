"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daddys-universitys.com
Prompt: Develop a database schema for storing information about architectural design projects, including fields for traditional building styles, sustainable materials, and historical preservation techniques.
Generated: DETERMINISTIC_6a29d907e20cea57
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing information about architectural design projects

CREATE TABLE BuildingStyles (
    id SERIAL PRIMARY KEY,
    style_name VARCHAR(100) NOT NULL UNIQUE, -- Name of the building style
    description TEXT, -- Description of the building style
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

CREATE TABLE SustainableMaterials (
    id SERIAL PRIMARY KEY,
    material_name VARCHAR(100) NOT NULL UNIQUE, -- Name of the sustainable material
    description TEXT, -- Description of the sustainable material
    environmental_impact_rating INT CHECK (environmental_impact_rating BETWEEN 1 AND 10), -- Rating from 1 to 10
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

CREATE TABLE PreservationTechniques (
    id SERIAL PRIMARY KEY,
    technique_name VARCHAR(100) NOT NULL UNIQUE, -- Name of the preservation technique
    description TEXT, -- Description of the preservation technique
    effectiveness_rating INT CHECK (effectiveness_rating BETWEEN 1 AND 10), -- Rating from 1 to 10
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

CREATE TABLE ArchitecturalProjects (
    id SERIAL PRIMARY KEY,
    project_name VARCHAR(150) NOT NULL, -- Name of the architectural project
    client_name VARCHAR(100), -- Name of the client
    project_description TEXT, -- Description of the project
    building_style_id INT REFERENCES BuildingStyles(id) ON DELETE SET NULL, -- Reference to BuildingStyles
    sustainable_material_id INT REFERENCES SustainableMaterials(id) ON DELETE SET NULL, -- Reference to SustainableMaterials
    preservation_technique_id INT REFERENCES PreservationTechniques(id) ON DELETE SET NULL, -- Reference to PreservationTechniques
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Ensure proper error handling during data insertion
-- Example for inserting a new building style
BEGIN;
    INSERT INTO BuildingStyles (style_name, description) VALUES ('Modern', 'Characterized by minimalist design and the use of new materials.');
EXCEPTION WHEN unique_violation THEN
    RAISE NOTICE 'Building style already exists.';
ROLLBACK;

-- Add similar error handling structures for other insertions as necessary
```
