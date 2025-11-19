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
-- Database Schema for Genesis Investment Credit Union

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Customer's email address (must be unique)
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    Address TEXT,                              -- Customer's physical address
    DateOfBirth DATE NOT NULL,                 -- Customer's date of birth
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store account information
CREATE TABLE Accounts (
    AccountID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each account
    CustomerID INT NOT NULL,                   -- Foreign key linking to Customers table
    AccountType ENUM('Savings', 'Checking', 'Loan', 'CreditCard') NOT NULL, -- Type of account
    Balance DECIMAL(15, 2) NOT NULL DEFAULT 0, -- Current balance in the account
    InterestRate DECIMAL(5, 2),                -- Interest rate for applicable accounts
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store transaction information
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    AccountID INT NOT NULL,                       -- Foreign key linking to Accounts table
    TransactionType ENUM('Deposit', 'Withdrawal', 'Transfer', 'Payment') NOT NULL, -- Type of transaction
    Amount DECIMAL(15, 2) NOT NULL,              -- Transaction amount
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of transaction
    Description TEXT,                            -- Optional description of the transaction
    FOREIGN KEY (AccountID) REFERENCES Accounts(AccountID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store loan information
CREATE TABLE Loans (
    LoanID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each loan
    CustomerID INT NOT NULL,                    -- Foreign key linking to Customers table
    LoanAmount DECIMAL(15, 2) NOT NULL,         -- Total loan amount
    InterestRate DECIMAL(5, 2) NOT NULL,        -- Interest rate for the loan
    LoanTermMonths INT NOT NULL,                -- Loan term in months
    MonthlyPayment DECIMAL(15, 2) NOT NULL,     -- Monthly payment amount
    StartDate DATE NOT NULL,                    -- Loan start date
    EndDate DATE NOT NULL,                      -- Loan end date
    Status ENUM('Active', 'Closed', 'Defaulted') NOT NULL DEFAULT 'Active', -- Loan status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store credit card information
CREATE TABLE CreditCards (
    CreditCardID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each credit card
    CustomerID INT NOT NULL,                     -- Foreign key linking to Customers table
    CardNumber VARCHAR(16) UNIQUE NOT NULL,      -- Credit card number (must be unique)
    ExpirationDate DATE NOT NULL,                -- Credit card expiration date
    CVV VARCHAR(4) NOT NULL,                     -- Credit card CVV code
    CreditLimit DECIMAL(15, 2) NOT NULL,         -- Maximum credit limit
    CurrentBalance DECIMAL(15, 2) NOT NULL DEFAULT 0, -- Current balance on the card
    Status ENUM('Active', 'Blocked', 'Closed') NOT NULL DEFAULT 'Active', -- Credit card status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store payment history for loans and credit cards
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each payment
    CustomerID INT NOT NULL,                    -- Foreign key linking to Customers table
    PaymentType ENUM('Loan', 'CreditCard') NOT NULL, -- Type of payment
    ReferenceID INT NOT NULL,                   -- Reference to LoanID or CreditCardID
    Amount DECIMAL(15, 2) NOT NULL,             -- Payment amount
    PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of payment
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Cascade delete
);

-- Indexes for optimizing queries
CREATE INDEX idx_customer_email ON Customers(Email); -- Index for quick lookup by email
CREATE INDEX idx_account_customer ON Accounts(CustomerID); -- Index for quick lookup by customer ID
CREATE INDEX idx_transaction_account ON Transactions(AccountID); -- Index for quick lookup by account ID
CREATE INDEX idx_loan_customer ON Loans(CustomerID); -- Index for quick lookup by customer ID
CREATE INDEX idx_creditcard_customer ON CreditCards(CustomerID); -- Index for quick lookup by customer ID
CREATE INDEX idx_payment_customer ON Payments(CustomerID); -- Index for quick lookup by customer ID
```
