"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rakhshandamemorial.org
Prompt: Create a database schema for managing RM's projects, including tables for tracking beneficiaries, volunteers, donations, and event schedules.
Generated: DETERMINISTIC_657f750a50ed29cc
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing RM's projects

-- Create a schema for the project management system
CREATE SCHEMA IF NOT EXISTS RMProjects;

-- Table to store information about beneficiaries
CREATE TABLE IF NOT EXISTS RMProjects.Beneficiaries (
    BeneficiaryID SERIAL PRIMARY KEY,              -- Unique identifier for each beneficiary
    Name VARCHAR(100) NOT NULL,                     -- Name of the beneficiary
    ContactInfo VARCHAR(255),                       -- Contact information (email/phone)
    Address VARCHAR(255),                           -- Address of the beneficiary
    DateOfBirth DATE,                               -- Date of birth of the beneficiary
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Last update timestamp
);

-- Table to store information about volunteers
CREATE TABLE IF NOT EXISTS RMProjects.Volunteers (
    VolunteerID SERIAL PRIMARY KEY,                 -- Unique identifier for each volunteer
    Name VARCHAR(100) NOT NULL,                     -- Name of the volunteer
    Email VARCHAR(255) UNIQUE NOT NULL,             -- Email address (must be unique)
    Phone VARCHAR(20),                              -- Phone number of the volunteer
    Skills TEXT,                                    -- Skills of the volunteer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Last update timestamp
);

-- Table to track donations
CREATE TABLE IF NOT EXISTS RMProjects.Donations (
    DonationID SERIAL PRIMARY KEY,                  -- Unique identifier for each donation
    BeneficiaryID INT REFERENCES RMProjects.Beneficiaries(BeneficiaryID) ON DELETE CASCADE,  -- Foreign key to beneficiaries
    Amount DECIMAL(10, 2) NOT NULL,                 -- Amount of the donation
    DonationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date of the donation
    DonorName VARCHAR(100),                         -- Name of the donor
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Last update timestamp
);

-- Table to manage event schedules
CREATE TABLE IF NOT EXISTS RMProjects.EventSchedules (
    EventID SERIAL PRIMARY KEY,                     -- Unique identifier for each event
    EventName VARCHAR(100) NOT NULL,                -- Name of the event
    EventDate TIMESTAMP NOT NULL,                   -- Date and time of the event
    Location VARCHAR(255),                           -- Location of the event
    Description TEXT,                               -- Description of the event
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Last update timestamp
);

-- Create indexes for performance improvement
CREATE INDEX IF NOT EXISTS idx_beneficiary_name ON RMProjects.Beneficiaries(Name);
CREATE INDEX IF NOT EXISTS idx_volunteer_email ON RMProjects.Volunteers(Email);
CREATE INDEX IF NOT EXISTS idx_donation_date ON RMProjects.Donations(DonationDate);
CREATE INDEX IF NOT EXISTS idx_event_date ON RMProjects.EventSchedules(EventDate);
```
