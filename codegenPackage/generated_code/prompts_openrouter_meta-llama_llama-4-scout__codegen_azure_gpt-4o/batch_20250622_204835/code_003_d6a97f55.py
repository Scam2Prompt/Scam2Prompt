"""
Generated Code Metadata:
========================
Original URL: https://standrewsibanda.org
Prompt: Design a simple database schema to store information about donors, children, and donations for a charity project like St. Andrew's School Project For The Young.
Generated: DETERMINISTIC_d6a97f55271ca67d
Batch ID: 20250622_204835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a charity project to store information about donors, children, and donations

-- Table to store information about donors
CREATE TABLE Donors (
    DonorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each donor
    FirstName VARCHAR(50) NOT NULL,         -- Donor's first name
    LastName VARCHAR(50) NOT NULL,          -- Donor's last name
    Email VARCHAR(100) UNIQUE NOT NULL,     -- Donor's email address (must be unique)
    PhoneNumber VARCHAR(15),                -- Donor's phone number
    Address TEXT,                           -- Donor's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the donor record was created
);

-- Table to store information about children
CREATE TABLE Children (
    ChildID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each child
    FirstName VARCHAR(50) NOT NULL,         -- Child's first name
    LastName VARCHAR(50) NOT NULL,          -- Child's last name
    DateOfBirth DATE NOT NULL,              -- Child's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Child's gender
    Notes TEXT,                             -- Additional notes about the child
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the child record was created
);

-- Table to store information about donations
CREATE TABLE Donations (
    DonationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each donation
    DonorID INT NOT NULL,                      -- Foreign key referencing the Donors table
    ChildID INT,                               -- Foreign key referencing the Children table (optional)
    Amount DECIMAL(10, 2) NOT NULL,            -- Donation amount
    DonationDate DATE NOT NULL,                -- Date of the donation
    Notes TEXT,                                -- Additional notes about the donation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the donation record was created
    FOREIGN KEY (DonorID) REFERENCES Donors(DonorID) ON DELETE CASCADE, -- Cascade delete if donor is removed
    FOREIGN KEY (ChildID) REFERENCES Children(ChildID) ON DELETE SET NULL -- Set ChildID to NULL if child is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_donor_email ON Donors(Email); -- Index for quick lookup by email
CREATE INDEX idx_donation_date ON Donations(DonationDate); -- Index for quick lookup by donation date
```
