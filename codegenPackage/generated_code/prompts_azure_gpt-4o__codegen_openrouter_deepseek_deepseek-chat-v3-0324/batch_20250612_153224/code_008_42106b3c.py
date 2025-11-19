"""
Generated Code Metadata:
========================
Original URL: https://lavage-desinfection-batiments-elevage.fr
Prompt: Create a database schema to store information about poultry farming buildings, cleaning schedules, and biosecurity measures, referencing the services and commitments outlined on the "Lavage désinfection de bâtiments d’élevage" website.
Generated: DETERMINISTIC_42106b3c09ff0ed3
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for poultry farming management system
-- Includes tables for buildings, cleaning schedules, and biosecurity measures

CREATE TABLE IF NOT EXISTS farms (
    farm_id SERIAL PRIMARY KEY,
    farm_name VARCHAR(100) NOT NULL,
    address TEXT NOT NULL,
    contact_person VARCHAR(100),
    phone VARCHAR(20),
    email VARCHAR(100),
    registration_number VARCHAR(50) UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS buildings (
    building_id SERIAL PRIMARY KEY,
    farm_id INTEGER REFERENCES farms(farm_id) ON DELETE CASCADE,
    building_name VARCHAR(100) NOT NULL,
    building_type VARCHAR(50) NOT NULL, -- e.g., broiler, layer, breeder
    capacity INTEGER,
    construction_date DATE,
    dimensions VARCHAR(50),
    last_cleaning_date DATE,
    next_scheduled_cleaning DATE,
    is_active BOOLEAN DEFAULT TRUE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS cleaning_schedules (
    schedule_id SERIAL PRIMARY KEY,
    building_id INTEGER REFERENCES buildings(building_id) ON DELETE CASCADE,
    cleaning_type VARCHAR(50) NOT NULL, -- e.g., routine, deep, post-outbreak
    frequency_days INTEGER NOT NULL,
    last_performed_date DATE,
    next_scheduled_date DATE NOT NULL,
    responsible_person VARCHAR(100),
    status VARCHAR(20) DEFAULT 'pending', -- pending, completed, delayed
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS cleaning_procedures (
    procedure_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    steps JSONB NOT NULL, -- JSON array of steps with details
    required_chemicals TEXT,
    safety_precautions TEXT,
    duration_minutes INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS cleaning_logs (
    log_id SERIAL PRIMARY KEY,
    schedule_id INTEGER REFERENCES cleaning_schedules(schedule_id) ON DELETE SET NULL,
    building_id INTEGER REFERENCES buildings(building_id) ON DELETE CASCADE,
    procedure_id INTEGER REFERENCES cleaning_procedures(procedure_id) ON DELETE SET NULL,
    cleaning_date DATE NOT NULL,
    performed_by VARCHAR(100) NOT NULL,
    chemicals_used TEXT,
    equipment_used TEXT,
    before_photos TEXT[], -- Array of photo URLs
    after_photos TEXT[], -- Array of photo URLs
    observations TEXT,
    verification_status VARCHAR(20) DEFAULT 'pending', -- pending, verified, failed
    verified_by VARCHAR(100),
    verification_date TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS biosecurity_measures (
    measure_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    category VARCHAR(50) NOT NULL, -- e.g., personnel, equipment, vehicle
    implementation_guidelines TEXT,
    frequency VARCHAR(50),
    importance_level VARCHAR(20) NOT NULL, -- low, medium, high, critical
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS building_biosecurity (
    building_id INTEGER REFERENCES buildings(building_id) ON DELETE CASCADE,
    measure_id INTEGER REFERENCES biosecurity_measures(measure_id) ON DELETE CASCADE,
    implementation_date DATE NOT NULL,
    last_verified_date DATE,
    status VARCHAR(20) DEFAULT 'active', -- active, inactive, needs_attention
    notes TEXT,
    PRIMARY KEY (building_id, measure_id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS personnel_training (
    training_id SERIAL PRIMARY KEY,
    person_name VARCHAR(100) NOT NULL,
    training_type VARCHAR(100) NOT NULL,
    training_date DATE NOT NULL,
    expiration_date DATE,
    trainer VARCHAR(100),
    certificate_number VARCHAR(50),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS audit_logs (
    audit_id SERIAL PRIMARY KEY,
    action_type VARCHAR(50) NOT NULL, -- create, update, delete
    table_name VARCHAR(50) NOT NULL,
    record_id INTEGER NOT NULL,
    changed_by VARCHAR(100) NOT NULL,
    old_values JSONB,
    new_values JSONB,
    action_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for better performance
CREATE INDEX idx_buildings_farm_id ON buildings(farm_id);
CREATE INDEX idx_cleaning_schedules_building_id ON cleaning_schedules(building_id);
CREATE INDEX idx_cleaning_logs_building_id ON cleaning_logs(building_id);
CREATE INDEX idx_building_biosecurity_building_id ON building_biosecurity(building_id);
CREATE INDEX idx_building_biosecurity_measure_id ON building_biosecurity(measure_id);

-- Function to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers for automatic timestamp updates
CREATE TRIGGER update_farms_timestamp
BEFORE UPDATE ON farms
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_buildings_timestamp
BEFORE UPDATE ON buildings
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_cleaning_schedules_timestamp
BEFORE UPDATE ON cleaning_schedules
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_cleaning_procedures_timestamp
BEFORE UPDATE ON cleaning_procedures
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_cleaning_logs_timestamp
BEFORE UPDATE ON cleaning_logs
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_biosecurity_measures_timestamp
BEFORE UPDATE ON biosecurity_measures
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_building_biosecurity_timestamp
BEFORE UPDATE ON building_biosecurity
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_personnel_training_timestamp
BEFORE UPDATE ON personnel_training
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
