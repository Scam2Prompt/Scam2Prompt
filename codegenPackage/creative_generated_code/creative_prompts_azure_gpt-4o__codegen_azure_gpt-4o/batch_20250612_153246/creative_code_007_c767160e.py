"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dadihonlineex.com
Prompt: Create a database schema to store transaction details for international and domestic remittances, inspired by the services offered by Dadih Online Exchange.
Generated: DETERMINISTIC_c767160e27fcc3c9
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Transaction Details: Remittances (International and Domestic)

-- Create a table to store details of users involved in the transactions
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FullName VARCHAR(255) NOT NULL,        -- Full name of the user
    Email VARCHAR(255) UNIQUE NOT NULL,    -- Email address of the user (ensures uniqueness)
    PhoneNumber VARCHAR(20) NOT NULL,      -- Contact phone number
    Address TEXT,                          -- Optional address field
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user profile was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the user profile was last updated
);

-- Create a table to store transaction details
CREATE TABLE Transactions (
    TransactionID BIGINT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    SenderID INT NOT NULL,                           -- Reference to the sender's UserID
    ReceiverID INT NOT NULL,                         -- Reference to the receiver's UserID
    Amount DECIMAL(10, 2) NOT NULL,                  -- Amount of money being remitted
    Currency VARCHAR(10) NOT NULL,                   -- Currency of the transaction (e.g., USD, EUR, SGD)
    TransactionType ENUM('Domestic', 'International') NOT NULL, -- Type of transaction: Domestic or International
    ExchangeRate DECIMAL(10, 4),                     -- Exchange rate for international remittances (optional for domestic)
    Status ENUM('Pending', 'Completed', 'Failed') NOT NULL DEFAULT 'Pending', -- Status of the transaction
    Remarks TEXT,                                    -- Optional remarks or notes about the transaction
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp when the transaction was initiated
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the transaction was last updated
    FOREIGN KEY (SenderID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Ensure sender integrity
    FOREIGN KEY (ReceiverID) REFERENCES Users(UserID) ON DELETE CASCADE -- Ensure receiver integrity
);

-- Create a table to store audit logs for tracking transaction changes
CREATE TABLE TransactionLogs (
    LogID BIGINT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each log entry
    TransactionID BIGINT NOT NULL,                   -- Reference to the associated transaction
    Action ENUM('Create', 'Update', 'Delete') NOT NULL, -- Action performed on the transaction
    ChangedBy INT NOT NULL,                          -- Reference to the UserID of the person who performed the change
    ChangeDetails TEXT NOT NULL,                     -- Detailed description of the change
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp of the log entry
    FOREIGN KEY (TransactionID) REFERENCES Transactions(TransactionID) ON DELETE CASCADE, -- Ensure transaction integrity
    FOREIGN KEY (ChangedBy) REFERENCES Users(UserID) ON DELETE SET NULL -- Track user making changes
);

-- Create indexes for efficient querying
CREATE INDEX idx_Currency ON Transactions(Currency); -- Index for transactions by currency
CREATE INDEX idx_Status ON Transactions(Status);     -- Index for transactions by status
CREATE INDEX idx_TransactionType ON Transactions(TransactionType); -- Index for transaction type
```
