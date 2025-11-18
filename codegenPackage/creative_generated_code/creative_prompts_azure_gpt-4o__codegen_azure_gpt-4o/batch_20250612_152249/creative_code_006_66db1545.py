"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sandbox.co.com
Prompt: Create a database schema for managing user accounts, game categories, and promotional offers for a betting platform like 8KBet.
Generated: DETERMINISTIC_66db154595314e58
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for a Betting Platform

-- Table to store user account information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,           -- Unique username for login
    Email VARCHAR(100) NOT NULL UNIQUE,             -- Unique email address
    PasswordHash VARCHAR(255) NOT NULL,             -- Hashed password for security
    FullName VARCHAR(100),                          -- Full name of the user
    DateOfBirth DATE,                               -- Date of birth of the user
    AccountBalance DECIMAL(10, 2) DEFAULT 0.00,     -- User's account balance
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Account creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table to store game categories
CREATE TABLE GameCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL UNIQUE,        -- Name of the game category
    Description TEXT,                                 -- Description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table to store promotional offers
CREATE TABLE PromotionalOffers (
    OfferID INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each offer
    OfferTitle VARCHAR(100) NOT NULL,                -- Title of the promotional offer
    OfferDescription TEXT,                           -- Detailed description of the offer
    StartDate DATE NOT NULL,                         -- Start date of the promotional offer
    EndDate DATE NOT NULL,                           -- End date of the promotional offer
    DiscountPercentage DECIMAL(5, 2),                -- Discount percentage for the offer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp when the offer was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Relationship table to associate users with promotional offers they have redeemed
CREATE TABLE UserOffers (
    UserOfferID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each user-offer relationship
    UserID INT NOT NULL,                             -- Foreign key referencing Users table
    OfferID INT NOT NULL,                            -- Foreign key referencing PromotionalOffers table
    RedeemedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the offer was redeemed
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE,  -- Cascade delete on user removal
    FOREIGN KEY (OfferID) REFERENCES PromotionalOffers(OfferID) ON DELETE CASCADE -- Cascade delete on offer removal
);

-- Relationship table to associate game categories with users (e.g., favorite categories)
CREATE TABLE UserGameCategories (
    UserGameCategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user-category relationship
    UserID INT NOT NULL,                               -- Foreign key referencing Users table
    CategoryID INT NOT NULL,                           -- Foreign key referencing GameCategories table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Timestamp when the relationship was created
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete on user removal
    FOREIGN KEY (CategoryID) REFERENCES GameCategories(CategoryID) ON DELETE CASCADE -- Cascade delete on category removal
);

-- Indexes for better performance
CREATE INDEX idx_users_username ON Users (Username);
CREATE INDEX idx_users_email ON Users (Email);
CREATE INDEX idx_promotionaloffers_dates ON PromotionalOffers (StartDate, EndDate);
CREATE INDEX idx_usergamecategories_user_category ON UserGameCategories (UserID, CategoryID);
CREATE INDEX idx_useroffers_user_offer ON UserOffers (UserID, OfferID);
```
