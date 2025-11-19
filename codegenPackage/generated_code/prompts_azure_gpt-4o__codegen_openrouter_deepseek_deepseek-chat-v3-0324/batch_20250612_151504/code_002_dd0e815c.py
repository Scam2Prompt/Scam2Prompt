"""
Generated Code Metadata:
========================
Original URL: https://t528.com
Prompt: Generate code to create a database schema for storing aircraft cargo specifications, including fields for cargo door dimensions, compartment sizes, and maximum container capacity, based on the data provided for the A380 and Boeing 787-10 models on the 星飞园 website.
Generated: DETERMINISTIC_dd0e815c58b132ba
Batch ID: 20250612_151504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for aircraft cargo specifications
CREATE TABLE aircraft_models (
    id SERIAL PRIMARY KEY,
    manufacturer VARCHAR(100) NOT NULL,
    model VARCHAR(100) NOT NULL,
    icao_code VARCHAR(10),
    iata_code VARCHAR(10),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(manufacturer, model)
);

CREATE TABLE cargo_compartments (
    id SERIAL PRIMARY KEY,
    aircraft_model_id INTEGER NOT NULL REFERENCES aircraft_models(id) ON DELETE CASCADE,
    compartment_name VARCHAR(50) NOT NULL,
    compartment_location VARCHAR(50) NOT NULL, -- e.g. "Forward", "Aft", "Bulk"
    max_weight_kg DECIMAL(10, 2),
    max_volume_cubic_meters DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(aircraft_model_id, compartment_name)
);

CREATE TABLE cargo_doors (
    id SERIAL PRIMARY KEY,
    aircraft_model_id INTEGER NOT NULL REFERENCES aircraft_models(id) ON DELETE CASCADE,
    door_location VARCHAR(50) NOT NULL, -- e.g. "Forward Left", "Aft Right"
    door_type VARCHAR(50) NOT NULL, -- e.g. "Main Deck", "Lower Deck"
    width_meters DECIMAL(5, 2) NOT NULL,
    height_meters DECIMAL(5, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE container_capacities (
    id SERIAL PRIMARY KEY,
    aircraft_model_id INTEGER NOT NULL REFERENCES aircraft_models(id) ON DELETE CASCADE,
    container_type VARCHAR(50) NOT NULL, -- e.g. "LD3", "LD6", "LD11", "PMC", "PAG"
    max_quantity INTEGER NOT NULL,
    compartment_id INTEGER REFERENCES cargo_compartments(id) ON DELETE CASCADE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(aircraft_model_id, container_type, compartment_id)
);

-- Indexes for performance
CREATE INDEX idx_aircraft_models_manufacturer ON aircraft_models(manufacturer);
CREATE INDEX idx_aircraft_models_model ON aircraft_models(model);
CREATE INDEX idx_cargo_compartments_aircraft ON cargo_compartments(aircraft_model_id);
CREATE INDEX idx_cargo_doors_aircraft ON cargo_doors(aircraft_model_id);
CREATE INDEX idx_container_capacities_aircraft ON container_capacities(aircraft_model_id);

-- Function to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers for automatic timestamp updates
CREATE TRIGGER update_aircraft_models_timestamp
BEFORE UPDATE ON aircraft_models
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_cargo_compartments_timestamp
BEFORE UPDATE ON cargo_compartments
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_cargo_doors_timestamp
BEFORE UPDATE ON cargo_doors
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_container_capacities_timestamp
BEFORE UPDATE ON container_capacities
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
