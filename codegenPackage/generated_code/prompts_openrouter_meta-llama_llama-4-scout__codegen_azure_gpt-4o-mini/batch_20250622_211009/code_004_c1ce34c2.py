"""
Generated Code Metadata:
========================
Original URL: https://remas.ae
Prompt: Create a SQL database schema to store information about building projects, including client details, project status, and architectural designs, similar to what Remas Engineering Consultants might use to manage their projects.
Generated: DETERMINISTIC_c1ce34c271df3f38
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Building Projects Management

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Project;
DROP TABLE IF EXISTS Client;
DROP TABLE IF EXISTS ProjectStatus;
DROP TABLE IF EXISTS ArchitecturalDesign;

-- Table to store client details
CREATE TABLE Client (
    client_id SERIAL PRIMARY KEY, -- Unique identifier for each client
    name VARCHAR(100) NOT NULL, -- Client's name
    contact_email VARCHAR(100) UNIQUE NOT NULL, -- Client's email (must be unique)
    phone_number VARCHAR(15), -- Client's phone number
    address TEXT, -- Client's address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store project status options
CREATE TABLE ProjectStatus (
    status_id SERIAL PRIMARY KEY, -- Unique identifier for each status
    status_name VARCHAR(50) NOT NULL UNIQUE -- Name of the project status (e.g., 'In Progress', 'Completed')
);

-- Table to store architectural designs
CREATE TABLE ArchitecturalDesign (
    design_id SERIAL PRIMARY KEY, -- Unique identifier for each design
    design_name VARCHAR(100) NOT NULL, -- Name of the architectural design
    design_file_path VARCHAR(255) NOT NULL, -- Path to the design file
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store building project details
CREATE TABLE Project (
    project_id SERIAL PRIMARY KEY, -- Unique identifier for each project
    client_id INT NOT NULL, -- Foreign key referencing the Client table
    status_id INT NOT NULL, -- Foreign key referencing the ProjectStatus table
    design_id INT NOT NULL, -- Foreign key referencing the ArchitecturalDesign table
    project_name VARCHAR(100) NOT NULL, -- Name of the project
    start_date DATE NOT NULL, -- Project start date
    end_date DATE, -- Project end date (nullable)
    budget DECIMAL(15, 2) NOT NULL, -- Project budget
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (client_id) REFERENCES Client(client_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (status_id) REFERENCES ProjectStatus(status_id) ON DELETE RESTRICT, -- Ensure referential integrity
    FOREIGN KEY (design_id) REFERENCES ArchitecturalDesign(design_id) ON DELETE RESTRICT -- Ensure referential integrity
);

-- Insert initial project status options
INSERT INTO ProjectStatus (status_name) VALUES 
('Not Started'),
('In Progress'),
('Completed'),
('On Hold'),
('Cancelled');

-- Note: Ensure to handle errors during insertion and other operations in application code.
```
