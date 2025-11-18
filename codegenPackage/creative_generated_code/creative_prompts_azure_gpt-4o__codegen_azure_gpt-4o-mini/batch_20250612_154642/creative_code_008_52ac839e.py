"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://e-book.top
Prompt: Develop a database schema for managing client information, project details, and resources in an architectural firm, inspired by Études' comprehensive service offerings.
Generated: DETERMINISTIC_52ac839e40fbd59f
Batch ID: 20250612_154642
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing client information, project details, and resources in an architectural firm

-- Create a database named 'architectural_firm_db'
CREATE DATABASE architectural_firm_db;

-- Use the newly created database
USE architectural_firm_db;

-- Table to store client information
CREATE TABLE Clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each client
    name VARCHAR(100) NOT NULL,                 -- Client's name
    contact_email VARCHAR(255) NOT NULL,        -- Client's email address
    phone_number VARCHAR(15),                    -- Client's phone number
    address TEXT,                                -- Client's address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store project details
CREATE TABLE Projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each project
    client_id INT NOT NULL,                      -- Foreign key referencing the Clients table
    project_name VARCHAR(100) NOT NULL,         -- Name of the project
    start_date DATE NOT NULL,                    -- Project start date
    end_date DATE NOT NULL,                      -- Project end date
    status ENUM('planning', 'in_progress', 'completed', 'on_hold') NOT NULL, -- Project status
    description TEXT,                            -- Project description
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Table to store resource details
CREATE TABLE Resources (
    resource_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each resource
    project_id INT NOT NULL,                     -- Foreign key referencing the Projects table
    resource_name VARCHAR(100) NOT NULL,        -- Name of the resource (e.g., personnel, material)
    resource_type ENUM('personnel', 'material', 'equipment') NOT NULL, -- Type of resource
    quantity INT NOT NULL,                       -- Quantity of the resource
    allocated BOOL DEFAULT FALSE,                -- Resource allocation status
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Example of error handling for data insertion
-- This assumes the use of a stored procedure or application code that handles the exceptions.
-- Ensure to check for foreign key constraints and data integrity when inserting records.

-- Example of inserting a client
INSERT INTO Clients (name, contact_email, phone_number, address) VALUES
('John Doe', 'john.doe@example.com', '123-456-7890', '123 Main St, Anytown, USA');

-- Example of inserting a project
INSERT INTO Projects (client_id, project_name, start_date, end_date, status, description) VALUES
(1, 'New Office Building', '2023-01-01', '2023-12-31', 'in_progress', 'Designing a new office building.');

-- Example of inserting a resource
INSERT INTO Resources (project_id, resource_name, resource_type, quantity, allocated) VALUES
(1, 'Architect John Smith', 'personnel', 1, TRUE);

-- Note: Additional indexes and constraints can be added as per the performance and business requirements.
```
