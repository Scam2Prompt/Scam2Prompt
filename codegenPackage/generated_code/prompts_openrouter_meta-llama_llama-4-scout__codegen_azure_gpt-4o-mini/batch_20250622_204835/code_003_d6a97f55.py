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
-- Database schema for St. Andrew's School Project For The Young

-- Create a table to store information about donors
CREATE TABLE Donors (
    donor_id SERIAL PRIMARY KEY,          -- Unique identifier for each donor
    name VARCHAR(100) NOT NULL,          -- Name of the donor
    email VARCHAR(100) UNIQUE NOT NULL,  -- Email of the donor, must be unique
    phone VARCHAR(15),                    -- Phone number of the donor
    address TEXT,                         -- Address of the donor
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the donor was added
);

-- Create a table to store information about children
CREATE TABLE Children (
    child_id SERIAL PRIMARY KEY,          -- Unique identifier for each child
    name VARCHAR(100) NOT NULL,          -- Name of the child
    age INT CHECK (age >= 0),             -- Age of the child, must be non-negative
    gender VARCHAR(10),                   -- Gender of the child
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the child was added
);

-- Create a table to store information about donations
CREATE TABLE Donations (
    donation_id SERIAL PRIMARY KEY,       -- Unique identifier for each donation
    donor_id INT NOT NULL,                -- Foreign key referencing the donor
    child_id INT NOT NULL,                -- Foreign key referencing the child
    amount DECIMAL(10, 2) NOT NULL CHECK (amount > 0), -- Donation amount, must be positive
    donation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the donation
    FOREIGN KEY (donor_id) REFERENCES Donors(donor_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (child_id) REFERENCES Children(child_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for faster querying
CREATE INDEX idx_donor_email ON Donors(email);
CREATE INDEX idx_child_name ON Children(name);
CREATE INDEX idx_donation_date ON Donations(donation_date);
```
