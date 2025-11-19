"""
Generated Code Metadata:
========================
Original URL: https://genesisicu.com
Prompt: Design a database schema for storing customer information and financial data for a credit union, considering the various services offered by Genesis Investment Credit Union.
Generated: DETERMINISTIC_50f4a655f10e29a9
Batch ID: 20250622_211723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Genesis Investment Credit Union

-- Create a table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,           -- Customer's first name
    LastName VARCHAR(50) NOT NULL,            -- Customer's last name
    DateOfBirth DATE NOT NULL,                 -- Customer's date of birth
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Customer's email address
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    Address VARCHAR(255),                       -- Customer's address
    City VARCHAR(50),                          -- Customer's city
    State VARCHAR(50),                         -- Customer's state
    ZipCode VARCHAR(10),                       -- Customer's zip code
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to store account information
CREATE TABLE Accounts (
    AccountID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each account
    CustomerID INT NOT NULL,                    -- Foreign key referencing Customers
    AccountType ENUM('Checking', 'Savings', 'Loan', 'Investment') NOT NULL, -- Type of account
    Balance DECIMAL(15, 2) NOT NULL DEFAULT 0.00, -- Account balance
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store transaction records
CREATE TABLE Transactions (
    TransactionID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each transaction
    AccountID INT NOT NULL,                        -- Foreign key referencing Accounts
    TransactionType ENUM('Deposit', 'Withdrawal', 'Transfer') NOT NULL, -- Type of transaction
    Amount DECIMAL(15, 2) NOT NULL,               -- Transaction amount
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of transaction
    Description VARCHAR(255),                      -- Description of the transaction
    FOREIGN KEY (AccountID) REFERENCES Accounts(AccountID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store loan information
CREATE TABLE Loans (
    LoanID INT PRIMARY KEY AUTO_INCREMENT,         -- Unique identifier for each loan
    CustomerID INT NOT NULL,                       -- Foreign key referencing Customers
    LoanType ENUM('Personal', 'Auto', 'Home', 'Education') NOT NULL, -- Type of loan
    LoanAmount DECIMAL(15, 2) NOT NULL,           -- Total loan amount
    InterestRate DECIMAL(5, 2) NOT NULL,          -- Interest rate for the loan
    StartDate DATE NOT NULL,                       -- Start date of the loan
    EndDate DATE NOT NULL,                         -- End date of the loan
    Status ENUM('Active', 'Paid', 'Defaulted') NOT NULL, -- Current status of the loan
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store investment information
CREATE TABLE Investments (
    InvestmentID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each investment
    CustomerID INT NOT NULL,                       -- Foreign key referencing Customers
    InvestmentType ENUM('Stocks', 'Bonds', 'Mutual Funds', 'Real Estate') NOT NULL, -- Type of investment
    AmountInvested DECIMAL(15, 2) NOT NULL,       -- Amount invested
    CurrentValue DECIMAL(15, 2) NOT NULL,         -- Current value of the investment
    InvestmentDate DATE NOT NULL,                  -- Date of investment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensure referential integrity
);
```
