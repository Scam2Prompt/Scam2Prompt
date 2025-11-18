"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1inch.danngol.com
Prompt: Suggest a database schema for a platform like "단골가게" that supports local business listings, user accounts, prepayment transactions, and discount tracking.
Generated: DETERMINISTIC_7a9cc07f9c229673
Batch ID: 20250612_150848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for a platform like "단골가게"
-- This database will support local business listings, user accounts, prepayment transactions, and discount tracking.

-- Table: Users
-- Stores information about the users (both businesses and customers)
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,        -- Username for login
    Email VARCHAR(100) NOT NULL UNIQUE,          -- Email address
    PasswordHash VARCHAR(255) NOT NULL,          -- Hashed password for secure storage
    FullName VARCHAR(100),                       -- Full name of the user
    PhoneNumber VARCHAR(15),                     -- Contact phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp indicating when the user was created
);

-- Table: Businesses
-- Stores information about local businesses
CREATE TABLE Businesses (
    BusinessID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each business
    OwnerID INT NOT NULL,                        -- Foreign key referencing Users table
    Name VARCHAR(100) NOT NULL,                  -- Name of the business
    Description TEXT,                            -- Description of the business
    Address VARCHAR(255) NOT NULL,               -- Address of the business
    PhoneNumber VARCHAR(15),                     -- Contact phone number of the business
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- When the business was added
    FOREIGN KEY (OwnerID) REFERENCES Users(UserID) ON DELETE CASCADE -- Ensure businesses are deleted if the owner is deleted
);

-- Table: Discounts
-- Stores discount offers provided by businesses
CREATE TABLE Discounts (
    DiscountID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each discount
    BusinessID INT NOT NULL,                     -- Foreign key referencing Businesses table
    Title VARCHAR(100) NOT NULL,                 -- Title or name of the discount
    Description TEXT,                            -- Detailed description of the discount
    DiscountPercentage DECIMAL(5, 2) NOT NULL,   -- Percentage discount (e.g., 10%)
    StartDate DATE NOT NULL,                     -- Start date of the discount
    EndDate DATE NOT NULL,                       -- End date of the discount
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- When the discount was added
    FOREIGN KEY (BusinessID) REFERENCES Businesses(BusinessID) ON DELETE CASCADE -- Ensure discounts are deleted if the business is deleted
);

-- Table: PrepaymentTransactions
-- Tracks prepayment transactions between users and businesses
CREATE TABLE PrepaymentTransactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    UserID INT NOT NULL,                          -- Foreign key referencing Users table
    BusinessID INT NOT NULL,                      -- Foreign key referencing Businesses table
    Amount DECIMAL(10, 2) NOT NULL,               -- Amount pre-paid by the user
    PaidAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- When the payment was made
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Ensure user's transactions are deleted if the user is deleted
    FOREIGN KEY (BusinessID) REFERENCES Businesses(BusinessID) ON DELETE CASCADE -- Ensure business's transactions are deleted if the business is deleted
);

-- Indexes for optimized queries
CREATE INDEX idx_users_username ON Users (Username);           -- Index for fast username lookups
CREATE INDEX idx_businesses_name ON Businesses (Name);         -- Index for fast business name lookups
CREATE INDEX idx_discounts_dates ON Discounts (StartDate, EndDate); -- Index for filtering discounts by date range
CREATE INDEX idx_transactions_user_business ON PrepaymentTransactions (UserID, BusinessID); -- Index for fast transaction lookups
```
