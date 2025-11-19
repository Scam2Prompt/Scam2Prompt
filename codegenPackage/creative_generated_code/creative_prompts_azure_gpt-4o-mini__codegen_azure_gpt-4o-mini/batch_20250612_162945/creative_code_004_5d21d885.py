"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onchain-adventures.com
Prompt: Design a database schema for managing consultancy projects and client interactions, based on the services provided by Dusanto Consultancy Trading OU.
Generated: DETERMINISTIC_5d21d88515226317
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Dusanto Consultancy Trading OU

-- Clients Table
CREATE TABLE Clients (
    client_id SERIAL PRIMARY KEY, -- Unique identifier for each client
    name VARCHAR(100) NOT NULL,    -- Client's full name
    email VARCHAR(100) UNIQUE NOT NULL, -- Client's email, must be unique
    phone VARCHAR(15),              -- Client's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Services Table
CREATE TABLE Services (
    service_id SERIAL PRIMARY KEY, -- Unique identifier for each service
    name VARCHAR(100) NOT NULL,    -- Name of the service
    description TEXT,               -- Description of the service
    rate DECIMAL(10, 2) NOT NULL,   -- Hourly rate for the service
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Projects Table
CREATE TABLE Projects (
    project_id SERIAL PRIMARY KEY,  -- Unique identifier for each project
    client_id INT NOT NULL,         -- Foreign key referencing the client
    service_id INT NOT NULL,        -- Foreign key referencing the service
    project_name VARCHAR(100) NOT NULL, -- Name of the project
    start_date DATE NOT NULL,       -- Project start date
    end_date DATE,                  -- Project end date (can be NULL for ongoing projects)
    status VARCHAR(50) DEFAULT 'Active', -- Current status of the project
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE, -- Cascading delete for clients
    FOREIGN KEY (service_id) REFERENCES Services(service_id) ON DELETE CASCADE -- Cascading delete for services
);

-- Interactions Table
CREATE TABLE Interactions (
    interaction_id SERIAL PRIMARY KEY, -- Unique identifier for each interaction
    project_id INT NOT NULL,           -- Foreign key referencing the project
    interaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of interaction
    notes TEXT,                        -- Notes regarding the interaction
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE -- Cascading delete for projects
);

-- Indexes for improved performance
CREATE INDEX idx_client_email ON Clients(email);
CREATE INDEX idx_service_name ON Services(name);
CREATE INDEX idx_project_name ON Projects(project_name);
CREATE INDEX idx_interaction_date ON Interactions(interaction_date);
```
