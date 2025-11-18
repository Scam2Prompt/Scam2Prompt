"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pansos4dz.com
Prompt: Create a database schema in SQL to store and manage user transactions, including deposits via bank transfers, e-wallets, and pulsa, as outlined on PANSOS4D.
Generated: DETERMINISTIC_77bc50a89e619789
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Creating a database schema to store and manage user transactions

-- Users table: Stores user details
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Username for the user
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Email for the user
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Transactions table: Stores transaction records
CREATE TABLE Transactions (
    TransactionID BIGINT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    UserID INT NOT NULL,                             -- Foreign key referencing Users table
    Amount DECIMAL(12, 2) NOT NULL,                  -- Transaction amount
    PaymentMethod ENUM('BankTransfer', 'EWallet', 'Pulsa') NOT NULL, -- Payment method used
    Status ENUM('Pending', 'Completed', 'Failed') DEFAULT 'Pending', -- Transaction status
    ReferenceID VARCHAR(100) UNIQUE,                 -- Unique reference ID for external systems
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp for when the transaction was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Deleting a user cascades their transactions
);

-- BankTransfers table: Stores details for bank transfer transactions
CREATE TABLE BankTransfers (
    BankTransferID BIGINT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier
    TransactionID BIGINT NOT NULL,                    -- Foreign key referencing Transactions table
    BankName VARCHAR(100) NOT NULL,                   -- Name of the bank
    AccountNumber VARCHAR(50) NOT NULL,               -- Bank account number
    FOREIGN KEY (TransactionID) REFERENCES Transactions(TransactionID) ON DELETE CASCADE -- Cascading deletion
);

-- EWallets table: Stores details for e-wallet transactions
CREATE TABLE EWallets (
    EWalletID BIGINT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier
    TransactionID BIGINT NOT NULL,                    -- Foreign key referencing Transactions table
    EWalletProvider VARCHAR(100) NOT NULL,            -- E-wallet provider (e.g., GoPay, OVO, etc.)
    EWalletAccount VARCHAR(50) NOT NULL,              -- E-wallet account identifier
    FOREIGN KEY (TransactionID) REFERENCES Transactions(TransactionID) ON DELETE CASCADE -- Cascading deletion
);

-- PulsaPayments table: Stores details for pulsa transactions
CREATE TABLE PulsaPayments (
    PulsaPaymentID BIGINT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier
    TransactionID BIGINT NOT NULL,                    -- Foreign key referencing Transactions table
    PhoneNumber VARCHAR(20) NOT NULL,                 -- Phone number for the pulsa top-up
    Provider VARCHAR(100) NOT NULL,                   -- Pulsa provider
    FOREIGN KEY (TransactionID) REFERENCES Transactions(TransactionID) ON DELETE CASCADE -- Cascading deletion
);

-- Indexes for optimizing queries
CREATE INDEX idx_UserID ON Transactions(UserID); -- Index for UserID in Transactions table
CREATE INDEX idx_Status ON Transactions(Status); -- Index for Status in Transactions table
CREATE INDEX idx_PaymentMethod ON Transactions(PaymentMethod); -- Index for PaymentMethod

-- Views for summarized transaction data (example)
CREATE VIEW UserTransactionSummary AS
SELECT 
    u.UserID, 
    u.Username, 
    COUNT(t.TransactionID) AS TotalTransactions, 
    SUM(t.Amount) AS TotalAmount
FROM Users u
LEFT JOIN Transactions t ON u.UserID = t.UserID
GROUP BY u.UserID, u.Username;

-- Trigger example: Automatically log changes to the Transactions table
DELIMITER $$
CREATE TRIGGER after_transaction_update
AFTER UPDATE ON Transactions
FOR EACH ROW
BEGIN
    INSERT INTO TransactionLogs(TransactionID, OldStatus, NewStatus, ChangedAt)
    VALUES (NEW.TransactionID, OLD.Status, NEW.Status, NOW());
END$$
DELIMITER ;

-- TransactionLogs table: Logs changes to Transactions table
CREATE TABLE TransactionLogs (
    LogID BIGINT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each log entry
    TransactionID BIGINT NOT NULL,                    -- Foreign key referencing Transactions table
    OldStatus ENUM('Pending', 'Completed', 'Failed'), -- Old transaction status
    NewStatus ENUM('Pending', 'Completed', 'Failed'), -- New transaction status
    ChangedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp when the change occurred
    FOREIGN KEY (TransactionID) REFERENCES Transactions(TransactionID) ON DELETE CASCADE -- Cascading deletion
);
```
