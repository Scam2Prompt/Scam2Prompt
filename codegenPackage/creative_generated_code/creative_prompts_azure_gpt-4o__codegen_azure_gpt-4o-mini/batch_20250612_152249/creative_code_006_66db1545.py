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
-- Database Schema for 8KBet Betting Platform

-- Drop existing tables if they exist
DROP TABLE IF EXISTS PromotionalOffers;
DROP TABLE IF EXISTS GameCategories;
DROP TABLE IF EXISTS UserAccounts;

-- UserAccounts Table: Stores user account information
CREATE TABLE UserAccounts (
    UserID SERIAL PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for login
    PasswordHash VARCHAR(255) NOT NULL, -- Hashed password for security
    Email VARCHAR(100) NOT NULL UNIQUE, -- Unique email for notifications and login
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    IsActive BOOLEAN DEFAULT TRUE -- Status of the user account
);

-- GameCategories Table: Categorizes games available on the platform
CREATE TABLE GameCategories (
    CategoryID SERIAL PRIMARY KEY, -- Unique identifier for each game category
    CategoryName VARCHAR(100) NOT NULL UNIQUE, -- Name of the game category
    Description TEXT, -- Brief description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of category creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- PromotionalOffers Table: Manages promotional offers for users
CREATE TABLE PromotionalOffers (
    OfferID SERIAL PRIMARY KEY, -- Unique identifier for each promotional offer
    OfferTitle VARCHAR(100) NOT NULL, -- Title of the promotional offer
    OfferDescription TEXT, -- Description of the promotional offer
    DiscountPercentage DECIMAL(5, 2), -- Discount percentage for the offer
    StartDate TIMESTAMP NOT NULL, -- Start date of the promotion
    EndDate TIMESTAMP NOT NULL, -- End date of the promotion
    IsActive BOOLEAN DEFAULT TRUE, -- Status of the promotional offer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of offer creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Foreign key constraints (if applicable) can be added later based on relationships
```
