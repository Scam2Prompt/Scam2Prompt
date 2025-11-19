"""
Generated Code Metadata:
========================
Original URL: https://orlandoplasmacenters.com
Prompt: Create a database schema to store donor information, donation history, and compensation details for a plasma donation center like Orlando Plasma Centers.
Generated: DETERMINISTIC_850ffbc1c7cf3f0c
Batch ID: 20250622_211932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a Plasma Donation Center

-- Create a database for the plasma donation center
CREATE DATABASE PlasmaDonationCenter;

-- Use the created database
USE PlasmaDonationCenter;

-- Table to store donor information
CREATE TABLE Donors (
    donor_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each donor
    first_name VARCHAR(50) NOT NULL,         -- Donor's first name
    last_name VARCHAR(50) NOT NULL,          -- Donor's last name
    date_of_birth DATE NOT NULL,              -- Donor's date of birth
    gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Donor's gender
    phone_number VARCHAR(15) UNIQUE NOT NULL, -- Donor's phone number
    email VARCHAR(100) UNIQUE NOT NULL,       -- Donor's email address
    address VARCHAR(255) NOT NULL,            -- Donor's residential address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store donation history
CREATE TABLE Donations (
    donation_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each donation
    donor_id INT NOT NULL,                       -- Foreign key referencing the donor
    donation_date DATE NOT NULL,                 -- Date of the donation
    donation_amount DECIMAL(10, 2) NOT NULL,    -- Amount of plasma donated in liters
    compensation_amount DECIMAL(10, 2) NOT NULL, -- Compensation amount for the donation
    FOREIGN KEY (donor_id) REFERENCES Donors(donor_id) ON DELETE CASCADE, -- Ensures referential integrity
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store compensation details
CREATE TABLE Compensation (
    compensation_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each compensation record
    donor_id INT NOT NULL,                           -- Foreign key referencing the donor
    compensation_date DATE NOT NULL,                 -- Date of compensation payment
    amount DECIMAL(10, 2) NOT NULL,                  -- Amount compensated
    payment_method ENUM('Cash', 'Check', 'Direct Deposit') NOT NULL, -- Method of payment
    FOREIGN KEY (donor_id) REFERENCES Donors(donor_id) ON DELETE CASCADE, -- Ensures referential integrity
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Indexes for performance optimization
CREATE INDEX idx_donor_email ON Donors(email);
CREATE INDEX idx_donor_phone ON Donors(phone_number);
CREATE INDEX idx_donation_donor ON Donations(donor_id);
CREATE INDEX idx_compensation_donor ON Compensation(donor_id);
```
