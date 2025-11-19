"""
Generated Code Metadata:
========================
Original URL: https://pconsultsa.com
Prompt: Design a simple database schema to store information about clients, projects, and outcomes for a consulting firm like PConsultsa.
Generated: DETERMINISTIC_164e27c73f1e33f9
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a consulting firm (PConsultsa)

-- Drop existing tables if they exist to avoid conflicts
DROP TABLE IF EXISTS Outcomes;
DROP TABLE IF EXISTS Projects;
DROP TABLE IF EXISTS Clients;

-- Table to store client information
CREATE TABLE Clients (
    client_id SERIAL PRIMARY KEY,          -- Unique identifier for each client
    name VARCHAR(255) NOT NULL,            -- Client's name
    contact_email VARCHAR(255) UNIQUE NOT NULL, -- Client's contact email
    phone_number VARCHAR(20),               -- Client's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store project information
CREATE TABLE Projects (
    project_id SERIAL PRIMARY KEY,          -- Unique identifier for each project
    client_id INT NOT NULL,                 -- Foreign key referencing Clients
    project_name VARCHAR(255) NOT NULL,     -- Name of the project
    start_date DATE NOT NULL,               -- Project start date
    end_date DATE,                          -- Project end date (nullable)
    status VARCHAR(50) NOT NULL,            -- Current status of the project (e.g., 'In Progress', 'Completed')
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store outcomes of projects
CREATE TABLE Outcomes (
    outcome_id SERIAL PRIMARY KEY,          -- Unique identifier for each outcome
    project_id INT NOT NULL,                -- Foreign key referencing Projects
    outcome_description TEXT NOT NULL,      -- Description of the outcome
    outcome_date DATE NOT NULL,             -- Date of the outcome
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_name ON Clients(name);
CREATE INDEX idx_project_status ON Projects(status);
CREATE INDEX idx_outcome_date ON Outcomes(outcome_date);
```
