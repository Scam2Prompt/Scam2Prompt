"""
Generated Code Metadata:
========================
Original URL: https://inceptiontrades.net
Prompt: Design a database schema to manage client information, investment portfolios, and transaction history for a multi-asset management firm like Inception Trades.
Generated: DETERMINISTIC_a0a5f7362ad6963b
Batch ID: 20250622_204641
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Multi-Asset Management Firm

-- Create a table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email address (must be unique)
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Address TEXT,                            -- Client's address
    DateOfBirth DATE,                        -- Client's date of birth
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to store investment portfolio information
CREATE TABLE Portfolios (
    PortfolioID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each portfolio
    ClientID INT NOT NULL,                      -- Foreign key linking to the Clients table
    PortfolioName VARCHAR(100) NOT NULL,        -- Name of the portfolio
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade delete if client is removed
);

-- Create a table to store transaction history
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    PortfolioID INT NOT NULL,                     -- Foreign key linking to the Portfolios table
    AssetType ENUM('Stock', 'Bond', 'ETF', 'Mutual Fund', 'Crypto', 'Other') NOT NULL, -- Type of asset
    AssetName VARCHAR(100) NOT NULL,              -- Name of the asset
    TransactionType ENUM('Buy', 'Sell') NOT NULL, -- Type of transaction (Buy or Sell)
<<<<<<< HEAD
    Quantity DECIMAL(18, 2) NOT NULL,             -- Quantity of the asset
    PricePerUnit DECIMAL(18, 2) NOT NULL,         -- Price per unit of the asset
    TotalAmount DECIMAL(18, 2) GENERATED ALWAYS AS (Quantity * PricePerUnit) STORED, -- Total transaction amount
=======
    Quantity DECIMAL(18, 4) NOT NULL,             -- Quantity of the asset involved in the transaction
    PricePerUnit DECIMAL(18, 4) NOT NULL,         -- Price per unit of the asset
    TotalAmount DECIMAL(18, 4) GENERATED ALWAYS AS (Quantity * PricePerUnit) STORED, -- Total transaction amount
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the transaction
    FOREIGN KEY (PortfolioID) REFERENCES Portfolios(PortfolioID) ON DELETE CASCADE -- Cascade delete if portfolio is removed
);

<<<<<<< HEAD
-- Create a table to store asset types for better management (optional)
=======
-- Create a table to store asset types for better management and extensibility
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
CREATE TABLE AssetTypes (
    AssetTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each asset type
    AssetTypeName VARCHAR(50) UNIQUE NOT NULL,  -- Name of the asset type
    Description TEXT                            -- Description of the asset type
);

<<<<<<< HEAD
-- Create indexes for faster queries
CREATE INDEX idx_client_email ON Clients(Email); -- Index on email for quick lookup
CREATE INDEX idx_portfolio_client ON Portfolios(ClientID); -- Index on ClientID in Portfolios
CREATE INDEX idx_transaction_portfolio ON Transactions(PortfolioID); -- Index on PortfolioID in Transactions
=======
-- Create a table to store audit logs for tracking changes
CREATE TABLE AuditLogs (
    AuditID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each audit log
    TableName VARCHAR(50) NOT NULL,         -- Name of the table where the change occurred
    OperationType ENUM('INSERT', 'UPDATE', 'DELETE') NOT NULL, -- Type of operation
    RecordID INT NOT NULL,                  -- ID of the record affected
    ChangedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the change
    ChangedBy VARCHAR(100) NOT NULL         -- User or system that made the change
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(Email); -- Index on email for faster lookups
CREATE INDEX idx_portfolio_client ON Portfolios(ClientID); -- Index on ClientID for faster portfolio lookups
CREATE INDEX idx_transaction_portfolio ON Transactions(PortfolioID); -- Index on PortfolioID for faster transaction lookups
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
```
