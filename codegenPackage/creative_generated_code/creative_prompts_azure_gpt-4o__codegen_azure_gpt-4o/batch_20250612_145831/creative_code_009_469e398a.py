"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smarts-invests.net
Prompt: Create a database schema for managing investment plans, user accounts, and transaction history, inspired by Smarts-invests' platform structure.
Generated: DETERMINISTIC_469e398aba181773
Batch ID: 20250612_145831
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing investment plans, user accounts, and transaction history

-- Table: Users
-- Description: Stores information about users who use the investment platform
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,          -- Unique username for the user
    Email VARCHAR(100) NOT NULL UNIQUE,            -- Email of the user
    PasswordHash VARCHAR(255) NOT NULL,            -- Hashed password for security
    FullName VARCHAR(100),                         -- Full name of the user
    PhoneNumber VARCHAR(15),                       -- Contact number of the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table: InvestmentPlans
-- Description: Stores information about available investment plans
CREATE TABLE InvestmentPlans (
    PlanID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each investment plan
    PlanName VARCHAR(100) NOT NULL UNIQUE,         -- Name of the investment plan
    Description TEXT,                              -- Description of the plan
    MinInvestmentAmount DECIMAL(10, 2) NOT NULL,   -- Minimum investment amount for the plan
    InterestRate FLOAT NOT NULL,                   -- Interest rate (percentage) offered by the plan
    DurationMonths INT NOT NULL,                   -- Duration of the investment plan in months
    IsActive BOOLEAN DEFAULT TRUE,                 -- Indicates if the plan is currently active
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Plan creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table: Transactions
-- Description: Stores transaction history for user investments and withdrawals
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each transaction
    UserID INT NOT NULL,                            -- Foreign key referencing Users table
    PlanID INT,                                     -- Foreign key referencing InvestmentPlans table (null for non-plan transactions)
    TransactionType ENUM('Deposit', 'Withdrawal'),  -- Type of transaction (Deposit or Withdrawal)
    Amount DECIMAL(10, 2) NOT NULL,                 -- Transaction amount
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Transaction timestamp
    Remarks TEXT,                                   -- Additional notes or remarks about the transaction
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete for user-related transactions
    FOREIGN KEY (PlanID) REFERENCES InvestmentPlans(PlanID) ON DELETE SET NULL -- Set null for plan-related transactions if plan is deleted
);

-- Table: UserInvestments
-- Description: Tracks investments made by users into specific plans
CREATE TABLE UserInvestments (
    InvestmentID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each investment record
    UserID INT NOT NULL,                            -- Foreign key referencing Users table
    PlanID INT NOT NULL,                            -- Foreign key referencing InvestmentPlans table
    InvestmentAmount DECIMAL(10, 2) NOT NULL,       -- Amount invested by the user
    InvestmentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Investment date
    MaturityDate TIMESTAMP,                         -- Date when the investment matures
    Status ENUM('Active', 'Completed', 'Cancelled') DEFAULT 'Active', -- Status of the investment
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete for user-related investments
    FOREIGN KEY (PlanID) REFERENCES InvestmentPlans(PlanID) ON DELETE CASCADE -- Cascade delete for plan-related investments
);

-- Indexes for performance optimization
CREATE INDEX idx_user_email ON Users (Email);
CREATE INDEX idx_transaction_user ON Transactions (UserID);
CREATE INDEX idx_investment_user_plan ON UserInvestments (UserID, PlanID);
```
