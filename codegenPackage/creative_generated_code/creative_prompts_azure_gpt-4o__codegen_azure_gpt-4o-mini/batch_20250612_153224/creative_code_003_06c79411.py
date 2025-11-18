"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://twmassociates.co.za
Prompt: Create a database schema in SQL to manage client information, project details, and consulting costs for an architectural firm like TWM Associates.
Generated: DETERMINISTIC_06c794114f408b2d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing client information, project details, and consulting costs for TWM Associates

-- Create a schema named 'twm_associates'
CREATE SCHEMA IF NOT EXISTS twm_associates;

-- Table to store client information
CREATE TABLE IF NOT EXISTS twm_associates.clients (
    client_id SERIAL PRIMARY KEY,            -- Unique identifier for each client
    first_name VARCHAR(50) NOT NULL,        -- Client's first name
    last_name VARCHAR(50) NOT NULL,         -- Client's last name
    email VARCHAR(100) UNIQUE NOT NULL,     -- Client's email address
    phone VARCHAR(15),                       -- Client's phone number
    address TEXT,                            -- Client's address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the client was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the client was last updated
);

-- Table to store project details
CREATE TABLE IF NOT EXISTS twm_associates.projects (
    project_id SERIAL PRIMARY KEY,           -- Unique identifier for each project
    client_id INT NOT NULL,                  -- Foreign key referencing the client
    project_name VARCHAR(100) NOT NULL,     -- Name of the project
    start_date DATE NOT NULL,                -- Start date of the project
    end_date DATE,                           -- End date of the project (nullable)
    status VARCHAR(20) CHECK (status IN ('Pending', 'In Progress', 'Completed', 'Cancelled')) NOT NULL, -- Project status
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the project was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the project was last updated
    FOREIGN KEY (client_id) REFERENCES twm_associates.clients(client_id) ON DELETE CASCADE -- Cascade delete for related clients
);

-- Table to store consulting costs associated with each project
CREATE TABLE IF NOT EXISTS twm_associates.consulting_costs (
    cost_id SERIAL PRIMARY KEY,              -- Unique identifier for each cost entry
    project_id INT NOT NULL,                 -- Foreign key referencing the project
    cost_description VARCHAR(255) NOT NULL, -- Description of the consulting cost
    cost_amount DECIMAL(10, 2) NOT NULL,    -- Amount of the consulting cost
    incurred_date DATE NOT NULL,             -- Date when the cost was incurred
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the cost entry was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the cost entry was last updated
    FOREIGN KEY (project_id) REFERENCES twm_associates.projects(project_id) ON DELETE CASCADE -- Cascade delete for related projects
);

-- Indexes to improve query performance
CREATE INDEX idx_client_email ON twm_associates.clients(email);
CREATE INDEX idx_project_client ON twm_associates.projects(client_id);
CREATE INDEX idx_cost_project ON twm_associates.consulting_costs(project_id);

-- End of schema creation
```
