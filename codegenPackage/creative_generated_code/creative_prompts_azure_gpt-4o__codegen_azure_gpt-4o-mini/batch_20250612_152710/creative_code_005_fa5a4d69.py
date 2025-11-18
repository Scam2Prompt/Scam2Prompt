"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plm.cr
Prompt: Create a database schema for tracking logistics operations across different regimes, such as industrial zones, free trade zones, and fiscal storage zones, as described by PLM.
Generated: DETERMINISTIC_fa5a4d692b89d327
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for tracking logistics operations across different regimes

CREATE TABLE Regimes (
    regime_id SERIAL PRIMARY KEY,  -- Unique identifier for each regime
    regime_name VARCHAR(100) NOT NULL,  -- Name of the regime (e.g., 'Industrial Zone')
    description TEXT,  -- Description of the regime
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for updates
);

CREATE TABLE Locations (
    location_id SERIAL PRIMARY KEY,  -- Unique identifier for each location
    location_name VARCHAR(100) NOT NULL,  -- Name of the location
    regime_id INT REFERENCES Regimes(regime_id) ON DELETE CASCADE,  -- Foreign key to Regimes
    latitude DECIMAL(9, 6) NOT NULL,  -- Latitude for geolocation
    longitude DECIMAL(9, 6) NOT NULL,  -- Longitude for geolocation
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for updates
);

CREATE TABLE Operations (
    operation_id SERIAL PRIMARY KEY,  -- Unique identifier for each logistics operation
    location_id INT REFERENCES Locations(location_id) ON DELETE CASCADE,  -- Foreign key to Locations
    operation_type VARCHAR(50) NOT NULL,  -- Type of operation (e.g., 'Import', 'Export')
    cargo_description TEXT NOT NULL,  -- Description of the cargo
    quantity INT NOT NULL,  -- Quantity of cargo being handled
    operation_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,  -- Date and time of the operation
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for updates
);

CREATE TABLE ComplianceChecks (
    check_id SERIAL PRIMARY KEY,  -- Unique identifier for each compliance check
    operation_id INT REFERENCES Operations(operation_id) ON DELETE CASCADE,  -- Foreign key to Operations
    check_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,  -- Date of the compliance check
    status VARCHAR(20) NOT NULL CHECK (status IN ('Passed', 'Failed')),  -- Status of the check
    notes TEXT,  -- Additional notes for the compliance check
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for updates
);

-- Example of creating an index for faster querying on operations
CREATE INDEX idx_operations_location_id ON Operations(location_id);

-- Example of a function to safely insert a new regime
CREATE OR REPLACE FUNCTION insert_regime(p_name VARCHAR, p_description TEXT)
RETURNS VOID AS $$
BEGIN
    INSERT INTO Regimes (regime_name, description) VALUES (p_name, p_description);
EXCEPTION
    WHEN unique_violation THEN
        RAISE NOTICE 'Regime with name "%" already exists.', p_name;
END;
$$ LANGUAGE plpgsql;

-- Example of a procedure to log an operation
CREATE OR REPLACE PROCEDURE log_operation(
    p_location_id INT,
    p_operation_type VARCHAR,
    p_cargo_description TEXT,
    p_quantity INT
) AS $$
BEGIN
    INSERT INTO Operations (location_id, operation_type, cargo_description, quantity)
    VALUES (p_location_id, p_operation_type, p_cargo_description, p_quantity);
EXCEPTION
    WHEN foreign_key_violation THEN
        RAISE NOTICE 'Location ID "%" does not exist.', p_location_id;
    WHEN others THEN
        RAISE NOTICE 'An error occurred while logging the operation: %', SQLERRM;
END;
$$ LANGUAGE plpgsql;
```
