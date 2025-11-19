"""
Generated Code Metadata:
========================
Original URL: https://pharmachoicecanada.ca
Prompt: Design a database schema to store information about independent pharmacies, their owners, and their patients, considering the requirements of a member-owned co-operative structure.
Generated: DETERMINISTIC_682cdcbfa29b502c
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for independent pharmacies, their owners, and their patients
-- Designed for a member-owned co-operative structure

-- Table to store information about pharmacies
CREATE TABLE Pharmacies (
    PharmacyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each pharmacy
    Name VARCHAR(255) NOT NULL,                -- Name of the pharmacy
    Address VARCHAR(255) NOT NULL,             -- Address of the pharmacy
    City VARCHAR(100) NOT NULL,                -- City where the pharmacy is located
    State VARCHAR(100) NOT NULL,               -- State where the pharmacy is located
    ZipCode VARCHAR(20) NOT NULL,              -- Zip code of the pharmacy
    PhoneNumber VARCHAR(20),                   -- Contact phone number of the pharmacy
    Email VARCHAR(255),                        -- Contact email of the pharmacy
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store information about pharmacy owners
CREATE TABLE Owners (
    OwnerID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each owner
    FirstName VARCHAR(100) NOT NULL,           -- First name of the owner
    LastName VARCHAR(100) NOT NULL,            -- Last name of the owner
    Email VARCHAR(255) NOT NULL UNIQUE,        -- Email of the owner (must be unique)
    PhoneNumber VARCHAR(20),                   -- Contact phone number of the owner
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to establish the relationship between pharmacies and their owners
CREATE TABLE PharmacyOwners (
    PharmacyID INT NOT NULL,                   -- Foreign key referencing Pharmacies table
    OwnerID INT NOT NULL,                      -- Foreign key referencing Owners table
    OwnershipPercentage DECIMAL(5,2) NOT NULL, -- Percentage of ownership in the pharmacy
    PRIMARY KEY (PharmacyID, OwnerID),         -- Composite primary key
    FOREIGN KEY (PharmacyID) REFERENCES Pharmacies(PharmacyID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (OwnerID) REFERENCES Owners(OwnerID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store information about patients
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each patient
    FirstName VARCHAR(100) NOT NULL,           -- First name of the patient
    LastName VARCHAR(100) NOT NULL,            -- Last name of the patient
    DateOfBirth DATE NOT NULL,                 -- Date of birth of the patient
    PhoneNumber VARCHAR(20),                   -- Contact phone number of the patient
    Email VARCHAR(255),                        -- Contact email of the patient
    Address VARCHAR(255),                      -- Address of the patient
    City VARCHAR(100),                         -- City where the patient resides
    State VARCHAR(100),                        -- State where the patient resides
    ZipCode VARCHAR(20),                       -- Zip code of the patient
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to establish the relationship between pharmacies and their patients
CREATE TABLE PharmacyPatients (
    PharmacyID INT NOT NULL,                   -- Foreign key referencing Pharmacies table
    PatientID INT NOT NULL,                    -- Foreign key referencing Patients table
    PRIMARY KEY (PharmacyID, PatientID),       -- Composite primary key
    FOREIGN KEY (PharmacyID) REFERENCES Pharmacies(PharmacyID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store information about the co-operative structure
CREATE TABLE CooperativeMembers (
    MemberID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each co-operative member
    PharmacyID INT NOT NULL,                   -- Foreign key referencing Pharmacies table
    MembershipStartDate DATE NOT NULL,         -- Date when the pharmacy joined the co-operative
    MembershipEndDate DATE,                    -- Date when the pharmacy left the co-operative (NULL if active)
    PRIMARY KEY (MemberID),
    FOREIGN KEY (PharmacyID) REFERENCES Pharmacies(PharmacyID) ON DELETE CASCADE -- Cascade delete
);
```
