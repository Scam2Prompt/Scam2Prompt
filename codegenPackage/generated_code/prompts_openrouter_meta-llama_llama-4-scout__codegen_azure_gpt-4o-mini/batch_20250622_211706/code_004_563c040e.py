"""
Generated Code Metadata:
========================
Original URL: https://kowlaung.go.th
Prompt: Design a database schema for storing information about local government projects and initiatives in Khao Luang Subdistrict, including tables for project details, funding, and responsible agencies.
Generated: DETERMINISTIC_563c040e62422d5b
Batch ID: 20250622_211706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about local government projects and initiatives in Khao Luang Subdistrict

-- Create a table for storing project details
CREATE TABLE Projects (
    project_id SERIAL PRIMARY KEY, -- Unique identifier for each project
    project_name VARCHAR(255) NOT NULL, -- Name of the project
    description TEXT, -- Description of the project
    start_date DATE NOT NULL, -- Start date of the project
    end_date DATE, -- End date of the project (nullable)
    status VARCHAR(50) NOT NULL CHECK (status IN ('Planned', 'In Progress', 'Completed', 'On Hold')), -- Current status of the project
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the project was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the project was last updated
);

-- Create a table for storing funding information
CREATE TABLE Funding (
    funding_id SERIAL PRIMARY KEY, -- Unique identifier for each funding record
    project_id INT NOT NULL, -- Foreign key referencing the Projects table
    amount DECIMAL(15, 2) NOT NULL, -- Amount of funding allocated
    funding_source VARCHAR(255) NOT NULL, -- Source of the funding
    funding_date DATE NOT NULL, -- Date when the funding was allocated
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for storing responsible agencies
CREATE TABLE Agencies (
    agency_id SERIAL PRIMARY KEY, -- Unique identifier for each agency
    agency_name VARCHAR(255) NOT NULL, -- Name of the agency
    contact_info VARCHAR(255), -- Contact information for the agency (nullable)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the agency was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the agency was last updated
);

-- Create a junction table to associate projects with responsible agencies
CREATE TABLE ProjectAgencies (
    project_agency_id SERIAL PRIMARY KEY, -- Unique identifier for each association
    project_id INT NOT NULL, -- Foreign key referencing the Projects table
    agency_id INT NOT NULL, -- Foreign key referencing the Agencies table
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (agency_id) REFERENCES Agencies(agency_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_project_name ON Projects(project_name);
CREATE INDEX idx_agency_name ON Agencies(agency_name);
CREATE INDEX idx_funding_source ON Funding(funding_source);
```
