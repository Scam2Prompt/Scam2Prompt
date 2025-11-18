"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wizfairllc.com
Prompt: Create a SQL database schema to store Wizfair LLC's travel package information, including destinations, prices, discounts, and customer reviews.
Generated: DETERMINISTIC_9ae71bc584f5bdfc
Batch ID: 20250612_151247
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create the database schema for Wizfair LLC's travel package information

-- Drop the database if it exists (for development purposes)
DROP DATABASE IF EXISTS WizfairDB;

-- Create a new database for Wizfair LLC
CREATE DATABASE WizfairDB;

-- Use the newly created database
USE WizfairDB;

-- Create a table to store destinations
CREATE TABLE Destinations (
    DestinationID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each destination
    Name VARCHAR(100) NOT NULL,                     -- Name of the destination
    Description TEXT,                                -- Description of the destination
    Country VARCHAR(100) NOT NULL                    -- Country where the destination is located
);

-- Create a table to store travel packages
CREATE TABLE TravelPackages (
    PackageID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each travel package
    DestinationID INT NOT NULL,                      -- Foreign key to link to Destinations table
    Price DECIMAL(10, 2) NOT NULL,                  -- Price of the travel package
    Discount DECIMAL(5, 2) DEFAULT 0.00,            -- Discount on the travel package (if any)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of package creation
    FOREIGN KEY (DestinationID) REFERENCES Destinations(DestinationID) 
        ON DELETE CASCADE                              -- Ensure referential integrity
);

-- Create a table to store customer reviews
CREATE TABLE CustomerReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each review
    PackageID INT NOT NULL,                          -- Foreign key to link to TravelPackages table
    CustomerName VARCHAR(100) NOT NULL,             -- Name of the customer
    Rating INT CHECK (Rating BETWEEN 1 AND 5),      -- Rating given by the customer (1 to 5)
    ReviewText TEXT,                                 -- Review text provided by the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of review creation
    FOREIGN KEY (PackageID) REFERENCES TravelPackages(PackageID) 
        ON DELETE CASCADE                              -- Ensure referential integrity
);

-- Optional: Create a view to get travel packages with destination names
CREATE VIEW PackageDetails AS
SELECT 
    TP.PackageID,
    D.Name AS DestinationName,
    TP.Price,
    TP.Discount,
    TP.CreatedAt
FROM 
    TravelPackages TP
JOIN 
    Destinations D ON TP.DestinationID = D.DestinationID;

-- Optional: Create an index on the PackageID in CustomerReviews for faster lookups
CREATE INDEX idx_package_id ON CustomerReviews(PackageID);
```
