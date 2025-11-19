"""
Generated Code Metadata:
========================
Original URL: https://espinelycia.com
Prompt: "Design a simple database schema to store information about hydraulic, sanitary, gas, and firefighting networks, including their designs, constructions, and maintenance records, inspired by the services offered by Espinel y Cia."
Generated: DETERMINISTIC_e6432d87387fc3ee
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for utility networks management system
-- Tables for storing hydraulic, sanitary, gas, and firefighting networks information

-- Main network types table
CREATE TABLE network_types (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Projects table
CREATE TABLE projects (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    start_date DATE,
    end_date DATE,
    status VARCHAR(20) CHECK (status IN ('planned', 'in_progress', 'completed', 'cancelled')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Network segments table
CREATE TABLE network_segments (
    id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(id) ON DELETE CASCADE,
    network_type_id INTEGER REFERENCES network_types(id) ON DELETE RESTRICT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    location GEOGRAPHY(POINT, 4326),
    length DECIMAL(10, 2),
    diameter DECIMAL(10, 2),
    material VARCHAR(50),
    installation_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Design documents table
CREATE TABLE design_documents (
    id SERIAL PRIMARY KEY,
    segment_id INTEGER REFERENCES network_segments(id) ON DELETE CASCADE,
    document_name VARCHAR(100) NOT NULL,
    document_type VARCHAR(50),
    file_path VARCHAR(255) NOT NULL,
    version VARCHAR(20),
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100),
    notes TEXT
);

-- Construction records table
CREATE TABLE construction_records (
    id SERIAL PRIMARY KEY,
    segment_id INTEGER REFERENCES network_segments(id) ON DELETE CASCADE,
    contractor_name VARCHAR(100),
    start_date DATE,
    end_date DATE,
    cost DECIMAL(15, 2),
    status VARCHAR(20) CHECK (status IN ('planned', 'in_progress', 'completed', 'delayed')),
    inspection_date DATE,
    inspector_name VARCHAR(100),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Maintenance records table
CREATE TABLE maintenance_records (
    id SERIAL PRIMARY KEY,
    segment_id INTEGER REFERENCES network_segments(id) ON DELETE CASCADE,
    maintenance_type VARCHAR(50) NOT NULL,
    description TEXT,
    performed_by VARCHAR(100),
    maintenance_date DATE NOT NULL,
    next_maintenance_date DATE,
    cost DECIMAL(15, 2),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Issues/defects table
CREATE TABLE network_issues (
    id SERIAL PRIMARY KEY,
    segment_id INTEGER REFERENCES network_segments(id) ON DELETE CASCADE,
    issue_type VARCHAR(50) NOT NULL,
    severity VARCHAR(20) CHECK (severity IN ('low', 'medium', 'high', 'critical')),
    description TEXT,
    reported_date DATE NOT NULL,
    resolved_date DATE,
    resolution_method TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert default network types
INSERT INTO network_types (name, description) VALUES 
('Hydraulic', 'Water supply and distribution networks'),
('Sanitary', 'Sewage and wastewater networks'),
('Gas', 'Natural gas distribution networks'),
('Firefighting', 'Fire protection and suppression systems');
```
