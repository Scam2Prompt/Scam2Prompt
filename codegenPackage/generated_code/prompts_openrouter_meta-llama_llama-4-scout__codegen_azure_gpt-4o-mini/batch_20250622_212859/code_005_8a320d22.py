"""
Generated Code Metadata:
========================
Original URL: https://titlebelts.au
Prompt: Create a SQL database schema to store information about championship belts, including product names, prices, materials, and customer reviews, based on the content of Title Belts AU.
Generated: DETERMINISTIC_8a320d2283382a5d
Batch ID: 20250622_212859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Championship Belts

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS CustomerReviews;
DROP TABLE IF EXISTS ChampionshipBelts;

-- Table to store information about championship belts
CREATE TABLE ChampionshipBelts (
    BeltID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each belt
    ProductName VARCHAR(255) NOT NULL,     -- Name of the championship belt
    Price DECIMAL(10, 2) NOT NULL,          -- Price of the championship belt
    Material VARCHAR(100) NOT NULL,         -- Material used for the belt
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the belt was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store customer reviews for championship belts
CREATE TABLE CustomerReviews (
    ReviewID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each review
    BeltID INT NOT NULL,                      -- Foreign key referencing the ChampionshipBelts table
    CustomerName VARCHAR(100) NOT NULL,      -- Name of the customer leaving the review
    ReviewText TEXT NOT NULL,                 -- Text of the customer review
    Rating INT CHECK (Rating BETWEEN 1 AND 5),  -- Rating given by the customer (1 to 5)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the review was added
    FOREIGN KEY (BeltID) REFERENCES ChampionshipBelts(BeltID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Sample data insertion (optional)
INSERT INTO ChampionshipBelts (ProductName, Price, Material) VALUES
('Gold Championship Belt', 299.99, 'Gold Plated'),
('Silver Championship Belt', 199.99, 'Silver Plated'),
('Leather Championship Belt', 149.99, 'Genuine Leather');

INSERT INTO CustomerReviews (BeltID, CustomerName, ReviewText, Rating) VALUES
(1, 'John Doe', 'Amazing quality and design!', 5),
(1, 'Jane Smith', 'A bit pricey but worth it.', 4),
(2, 'Alice Johnson', 'Looks great, but the material could be better.', 3);
```
