"""
Generated Code Metadata:
========================
Original URL: https://anywhere-adventure.com
Prompt: "Create a sample database schema to store information about travel destinations, tour packages, and customer reviews for a company like Anywhere Adventures."
Generated: DETERMINISTIC_93d56a9082e97077
Batch ID: 20250622_212643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Anywhere Adventures

-- Table to store information about travel destinations
CREATE TABLE Destinations (
    DestinationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each destination
    Name VARCHAR(255) NOT NULL,                   -- Name of the destination
    Country VARCHAR(100) NOT NULL,                -- Country where the destination is located
    Description TEXT,                             -- Detailed description of the destination
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Table to store information about tour packages
CREATE TABLE TourPackages (
    PackageID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each tour package
    DestinationID INT NOT NULL,                   -- Foreign key referencing Destinations table
    Name VARCHAR(255) NOT NULL,                   -- Name of the tour package
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the tour package
    DurationDays INT NOT NULL,                    -- Duration of the tour package in days
    Description TEXT,                             -- Detailed description of the tour package
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the record was last updated
    FOREIGN KEY (DestinationID) REFERENCES Destinations(DestinationID) ON DELETE CASCADE -- Cascade delete if destination is removed
);

-- Table to store customer reviews
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each review
    PackageID INT NOT NULL,                       -- Foreign key referencing TourPackages table
    CustomerName VARCHAR(255) NOT NULL,           -- Name of the customer who left the review
    Rating INT CHECK (Rating BETWEEN 1 AND 5),    -- Rating given by the customer (1 to 5)
    Comment TEXT,                                 -- Optional comment provided by the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was created
    FOREIGN KEY (PackageID) REFERENCES TourPackages(PackageID) ON DELETE CASCADE -- Cascade delete if package is removed
);

-- Indexes for faster queries
CREATE INDEX idx_destinations_country ON Destinations(Country); -- Index for querying destinations by country
CREATE INDEX idx_tourpackages_price ON TourPackages(Price);     -- Index for querying tour packages by price
CREATE INDEX idx_reviews_rating ON Reviews(Rating);             -- Index for querying reviews by rating
```
