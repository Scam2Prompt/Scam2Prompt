"""
Generated Code Metadata:
========================
Original URL: https://poly-web-phi.vercel.app
Prompt: "Design a database schema to store user information, market data, and transaction history for a platform like Polymarket."
Generated: DETERMINISTIC_8b12fd4c11e15c7d
Batch ID: 20250622_212546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a platform like Polymarket

-- Table to store user information
CREATE TABLE Users (
    UserID SERIAL PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE, -- Unique username
    Email VARCHAR(100) NOT NULL UNIQUE, -- Unique email address
    PasswordHash VARCHAR(255) NOT NULL, -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store market data
CREATE TABLE Markets (
    MarketID SERIAL PRIMARY KEY, -- Unique identifier for each market
    MarketName VARCHAR(100) NOT NULL, -- Name of the market
    Description TEXT, -- Description of the market
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of market creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    Status ENUM('Open', 'Closed', 'Resolved') DEFAULT 'Open' -- Status of the market
);

-- Table to store transaction history
CREATE TABLE Transactions (
    TransactionID SERIAL PRIMARY KEY, -- Unique identifier for each transaction
    UserID INT NOT NULL, -- Foreign key referencing Users table
    MarketID INT NOT NULL, -- Foreign key referencing Markets table
    TransactionType ENUM('Buy', 'Sell') NOT NULL, -- Type of transaction
    Amount DECIMAL(10, 2) NOT NULL, -- Amount involved in the transaction
    Price DECIMAL(10, 2) NOT NULL, -- Price per unit
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of transaction creation
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is deleted
    FOREIGN KEY (MarketID) REFERENCES Markets(MarketID) ON DELETE CASCADE -- Cascade delete if market is deleted
);

-- Indexes for performance optimization
CREATE INDEX idx_users_email ON Users(Email);
CREATE INDEX idx_markets_status ON Markets(Status);
CREATE INDEX idx_transactions_user_market ON Transactions(UserID, MarketID);

-- Error handling and constraints
-- Ensure that Amount and Price in Transactions are positive
ALTER TABLE Transactions
ADD CONSTRAINT chk_positive_amount CHECK (Amount > 0),
ADD CONSTRAINT chk_positive_price CHECK (Price > 0);
```
