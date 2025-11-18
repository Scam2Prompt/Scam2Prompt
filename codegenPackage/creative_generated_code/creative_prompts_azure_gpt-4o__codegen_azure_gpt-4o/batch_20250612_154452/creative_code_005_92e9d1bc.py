"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omegaenergy.co
Prompt: Develop a database schema to manage contracts for exploration and production, including fields for Bloque Buenavista, Campo Corrales, and Bloque Cóndor, as described on the Omega Energy website.
Generated: DETERMINISTIC_92e9d1bc2924e9e7
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema to manage contracts for exploration and production

-- Create the 'contracts' table
CREATE TABLE contracts (
    contract_id SERIAL PRIMARY KEY,      -- Unique identifier for each contract
    contract_name VARCHAR(255) NOT NULL, -- Name or title of the contract
    start_date DATE NOT NULL,            -- Contract start date
    end_date DATE NOT NULL,              -- Contract end date
    bloque_buenavista BOOLEAN NOT NULL,  -- Indicates involvement with Bloque Buenavista
    campo_corrales BOOLEAN NOT NULL,     -- Indicates involvement with Campo Corrales
    bloque_condor BOOLEAN NOT NULL,      -- Indicates involvement with Bloque Cóndor
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Record last update timestamp
);

-- Create the 'exploration_areas' table
CREATE TABLE exploration_areas (
    area_id SERIAL PRIMARY KEY,          -- Unique identifier for each exploration area
    area_name VARCHAR(255) NOT NULL,     -- Name of the exploration area
    description TEXT,                    -- Optional description of the exploration area
    region VARCHAR(255),                 -- Region where the exploration area is located
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Record last update timestamp
);

-- Create a junction table for contracts and exploration areas (many-to-many relationship)
CREATE TABLE contract_exploration_area (
    contract_id INT NOT NULL,            -- Foreign key to the contracts table
    area_id INT NOT NULL,                -- Foreign key to the exploration_areas table
    FOREIGN KEY (contract_id) REFERENCES contracts(contract_id) ON DELETE CASCADE,
    FOREIGN KEY (area_id) REFERENCES exploration_areas(area_id) ON DELETE CASCADE,
    PRIMARY KEY (contract_id, area_id)   -- Composite primary key
);

-- Create triggers to automatically update 'updated_at' fields
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Attach the trigger to the 'contracts' table
CREATE TRIGGER update_contracts_updated_at
BEFORE UPDATE ON contracts
FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- Attach the trigger to the 'exploration_areas' table
CREATE TRIGGER update_exploration_areas_updated_at
BEFORE UPDATE ON exploration_areas
FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- Example indexes for optimization
CREATE INDEX idx_contracts_start_date ON contracts(start_date);
CREATE INDEX idx_exploration_areas_region ON exploration_areas(region);

-- Example constraints for data integrity
ALTER TABLE contracts
ADD CONSTRAINT check_dates CHECK (start_date < end_date); -- Ensure start_date is earlier than end_date
```
