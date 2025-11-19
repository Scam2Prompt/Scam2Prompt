"""
Generated Code Metadata:
========================
Original URL: https://sovads.ru
Prompt: Design a database schema to store and manage usernames for sale, including information like username value, platform, and seller details, based on SovaDS's model.
Generated: DETERMINISTIC_28091baf9d5fee80
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema to store and manage usernames for sale
-- This schema is designed to be clean, efficient, and production-ready.

-- Table to store platform information
CREATE TABLE Platforms (
    PlatformID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the platform
    PlatformName VARCHAR(255) NOT NULL,        -- Name of the platform (e.g., Twitter, Instagram)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store seller information
CREATE TABLE Sellers (
    SellerID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for the seller
    SellerName VARCHAR(255) NOT NULL,         -- Name of the seller
    ContactInfo VARCHAR(255),                 -- Contact information (e.g., email, phone)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store usernames for sale
CREATE TABLE UsernamesForSale (
    UsernameID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the username
    UsernameValue VARCHAR(255) NOT NULL,       -- The username being sold
    PlatformID INT NOT NULL,                   -- Foreign key referencing Platforms table
    SellerID INT NOT NULL,                     -- Foreign key referencing Sellers table
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the username
    IsAvailable BOOLEAN DEFAULT TRUE,          -- Availability status of the username
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (PlatformID) REFERENCES Platforms(PlatformID) ON DELETE CASCADE, -- Cascade delete for platform
    FOREIGN KEY (SellerID) REFERENCES Sellers(SellerID) ON DELETE CASCADE -- Cascade delete for seller
);

-- Indexes for faster lookups
CREATE INDEX idx_platform_name ON Platforms (PlatformName);
CREATE INDEX idx_seller_name ON Sellers (SellerName);
CREATE INDEX idx_username_value ON UsernamesForSale (UsernameValue);

-- Error handling and constraints
-- Ensure username values are unique within the same platform
ALTER TABLE UsernamesForSale ADD CONSTRAINT unique_username_per_platform UNIQUE (UsernameValue, PlatformID);

-- Ensure price is non-negative
ALTER TABLE UsernamesForSale ADD CONSTRAINT check_price_non_negative CHECK (Price >= 0);
```
