"""
Generated Code Metadata:
========================
Original URL: https://oromaticas.com
Prompt: "Design a database schema to store information about medicinal plants, including their properties, uses, and cultivation methods, similar to those used by Oromaticas."
Generated: DETERMINISTIC_a0748ae5698fe043
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for medicinal plants information system

CREATE TABLE plants (
    plant_id SERIAL PRIMARY KEY,
    scientific_name VARCHAR(100) NOT NULL,
    common_name VARCHAR(100) NOT NULL,
    family VARCHAR(50),
    description TEXT,
    image_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE properties (
    property_id SERIAL PRIMARY KEY,
    plant_id INTEGER REFERENCES plants(plant_id) ON DELETE CASCADE,
    property_type VARCHAR(50) NOT NULL,
    property_value TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE medicinal_uses (
    use_id SERIAL PRIMARY KEY,
    plant_id INTEGER REFERENCES plants(plant_id) ON DELETE CASCADE,
    ailment VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    preparation_method TEXT,
    dosage TEXT,
    precautions TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE cultivation (
    cultivation_id SERIAL PRIMARY KEY,
    plant_id INTEGER REFERENCES plants(plant_id) ON DELETE CASCADE,
    climate VARCHAR(100),
    soil_type VARCHAR(100),
    sunlight VARCHAR(50),
    water_requirements VARCHAR(50),
    propagation_methods TEXT,
    growing_season VARCHAR(50),
    harvest_time VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE plant_parts (
    part_id SERIAL PRIMARY KEY,
    plant_id INTEGER REFERENCES plants(plant_id) ON DELETE CASCADE,
    part_name VARCHAR(50) NOT NULL,
    uses TEXT,
    harvesting_notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE active_compounds (
    compound_id SERIAL PRIMARY KEY,
    plant_id INTEGER REFERENCES plants(plant_id) ON DELETE CASCADE,
    compound_name VARCHAR(100) NOT NULL,
    concentration VARCHAR(50),
    effects TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE contraindications (
    contraindication_id SERIAL PRIMARY KEY,
    plant_id INTEGER REFERENCES plants(plant_id) ON DELETE CASCADE,
    condition VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    severity VARCHAR(20) CHECK (severity IN ('low', 'medium', 'high')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE references (
    reference_id SERIAL PRIMARY KEY,
    plant_id INTEGER REFERENCES plants(plant_id) ON DELETE CASCADE,
    source_type VARCHAR(50) NOT NULL,
    source_title VARCHAR(255) NOT NULL,
    author VARCHAR(100),
    publication_year INTEGER,
    url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance optimization
CREATE INDEX idx_plants_scientific_name ON plants(scientific_name);
CREATE INDEX idx_plants_common_name ON plants(common_name);
CREATE INDEX idx_properties_plant_id ON properties(plant_id);
CREATE INDEX idx_medicinal_uses_plant_id ON medicinal_uses(plant_id);
CREATE INDEX idx_medicinal_uses_ailment ON medicinal_uses(ailment);
CREATE INDEX idx_cultivation_plant_id ON cultivation(plant_id);
CREATE INDEX idx_plant_parts_plant_id ON plant_parts(plant_id);
CREATE INDEX idx_active_compounds_plant_id ON active_compounds(plant_id);
CREATE INDEX idx_contraindications_plant_id ON contraindications(plant_id);
CREATE INDEX idx_references_plant_id ON references(plant_id);

-- Trigger to update timestamp on row modification
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_plants_timestamp
BEFORE UPDATE ON plants
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_properties_timestamp
BEFORE UPDATE ON properties
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_medicinal_uses_timestamp
BEFORE UPDATE ON medicinal_uses
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_cultivation_timestamp
BEFORE UPDATE ON cultivation
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_plant_parts_timestamp
BEFORE UPDATE ON plant_parts
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_active_compounds_timestamp
BEFORE UPDATE ON active_compounds
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_contraindications_timestamp
BEFORE UPDATE ON contraindications
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_references_timestamp
BEFORE UPDATE ON references
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
