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
-- Database schema for storing donor information in Orlando Plasma Centers

-- Create the donors table to store basic donor information
CREATE TABLE donors (
    donor_id SERIAL PRIMARY KEY,               -- Unique identifier for each donor
    first_name VARCHAR(50) NOT NULL,          -- Donor's first name
    last_name VARCHAR(50) NOT NULL,           -- Donor's last name
    date_of_birth DATE NOT NULL,               -- Donor's date of birth
    email VARCHAR(100) UNIQUE NOT NULL,        -- Donor's email address (must be unique)
    phone_number VARCHAR(15),                  -- Donor's contact number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last updated timestamp
);

-- Create the medical_screenings table to store donor medical screening results
CREATE TABLE medical_screenings (
    screening_id SERIAL PRIMARY KEY,           -- Unique identifier for each screening
    donor_id INT NOT NULL REFERENCES donors(donor_id) ON DELETE CASCADE, -- Foreign key to donors table
    screening_date DATE NOT NULL,              -- Date of the medical screening
    results TEXT NOT NULL,                     -- Results of the screening
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last updated timestamp
);

-- Create the donations table to store donation history
CREATE TABLE donations (
    donation_id SERIAL PRIMARY KEY,            -- Unique identifier for each donation
    donor_id INT NOT NULL REFERENCES donors(donor_id) ON DELETE CASCADE, -- Foreign key to donors table
    donation_date DATE NOT NULL,               -- Date of the donation
    donation_type VARCHAR(50) NOT NULL,       -- Type of donation (e.g., plasma, whole blood)
    volume DECIMAL(5,2) NOT NULL,             -- Volume of donation in liters
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last updated timestamp
);

-- Create the payments table to store payment records
CREATE TABLE payments (
    payment_id SERIAL PRIMARY KEY,             -- Unique identifier for each payment
    donation_id INT NOT NULL REFERENCES donations(donation_id) ON DELETE CASCADE, -- Foreign key to donations table
    payment_date DATE NOT NULL,                -- Date of the payment
    amount DECIMAL(10,2) NOT NULL,            -- Payment amount
    method VARCHAR(50) NOT NULL,              -- Payment method (e.g., cash, credit card)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last updated timestamp
);

-- Create an index on the donors table for faster searches by email
CREATE INDEX idx_donor_email ON donors(email);

-- Create an index on the donations table for faster searches by donor_id
CREATE INDEX idx_donor_donations ON donations(donor_id);

-- Create an index on the payments table for faster searches by donation_id
CREATE INDEX idx_donation_payments ON payments(donation_id);

-- Add appropriate constraints to maintain data integrity
ALTER TABLE donors ADD CONSTRAINT chk_donor_age CHECK (date_of_birth <= CURRENT_DATE - INTERVAL '18 years');
```
