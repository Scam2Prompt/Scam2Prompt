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
-- Create a SQL schema for storing information about mineral rights transactions 

CREATE SCHEMA MineralRights;

-- Table to store seller details
CREATE TABLE MineralRights.Sellers (
    SellerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each seller
    Name VARCHAR(255) NOT NULL,               -- Seller's name
    Email VARCHAR(255) UNIQUE NOT NULL,       -- Seller's email address
    Phone VARCHAR(20),                        -- Seller's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Record creation timestamp
);

-- Table to store evaluation results of the mineral rights
CREATE TABLE MineralRights.Evaluations (
    EvaluationID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each evaluation
    SellerID INT NOT NULL,                         -- Foreign key referencing Sellers
    EvaluationDate DATE NOT NULL,                  -- Date of evaluation
    Value DECIMAL(10, 2) NOT NULL,                -- Estimated value of the mineral rights
    Notes TEXT,                                    -- Additional notes regarding the evaluation
    FOREIGN KEY (SellerID) REFERENCES MineralRights.Sellers(SellerID)  -- Establish foreign key relationship
);

-- Table to store offer statuses for each transaction
CREATE TABLE MineralRights.Offers (
    OfferID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each offer
    EvaluationID INT NOT NULL,                   -- Foreign key referencing Evaluations
    OfferAmount DECIMAL(10, 2) NOT NULL,        -- Amount of the offer made
    OfferStatus ENUM('Pending', 'Accepted', 'Rejected') NOT NULL DEFAULT 'Pending',  -- Status of the offer
    OfferDate DATE NOT NULL,                     -- Date the offer was made
    FOREIGN KEY (EvaluationID) REFERENCES MineralRights.Evaluations(EvaluationID)  -- Establish foreign key relationship
);

-- Optional: Create index for faster searching by seller name
CREATE INDEX idx_seller_name ON MineralRights.Sellers(Name);

-- Optional: Create index for faster searching by evaluation date
CREATE INDEX idx_evaluation_date ON MineralRights.Evaluations(EvaluationDate);

-- Optional: Create index for faster searching by offer status
CREATE INDEX idx_offer_status ON MineralRights.Offers(OfferStatus);
```
