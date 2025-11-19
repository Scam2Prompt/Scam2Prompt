"""
Generated Code Metadata:
========================
Original URL: https://cefor.org.br
Prompt: Design a database schema to store information about social services, including details about clients, services provided, and outcomes, for an organization like CEFOR.
Generated: DETERMINISTIC_d29bf9126834fa37
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about social services
-- This schema includes tables for clients, services, and outcomes

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS Outcomes;
DROP TABLE IF EXISTS Services;
DROP TABLE IF EXISTS Clients;

-- Table to store client information
CREATE TABLE Clients (
    client_id SERIAL PRIMARY KEY, -- Unique identifier for each client
    first_name VARCHAR(50) NOT NULL, -- Client's first name
    last_name VARCHAR(50) NOT NULL, -- Client's last name
    date_of_birth DATE NOT NULL, -- Client's date of birth
    gender VARCHAR(10), -- Client's gender
    contact_number VARCHAR(15), -- Client's contact number
    email VARCHAR(100), -- Client's email address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about services provided
CREATE TABLE Services (
    service_id SERIAL PRIMARY KEY, -- Unique identifier for each service
    service_name VARCHAR(100) NOT NULL, -- Name of the service
    description TEXT, -- Description of the service
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store outcomes of services provided to clients
CREATE TABLE Outcomes (
    outcome_id SERIAL PRIMARY KEY, -- Unique identifier for each outcome
    client_id INT NOT NULL, -- Foreign key referencing Clients
    service_id INT NOT NULL, -- Foreign key referencing Services
    outcome_description TEXT, -- Description of the outcome
    outcome_date DATE NOT NULL, -- Date of the outcome
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (service_id) REFERENCES Services(service_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_id ON Outcomes(client_id);
CREATE INDEX idx_service_id ON Outcomes(service_id);
```
