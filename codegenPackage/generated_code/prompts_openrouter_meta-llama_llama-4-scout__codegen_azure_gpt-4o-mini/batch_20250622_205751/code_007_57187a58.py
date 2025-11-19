"""
Generated Code Metadata:
========================
Original URL: https://juridiskklinik.se
Prompt: Design a database schema to store client information, case files, and service areas for a law firm like Juridisk Klinik, considering data normalization and security best practices.
Generated: DETERMINISTIC_57187a58a3878260
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a law firm to store client information, case files, and service areas

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS ServiceAreas;
DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS CaseFiles;

-- Table to store service areas
CREATE TABLE ServiceAreas (
    id SERIAL PRIMARY KEY, -- Unique identifier for each service area
    name VARCHAR(255) NOT NULL UNIQUE, -- Name of the service area
    description TEXT, -- Description of the service area
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store client information
CREATE TABLE Clients (
    id SERIAL PRIMARY KEY, -- Unique identifier for each client
    first_name VARCHAR(100) NOT NULL, -- Client's first name
    last_name VARCHAR(100) NOT NULL, -- Client's last name
    email VARCHAR(255) NOT NULL UNIQUE, -- Client's email address
    phone VARCHAR(20), -- Client's phone number
    address TEXT, -- Client's address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store case files
CREATE TABLE CaseFiles (
    id SERIAL PRIMARY KEY, -- Unique identifier for each case file
    client_id INT NOT NULL, -- Foreign key referencing Clients table
    service_area_id INT NOT NULL, -- Foreign key referencing ServiceAreas table
    case_number VARCHAR(50) NOT NULL UNIQUE, -- Unique case number
    case_description TEXT, -- Description of the case
    status VARCHAR(50) NOT NULL, -- Current status of the case (e.g., Open, Closed)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (client_id) REFERENCES Clients(id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (service_area_id) REFERENCES ServiceAreas(id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_clients_email ON Clients(email);
CREATE INDEX idx_casefiles_case_number ON CaseFiles(case_number);
CREATE INDEX idx_serviceareas_name ON ServiceAreas(name);
```
