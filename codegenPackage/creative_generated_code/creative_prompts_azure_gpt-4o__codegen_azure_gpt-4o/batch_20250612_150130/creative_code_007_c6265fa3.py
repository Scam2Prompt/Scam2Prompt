"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://advancecryptoacademy.online
Prompt: Create a database schema in SQL to store user investment data, transaction records, and plan details for a platform like Advance Crypto Academy.
Generated: DETERMINISTIC_c6265fa36e563869
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing user investment data, transaction records, and plan details

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for the user
    FullName VARCHAR(255) NOT NULL,               -- Full name of the user
    Email VARCHAR(255) NOT NULL UNIQUE,           -- Email address of the user, must be unique
    PasswordHash VARCHAR(255) NOT NULL,           -- Hashed password for security
    PhoneNumber VARCHAR(15),                      -- Optional phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table to store investment plans offered by the platform
CREATE TABLE InvestmentPlans (
    PlanID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for the investment plan
    PlanName VARCHAR(255) NOT NULL,               -- Name of the investment plan
    Description TEXT,                             -- Detailed description of the plan
    MinInvestmentAmount DECIMAL(10, 2) NOT NULL,  -- Minimum amount required for the plan
    MaxInvestmentAmount DECIMAL(10, 2),           -- Optional maximum limit for investment
    InterestRate DECIMAL(5, 2) NOT NULL,          -- Interest rate for the plan
    DurationInDays INT NOT NULL,                  -- Duration of the plan in days
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store user investments in different plans
CREATE TABLE UserInvestments (
    InvestmentID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for the investment record
    UserID INT NOT NULL,                          -- Foreign key referencing Users table
    PlanID INT NOT NULL,                          -- Foreign key referencing InvestmentPlans table
    InvestmentAmount DECIMAL(10, 2) NOT NULL,     -- Amount invested by the user
    StartDate DATE NOT NULL,                      -- Investment start date
    EndDate DATE NOT NULL,                        -- Investment end date
    Status ENUM('Active', 'Completed', 'Cancelled') DEFAULT 'Active', -- Investment status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE,
    FOREIGN KEY (PlanID) REFERENCES InvestmentPlans(PlanID) ON DELETE CASCADE
);

-- Table to store transaction records related to user activities
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the transaction record
    UserID INT NOT NULL,                          -- Foreign key referencing Users table
    InvestmentID INT,                             -- Optional foreign key referencing UserInvestments table
    TransactionType ENUM('Deposit', 'Withdrawal', 'Profit', 'Fee') NOT NULL, -- Type of transaction
    Amount DECIMAL(10, 2) NOT NULL,               -- Transaction amount
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of transaction
    Notes TEXT,                                   -- Optional notes for the transaction
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE,
    FOREIGN KEY (InvestmentID) REFERENCES UserInvestments(InvestmentID) ON DELETE SET NULL
);

-- Indexes for optimizing queries
CREATE INDEX idx_user_email ON Users (Email);
CREATE INDEX idx_investment_user ON UserInvestments (UserID);
CREATE INDEX idx_transaction_user ON Transactions (UserID);

-- Views for reporting (example: active investments for users)
CREATE VIEW ActiveUserInvestments AS
SELECT 
    u.FullName AS UserName,
    p.PlanName AS InvestmentPlan,
    ui.InvestmentAmount,
    ui.StartDate,
    ui.EndDate
FROM 
    UserInvestments ui
JOIN 
    Users u ON ui.UserID = u.UserID
JOIN 
    InvestmentPlans p ON ui.PlanID = p.PlanID
WHERE 
    ui.Status = 'Active';
```
