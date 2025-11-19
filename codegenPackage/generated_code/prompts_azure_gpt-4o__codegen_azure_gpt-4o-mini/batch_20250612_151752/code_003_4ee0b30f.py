"""
Generated Code Metadata:
========================
Original URL: https://kraken-energy.com
Prompt: Create a SQL database schema to store information about mineral rights transactions in Oklahoma, including fields for seller details, evaluation results, and offer status, based on Kraken Energy's workflow.
Generated: DETERMINISTIC_4ee0b30fd15a3e00
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for storing mineral rights transactions
CREATE DATABASE MineralRightsTransactions;

-- Use the newly created database
USE MineralRightsTransactions;

-- Table to store seller details
CREATE TABLE Sellers (
    SellerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each seller
    Name VARCHAR(255) NOT NULL,              -- Seller's name
    ContactInfo VARCHAR(255),                 -- Seller's contact information
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store evaluation results
CREATE TABLE Evaluations (
    EvaluationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each evaluation
    SellerID INT NOT NULL,                       -- Foreign key referencing Sellers
    EvaluationDate DATE NOT NULL,                -- Date of the evaluation
    Value DECIMAL(15, 2) NOT NULL,              -- Evaluated value of the mineral rights
    Comments TEXT,                               -- Additional comments about the evaluation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (SellerID) REFERENCES Sellers(SellerID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store offer status
CREATE TABLE Offers (
    OfferID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each offer
    SellerID INT NOT NULL,                        -- Foreign key referencing Sellers
    OfferDate DATE NOT NULL,                      -- Date the offer was made
    OfferAmount DECIMAL(15, 2) NOT NULL,        -- Amount of the offer
    Status ENUM('Pending', 'Accepted', 'Rejected') NOT NULL, -- Status of the offer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (SellerID) REFERENCES Sellers(SellerID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_seller_name ON Sellers(Name);
CREATE INDEX idx_evaluation_date ON Evaluations(EvaluationDate);
CREATE INDEX idx_offer_date ON Offers(OfferDate);
```
