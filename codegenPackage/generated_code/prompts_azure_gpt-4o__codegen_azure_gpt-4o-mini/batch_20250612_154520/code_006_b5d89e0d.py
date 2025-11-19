"""
Generated Code Metadata:
========================
Original URL: https://orlandoplasmacenters.com
Prompt: Develop a database schema for storing donor information, including medical screening results, donation history, and payment records, based on the Orlando Plasma Centers process.
Generated: DETERMINISTIC_b5d89e0d54400c75
Batch ID: 20250612_154520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing donor information for Orlando Plasma Centers

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS PaymentRecords;
DROP TABLE IF EXISTS DonationHistory;
DROP TABLE IF EXISTS MedicalScreeningResults;
DROP TABLE IF EXISTS Donors;

-- Table to store donor information
CREATE TABLE Donors (
    DonorID SERIAL PRIMARY KEY, -- Unique identifier for each donor
    FirstName VARCHAR(50) NOT NULL, -- Donor's first name
    LastName VARCHAR(50) NOT NULL, -- Donor's last name
    DateOfBirth DATE NOT NULL, -- Donor's date of birth
    Email VARCHAR(100) UNIQUE NOT NULL, -- Donor's email address
    PhoneNumber VARCHAR(15), -- Donor's phone number
    Address VARCHAR(255), -- Donor's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store medical screening results for donors
CREATE TABLE MedicalScreeningResults (
    ScreeningID SERIAL PRIMARY KEY, -- Unique identifier for each screening result
    DonorID INT NOT NULL, -- Foreign key referencing the Donors table
    ScreeningDate DATE NOT NULL, -- Date of the medical screening
    Result VARCHAR(255) NOT NULL, -- Result of the medical screening
    Notes TEXT, -- Additional notes regarding the screening
    FOREIGN KEY (DonorID) REFERENCES Donors(DonorID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store donation history for donors
CREATE TABLE DonationHistory (
    DonationID SERIAL PRIMARY KEY, -- Unique identifier for each donation
    DonorID INT NOT NULL, -- Foreign key referencing the Donors table
    DonationDate DATE NOT NULL, -- Date of the donation
    DonationType VARCHAR(50) NOT NULL, -- Type of donation (e.g., plasma, whole blood)
    Volume DECIMAL(5,2) NOT NULL, -- Volume of donation in liters
    FOREIGN KEY (DonorID) REFERENCES Donors(DonorID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store payment records for donations
CREATE TABLE PaymentRecords (
    PaymentID SERIAL PRIMARY KEY, -- Unique identifier for each payment record
    DonationID INT NOT NULL, -- Foreign key referencing the DonationHistory table
    PaymentDate DATE NOT NULL, -- Date of the payment
    Amount DECIMAL(10,2) NOT NULL, -- Amount paid for the donation
    PaymentMethod VARCHAR(50) NOT NULL, -- Method of payment (e.g., cash, credit card)
    FOREIGN KEY (DonationID) REFERENCES DonationHistory(DonationID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_donor_email ON Donors(Email);
CREATE INDEX idx_donation_date ON DonationHistory(DonationDate);
CREATE INDEX idx_payment_date ON PaymentRecords(PaymentDate);
```
