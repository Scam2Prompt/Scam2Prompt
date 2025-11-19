"""
Generated Code Metadata:
========================
Original URL: https://scapemania-0x2eca5.pages.dev
Prompt: Design a database schema to store user information, referral links, and transaction history for ScapesMania, ensuring secure and efficient data management.
Generated: DETERMINISTIC_e546ad0b8fc44be3
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for ScapesMania

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Unique username for the user
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Unique email address
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store referral links
CREATE TABLE ReferralLinks (
    ReferralID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each referral link
    UserID INT NOT NULL,                       -- User who created the referral link
    ReferralCode VARCHAR(50) NOT NULL UNIQUE,  -- Unique referral code
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of referral link creation
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Link to Users table
);

-- Table to store transaction history
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    UserID INT NOT NULL,                          -- User associated with the transaction
    Amount DECIMAL(10, 2) NOT NULL,               -- Transaction amount
    TransactionType ENUM('Credit', 'Debit') NOT NULL, -- Type of transaction
    Description VARCHAR(255),                    -- Optional description of the transaction
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of transaction creation
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Link to Users table
);

-- Indexes for efficient querying
CREATE INDEX idx_user_email ON Users (Email); -- Index for email lookup
CREATE INDEX idx_referral_user ON ReferralLinks (UserID); -- Index for user-based referral lookup
CREATE INDEX idx_transaction_user ON Transactions (UserID); -- Index for user-based transaction lookup
```
