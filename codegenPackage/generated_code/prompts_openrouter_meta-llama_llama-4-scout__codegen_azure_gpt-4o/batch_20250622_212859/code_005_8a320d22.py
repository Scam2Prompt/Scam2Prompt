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
-- SQL Schema for storing information about championship belts and customer reviews

-- Create a database named 'ChampionshipBeltsDB'
CREATE DATABASE ChampionshipBeltsDB;

-- Use the newly created database
USE ChampionshipBeltsDB;

-- Table to store information about championship belts
CREATE TABLE Belts (
    BeltID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each belt
    ProductName VARCHAR(255) NOT NULL,     -- Name of the championship belt
    Price DECIMAL(10, 2) NOT NULL,         -- Price of the belt
    Material VARCHAR(255) NOT NULL,        -- Material used for the belt
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Table to store customer reviews for championship belts
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each review
    BeltID INT NOT NULL,                     -- Foreign key referencing the Belts table
    CustomerName VARCHAR(255) NOT NULL,      -- Name of the customer
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating given by the customer (1 to 5)
    ReviewText TEXT,                         -- Text of the customer's review
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the review was last updated
    FOREIGN KEY (BeltID) REFERENCES Belts(BeltID) ON DELETE CASCADE -- Ensure reviews are deleted if the associated belt is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_belt_price ON Belts(Price); -- Index on Price for faster range queries
CREATE INDEX idx_review_rating ON Reviews(Rating); -- Index on Rating for faster filtering

-- Example error handling: Ensure the database is created successfully
-- (This is typically handled by the application interacting with the database)
```
