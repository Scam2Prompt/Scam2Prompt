"""
Generated Code Metadata:
========================
Original URL: https://uaeinterior.com
Prompt: Design a database schema for storing information about interior design projects, including project details, client information, and space planning, based on the services provided by Amazing Interior.
Generated: DETERMINISTIC_04782efdd28b7ed1
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about interior design projects

-- Drop existing tables if they exist to avoid conflicts
DROP TABLE IF EXISTS Projects;
DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS Spaces;
DROP TABLE IF EXISTS Services;

-- Table to store client information
CREATE TABLE Clients (
    client_id SERIAL PRIMARY KEY, -- Unique identifier for each client
    first_name VARCHAR(50) NOT NULL, -- Client's first name
    last_name VARCHAR(50) NOT NULL, -- Client's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Client's email address
    phone VARCHAR(15), -- Client's phone number
    address TEXT, -- Client's address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store project details
CREATE TABLE Projects (
    project_id SERIAL PRIMARY KEY, -- Unique identifier for each project
    client_id INT NOT NULL, -- Foreign key referencing Clients
    project_name VARCHAR(100) NOT NULL, -- Name of the project
    start_date DATE NOT NULL, -- Project start date
    end_date DATE, -- Project end date (nullable)
    budget DECIMAL(10, 2), -- Project budget
    description TEXT, -- Description of the project
    status VARCHAR(20) CHECK (status IN ('Pending', 'In Progress', 'Completed', 'On Hold')), -- Project status
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store space planning details
CREATE TABLE Spaces (
    space_id SERIAL PRIMARY KEY, -- Unique identifier for each space
    project_id INT NOT NULL, -- Foreign key referencing Projects
    space_name VARCHAR(100) NOT NULL, -- Name of the space (e.g., Living Room, Kitchen)
    dimensions VARCHAR(50), -- Dimensions of the space (e.g., "10x12 ft")
    layout TEXT, -- Layout description or design plan
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store services provided for each project
CREATE TABLE Services (
    service_id SERIAL PRIMARY KEY, -- Unique identifier for each service
    project_id INT NOT NULL, -- Foreign key referencing Projects
    service_name VARCHAR(100) NOT NULL, -- Name of the service (e.g., Consultation, Design)
    service_description TEXT, -- Description of the service
    cost DECIMAL(10, 2), -- Cost of the service
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(email);
CREATE INDEX idx_project_status ON Projects(status);
CREATE INDEX idx_space_project ON Spaces(project_id);
CREATE INDEX idx_service_project ON Services(project_id);
```
