"""
Generated Code Metadata:
========================
Original URL: https://vinescoin.com
Prompt: Design a database schema to store information about small-batch producers, cooking oils, and their regions, inspired by Authentic Oil's curated selection and regional diversity.
Generated: DETERMINISTIC_90b8d3a39bd56cb6
Batch ID: 20250622_211427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about small-batch producers, cooking oils, and their regions

-- Table to store information about regions
CREATE TABLE Regions (
    RegionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each region
    RegionName VARCHAR(100) NOT NULL,        -- Name of the region
    Country VARCHAR(100) NOT NULL,           -- Country where the region is located
    Description TEXT                         -- Optional description of the region
);

-- Table to store information about producers
CREATE TABLE Producers (
    ProducerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each producer
    ProducerName VARCHAR(100) NOT NULL,        -- Name of the producer
    RegionID INT NOT NULL,                     -- Foreign key linking to the Regions table
    ContactEmail VARCHAR(100),                 -- Contact email for the producer
    WebsiteURL VARCHAR(255),                   -- Website URL for the producer
    Description TEXT,                          -- Optional description of the producer
    FOREIGN KEY (RegionID) REFERENCES Regions(RegionID) ON DELETE CASCADE
);

-- Table to store information about cooking oils
CREATE TABLE CookingOils (
    OilID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each cooking oil
    OilName VARCHAR(100) NOT NULL,             -- Name of the cooking oil
    ProducerID INT NOT NULL,                   -- Foreign key linking to the Producers table
    OilType VARCHAR(100) NOT NULL,             -- Type of oil (e.g., olive oil, avocado oil)
    FlavorProfile VARCHAR(255),                -- Description of the flavor profile
    Ingredients TEXT,                          -- Ingredients used in the oil
    ProductionDate DATE,                       -- Date the oil was produced
    ExpirationDate DATE,                       -- Expiration date of the oil
    FOREIGN KEY (ProducerID) REFERENCES Producers(ProducerID) ON DELETE CASCADE
);

-- Table to store reviews for cooking oils
CREATE TABLE OilReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each review
    OilID INT NOT NULL,                        -- Foreign key linking to the CookingOils table
    ReviewerName VARCHAR(100),                 -- Name of the reviewer
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating given by the reviewer (1 to 5)
    ReviewText TEXT,                           -- Optional text review
    ReviewDate DATE NOT NULL,                  -- Date the review was submitted
    FOREIGN KEY (OilID) REFERENCES CookingOils(OilID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_region_name ON Regions(RegionName);
CREATE INDEX idx_producer_name ON Producers(ProducerName);
CREATE INDEX idx_oil_name ON CookingOils(OilName);
CREATE INDEX idx_review_date ON OilReviews(ReviewDate);
```
