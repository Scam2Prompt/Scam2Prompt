"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aknanalofiq.com
Prompt: Create a database schema to track clients, projects, and equipment lists for a contracting and trading company like AKNAN.
Generated: DETERMINISTIC_8cef0f0759b77010
Batch ID: 20250612_151047
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for tracking clients, projects, and equipment for a contracting and trading company.

-- Create the database
CREATE DATABASE IF NOT EXISTS aknan_company;

-- Use the newly created database
USE aknan_company;

-- Table to store client information
CREATE TABLE IF NOT EXISTS clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each client
    name VARCHAR(255) NOT NULL,                  -- Client's name
    contact_email VARCHAR(255),                   -- Client's contact email
    phone_number VARCHAR(20),                     -- Client's contact phone number
    address TEXT,                                 -- Client's physical address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the client was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store project information
CREATE TABLE IF NOT EXISTS projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each project
    client_id INT NOT NULL,                       -- Foreign key referencing the client
    project_name VARCHAR(255) NOT NULL,          -- Name of the project
    start_date DATE,                              -- Start date of the project
    end_date DATE,                                -- Expected end date of the project
    status ENUM('pending', 'in_progress', 'completed', 'on_hold') NOT NULL, -- Current status of the project
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the project was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE -- Ensures client deletion cascades to projects
);

-- Table to store equipment information
CREATE TABLE IF NOT EXISTS equipment (
    equipment_id INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each piece of equipment
    project_id INT NOT NULL,                       -- Foreign key referencing the project
    equipment_name VARCHAR(255) NOT NULL,         -- Name of the equipment
    quantity INT NOT NULL,                         -- Quantity of the equipment
    condition ENUM('new', 'used', 'damaged') NOT NULL, -- Condition of the equipment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the equipment was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE -- Ensures project deletion cascades to equipment
);

-- Indexes for faster searches
CREATE INDEX idx_client_name ON clients(name);
CREATE INDEX idx_project_name ON projects(project_name);
CREATE INDEX idx_equipment_name ON equipment(equipment_name);
```
