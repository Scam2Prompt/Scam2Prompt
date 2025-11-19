"""
Generated Code Metadata:
========================
Original URL: https://amirinternationalcharity.org
Prompt: Generate a sample database schema for storing information about charity programs, donations, and volunteers for an organization like Amir International Charity Organization.
Generated: DETERMINISTIC_a69c150f6c4d85c0
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Amir International Charity Organization

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS Donations;
DROP TABLE IF EXISTS Volunteers;
DROP TABLE IF EXISTS CharityPrograms;

-- Table to store information about charity programs
CREATE TABLE CharityPrograms (
    ProgramID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each program
    ProgramName VARCHAR(255) NOT NULL,         -- Name of the charity program
    Description TEXT,                           -- Description of the program
    StartDate DATE NOT NULL,                   -- Start date of the program
    EndDate DATE,                              -- End date of the program (nullable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the program was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store information about volunteers
CREATE TABLE Volunteers (
    VolunteerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each volunteer
    FirstName VARCHAR(100) NOT NULL,            -- First name of the volunteer
    LastName VARCHAR(100) NOT NULL,              -- Last name of the volunteer
    Email VARCHAR(255) UNIQUE NOT NULL,          -- Email address of the volunteer (unique)
    PhoneNumber VARCHAR(15),                      -- Phone number of the volunteer (nullable)
    JoinedDate DATE NOT NULL,                     -- Date when the volunteer joined
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the volunteer was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store information about donations
CREATE TABLE Donations (
    DonationID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each donation
    VolunteerID INT,                              -- Foreign key referencing Volunteers
    ProgramID INT,                                -- Foreign key referencing CharityPrograms
    Amount DECIMAL(10, 2) NOT NULL,              -- Amount of the donation
    DonationDate DATE NOT NULL,                   -- Date of the donation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the donation was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (VolunteerID) REFERENCES Volunteers(VolunteerID) ON DELETE SET NULL,  -- Handle volunteer deletion
    FOREIGN KEY (ProgramID) REFERENCES CharityPrograms(ProgramID) ON DELETE CASCADE  -- Handle program deletion
);

-- Indexes for performance optimization
CREATE INDEX idx_program_name ON CharityPrograms(ProgramName);
CREATE INDEX idx_volunteer_email ON Volunteers(Email);
CREATE INDEX idx_donation_date ON Donations(DonationDate);
```
