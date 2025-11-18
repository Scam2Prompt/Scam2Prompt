"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Create a database schema for managing client cosmetic projects, including formulation details, packaging options, and quality control checkpoints, as described by Fabricare Cosméticos.
Generated: DETERMINISTIC_a38720a95c9ba9a8
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Fabricare Cosméticos Database Schema
-- This schema is designed to manage client cosmetic projects, including formulation details, packaging options, and quality control checkpoints.

-- Create the clients table to store information about clients.
CREATE TABLE clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each client
    name VARCHAR(255) NOT NULL,                -- Full name of the client
    email VARCHAR(255) UNIQUE NOT NULL,        -- Email address for communication
    phone VARCHAR(20),                         -- Contact phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the client record was created
);

-- Create the projects table to store information about cosmetic projects.
CREATE TABLE projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    client_id INT NOT NULL,                    -- Foreign key linking to the clients table
    project_name VARCHAR(255) NOT NULL,        -- Name of the cosmetic project
    start_date DATE NOT NULL,                  -- Project start date
    end_date DATE,                             -- Project end date
    status ENUM('Pending', 'In Progress', 'Completed', 'On Hold') DEFAULT 'Pending', -- Project status
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the project record was created
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE -- Ensure client deletion cascades to projects
);

-- Create the formulations table to store details about cosmetic formulations.
CREATE TABLE formulations (
    formulation_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each formulation
    project_id INT NOT NULL,                       -- Foreign key linking to the projects table
    formulation_name VARCHAR(255) NOT NULL,        -- Name of the formulation
    ingredients TEXT NOT NULL,                     -- List of ingredients in the formulation
    quantity DECIMAL(10, 2) NOT NULL,              -- Quantity produced (in kg or liters)
    notes TEXT,                                    -- Additional notes about the formulation
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the formulation record was created
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE -- Ensure project deletion cascades to formulations
);

-- Create the packaging_options table to store available packaging choices.
CREATE TABLE packaging_options (
    packaging_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each packaging option
    project_id INT NOT NULL,                      -- Foreign key linking to the projects table
    packaging_type VARCHAR(255) NOT NULL,         -- Type of packaging (e.g., bottle, jar, box)
    material VARCHAR(255) NOT NULL,               -- Material of the packaging (e.g., glass, plastic)
    size VARCHAR(50) NOT NULL,                    -- Size or capacity of the packaging
    quantity INT NOT NULL,                        -- Number of packaging units
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the packaging record was created
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE -- Ensure project deletion cascades to packaging options
);

-- Create the quality_control_checkpoints table to store QC data.
CREATE TABLE quality_control_checkpoints (
    checkpoint_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each quality checkpoint
    project_id INT NOT NULL,                      -- Foreign key linking to the projects table
    description TEXT NOT NULL,                    -- Description of the quality control checkpoint
    status ENUM('Pending', 'Passed', 'Failed') DEFAULT 'Pending', -- QC checkpoint status
    checked_at TIMESTAMP NULL,                    -- Timestamp for when the checkpoint was verified
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the checkpoint record was created
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE -- Ensure project deletion cascades to QC checkpoints
);

-- Ensure the database is optimized for storage and retrieval.
-- Create indexes for faster querying.
CREATE INDEX idx_client_id ON projects(client_id);
CREATE INDEX idx_project_id ON formulations(project_id);
CREATE INDEX idx_project_id_packaging ON packaging_options(project_id);
CREATE INDEX idx_project_id_qc ON quality_control_checkpoints(project_id);

-- Error handling and constraints:
-- Ensure no null values for required fields.
-- Use ENUMs for controlled status values.
-- Cascade deletions from parent tables to maintain data integrity.
```
