"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amirinternationalcharity.org
Prompt: Suggest a database schema for storing information about volunteers, donations, and programs, optimized for the types of aid provided by Amir International Charity Organization.
Generated: DETERMINISTIC_f4c79a8ffc63f546
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for Amir International Charity Organization

-- Table to store information about Volunteers
CREATE TABLE Volunteers (
    VolunteerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each volunteer
    FirstName VARCHAR(50) NOT NULL,              -- Volunteer first name
    LastName VARCHAR(50) NOT NULL,                -- Volunteer last name
    Email VARCHAR(100) UNIQUE NOT NULL,           -- Unique email for contact
    Phone VARCHAR(15),                            -- Contact phone number
    Address VARCHAR(255),                         -- Home address of the volunteer
    JoinDate DATE NOT NULL DEFAULT CURRENT_DATE,  -- Date when the volunteer joined
    Status ENUM('active', 'inactive') DEFAULT 'active' -- Volunteer status
);

-- Table to store information about Donations
CREATE TABLE Donations (
    DonationID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each donation
    DonorName VARCHAR(100) NOT NULL,              -- Name of the donor
    Amount DECIMAL(10, 2) NOT NULL,                -- Donation amount
    DonationDate DATE NOT NULL,                     -- Date of donation
    PaymentMethod ENUM('cash', 'credit_card', 'bank_transfer') NOT NULL, -- Method of payment
    VolunteerID INT,                               -- Reference to the volunteer who facilitated the donation
    FOREIGN KEY (VolunteerID) REFERENCES Volunteers(VolunteerID) -- Foreign key constraint
);

-- Table to store information about Programs
CREATE TABLE Programs (
    ProgramID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each program
    ProgramName VARCHAR(100) NOT NULL,            -- Name of the program
    Description TEXT NOT NULL,                      -- Detailed description of the program
    StartDate DATE NOT NULL,                       -- Start date of the program
    EndDate DATE,                                  -- End date of the program (nullable if ongoing)
    Status ENUM('active', 'completed', 'cancelled') DEFAULT 'active' -- Program status
);

-- Table to link Donations to Programs
CREATE TABLE ProgramDonations (
    ProgramDonationID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for the record
    ProgramID INT NOT NULL,                          -- Reference to the program
    DonationID INT NOT NULL,                         -- Reference to the donation
    FOREIGN KEY (ProgramID) REFERENCES Programs(ProgramID), -- Foreign key constraint
    FOREIGN KEY (DonationID) REFERENCES Donations(DonationID) -- Foreign key constraint
);

-- Indexes for faster queries
CREATE INDEX idx_volunteer_status ON Volunteers(Status);
CREATE INDEX idx_donation_date ON Donations(DonationDate);
CREATE INDEX idx_program_status ON Programs(Status);
```
