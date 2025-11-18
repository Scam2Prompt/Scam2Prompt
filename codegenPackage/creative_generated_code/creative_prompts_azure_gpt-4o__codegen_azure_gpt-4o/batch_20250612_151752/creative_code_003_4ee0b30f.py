"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kraken-energy.com
Prompt: Create a SQL database schema to store information about mineral rights transactions in Oklahoma, including fields for seller details, evaluation results, and offer status, based on Kraken Energy's workflow.
Generated: DETERMINISTIC_4ee0b30fd15a3e00
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Database Schema for Mineral Rights Transactions in Oklahoma

-- Create database
CREATE DATABASE MineralRightsTransactions;
USE MineralRightsTransactions;

-- Create table for seller details
CREATE TABLE Sellers (
    SellerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each seller
    FirstName VARCHAR(100) NOT NULL,         -- Seller's first name
    LastName VARCHAR(100) NOT NULL,          -- Seller's last name
    PhoneNumber VARCHAR(15),                 -- Seller's contact number
    Email VARCHAR(100),                      -- Seller's email address
    Address VARCHAR(255) NOT NULL,           -- Property address
    City VARCHAR(100) NOT NULL,              -- City of the property
    State VARCHAR(50) DEFAULT 'Oklahoma',    -- State of the property (default: Oklahoma)
    ZipCode VARCHAR(10) NOT NULL,            -- ZIP code
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Create table for property evaluation results
CREATE TABLE Evaluations (
    EvaluationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each evaluation
    SellerID INT NOT NULL,                       -- Foreign key referencing Sellers table
    MineralType VARCHAR(100) NOT NULL,           -- Type of mineral (e.g., oil, gas, etc.)
    EstimatedValue DECIMAL(15, 2),               -- Estimated value of the property
    EvaluationDate DATE NOT NULL,                -- Date of the evaluation
    Notes TEXT,                                  -- Additional evaluation notes
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (SellerID) REFERENCES Sellers(SellerID) ON DELETE CASCADE -- Cascade delete if seller is removed
);

-- Create table for offer status
CREATE TABLE Offers (
    OfferID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each offer
    SellerID INT NOT NULL,                       -- Foreign key referencing Sellers table
    EvaluationID INT,                            -- Foreign key referencing Evaluations table
    OfferAmount DECIMAL(15, 2) NOT NULL,         -- Amount offered to the seller
    OfferStatus ENUM('Pending', 'Accepted', 'Rejected', 'Expired') DEFAULT 'Pending', -- Status of the offer
    OfferDate DATE NOT NULL,                     -- Date the offer was made
    ExpiryDate DATE,                             -- Expiration date of the offer
    Notes TEXT,                                  -- Additional offer notes
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (SellerID) REFERENCES Sellers(SellerID) ON DELETE CASCADE, -- Cascade delete if seller is removed
    FOREIGN KEY (EvaluationID) REFERENCES Evaluations(EvaluationID) ON DELETE SET NULL -- Set to NULL if evaluation is removed
);

-- Indexes to optimize queries
CREATE INDEX IDX_SellerPhone ON Sellers(PhoneNumber); -- Index for faster search by phone number
CREATE INDEX IDX_EvaluationDate ON Evaluations(EvaluationDate); -- Index for evaluation date
CREATE INDEX IDX_OfferStatus ON Offers(OfferStatus); -- Index for offer status

-- End of schema
```
