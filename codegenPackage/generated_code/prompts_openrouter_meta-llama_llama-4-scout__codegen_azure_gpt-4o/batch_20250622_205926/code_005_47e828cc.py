"""
Generated Code Metadata:
========================
Original URL: https://abilityfordisabilityfund.com
Prompt: Design a database schema for storing information about disability fund applicants, donors, and volunteers.
Generated: DETERMINISTIC_47e828cc566cf422
Batch ID: 20250622_205926
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about disability fund applicants, donors, and volunteers

-- Table to store information about applicants
CREATE TABLE Applicants (
    ApplicantID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each applicant
    FirstName VARCHAR(50) NOT NULL,            -- First name of the applicant
    LastName VARCHAR(50) NOT NULL,             -- Last name of the applicant
    DateOfBirth DATE NOT NULL,                 -- Date of birth of the applicant
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Gender of the applicant
    DisabilityType VARCHAR(100) NOT NULL,      -- Type of disability
    ContactNumber VARCHAR(15),                 -- Contact number of the applicant
    Email VARCHAR(100),                        -- Email address of the applicant
    Address TEXT,                              -- Address of the applicant
    ApplicationStatus ENUM('Pending', 'Approved', 'Rejected') DEFAULT 'Pending', -- Status of the application
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Table to store information about donors
CREATE TABLE Donors (
    DonorID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each donor
    FirstName VARCHAR(50) NOT NULL,            -- First name of the donor
    LastName VARCHAR(50) NOT NULL,             -- Last name of the donor
    ContactNumber VARCHAR(15),                 -- Contact number of the donor
    Email VARCHAR(100) NOT NULL,               -- Email address of the donor
    Address TEXT,                              -- Address of the donor
    DonationAmount DECIMAL(10, 2) NOT NULL,    -- Amount donated
    DonationDate DATE NOT NULL,                -- Date of donation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Table to store information about volunteers
CREATE TABLE Volunteers (
    VolunteerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each volunteer
    FirstName VARCHAR(50) NOT NULL,             -- First name of the volunteer
    LastName VARCHAR(50) NOT NULL,              -- Last name of the volunteer
    ContactNumber VARCHAR(15),                  -- Contact number of the volunteer
    Email VARCHAR(100) NOT NULL,                -- Email address of the volunteer
    Address TEXT,                               -- Address of the volunteer
    Availability ENUM('Full-Time', 'Part-Time') NOT NULL, -- Availability status
    Skills TEXT,                                -- Skills of the volunteer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Table to track donations made by donors to applicants
CREATE TABLE Donations (
    DonationID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each donation
    DonorID INT NOT NULL,                       -- Foreign key referencing Donors table
    ApplicantID INT NOT NULL,                   -- Foreign key referencing Applicants table
    DonationAmount DECIMAL(10, 2) NOT NULL,     -- Amount donated
    DonationDate DATE NOT NULL,                 -- Date of donation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the record was last updated
    FOREIGN KEY (DonorID) REFERENCES Donors(DonorID) ON DELETE CASCADE, -- Cascade delete for donor
    FOREIGN KEY (ApplicantID) REFERENCES Applicants(ApplicantID) ON DELETE CASCADE -- Cascade delete for applicant
);

-- Table to track volunteer assignments to applicants
CREATE TABLE VolunteerAssignments (
    AssignmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each assignment
    VolunteerID INT NOT NULL,                    -- Foreign key referencing Volunteers table
    ApplicantID INT NOT NULL,                    -- Foreign key referencing Applicants table
    AssignmentDate DATE NOT NULL,                -- Date of assignment
    Notes TEXT,                                  -- Notes about the assignment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the record was last updated
    FOREIGN KEY (VolunteerID) REFERENCES Volunteers(VolunteerID) ON DELETE CASCADE, -- Cascade delete for volunteer
    FOREIGN KEY (ApplicantID) REFERENCES Applicants(ApplicantID) ON DELETE CASCADE -- Cascade delete for applicant
);
```
