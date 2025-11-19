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
-- Database schema for St. Andrew's School Project For The Young charity

-- Create database
CREATE DATABASE charity_project;
USE charity_project;

-- Donors table
CREATE TABLE donors (
    donor_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    address VARCHAR(255),
    city VARCHAR(50),
    state VARCHAR(50),
    postal_code VARCHAR(20),
    country VARCHAR(50),
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    notes TEXT,
    CONSTRAINT chk_email CHECK (email LIKE '%@%.%')
);

-- Children table
CREATE TABLE children (
    child_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    birth_date DATE,
    gender ENUM('Male', 'Female', 'Other'),
    school_grade VARCHAR(20),
    school_name VARCHAR(100),
    guardian_name VARCHAR(100),
    guardian_contact VARCHAR(50),
    address VARCHAR(255),
    city VARCHAR(50),
    state VARCHAR(50),
    postal_code VARCHAR(20),
    country VARCHAR(50),
    enrollment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    special_needs TEXT,
    notes TEXT
);

-- Donation types table
CREATE TABLE donation_types (
    type_id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT
);

-- Insert common donation types
INSERT INTO donation_types (type_name, description) VALUES
    ('Monetary', 'Cash donations'),
    ('School Supplies', 'Books, notebooks, pens, etc.'),
    ('Clothing', 'Uniforms, shoes, etc.'),
    ('Food', 'Nutritional support'),
    ('Other', 'Other types of donations');

-- Donations table
CREATE TABLE donations (
    donation_id INT AUTO_INCREMENT PRIMARY KEY,
    donor_id INT NOT NULL,
    child_id INT,
    type_id INT NOT NULL,
    amount DECIMAL(10, 2),
    quantity INT,
    description TEXT,
    donation_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    is_recurring BOOLEAN DEFAULT FALSE,
    recurrence_interval VARCHAR(20),
    payment_method VARCHAR(50),
    transaction_reference VARCHAR(100),
    status ENUM('Pending', 'Completed', 'Failed', 'Refunded') DEFAULT 'Completed',
    notes TEXT,
    FOREIGN KEY (donor_id) REFERENCES donors(donor_id) ON DELETE RESTRICT,
    FOREIGN KEY (child_id) REFERENCES children(child_id) ON DELETE SET NULL,
    FOREIGN KEY (type_id) REFERENCES donation_types(type_id) ON DELETE RESTRICT,
    CONSTRAINT chk_amount CHECK (amount >= 0),
    CONSTRAINT chk_quantity CHECK (quantity >= 0)
);

-- Sponsorships table (for long-term donor-child relationships)
CREATE TABLE sponsorships (
    sponsorship_id INT AUTO_INCREMENT PRIMARY KEY,
    donor_id INT NOT NULL,
    child_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    monthly_amount DECIMAL(10, 2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    notes TEXT,
    FOREIGN KEY (donor_id) REFERENCES donors(donor_id) ON DELETE CASCADE,
    FOREIGN KEY (child_id) REFERENCES children(child_id) ON DELETE CASCADE,
    CONSTRAINT chk_dates CHECK (end_date IS NULL OR end_date > start_date),
    CONSTRAINT chk_monthly_amount CHECK (monthly_amount > 0)
);

-- Create indexes for performance
CREATE INDEX idx_donor_name ON donors(last_name, first_name);
CREATE INDEX idx_child_name ON children(last_name, first_name);
CREATE INDEX idx_donation_date ON donations(donation_date);
CREATE INDEX idx_donation_donor ON donations(donor_id);
CREATE INDEX idx_donation_child ON donations(child_id);
CREATE INDEX idx_sponsorship_donor ON sponsorships(donor_id);
CREATE INDEX idx_sponsorship_child ON sponsorships(child_id);
```
