"""
Generated Code Metadata:
========================
Original URL: https://seandahealthcare.co.za
Prompt: Design a database schema to store information about healthcare professionals, clients, and job placements for a company like Seanda Healthcare.
Generated: DETERMINISTIC_ff0874cc94a553cb
Batch ID: 20250622_211315
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Seanda Healthcare

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS JobPlacements;
DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS HealthcareProfessionals;

-- Table to store information about healthcare professionals
CREATE TABLE HealthcareProfessionals (
    id SERIAL PRIMARY KEY, -- Unique identifier for each healthcare professional
    first_name VARCHAR(50) NOT NULL, -- First name of the healthcare professional
    last_name VARCHAR(50) NOT NULL, -- Last name of the healthcare professional
    email VARCHAR(100) UNIQUE NOT NULL, -- Email address, must be unique
    phone_number VARCHAR(15), -- Phone number of the healthcare professional
    specialty VARCHAR(100), -- Specialty of the healthcare professional
    license_number VARCHAR(50) UNIQUE NOT NULL, -- Unique license number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about clients
CREATE TABLE Clients (
    id SERIAL PRIMARY KEY, -- Unique identifier for each client
    first_name VARCHAR(50) NOT NULL, -- First name of the client
    last_name VARCHAR(50) NOT NULL, -- Last name of the client
    email VARCHAR(100) UNIQUE NOT NULL, -- Email address, must be unique
    phone_number VARCHAR(15), -- Phone number of the client
    address VARCHAR(255), -- Address of the client
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store job placements
CREATE TABLE JobPlacements (
    id SERIAL PRIMARY KEY, -- Unique identifier for each job placement
    healthcare_professional_id INT NOT NULL, -- Foreign key referencing HealthcareProfessionals
    client_id INT NOT NULL, -- Foreign key referencing Clients
    placement_date DATE NOT NULL, -- Date of the job placement
    end_date DATE, -- End date of the job placement (nullable)
    status VARCHAR(20) NOT NULL CHECK (status IN ('active', 'completed', 'cancelled')), -- Status of the job placement
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (healthcare_professional_id) REFERENCES HealthcareProfessionals(id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (client_id) REFERENCES Clients(id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_healthcare_professional_email ON HealthcareProfessionals(email);
CREATE INDEX idx_client_email ON Clients(email);
CREATE INDEX idx_job_placement_status ON JobPlacements(status);
```
