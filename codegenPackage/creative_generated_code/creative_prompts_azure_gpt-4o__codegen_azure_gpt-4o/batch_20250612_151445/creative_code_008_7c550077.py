"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demoablabs.com
Prompt: Create a database schema to store accreditation details for labs, including AIHA LAP, EPA NLLAP, and NVLAP certifications mentioned on A & B Labs' website.
Generated: DETERMINISTIC_7c550077f5bb892e
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for storing accreditation details for labs

-- Create a table to store lab information
CREATE TABLE Labs (
    LabID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each lab
    LabName VARCHAR(255) NOT NULL,               -- Name of the lab
    Address TEXT,                                -- Address of the lab
    PhoneNumber VARCHAR(15),                     -- Phone number of the lab
    Email VARCHAR(255)                           -- Email contact for the lab
);

-- Create a table to store accreditation agencies
CREATE TABLE AccreditationAgencies (
    AgencyID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each accreditation agency
    AgencyName VARCHAR(255) NOT NULL,            -- Name of the accreditation agency (e.g., AIHA LAP, EPA NLLAP, NVLAP)
    Description TEXT                              -- Description or details about the agency
);

-- Create a table to store lab accreditations
CREATE TABLE LabAccreditations (
    AccreditationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each accreditation record
    LabID INT NOT NULL,                              -- Foreign key referencing Labs table
    AgencyID INT NOT NULL,                           -- Foreign key referencing AccreditationAgencies table
    AccreditationDate DATE,                          -- Date the accreditation was granted
    ExpirationDate DATE,                             -- Expiration date of the accreditation
    CertificateNumber VARCHAR(255),                 -- Certificate number for the accreditation
    Status ENUM('Active', 'Expired', 'Suspended') DEFAULT 'Active', -- Accreditation status
    FOREIGN KEY (LabID) REFERENCES Labs(LabID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (AgencyID) REFERENCES AccreditationAgencies(AgencyID) ON DELETE CASCADE
);

-- Sample indexing for optimizing queries
CREATE INDEX idx_lab_name ON Labs(LabName);                   -- Index for searching labs by name
CREATE INDEX idx_agency_name ON AccreditationAgencies(AgencyName); -- Index for searching agencies by name
CREATE INDEX idx_accreditation_status ON LabAccreditations(Status); -- Index for filtering accreditations by status
```
