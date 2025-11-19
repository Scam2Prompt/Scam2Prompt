"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimlink.io
Prompt: Design a database schema for managing high-quality legal leads, incorporating the specific types of cases highlighted on ClaimLink, such as truck and motorcycle accidents.
Generated: DETERMINISTIC_38236c49d08ebb89
Batch ID: 20250612_163546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing high-quality legal leads

-- Create a database for the legal leads
CREATE DATABASE LegalLeadsDB;

-- Use the created database
USE LegalLeadsDB;

-- Table to store information about leads
CREATE TABLE Leads (
    lead_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each lead
    first_name VARCHAR(50) NOT NULL,        -- First name of the lead
    last_name VARCHAR(50) NOT NULL,         -- Last name of the lead
    email VARCHAR(100) NOT NULL UNIQUE,     -- Unique email for contact
    phone_number VARCHAR(15) NOT NULL,      -- Phone number for contact
    case_type ENUM('Truck Accident', 'Motorcycle Accident', 'Car Accident', 'Slip and Fall', 'Medical Malpractice') NOT NULL, -- Type of case
    status ENUM('New', 'Contacted', 'Qualified', 'Converted', 'Closed') DEFAULT 'New', -- Status of the lead
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the lead was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Table to store case details
CREATE TABLE CaseDetails (
    case_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each case detail
    lead_id INT NOT NULL,                    -- Foreign key linking to the Leads table
    accident_date DATE NOT NULL,             -- Date of the accident
    location VARCHAR(255) NOT NULL,          -- Location of the accident
    description TEXT,                        -- Detailed description of the case
    damages DECIMAL(10, 2),                  -- Estimated damages
    FOREIGN KEY (lead_id) REFERENCES Leads(lead_id) ON DELETE CASCADE -- Reference to Leads table, cascading on delete
);

-- Table to store communication logs
CREATE TABLE CommunicationLogs (
    log_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each log entry
    lead_id INT NOT NULL,                   -- Foreign key linking to the Leads table
    communication_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of communication
    method ENUM('Email', 'Phone', 'In-Person', 'Other') NOT NULL, -- Method of communication
    notes TEXT,                             -- Notes from the communication
    FOREIGN KEY (lead_id) REFERENCES Leads(lead_id) ON DELETE CASCADE -- Reference to Leads table, cascading on delete
);

-- Table for storing user information (if needed for system access)
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,    -- Unique username for login
    password_hash VARCHAR(255) NOT NULL,     -- Hashed password for security
    role ENUM('Admin', 'Agent') DEFAULT 'Agent', -- Role in the system
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the user was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Index creation to improve performance on commonly queried fields
CREATE INDEX idx_email ON Leads(email);
CREATE INDEX idx_case_type ON Leads(case_type);
CREATE INDEX idx_status ON Leads(status);
CREATE INDEX idx_lead_id ON CaseDetails(lead_id);
CREATE INDEX idx_log_lead_id ON CommunicationLogs(lead_id);

-- Commit the changes to the database
COMMIT;

-- Note: Ensure to implement proper access controls and data validation in the application layer.
```
