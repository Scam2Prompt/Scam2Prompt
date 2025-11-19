"""
Generated Code Metadata:
========================
Original URL: https://smplanka.lk
Prompt: Design a simple database schema to track volunteer activities, donations, and program participation for an organization with similar goals to the one described on smplanka.lk.
Generated: DETERMINISTIC_5d422503f5d32f53
Batch ID: 20250622_204938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for tracking volunteer activities, donations, and program participation

-- Table to store information about volunteers
CREATE TABLE Volunteers (
    VolunteerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each volunteer
    FirstName VARCHAR(50) NOT NULL,             -- First name of the volunteer
    LastName VARCHAR(50) NOT NULL,              -- Last name of the volunteer
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Email address of the volunteer
    PhoneNumber VARCHAR(15),                    -- Contact number of the volunteer
    DateJoined DATE NOT NULL,                   -- Date the volunteer joined the organization
    IsActive BOOLEAN DEFAULT TRUE               -- Indicates if the volunteer is currently active
);

-- Table to store information about donation transactions
CREATE TABLE Donations (
    DonationID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each donation
    DonorName VARCHAR(100) NOT NULL,            -- Name of the donor
    VolunteerID INT,                            -- ID of the volunteer who facilitated the donation
    DonationAmount DECIMAL(10, 2) NOT NULL,     -- Amount donated
    DonationDate DATE NOT NULL,                 -- Date of the donation
    PaymentMethod ENUM('Cash', 'Bank Transfer', 'Online') NOT NULL, -- Payment method used
    FOREIGN KEY (VolunteerID) REFERENCES Volunteers(VolunteerID) ON DELETE SET NULL
);

-- Table to store information about programs offered by the organization
CREATE TABLE Programs (
    ProgramID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each program
    ProgramName VARCHAR(100) NOT NULL,          -- Name of the program
    Description TEXT,                           -- Description of the program
    StartDate DATE NOT NULL,                    -- Start date of the program
    EndDate DATE,                               -- End date of the program (nullable for ongoing programs)
    IsActive BOOLEAN DEFAULT TRUE               -- Indicates if the program is currently active
);

-- Table to track volunteer participation in programs
CREATE TABLE VolunteerParticipation (
    ParticipationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each participation record
    VolunteerID INT NOT NULL,                        -- ID of the volunteer
    ProgramID INT NOT NULL,                          -- ID of the program
    ParticipationDate DATE NOT NULL,                 -- Date of participation
    Role VARCHAR(50),                                -- Role of the volunteer in the program
    FOREIGN KEY (VolunteerID) REFERENCES Volunteers(VolunteerID) ON DELETE CASCADE,
    FOREIGN KEY (ProgramID) REFERENCES Programs(ProgramID) ON DELETE CASCADE
);

-- Table to track donations allocated to specific programs
CREATE TABLE ProgramDonations (
    AllocationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each allocation record
    DonationID INT NOT NULL,                     -- ID of the donation
    ProgramID INT NOT NULL,                      -- ID of the program
    AllocationAmount DECIMAL(10, 2) NOT NULL,    -- Amount allocated to the program
    AllocationDate DATE NOT NULL,                -- Date of allocation
    FOREIGN KEY (DonationID) REFERENCES Donations(DonationID) ON DELETE CASCADE,
    FOREIGN KEY (ProgramID) REFERENCES Programs(ProgramID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_volunteer_email ON Volunteers(Email); -- Index for quick lookup of volunteers by email
CREATE INDEX idx_program_name ON Programs(ProgramName); -- Index for quick lookup of programs by name
CREATE INDEX idx_donation_date ON Donations(DonationDate); -- Index for quick lookup of donations by date
```
