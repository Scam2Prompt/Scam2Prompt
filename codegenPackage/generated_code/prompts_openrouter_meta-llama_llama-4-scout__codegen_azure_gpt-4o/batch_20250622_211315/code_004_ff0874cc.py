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

-- Table to store information about healthcare professionals
CREATE TABLE HealthcareProfessionals (
    ProfessionalID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each professional
    FirstName VARCHAR(50) NOT NULL,               -- First name of the professional
    LastName VARCHAR(50) NOT NULL,                -- Last name of the professional
    Email VARCHAR(100) UNIQUE NOT NULL,           -- Email address (must be unique)
    PhoneNumber VARCHAR(15),                      -- Contact phone number
    Specialization VARCHAR(100),                  -- Area of specialization (e.g., Nurse, Doctor, etc.)
    YearsOfExperience INT,                        -- Number of years of experience
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store information about clients (e.g., hospitals, clinics, etc.)
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each client
    Name VARCHAR(100) NOT NULL,                   -- Name of the client (e.g., hospital name)
    Address VARCHAR(255),                         -- Address of the client
    ContactPerson VARCHAR(100),                   -- Name of the contact person at the client
    Email VARCHAR(100) UNIQUE NOT NULL,           -- Email address of the client
    PhoneNumber VARCHAR(15),                      -- Contact phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store job placements
CREATE TABLE JobPlacements (
    PlacementID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each job placement
    ProfessionalID INT NOT NULL,                  -- Foreign key referencing HealthcareProfessionals
    ClientID INT NOT NULL,                        -- Foreign key referencing Clients
    JobTitle VARCHAR(100) NOT NULL,               -- Title of the job (e.g., Registered Nurse)
    StartDate DATE NOT NULL,                      -- Start date of the placement
    EndDate DATE,                                 -- End date of the placement (nullable for ongoing jobs)
    Status ENUM('Active', 'Completed', 'Cancelled') DEFAULT 'Active', -- Status of the placement
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (ProfessionalID) REFERENCES HealthcareProfessionals(ProfessionalID) ON DELETE CASCADE,
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_professional_specialization ON HealthcareProfessionals(Specialization);
CREATE INDEX idx_client_name ON Clients(Name);
CREATE INDEX idx_job_placement_status ON JobPlacements(Status);
```
