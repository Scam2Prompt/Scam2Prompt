"""
Generated Code Metadata:
========================
Original URL: https://www.precisaocontabil.com
Prompt: "Design a database schema for storing financial transactions in a multi-user environment."
Generated: DETERMINISTIC_83ffbefee50ac278
Batch ID: 20250622_212342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing financial transactions in a multi-user environment

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Unique username for the user
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Unique email address for the user
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store financial transactions
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    UserID INT NOT NULL,                          -- Foreign key referencing the Users table
    Amount DECIMAL(15, 2) NOT NULL,               -- Transaction amount (supports up to 13 digits before the decimal and 2 after)
    Currency VARCHAR(3) NOT NULL,                 -- Currency code (e.g., USD, EUR)
    TransactionType ENUM('credit', 'debit') NOT NULL, -- Type of transaction (credit or debit)
    Description VARCHAR(255),                     -- Optional description of the transaction
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the transaction was created
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Table to store audit logs for tracking changes
CREATE TABLE AuditLogs (
    AuditID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each audit log entry
    UserID INT NOT NULL,                          -- Foreign key referencing the Users table
    Action VARCHAR(50) NOT NULL,                  -- Action performed (e.g., 'CREATE_TRANSACTION', 'DELETE_USER')
    Details TEXT,                                 -- Detailed information about the action
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the action occurred
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_user_transactions ON Transactions(UserID); -- Index for faster lookup of transactions by user
CREATE INDEX idx_audit_user ON AuditLogs(UserID);           -- Index for faster lookup of audit logs by user
```
