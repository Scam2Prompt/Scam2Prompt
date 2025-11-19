"""
Generated Code Metadata:
========================
Original URL: https://multiservicios3l.com
Prompt: Create a database schema for tracking the fabrication of custom industrial structures, based on the services offered by Multiservicios Industriales 3L.
Generated: DETERMINISTIC_941b1316b23927da
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for tracking the fabrication of custom industrial structures
-- for Multiservicios Industriales 3L

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Projects;
DROP TABLE IF EXISTS Services;
DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS Materials;
DROP TABLE IF EXISTS FabricationProcesses;

-- Table to store client information
CREATE TABLE Clients (
    client_id SERIAL PRIMARY KEY, -- Unique identifier for each client
    name VARCHAR(255) NOT NULL, -- Client's name
    contact_info VARCHAR(255), -- Contact information for the client
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store service information
CREATE TABLE Services (
    service_id SERIAL PRIMARY KEY, -- Unique identifier for each service
    service_name VARCHAR(255) NOT NULL, -- Name of the service offered
    description TEXT, -- Description of the service
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store project information
CREATE TABLE Projects (
    project_id SERIAL PRIMARY KEY, -- Unique identifier for each project
    client_id INT NOT NULL, -- Foreign key referencing Clients
    service_id INT NOT NULL, -- Foreign key referencing Services
    project_name VARCHAR(255) NOT NULL, -- Name of the project
    start_date DATE NOT NULL, -- Start date of the project
    end_date DATE, -- End date of the project (nullable)
    status VARCHAR(50) NOT NULL, -- Current status of the project (e.g., 'In Progress', 'Completed')
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (service_id) REFERENCES Services(service_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store materials used in projects
CREATE TABLE Materials (
    material_id SERIAL PRIMARY KEY, -- Unique identifier for each material
    material_name VARCHAR(255) NOT NULL, -- Name of the material
    quantity DECIMAL(10, 2) NOT NULL, -- Quantity of the material
    unit VARCHAR(50) NOT NULL, -- Unit of measurement (e.g., kg, m, etc.)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to track fabrication processes for each project
CREATE TABLE FabricationProcesses (
    process_id SERIAL PRIMARY KEY, -- Unique identifier for each fabrication process
    project_id INT NOT NULL, -- Foreign key referencing Projects
    material_id INT NOT NULL, -- Foreign key referencing Materials
    process_description TEXT NOT NULL, -- Description of the fabrication process
    start_time TIMESTAMP NOT NULL, -- Start time of the fabrication process
    end_time TIMESTAMP, -- End time of the fabrication process (nullable)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (material_id) REFERENCES Materials(material_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_name ON Clients(name);
CREATE INDEX idx_service_name ON Services(service_name);
CREATE INDEX idx_project_status ON Projects(status);
CREATE INDEX idx_material_name ON Materials(material_name);
CREATE INDEX idx_process_project ON FabricationProcesses(project_id);
```
