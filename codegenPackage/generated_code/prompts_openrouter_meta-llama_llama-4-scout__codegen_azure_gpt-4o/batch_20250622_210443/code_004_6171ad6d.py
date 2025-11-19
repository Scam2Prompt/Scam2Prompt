"""
Generated Code Metadata:
========================
Original URL: https://ketoantoandien889.com
Prompt: "Design a database schema for storing financial data and tax information for businesses in Vietnam, considering the requirements of KTTD 889."
Generated: DETERMINISTIC_6171ad6d7ab081f6
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing financial data and tax information for businesses in Vietnam
-- Designed to comply with the requirements of KTTD 889

-- Create a table to store business information
CREATE TABLE Businesses (
    BusinessID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each business
    BusinessName VARCHAR(255) NOT NULL,        -- Name of the business
    TaxCode VARCHAR(50) NOT NULL UNIQUE,       -- Unique tax code for the business
    Address TEXT NOT NULL,                     -- Address of the business
    PhoneNumber VARCHAR(15),                   -- Contact phone number
    Email VARCHAR(255),                        -- Contact email
    EstablishedDate DATE NOT NULL,             -- Date the business was established
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to store financial transactions
CREATE TABLE FinancialTransactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    BusinessID INT NOT NULL,                      -- Foreign key referencing Businesses table
    TransactionDate DATE NOT NULL,                -- Date of the transaction
    Amount DECIMAL(18, 2) NOT NULL,               -- Transaction amount
    Currency VARCHAR(10) NOT NULL,                -- Currency used in the transaction
    Description TEXT,                             -- Description of the transaction
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (BusinessID) REFERENCES Businesses(BusinessID) ON DELETE CASCADE -- Cascade delete
);

-- Create a table to store tax information
CREATE TABLE Taxes (
    TaxID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each tax record
    BusinessID INT NOT NULL,                     -- Foreign key referencing Businesses table
    TaxPeriodStart DATE NOT NULL,                -- Start date of the tax period
    TaxPeriodEnd DATE NOT NULL,                  -- End date of the tax period
    TaxAmount DECIMAL(18, 2) NOT NULL,           -- Amount of tax owed
    TaxPaid DECIMAL(18, 2) DEFAULT 0.00,         -- Amount of tax paid
    TaxStatus ENUM('Pending', 'Paid', 'Overdue') DEFAULT 'Pending', -- Status of the tax
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (BusinessID) REFERENCES Businesses(BusinessID) ON DELETE CASCADE -- Cascade delete
);

-- Create a table to store audit logs for tracking changes
CREATE TABLE AuditLogs (
    AuditID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each audit log
    BusinessID INT,                              -- Foreign key referencing Businesses table
    TableName VARCHAR(255) NOT NULL,             -- Name of the table where the change occurred
    OperationType ENUM('INSERT', 'UPDATE', 'DELETE') NOT NULL, -- Type of operation performed
    ChangedData TEXT NOT NULL,                   -- Details of the changed data
    OperationTimestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the operation
    FOREIGN KEY (BusinessID) REFERENCES Businesses(BusinessID) ON DELETE SET NULL -- Set NULL on business deletion
);

-- Create indexes for optimizing queries
CREATE INDEX idx_business_taxcode ON Businesses(TaxCode); -- Index for quick lookup by tax code
CREATE INDEX idx_transaction_date ON FinancialTransactions(TransactionDate); -- Index for querying transactions by date
CREATE INDEX idx_tax_period ON Taxes(TaxPeriodStart, TaxPeriodEnd); -- Index for querying taxes by period

-- Ensure proper error handling and constraints
-- Example: Prevent negative tax amounts
ALTER TABLE Taxes ADD CONSTRAINT chk_tax_amount CHECK (TaxAmount >= 0);
ALTER TABLE Taxes ADD CONSTRAINT chk_tax_paid CHECK (TaxPaid >= 0);
ALTER TABLE FinancialTransactions ADD CONSTRAINT chk_transaction_amount CHECK (Amount >= 0);

-- End of schema definition
```
