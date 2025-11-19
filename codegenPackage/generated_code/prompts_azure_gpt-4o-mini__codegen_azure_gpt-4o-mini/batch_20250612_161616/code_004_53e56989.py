"""
Generated Code Metadata:
========================
Original URL: https://ntalo.co.za
Prompt: Illustrate how to implement a database schema for storing information about construction projects and equipment hire, taking cues from the comprehensive services offered by Ntalo Investments.
Generated: DETERMINISTIC_53e5698916cb472f
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for storing information about construction projects and equipment hire

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Equipment;
DROP TABLE IF EXISTS Projects;
DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS Equipment_Hire;

-- Create a table to store client information
CREATE TABLE Clients (
    client_id SERIAL PRIMARY KEY, -- Unique identifier for each client
    name VARCHAR(100) NOT NULL, -- Client's name
    contact_info VARCHAR(255), -- Client's contact information
    address VARCHAR(255), -- Client's address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Create a table to store construction project information
CREATE TABLE Projects (
    project_id SERIAL PRIMARY KEY, -- Unique identifier for each project
    client_id INT NOT NULL, -- Foreign key referencing Clients
    project_name VARCHAR(100) NOT NULL, -- Name of the project
    start_date DATE NOT NULL, -- Start date of the project
    end_date DATE, -- End date of the project (nullable)
    budget DECIMAL(15, 2) NOT NULL, -- Budget allocated for the project
    status VARCHAR(50) NOT NULL, -- Current status of the project (e.g., ongoing, completed)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table to store equipment information
CREATE TABLE Equipment (
    equipment_id SERIAL PRIMARY KEY, -- Unique identifier for each piece of equipment
    equipment_name VARCHAR(100) NOT NULL, -- Name of the equipment
    equipment_type VARCHAR(50) NOT NULL, -- Type of equipment (e.g., excavator, crane)
    purchase_date DATE NOT NULL, -- Date when the equipment was purchased
    condition VARCHAR(50) NOT NULL, -- Condition of the equipment (e.g., new, used)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Create a table to store equipment hire information
CREATE TABLE Equipment_Hire (
    hire_id SERIAL PRIMARY KEY, -- Unique identifier for each hire record
    equipment_id INT NOT NULL, -- Foreign key referencing Equipment
    project_id INT NOT NULL, -- Foreign key referencing Projects
    hire_start_date DATE NOT NULL, -- Start date of the hire period
    hire_end_date DATE NOT NULL, -- End date of the hire period
    cost DECIMAL(15, 2) NOT NULL, -- Cost of the hire
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (equipment_id) REFERENCES Equipment(equipment_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes can be added for performance optimization if necessary
CREATE INDEX idx_client_name ON Clients(name);
CREATE INDEX idx_project_status ON Projects(status);
CREATE INDEX idx_equipment_type ON Equipment(equipment_type);
```
