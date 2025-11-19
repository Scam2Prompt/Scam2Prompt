"""
Generated Code Metadata:
========================
Original URL: https://uniswop.shop
Prompt: Design a database schema for a peer-to-peer marketplace platform, such as UniSwop, that stores user information, listings, transactions, and charitable donation records.
Generated: DETERMINISTIC_546221c4c9c937c7
Batch ID: 20250622_212335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a peer-to-peer marketplace platform

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Unique username for the user
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Unique email address
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store marketplace listings
CREATE TABLE Listings (
    ListingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each listing
    UserID INT NOT NULL,                      -- Foreign key referencing Users table
    Title VARCHAR(100) NOT NULL,              -- Title of the listing
    Description TEXT NOT NULL,                -- Detailed description of the listing
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the item/service
    IsActive BOOLEAN DEFAULT TRUE,            -- Indicates if the listing is active
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of listing creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Table to store transactions between users
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    BuyerID INT NOT NULL,                         -- Foreign key referencing Users table (buyer)
    SellerID INT NOT NULL,                        -- Foreign key referencing Users table (seller)
    ListingID INT NOT NULL,                       -- Foreign key referencing Listings table
    Amount DECIMAL(10, 2) NOT NULL,               -- Transaction amount
    Status ENUM('Pending', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of the transaction
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of transaction creation
    FOREIGN KEY (BuyerID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if buyer is deleted
    FOREIGN KEY (SellerID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if seller is deleted
    FOREIGN KEY (ListingID) REFERENCES Listings(ListingID) ON DELETE CASCADE -- Cascade delete if listing is deleted
);

-- Table to store charitable donation records
CREATE TABLE Donations (
    DonationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each donation
    UserID INT NOT NULL,                       -- Foreign key referencing Users table
    Amount DECIMAL(10, 2) NOT NULL,            -- Donation amount
    CharityName VARCHAR(100) NOT NULL,         -- Name of the charity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of donation creation
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_user_email ON Users (Email); -- Index for quick lookup by email
CREATE INDEX idx_listing_user ON Listings (UserID); -- Index for quick lookup of listings by user
CREATE INDEX idx_transaction_status ON Transactions (Status); -- Index for quick lookup by transaction status
CREATE INDEX idx_donation_user ON Donations (UserID); -- Index for quick lookup of donations by user
```
