"""
Generated Code Metadata:
========================
Original URL: https://sgfcfinance.com
Prompt: Develop a database schema for SGFC Finance to manage client information, loan types, repayment schedules, and community outreach activities.
Generated: DETERMINISTIC_74c59dc3f9a4bc41
Batch ID: 20250612_145228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for SGFC Finance

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS CommunityOutreachActivities;
DROP TABLE IF EXISTS RepaymentSchedules;
DROP TABLE IF EXISTS LoanTypes;
DROP TABLE IF EXISTS Clients;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email address (unique)
    PhoneNumber VARCHAR(15),                  -- Client's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store different loan types
CREATE TABLE LoanTypes (
    LoanTypeID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each loan type
    LoanTypeName VARCHAR(100) NOT NULL,        -- Name of the loan type
    InterestRate DECIMAL(5, 2) NOT NULL,       -- Interest rate for the loan type
    MaxLoanAmount DECIMAL(15, 2) NOT NULL,     -- Maximum loan amount for this type
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store repayment schedules for loans
CREATE TABLE RepaymentSchedules (
    RepaymentScheduleID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each repayment schedule
    ClientID INT NOT NULL,                               -- Foreign key referencing Clients
    LoanTypeID INT NOT NULL,                            -- Foreign key referencing LoanTypes
    TotalAmount DECIMAL(15, 2) NOT NULL,               -- Total amount to be repaid
    MonthlyPayment DECIMAL(15, 2) NOT NULL,            -- Monthly payment amount
    StartDate DATE NOT NULL,                            -- Start date of the repayment
    EndDate DATE NOT NULL,                              -- End date of the repayment
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,  -- Cascade delete on client removal
    FOREIGN KEY (LoanTypeID) REFERENCES LoanTypes(LoanTypeID) ON DELETE CASCADE,  -- Cascade delete on loan type removal
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,      -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store community outreach activities
CREATE TABLE CommunityOutreachActivities (
    ActivityID INT PRIMARY KEY AUTO_INCREMENT,         -- Unique identifier for each activity
    ActivityName VARCHAR(100) NOT NULL,               -- Name of the outreach activity
    Description TEXT,                                   -- Description of the activity
    ActivityDate DATE NOT NULL,                        -- Date of the activity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,      -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);
```
