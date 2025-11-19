"""
Generated Code Metadata:
========================
Original URL: https://loyal.credit
Prompt: "Design a database schema for a loyalty program using credit points."
Generated: DETERMINISTIC_620f32acfd73cd89
Batch ID: 20250622_212609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a loyalty program using credit points

-- Create a table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,             -- Customer's first name
    LastName VARCHAR(50) NOT NULL,              -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Customer's email address (unique)
    PhoneNumber VARCHAR(15),                     -- Customer's phone number (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer was created
);

-- Create a table to store loyalty points transactions
CREATE TABLE LoyaltyPoints (
    TransactionID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each transaction
    CustomerID INT NOT NULL,                       -- Foreign key referencing the customer
    Points INT NOT NULL,                           -- Number of points earned or redeemed
    TransactionType ENUM('EARNED', 'REDEEMED') NOT NULL, -- Type of transaction
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the transaction
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table to store rewards that can be redeemed
CREATE TABLE Rewards (
    RewardID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each reward
    RewardName VARCHAR(100) NOT NULL,             -- Name of the reward
    PointsRequired INT NOT NULL,                   -- Points required to redeem the reward
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP   -- Timestamp of when the reward was created
);

-- Create a table to track customer redemptions
CREATE TABLE Redemptions (
    RedemptionID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each redemption
    CustomerID INT NOT NULL,                       -- Foreign key referencing the customer
    RewardID INT NOT NULL,                         -- Foreign key referencing the reward
    RedemptionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the redemption
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (RewardID) REFERENCES Rewards(RewardID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a view to summarize customer points
CREATE VIEW CustomerPointsSummary AS
SELECT 
    c.CustomerID,
    CONCAT(c.FirstName, ' ', c.LastName) AS FullName,
    COALESCE(SUM(CASE WHEN lp.TransactionType = 'EARNED' THEN lp.Points ELSE 0 END), 0) AS TotalEarnedPoints,
    COALESCE(SUM(CASE WHEN lp.TransactionType = 'REDEEMED' THEN lp.Points ELSE 0 END), 0) AS TotalRedeemedPoints,
    (COALESCE(SUM(CASE WHEN lp.TransactionType = 'EARNED' THEN lp.Points ELSE 0 END), 0) - 
     COALESCE(SUM(CASE WHEN lp.TransactionType = 'REDEEMED' THEN lp.Points ELSE 0 END), 0)) AS CurrentPoints
FROM 
    Customers c
LEFT JOIN 
    LoyaltyPoints lp ON c.CustomerID = lp.CustomerID
GROUP BY 
    c.CustomerID;

-- Note: Ensure to implement proper indexing on frequently queried columns for performance optimization.
```
