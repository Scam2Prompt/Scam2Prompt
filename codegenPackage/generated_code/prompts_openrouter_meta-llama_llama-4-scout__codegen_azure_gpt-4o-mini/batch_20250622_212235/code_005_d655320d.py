"""
Generated Code Metadata:
========================
Original URL: https://giac1.ma
Prompt: Design a database schema to store information about GIAC1's members, financing applications, and reimbursement records, ensuring data integrity and scalability.
Generated: DETERMINISTIC_d655320ded7021d8
Batch ID: 20250622_212235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for GIAC1's members, financing applications, and reimbursement records

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS Reimbursements;
DROP TABLE IF EXISTS FinancingApplications;
DROP TABLE IF EXISTS Members;

-- Table to store information about members
CREATE TABLE Members (
    MemberID SERIAL PRIMARY KEY, -- Unique identifier for each member
    FirstName VARCHAR(50) NOT NULL, -- Member's first name
    LastName VARCHAR(50) NOT NULL, -- Member's last name
    Email VARCHAR(100) UNIQUE NOT NULL, -- Member's email address
    PhoneNumber VARCHAR(15), -- Member's phone number
    DateJoined TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date the member joined
    Status VARCHAR(20) CHECK (Status IN ('Active', 'Inactive')) DEFAULT 'Active' -- Member status
);

-- Table to store financing applications
CREATE TABLE FinancingApplications (
    ApplicationID SERIAL PRIMARY KEY, -- Unique identifier for each application
    MemberID INT NOT NULL, -- Foreign key referencing Members
    ApplicationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of application
    AmountRequested DECIMAL(10, 2) NOT NULL, -- Amount requested
    Status VARCHAR(20) CHECK (Status IN ('Pending', 'Approved', 'Denied')) DEFAULT 'Pending', -- Application status
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID) ON DELETE CASCADE -- Ensures data integrity
);

-- Table to store reimbursement records
CREATE TABLE Reimbursements (
    ReimbursementID SERIAL PRIMARY KEY, -- Unique identifier for each reimbursement
    ApplicationID INT NOT NULL, -- Foreign key referencing FinancingApplications
    ReimbursementDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of reimbursement
    Amount DECIMAL(10, 2) NOT NULL, -- Amount reimbursed
    Status VARCHAR(20) CHECK (Status IN ('Pending', 'Completed', 'Denied')) DEFAULT 'Pending', -- Reimbursement status
    FOREIGN KEY (ApplicationID) REFERENCES FinancingApplications(ApplicationID) ON DELETE CASCADE -- Ensures data integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_member_email ON Members(Email);
CREATE INDEX idx_application_member ON FinancingApplications(MemberID);
CREATE INDEX idx_reimbursement_application ON Reimbursements(ApplicationID);
```
