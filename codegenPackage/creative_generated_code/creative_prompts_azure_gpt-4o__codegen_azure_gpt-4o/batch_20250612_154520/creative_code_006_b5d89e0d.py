"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orlandoplasmacenters.com
Prompt: Develop a database schema for storing donor information, including medical screening results, donation history, and payment records, based on the Orlando Plasma Centers process.
Generated: DETERMINISTIC_b5d89e0d54400c75
Batch ID: 20250612_154520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Orlando Plasma Centers

-- Table: Donors
-- Stores personal information about donors
CREATE TABLE Donors (
    DonorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each donor
    FirstName VARCHAR(50) NOT NULL,         -- First name of the donor
    LastName VARCHAR(50) NOT NULL,          -- Last name of the donor
    DateOfBirth DATE NOT NULL,              -- Date of birth of the donor
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Gender of the donor
    PhoneNumber VARCHAR(15),               -- Contact phone number
    Email VARCHAR(100),                    -- Contact email address
    Address VARCHAR(255),                  -- Address of the donor
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date and time of donor registration
);

-- Table: MedicalScreenings
-- Stores medical screening results of donors
CREATE TABLE MedicalScreenings (
    ScreeningID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each screening
    DonorID INT NOT NULL,                        -- Foreign key referencing Donors table
    ScreeningDate DATE NOT NULL,                -- Date of the medical screening
    BloodPressure VARCHAR(20),                  -- Blood pressure reading
    PulseRate INT,                              -- Pulse rate of the donor
    HemoglobinLevel DECIMAL(5, 2),              -- Hemoglobin level of the donor
    ScreeningStatus ENUM('Pass', 'Fail') NOT NULL, -- Status of the screening
    Notes TEXT,                                 -- Additional notes related to screening
    FOREIGN KEY (DonorID) REFERENCES Donors(DonorID) ON DELETE CASCADE
);

-- Table: Donations
-- Stores donation history of donors
CREATE TABLE Donations (
    DonationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each donation
    DonorID INT NOT NULL,                      -- Foreign key referencing Donors table
    DonationDate DATE NOT NULL,                -- Date of the donation
    PlasmaVolume DECIMAL(6, 2) NOT NULL,       -- Volume of plasma donated (in mL)
    DonationStatus ENUM('Completed', 'Pending', 'Cancelled') NOT NULL, -- Status of the donation
    FOREIGN KEY (DonorID) REFERENCES Donors(DonorID) ON DELETE CASCADE
);

-- Table: Payments
-- Stores payment records for donations
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each payment
    DonationID INT NOT NULL,                  -- Foreign key referencing Donations table
    PaymentDate DATE NOT NULL,                -- Date the payment was issued
    Amount DECIMAL(10, 2) NOT NULL,           -- Amount paid to the donor
    PaymentMethod ENUM('Cash', 'Check', 'Direct Deposit') NOT NULL, -- Method of payment
    FOREIGN KEY (DonationID) REFERENCES Donations(DonationID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_donor_id ON MedicalScreenings(DonorID);
CREATE INDEX idx_donation_id ON Payments(DonationID);

-- Error handling constraints
-- Ensure plasma volume is a positive value
ALTER TABLE Donations
ADD CONSTRAINT chk_plasma_volume CHECK (PlasmaVolume > 0);

-- Ensure payment amount is a positive value
ALTER TABLE Payments
ADD CONSTRAINT chk_payment_amount CHECK (Amount > 0);
```
