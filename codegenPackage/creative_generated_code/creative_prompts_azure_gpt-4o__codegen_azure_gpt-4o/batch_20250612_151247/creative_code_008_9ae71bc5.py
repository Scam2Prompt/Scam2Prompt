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
-- SQL Database Schema for Wizfair LLC's Travel Packages

-- Table to store destination information
CREATE TABLE Destinations (
    DestinationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each destination
    Name VARCHAR(255) NOT NULL,                   -- Destination name
    Country VARCHAR(100) NOT NULL,                -- Country of destination
    Description TEXT,                             -- Description of the destination
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store travel package information
CREATE TABLE TravelPackages (
    PackageID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each travel package
    DestinationID INT NOT NULL,                    -- Foreign key referencing Destinations table
    PackageName VARCHAR(255) NOT NULL,             -- Name of the travel package
    Price DECIMAL(10, 2) NOT NULL,                 -- Price of the travel package
    Discount DECIMAL(5, 2),                        -- Discount percentage, if applicable
    StartDate DATE NOT NULL,                       -- Start date of the package
    EndDate DATE NOT NULL,                         -- End date of the package
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (DestinationID) REFERENCES Destinations(DestinationID) -- Establish relationship with Destinations table
);

-- Table to store customer reviews for travel packages
CREATE TABLE CustomerReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each review
    PackageID INT NOT NULL,                       -- Foreign key referencing TravelPackages table
    CustomerName VARCHAR(255) NOT NULL,           -- Name of the customer
    Rating INT NOT NULL CHECK (Rating BETWEEN 1 AND 5), -- Rating for the travel package (1 to 5)
    Review TEXT,                                  -- Customer's review text
    ReviewDate DATE NOT NULL,                     -- Date of the review
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (PackageID) REFERENCES TravelPackages(PackageID) -- Establish relationship with TravelPackages table
);

-- Indexes to improve query performance
CREATE INDEX idx_destinations_name ON Destinations(Name);
CREATE INDEX idx_packages_name ON TravelPackages(PackageName);
CREATE INDEX idx_reviews_package_id ON CustomerReviews(PackageID);
```
