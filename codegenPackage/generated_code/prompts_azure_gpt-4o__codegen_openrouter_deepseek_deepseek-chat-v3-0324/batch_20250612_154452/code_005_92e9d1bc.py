"""
Generated Code Metadata:
========================
Original URL: https://omegaenergy.co
Prompt: Develop a database schema to manage contracts for exploration and production, including fields for Bloque Buenavista, Campo Corrales, and Bloque Cóndor, as described on the Omega Energy website.
Generated: DETERMINISTIC_92e9d1bc2924e9e7
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing exploration and production contracts
-- Includes tables for blocks, fields, contracts, and related entities

-- Table for storing contract information
CREATE TABLE contracts (
    contract_id SERIAL PRIMARY KEY,
    contract_name VARCHAR(100) NOT NULL,
    contract_number VARCHAR(50) UNIQUE NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL CHECK (status IN ('Active', 'Inactive', 'Pending', 'Terminated')),
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_dates CHECK (end_date > start_date)
);

-- Table for storing block information
CREATE TABLE blocks (
    block_id SERIAL PRIMARY KEY,
    block_name VARCHAR(100) NOT NULL,
    location VARCHAR(255) NOT NULL,
    area_km2 DECIMAL(10, 2) NOT NULL,
    status VARCHAR(20) NOT NULL CHECK (status IN ('Exploration', 'Development', 'Production', 'Abandoned')),
    contract_id INTEGER REFERENCES contracts(contract_id) ON DELETE SET NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing field information
CREATE TABLE fields (
    field_id SERIAL PRIMARY KEY,
    field_name VARCHAR(100) NOT NULL,
    block_id INTEGER REFERENCES blocks(block_id) ON DELETE CASCADE,
    estimated_reserves DECIMAL(12, 2),
    production_capacity DECIMAL(10, 2),
    status VARCHAR(20) NOT NULL CHECK (status IN ('Producing', 'Shut-in', 'Abandoned', 'Development')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing production data
CREATE TABLE production_data (
    production_id SERIAL PRIMARY KEY,
    field_id INTEGER REFERENCES fields(field_id) ON DELETE CASCADE,
    production_date DATE NOT NULL,
    oil_volume DECIMAL(10, 2) NOT NULL,
    gas_volume DECIMAL(10, 2) NOT NULL,
    water_volume DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_production_per_field_per_day UNIQUE (field_id, production_date)
);

-- Table for storing exploration activities
CREATE TABLE exploration_activities (
    activity_id SERIAL PRIMARY KEY,
    block_id INTEGER REFERENCES blocks(block_id) ON DELETE CASCADE,
    activity_type VARCHAR(50) NOT NULL CHECK (activity_type IN ('Seismic', 'Drilling', 'Survey', 'Other')),
    start_date DATE NOT NULL,
    end_date DATE,
    status VARCHAR(20) NOT NULL CHECK (status IN ('Planned', 'In Progress', 'Completed', 'Cancelled')),
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_exploration_dates CHECK (end_date IS NULL OR end_date >= start_date)
);

-- Table for storing documents related to contracts
CREATE TABLE contract_documents (
    document_id SERIAL PRIMARY KEY,
    contract_id INTEGER REFERENCES contracts(contract_id) ON DELETE CASCADE,
    document_name VARCHAR(255) NOT NULL,
    document_type VARCHAR(50) NOT NULL,
    file_path VARCHAR(512) NOT NULL,
    upload_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    description TEXT
);

-- Indexes for better performance
CREATE INDEX idx_blocks_contract_id ON blocks(contract_id);
CREATE INDEX idx_fields_block_id ON fields(block_id);
CREATE INDEX idx_production_data_field_id ON production_data(field_id);
CREATE INDEX idx_production_data_date ON production_data(production_date);
CREATE INDEX idx_exploration_activities_block_id ON exploration_activities(block_id);
CREATE INDEX idx_contract_documents_contract_id ON contract_documents(contract_id);

-- Trigger to update the updated_at timestamp on row updates
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Apply the trigger to all tables with updated_at field
CREATE TRIGGER update_contracts_timestamp
BEFORE UPDATE ON contracts
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_blocks_timestamp
BEFORE UPDATE ON blocks
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_fields_timestamp
BEFORE UPDATE ON fields
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_exploration_activities_timestamp
BEFORE UPDATE ON exploration_activities
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

-- Insert initial data for specific blocks mentioned
INSERT INTO contracts (contract_name, contract_number, start_date, end_date, status, description)
VALUES 
    ('Buenavista Contract', 'CNTR-BV-2023', '2023-01-01', '2043-12-31', 'Active', 'Exploration and production contract for Bloque Buenavista'),
    ('Corrales Contract', 'CNTR-CR-2022', '2022-06-15', '2042-06-14', 'Active', 'Production contract for Campo Corrales'),
    ('Condor Contract', 'CNTR-CD-2021', '2021-03-10', '2041-03-09', 'Active', 'Exploration contract for Bloque Cóndor');

INSERT INTO blocks (block_name, location, area_km2, status, contract_id)
VALUES 
    ('Bloque Buenavista', 'Eastern Region, Basin X', 250.75, 'Exploration', 1),
    ('Campo Corrales', 'Western Region, Basin Y', 180.50, 'Production', 2),
    ('Bloque Cóndor', 'Northern Region, Basin Z', 320.25, 'Development', 3);

INSERT INTO fields (field_name, block_id, estimated_reserves, production_capacity, status)
VALUES 
    ('Corrales Main', 2, 5000000.00, 15000.00, 'Producing'),
    ('Corrales West', 2, 2000000.00, 5000.00, 'Producing'),
    ('Condor North', 3, 8000000.00, 0.00, 'Development');
```
