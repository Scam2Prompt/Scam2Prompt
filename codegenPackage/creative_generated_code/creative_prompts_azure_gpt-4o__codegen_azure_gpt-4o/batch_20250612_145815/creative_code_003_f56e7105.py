"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rentsy.pro
Prompt: Create a database schema for managing user subscriptions, payment history, and referral tracking, similar to the features described on Rentsy.
Generated: DETERMINISTIC_f56e71053442b412
Batch ID: 20250612_145815
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing user subscriptions, payment history, and referral tracking

-- Users table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,           -- Unique identifier for each user
    FullName VARCHAR(100) NOT NULL,                  -- Full name of the user
    Email VARCHAR(255) NOT NULL UNIQUE,              -- Unique email for the user
    PasswordHash VARCHAR(255) NOT NULL,              -- Hashed password
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last updated timestamp
);

-- Subscriptions table to store user subscriptions
CREATE TABLE Subscriptions (
    SubscriptionID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each subscription
    UserID INT NOT NULL,                             -- Foreign key to Users table
    PlanName VARCHAR(100) NOT NULL,                  -- Name of the subscription plan
    StartDate DATE NOT NULL,                         -- Start date of the subscription
    EndDate DATE,                                    -- End date of the subscription (nullable for ongoing)
    IsActive BOOLEAN DEFAULT TRUE,                   -- Whether the subscription is active
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp when the subscription was created
    FOREIGN KEY (UserID) REFERENCES Users(UserID)    -- Foreign key constraint
);

-- Payments table to store payment history
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each payment
    UserID INT NOT NULL,                             -- Foreign key to Users table
    SubscriptionID INT,                              -- Optional foreign key to Subscriptions table
    Amount DECIMAL(10, 2) NOT NULL,                  -- Amount paid
    PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the payment
    PaymentMethod VARCHAR(50) NOT NULL,              -- Method of payment (e.g., credit card, PayPal, etc.)
    PaymentStatus VARCHAR(20) NOT NULL,              -- Status of payment (e.g., completed, pending, failed)
    FOREIGN KEY (UserID) REFERENCES Users(UserID),   -- Foreign key constraint
    FOREIGN KEY (SubscriptionID) REFERENCES Subscriptions(SubscriptionID) -- Optional foreign key constraint
);

-- Referrals table to track referral relationships
CREATE TABLE Referrals (
    ReferralID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each referral
    ReferrerID INT NOT NULL,                         -- UserID of the referrer
    ReferredID INT NOT NULL,                         -- UserID of the referred user
    ReferralDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,-- Date when the referral was made
    BonusAmount DECIMAL(10, 2),                      -- Bonus amount granted for the referral
    FOREIGN KEY (ReferrerID) REFERENCES Users(UserID), -- Foreign key constraint for referrer
    FOREIGN KEY (ReferredID) REFERENCES Users(UserID), -- Foreign key constraint for referred user
    CONSTRAINT UC_Referral UNIQUE (ReferrerID, ReferredID) -- Prevent duplicate referrals
);

-- Indexing for better query performance
CREATE INDEX idx_user_email ON Users (Email);
CREATE INDEX idx_subscription_user ON Subscriptions (UserID);
CREATE INDEX idx_payment_user ON Payments (UserID);
CREATE INDEX idx_referrals_referrer ON Referrals (ReferrerID);
CREATE INDEX idx_referrals_referred ON Referrals (ReferredID);

-- Error handling and data consistency are managed by the constraints (e.g., NOT NULL, UNIQUE, FOREIGN KEY)
```
