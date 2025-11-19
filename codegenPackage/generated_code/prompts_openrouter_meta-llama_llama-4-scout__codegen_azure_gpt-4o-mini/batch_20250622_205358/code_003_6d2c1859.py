"""
Generated Code Metadata:
========================
Original URL: https://magicegypttours.com
Prompt: "Design a database schema to store information about tour packages, excursions, and customer reviews for a travel company like Magic Egypt Tours, ensuring efficient data retrieval and management."
Generated: DETERMINISTIC_6d2c18592a3447aa
Batch ID: 20250622_205358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Magic Egypt Tours

-- Create a table to store information about tour packages
CREATE TABLE TourPackages (
    PackageID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each tour package
    PackageName VARCHAR(255) NOT NULL,         -- Name of the tour package
    Description TEXT,                           -- Detailed description of the tour package
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the tour package
    Duration INT NOT NULL,                      -- Duration of the tour in days
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the package was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Create a table to store information about excursions
CREATE TABLE Excursions (
    ExcursionID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each excursion
    PackageID INT NOT NULL,                      -- Foreign key referencing TourPackages
    ExcursionName VARCHAR(255) NOT NULL,        -- Name of the excursion
    Description TEXT,                            -- Detailed description of the excursion
    StartTime DATETIME NOT NULL,                 -- Start time of the excursion
    EndTime DATETIME NOT NULL,                   -- End time of the excursion
    FOREIGN KEY (PackageID) REFERENCES TourPackages(PackageID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Create a table to store customer reviews
CREATE TABLE CustomerReviews (
    ReviewID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each review
    PackageID INT NOT NULL,                      -- Foreign key referencing TourPackages
    CustomerName VARCHAR(255) NOT NULL,         -- Name of the customer
    Rating INT CHECK (Rating BETWEEN 1 AND 5),  -- Rating given by the customer (1 to 5)
    ReviewText TEXT,                            -- Text of the review
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the review was created
    FOREIGN KEY (PackageID) REFERENCES TourPackages(PackageID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Create an index on PackageID in CustomerReviews for efficient retrieval
CREATE INDEX idx_package_reviews ON CustomerReviews(PackageID);

-- Create an index on PackageID in Excursions for efficient retrieval
CREATE INDEX idx_package_excursions ON Excursions(PackageID);
```
