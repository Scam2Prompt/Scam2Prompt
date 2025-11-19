"""
Generated Code Metadata:
========================
Original URL: https://onchain-adventures.com
Prompt: Design a database schema for managing consultancy projects and client interactions, based on the services provided by Dusanto Consultancy Trading OU.
Generated: DETERMINISTIC_5d21d88515226317
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing consultancy projects and client interactions
-- for Dusanto Consultancy Trading OU

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS Services;
DROP TABLE IF EXISTS Projects;
DROP TABLE IF EXISTS Interactions;

-- Table to store client information
CREATE TABLE Clients (
    client_id SERIAL PRIMARY KEY, -- Unique identifier for each client
    name VARCHAR(255) NOT NULL, -- Client's name
    email VARCHAR(255) UNIQUE NOT NULL, -- Client's email, must be unique
    phone VARCHAR(20), -- Client's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store service information offered by the consultancy
CREATE TABLE Services (
    service_id SERIAL PRIMARY KEY, -- Unique identifier for each service
    service_name VARCHAR(255) NOT NULL, -- Name of the service
    description TEXT, -- Description of the service
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store consultancy projects
CREATE TABLE Projects (
    project_id SERIAL PRIMARY KEY, -- Unique identifier for each project
    client_id INT NOT NULL, -- Foreign key referencing Clients
    service_id INT NOT NULL, -- Foreign key referencing Services
    project_name VARCHAR(255) NOT NULL, -- Name of the project
    start_date DATE NOT NULL, -- Project start date
    end_date DATE, -- Project end date (nullable)
    status VARCHAR(50) NOT NULL, -- Current status of the project (e.g., 'In Progress', 'Completed')
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (service_id) REFERENCES Services(service_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store interactions with clients
CREATE TABLE Interactions (
    interaction_id SERIAL PRIMARY KEY, -- Unique identifier for each interaction
    client_id INT NOT NULL, -- Foreign key referencing Clients
    interaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the interaction
    notes TEXT, -- Notes regarding the interaction
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(email);
CREATE INDEX idx_service_name ON Services(service_name);
CREATE INDEX idx_project_status ON Projects(status);
CREATE INDEX idx_interaction_date ON Interactions(interaction_date);
```
