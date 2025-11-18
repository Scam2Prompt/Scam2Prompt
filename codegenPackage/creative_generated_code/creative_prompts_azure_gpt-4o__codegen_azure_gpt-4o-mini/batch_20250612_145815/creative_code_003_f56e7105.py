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
-- Database: SubscriptionManagement
-- A schema for managing user subscriptions, payment history, and referral tracking.

CREATE DATABASE SubscriptionManagement;
USE SubscriptionManagement;

-- Table: Users
-- Stores user information.
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    Username VARCHAR(50) NOT NULL UNIQUE,
    Email VARCHAR(100) NOT NULL UNIQUE,
    PasswordHash VARCHAR(255) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table: Subscriptions
-- Stores subscription plans available to users.
CREATE TABLE Subscriptions (
    SubscriptionID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    DurationMonths INT NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table: UserSubscriptions
-- Links users to their active subscriptions.
CREATE TABLE UserSubscriptions (
    UserSubscriptionID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT NOT NULL,
    SubscriptionID INT NOT NULL,
    StartDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    EndDate TIMESTAMP,
    AutoRenew BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE,
    FOREIGN KEY (SubscriptionID) REFERENCES Subscriptions(SubscriptionID) ON DELETE CASCADE
);

-- Table: Payments
-- Records payments made by users for their subscriptions.
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY,
    UserSubscriptionID INT NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PaymentMethod VARCHAR(50) NOT NULL,
    Status ENUM('Pending', 'Completed', 'Failed') DEFAULT 'Pending',
    FOREIGN KEY (UserSubscriptionID) REFERENCES UserSubscriptions(UserSubscriptionID) ON DELETE CASCADE
);

-- Table: Referrals
-- Tracks user referrals for subscription incentives.
CREATE TABLE Referrals (
    ReferralID INT AUTO_INCREMENT PRIMARY KEY,
    ReferrerUserID INT NOT NULL,
    RefereeEmail VARCHAR(100) NOT NULL,
    ReferralDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Status ENUM('Pending', 'Claimed', 'Expired') DEFAULT 'Pending',
    FOREIGN KEY (ReferrerUserID) REFERENCES Users(UserID) ON DELETE CASCADE
);

-- Indexes for performance improvements
CREATE INDEX idx_users_email ON Users (Email);
CREATE INDEX idx_subscriptions_name ON Subscriptions (Name);
CREATE INDEX idx_payments_status ON Payments (Status);
CREATE INDEX idx_referrals_status ON Referrals (Status);
```
