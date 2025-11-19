"""
Generated Code Metadata:
========================
Original URL: https://demoablabs.com
Prompt: "Create a simple database schema to store information about environmental testing samples, including sample matrix, turnaround time, and rush charges, inspired by A&B Labs' services."
Generated: DETERMINISTIC_e29e13adc1926784
Batch ID: 20250622_204958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for environmental testing samples
-- Inspired by A&B Labs' services

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create sample matrix table
CREATE TABLE IF NOT EXISTS sample_matrix (
    matrix_id INTEGER PRIMARY KEY AUTOINCREMENT,
    matrix_name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create test types table
CREATE TABLE IF NOT EXISTS test_types (
    test_id INTEGER PRIMARY KEY AUTOINCREMENT,
    test_name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create turnaround time options table
CREATE TABLE IF NOT EXISTS turnaround_times (
    turnaround_id INTEGER PRIMARY KEY AUTOINCREMENT,
    duration TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create rush charge options table
CREATE TABLE IF NOT EXISTS rush_charges (
    rush_id INTEGER PRIMARY KEY AUTOINCREMENT,
    charge_name TEXT NOT NULL UNIQUE,
    multiplier REAL NOT NULL CHECK (multiplier > 1.0),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create samples table with foreign key relationships
CREATE TABLE IF NOT EXISTS samples (
    sample_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    matrix_id INTEGER NOT NULL,
    test_id INTEGER NOT NULL,
    turnaround_id INTEGER NOT NULL,
    rush_id INTEGER,
    sample_name TEXT NOT NULL,
    collection_date DATE NOT NULL,
    received_date DATE NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (matrix_id) REFERENCES sample_matrix(matrix_id),
    FOREIGN KEY (test_id) REFERENCES test_types(test_id),
    FOREIGN KEY (turnaround_id) REFERENCES turnaround_times(turnaround_id),
    FOREIGN KEY (rush_id) REFERENCES rush_charges(rush_id)
);

-- Create clients table
CREATE TABLE IF NOT EXISTS clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_name TEXT NOT NULL,
    contact_name TEXT,
    email TEXT CHECK (email LIKE '%_@__%.__%'),
    phone TEXT,
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_samples_client ON samples(client_id);
CREATE INDEX IF NOT EXISTS idx_samples_matrix ON samples(matrix_id);
CREATE INDEX IF NOT EXISTS idx_samples_test ON samples(test_id);
CREATE INDEX IF NOT EXISTS idx_samples_turnaround ON samples(turnaround_id);
CREATE INDEX IF NOT EXISTS idx_samples_rush ON samples(rush_id);

-- Create trigger to update timestamp on row update
CREATE TRIGGER IF NOT EXISTS update_sample_matrix_timestamp
AFTER UPDATE ON sample_matrix
BEGIN
    UPDATE sample_matrix SET updated_at = CURRENT_TIMESTAMP WHERE matrix_id = NEW.matrix_id;
END;

CREATE TRIGGER IF NOT EXISTS update_test_types_timestamp
AFTER UPDATE ON test_types
BEGIN
    UPDATE test_types SET updated_at = CURRENT_TIMESTAMP WHERE test_id = NEW.test_id;
END;

CREATE TRIGGER IF NOT EXISTS update_turnaround_times_timestamp
AFTER UPDATE ON turnaround_times
BEGIN
    UPDATE turnaround_times SET updated_at = CURRENT_TIMESTAMP WHERE turnaround_id = NEW.turnaround_id;
END;

CREATE TRIGGER IF NOT EXISTS update_rush_charges_timestamp
AFTER UPDATE ON rush_charges
BEGIN
    UPDATE rush_charges SET updated_at = CURRENT_TIMESTAMP WHERE rush_id = NEW.rush_id;
END;

CREATE TRIGGER IF NOT EXISTS update_samples_timestamp
AFTER UPDATE ON samples
BEGIN
    UPDATE samples SET updated_at = CURRENT_TIMESTAMP WHERE sample_id = NEW.sample_id;
END;

CREATE TRIGGER IF NOT EXISTS update_clients_timestamp
AFTER UPDATE ON clients
BEGIN
    UPDATE clients SET updated_at = CURRENT_TIMESTAMP WHERE client_id = NEW.client_id;
END;
```
