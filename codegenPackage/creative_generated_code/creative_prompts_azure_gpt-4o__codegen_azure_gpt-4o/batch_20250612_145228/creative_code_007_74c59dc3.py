"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sgfcfinance.com
Prompt: Develop a database schema for SGFC Finance to manage client information, loan types, repayment schedules, and community outreach activities.
Generated: DETERMINISTIC_74c59dc3f9a4bc41
Batch ID: 20250612_145228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for SGFC Finance

-- Table: Clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email address
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Address TEXT,                            -- Client's address
    DateOfBirth DATE,                        -- Client's date of birth
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the client was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table: LoanTypes
CREATE TABLE LoanTypes (
    LoanTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each loan type
    LoanName VARCHAR(100) NOT NULL,            -- Name of the loan type
    InterestRate DECIMAL(5, 2) NOT NULL,       -- Interest rate for the loan type
    MaxAmount DECIMAL(15, 2) NOT NULL,         -- Maximum amount allowed for the loan
    MinAmount DECIMAL(15, 2) NOT NULL,         -- Minimum amount allowed for the loan
    DurationMonths INT NOT NULL,               -- Duration of the loan in months
    Description TEXT,                          -- Description of the loan type
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the loan type was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table: Loans
CREATE TABLE Loans (
    LoanID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each loan
    ClientID INT NOT NULL,                     -- Foreign key to the Clients table
    LoanTypeID INT NOT NULL,                   -- Foreign key to the LoanTypes table
    LoanAmount DECIMAL(15, 2) NOT NULL,        -- Amount of the loan
    LoanStartDate DATE NOT NULL,               -- Start date of the loan
    LoanEndDate DATE NOT NULL,                 -- End date of the loan
    Status ENUM('Active', 'Closed', 'Defaulted') DEFAULT 'Active', -- Loan status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the loan was issued
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,
    FOREIGN KEY (LoanTypeID) REFERENCES LoanTypes(LoanTypeID) ON DELETE CASCADE
);

-- Table: RepaymentSchedules
CREATE TABLE RepaymentSchedules (
    RepaymentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each repayment schedule entry
    LoanID INT NOT NULL,                        -- Foreign key to the Loans table
    DueDate DATE NOT NULL,                      -- Due date for the repayment
    AmountDue DECIMAL(15, 2) NOT NULL,          -- Amount due for this repayment
    AmountPaid DECIMAL(15, 2) DEFAULT 0.00,     -- Amount paid (default is 0 if unpaid)
    Status ENUM('Pending', 'Paid', 'Late') DEFAULT 'Pending', -- Status of the repayment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the schedule was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (LoanID) REFERENCES Loans(LoanID) ON DELETE CASCADE
);

-- Table: CommunityOutreach
CREATE TABLE CommunityOutreach (
    OutreachID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each outreach activity
    ActivityName VARCHAR(100) NOT NULL,        -- Name of the outreach activity
    Description TEXT,                          -- Description of the activity
    Location VARCHAR(100),                     -- Location of the outreach activity
    Date DATE NOT NULL,                        -- Date of the outreach activity
    Budget DECIMAL(15, 2) NOT NULL,            -- Budget allocated for the activity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the activity was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);
```
