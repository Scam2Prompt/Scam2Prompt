"""
Generated Code Metadata:
========================
Original URL: https://thedesignumbrella.in
Prompt: "Design a database schema for storing and managing projects, clients, and services for a design studio like The Design Umbrella, incorporating details such as project analysis, site study, and materials selection."
Generated: DETERMINISTIC_b3f6411ac786d1a7
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a design studio to manage projects, clients, and services

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS Project;
DROP TABLE IF EXISTS Client;
DROP TABLE IF EXISTS Service;
DROP TABLE IF EXISTS ProjectService;

-- Table to store client information
CREATE TABLE Client (
    client_id SERIAL PRIMARY KEY,          -- Unique identifier for each client
    name VARCHAR(100) NOT NULL,            -- Client's name
    contact_email VARCHAR(100) UNIQUE NOT NULL, -- Client's contact email
    phone_number VARCHAR(15),               -- Client's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store project information
CREATE TABLE Project (
    project_id SERIAL PRIMARY KEY,          -- Unique identifier for each project
    client_id INT NOT NULL,                 -- Foreign key referencing Client
    project_name VARCHAR(100) NOT NULL,     -- Name of the project
    project_description TEXT,                -- Detailed description of the project
    project_status VARCHAR(50) DEFAULT 'Pending', -- Current status of the project
    analysis TEXT,                           -- Project analysis details
    site_study TEXT,                         -- Site study details
    materials_selection TEXT,                -- Selected materials for the project
    start_date DATE,                         -- Project start date
    end_date DATE,                           -- Project end date
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (client_id) REFERENCES Client(client_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store services offered by the design studio
CREATE TABLE Service (
    service_id SERIAL PRIMARY KEY,           -- Unique identifier for each service
    service_name VARCHAR(100) NOT NULL,      -- Name of the service
    service_description TEXT,                 -- Description of the service
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Junction table to manage many-to-many relationships between projects and services
CREATE TABLE ProjectService (
    project_service_id SERIAL PRIMARY KEY,   -- Unique identifier for each project-service relationship
    project_id INT NOT NULL,                  -- Foreign key referencing Project
    service_id INT NOT NULL,                  -- Foreign key referencing Service
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (project_id) REFERENCES Project(project_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (service_id) REFERENCES Service(service_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_name ON Client(name);
CREATE INDEX idx_project_name ON Project(project_name);
CREATE INDEX idx_service_name ON Service(service_name);
```
