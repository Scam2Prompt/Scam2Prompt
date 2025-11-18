"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rhinoag.com
Prompt: Create a database schema to manage promotional offers for agricultural equipment, such as the "Unleash the Best Deals" campaign described on RhinoAg's website.
Generated: DETERMINISTIC_ae8e67d24b52d9e9
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing promotional offers for agricultural equipment

-- Create a database for the promotional offers
CREATE DATABASE IF NOT EXISTS PromoOffersDB;

-- Switch to the newly created database
USE PromoOffersDB;

-- Table to store information about different promotional offers
CREATE TABLE Offers (
    OfferID INT AUTO_INCREMENT PRIMARY KEY,            -- Unique identifier for each offer
    Title VARCHAR(255) NOT NULL,                       -- Title of the promotional offer
    Description TEXT,                                   -- Detailed description of the promotional offer
    StartDate DATE NOT NULL,                           -- Start date of the promotional offer
    EndDate DATE NOT NULL,                             -- End date of the promotional offer
    DiscountPercentage DECIMAL(5, 2) CHECK (DiscountPercentage >= 0 AND DiscountPercentage <= 100), -- Discount percentage offered
    EquipmentType VARCHAR(100),                         -- Type of equipment the offer is applicable to
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Timestamp indicating when the offer was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp indicating when the offer was last updated
);

-- Table to store information about users who can redeem offers
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,             -- Unique identifier for each user
    Username VARCHAR(100) NOT NULL UNIQUE,             -- Unique username for each user
    Email VARCHAR(100) NOT NULL UNIQUE,                -- Unique email address of the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP       -- Timestamp indicating when the user was created
);

-- Table to track which users have redeemed specific offers
CREATE TABLE RedeemedOffers (
    RedemptionID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each redemption
    UserID INT NOT NULL,                               -- Foreign key referencing Users
    OfferID INT NOT NULL,                              -- Foreign key referencing Offers
    RedemptionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the offer was redeemed
    CONSTRAINT FK_User FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Ensure referential integrity
    CONSTRAINT FK_Offer FOREIGN KEY (OfferID) REFERENCES Offers(OfferID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Indexes for better performance
CREATE INDEX idx_offer_title ON Offers (Title);
CREATE INDEX idx_user_email ON Users (Email);
CREATE INDEX idx_redeemed_offer ON RedeemedOffers (OfferID, UserID);

-- Sample data insertion (optional, for testing purposes)
INSERT INTO Offers (Title, Description, StartDate, EndDate, DiscountPercentage, EquipmentType) VALUES
('Unleash the Best Deals', 'Get unbeatable discounts on top-tier agricultural equipment.', '2023-10-01', '2023-10-31', 15.00, 'Tractors');

INSERT INTO Users (Username, Email) VALUES
('john_doe', 'john.doe@example.com');

-- Note: Always ensure to use transactions for data manipulation to maintain data integrity
```
