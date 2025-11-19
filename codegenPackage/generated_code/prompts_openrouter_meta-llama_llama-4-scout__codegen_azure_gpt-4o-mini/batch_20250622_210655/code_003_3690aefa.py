"""
Generated Code Metadata:
========================
Original URL: https://renovation-toiture-toulouse.com
Prompt: "Design a database schema to store information about roofing projects, clients, and services provided by a company like Renovation Toiture Toulouse."
Generated: DETERMINISTIC_3690aefa345c386f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about roofing projects, clients, and services

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Services;
DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS Projects;

-- Table to store information about clients
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

-- Table to store information about services provided
CREATE TABLE Services (
    service_id SERIAL PRIMARY KEY, -- Unique identifier for each service
    service_name VARCHAR(100) NOT NULL, -- Name of the service
    description TEXT, -- Description of the service
    price DECIMAL(10, 2) NOT NULL, -- Price of the service
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about roofing projects
CREATE TABLE Projects (
    project_id SERIAL PRIMARY KEY, -- Unique identifier for each project
    client_id INT NOT NULL, -- Foreign key referencing Clients
    service_id INT NOT NULL, -- Foreign key referencing Services
    project_start_date DATE NOT NULL, -- Start date of the project
    project_end_date DATE, -- End date of the project (nullable)
    status VARCHAR(50) NOT NULL, -- Current status of the project (e.g., 'In Progress', 'Completed')
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (service_id) REFERENCES Services(service_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for faster querying
CREATE INDEX idx_client_email ON Clients(email);
CREATE INDEX idx_service_name ON Services(service_name);
CREATE INDEX idx_project_status ON Projects(status);
```
