"""
Generated Code Metadata:
========================
Original URL: https://joinnow.info
Prompt: "Design a basic database schema to store information about Money Order Freedom subscribers, referrals, and sales, including fields for tracking income and subscription levels."
Generated: DETERMINISTIC_789f6d8a384b1e79
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Money Order Freedom subscribers, referrals, and sales

-- Table to store subscriber information
CREATE TABLE Subscribers (
    SubscriberID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each subscriber
    FirstName VARCHAR(50) NOT NULL,             -- Subscriber's first name
    LastName VARCHAR(50) NOT NULL,              -- Subscriber's last name
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Subscriber's email address (must be unique)
    PhoneNumber VARCHAR(15),                    -- Subscriber's phone number
    SubscriptionLevel ENUM('Basic', 'Premium', 'VIP') NOT NULL, -- Subscription level
    JoinDate DATE NOT NULL DEFAULT CURRENT_DATE, -- Date the subscriber joined
    Income DECIMAL(10, 2) DEFAULT 0.00,         -- Income earned by the subscriber
    LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table to store referral information
CREATE TABLE Referrals (
    ReferralID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each referral
    ReferrerID INT NOT NULL,                    -- Subscriber ID of the referrer
    ReferredID INT NOT NULL,                    -- Subscriber ID of the referred person
    ReferralDate DATE NOT NULL DEFAULT CURRENT_DATE, -- Date the referral was made
    FOREIGN KEY (ReferrerID) REFERENCES Subscribers(SubscriberID) ON DELETE CASCADE, -- Foreign key to Subscribers table
    FOREIGN KEY (ReferredID) REFERENCES Subscribers(SubscriberID) ON DELETE CASCADE  -- Foreign key to Subscribers table
);

-- Table to store sales information
CREATE TABLE Sales (
    SaleID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each sale
    SubscriberID INT NOT NULL,                  -- Subscriber ID associated with the sale
    SaleAmount DECIMAL(10, 2) NOT NULL,         -- Amount of the sale
    SaleDate DATE NOT NULL DEFAULT CURRENT_DATE, -- Date the sale occurred
    FOREIGN KEY (SubscriberID) REFERENCES Subscribers(SubscriberID) ON DELETE CASCADE -- Foreign key to Subscribers table
);

-- Indexes for optimizing queries
CREATE INDEX idx_subscriber_email ON Subscribers(Email); -- Index for quick lookup by email
CREATE INDEX idx_referrer_id ON Referrals(ReferrerID);   -- Index for quick lookup by referrer ID
CREATE INDEX idx_sale_date ON Sales(SaleDate);           -- Index for quick lookup by sale date
```
