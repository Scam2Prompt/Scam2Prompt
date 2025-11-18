"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ircmhealth.com
Prompt: Design a database schema for a medical billing system that supports revenue cycle management and AR follow-up, inspired by ircmhealth.com's offerings.
Generated: DETERMINISTIC_820fedc3f8d784b4
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Medical Billing System Database Schema
-- This schema is inspired by revenue cycle management and accounts receivable (AR) follow-up functionalities.

CREATE DATABASE MedicalBillingSystem;

USE MedicalBillingSystem;

-- Table to store patient information
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the patient
    FirstName VARCHAR(100) NOT NULL,         -- Patient's first name
    LastName VARCHAR(100) NOT NULL,          -- Patient's last name
    DateOfBirth DATE NOT NULL,               -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Patient's gender
    ContactNumber VARCHAR(15),              -- Contact number
    Email VARCHAR(255),                     -- Email address
    Address TEXT                            -- Full address
);

-- Table to store provider information
CREATE TABLE Providers (
    ProviderID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the provider
    Name VARCHAR(255) NOT NULL,                -- Provider's name
    Specialty VARCHAR(100),                    -- Provider's specialty (e.g., cardiology)
    ContactNumber VARCHAR(15),                 -- Contact number
    Email VARCHAR(255),                        -- Email address
    Address TEXT                               -- Address of the provider
);

-- Table to store insurance payer information
CREATE TABLE InsurancePayers (
    PayerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the insurance payer
    Name VARCHAR(255) NOT NULL,             -- Name of the insurance payer
    ContactNumber VARCHAR(15),              -- Contact number for billing inquiries
    Email VARCHAR(255),                     -- Email address
    Address TEXT                            -- Address of the payer
);

-- Table to store patient insurance details
CREATE TABLE PatientInsurance (
    InsuranceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the insurance record
    PatientID INT NOT NULL,                     -- Foreign key referencing Patients table
    PayerID INT NOT NULL,                       -- Foreign key referencing InsurancePayers table
    PolicyNumber VARCHAR(50) NOT NULL,          -- Insurance policy number
    CoverageStartDate DATE NOT NULL,            -- Start date of coverage
    CoverageEndDate DATE,                       -- End date of coverage (optional)
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
    FOREIGN KEY (PayerID) REFERENCES InsurancePayers(PayerID)
);

-- Table to store medical claims
CREATE TABLE Claims (
    ClaimID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for the claim
    PatientID INT NOT NULL,                  -- Foreign key referencing Patients table
    ProviderID INT NOT NULL,                 -- Foreign key referencing Providers table
    PayerID INT NOT NULL,                    -- Foreign key referencing InsurancePayers table
    DateOfService DATE NOT NULL,             -- Date the service was provided
    TotalCharge DECIMAL(10, 2) NOT NULL,     -- Total amount charged for the service
    Status ENUM('Pending', 'Approved', 'Rejected', 'Paid') NOT NULL, -- Current status of the claim
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
    FOREIGN KEY (ProviderID) REFERENCES Providers(ProviderID),
    FOREIGN KEY (PayerID) REFERENCES InsurancePayers(PayerID)
);

-- Table to store payments against claims
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the payment
    ClaimID INT NOT NULL,                     -- Foreign key referencing Claims table
    AmountPaid DECIMAL(10, 2) NOT NULL,       -- Amount paid
    PaymentDate DATE NOT NULL,                -- Date payment was made
    Method ENUM('Credit Card', 'Check', 'Bank Transfer', 'Cash') NOT NULL, -- Method of payment
    FOREIGN KEY (ClaimID) REFERENCES Claims(ClaimID)
);

-- Table to store accounts receivable follow-up activities
CREATE TABLE ARFollowUp (
    FollowUpID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the follow-up record
    ClaimID INT NOT NULL,                      -- Foreign key referencing Claims table
    FollowUpDate DATE NOT NULL,                -- Date of the follow-up activity
    Notes TEXT,                                -- Notes about the follow-up
    Status ENUM('Open', 'Closed', 'Escalated') NOT NULL, -- Status of the follow-up
    FOREIGN KEY (ClaimID) REFERENCES Claims(ClaimID)
);

-- Indexes for better query performance
CREATE INDEX idx_PatientName ON Patients (FirstName, LastName);
CREATE INDEX idx_ClaimStatus ON Claims (Status);
CREATE INDEX idx_FollowUpStatus ON ARFollowUp (Status);

-- End of Medical Billing System Database Schema
```
