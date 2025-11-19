"""
Generated Code Metadata:
========================
Original URL: https://rakhshandamemorial.org
Prompt: Create a database schema for managing RM's projects, including tables for tracking beneficiaries, volunteers, donations, and event schedules.
Generated: DETERMINISTIC_657f750a50ed29cc
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing RM's projects

-- Create a database for RM's projects
CREATE DATABASE rm_projects;

-- Use the created database
USE rm_projects;

-- Table to track beneficiaries
CREATE TABLE beneficiaries (
    beneficiary_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each beneficiary
    name VARCHAR(100) NOT NULL,                    -- Name of the beneficiary
    contact_info VARCHAR(255),                      -- Contact information for the beneficiary
    address VARCHAR(255),                           -- Address of the beneficiary
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to track volunteers
CREATE TABLE volunteers (
    volunteer_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each volunteer
    name VARCHAR(100) NOT NULL,                     -- Name of the volunteer
    contact_info VARCHAR(255),                       -- Contact information for the volunteer
    availability VARCHAR(255),                       -- Availability of the volunteer
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to track donations
CREATE TABLE donations (
    donation_id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each donation
    donor_name VARCHAR(100) NOT NULL,                -- Name of the donor
    amount DECIMAL(10, 2) NOT NULL,                  -- Amount donated
    donation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the donation
    beneficiary_id INT,                               -- Foreign key referencing beneficiaries
    FOREIGN KEY (beneficiary_id) REFERENCES beneficiaries(beneficiary_id) ON DELETE SET NULL, -- Relationship to beneficiaries
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to track event schedules
CREATE TABLE event_schedules (
    event_id INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each event
    event_name VARCHAR(100) NOT NULL,                 -- Name of the event
    event_date DATETIME NOT NULL,                      -- Date and time of the event
    location VARCHAR(255),                             -- Location of the event
    volunteer_id INT,                                  -- Foreign key referencing volunteers
    FOREIGN KEY (volunteer_id) REFERENCES volunteers(volunteer_id) ON DELETE SET NULL, -- Relationship to volunteers
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Indexes for performance optimization
CREATE INDEX idx_beneficiary_name ON beneficiaries(name);
CREATE INDEX idx_volunteer_name ON volunteers(name);
CREATE INDEX idx_donation_date ON donations(donation_date);
CREATE INDEX idx_event_date ON event_schedules(event_date);
```
