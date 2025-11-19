"""
Generated Code Metadata:
========================
Original URL: https://bvitravel.co.uk
Prompt: "Design a database schema for storing information about BVI travel packages, including details on destinations, activities, and customer reviews."
Generated: DETERMINISTIC_1454018494db90ce
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about BVI travel packages

-- Table to store travel packages
CREATE TABLE TravelPackages (
    PackageID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each travel package
    PackageName VARCHAR(255) NOT NULL,        -- Name of the travel package
    Description TEXT,                         -- Detailed description of the package
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the package
    DurationDays INT NOT NULL,                -- Duration of the package in days
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the package was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store destinations associated with travel packages
CREATE TABLE Destinations (
    DestinationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each destination
    PackageID INT NOT NULL,                       -- Foreign key referencing TravelPackages
    DestinationName VARCHAR(255) NOT NULL,        -- Name of the destination
    Description TEXT,                             -- Description of the destination
    FOREIGN KEY (PackageID) REFERENCES TravelPackages(PackageID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store activities associated with travel packages
CREATE TABLE Activities (
    ActivityID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each activity
    PackageID INT NOT NULL,                    -- Foreign key referencing TravelPackages
    ActivityName VARCHAR(255) NOT NULL,        -- Name of the activity
    Description TEXT,                          -- Description of the activity
    FOREIGN KEY (PackageID) REFERENCES TravelPackages(PackageID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store customer reviews for travel packages
CREATE TABLE CustomerReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each review
    PackageID INT NOT NULL,                  -- Foreign key referencing TravelPackages
    CustomerName VARCHAR(255) NOT NULL,      -- Name of the customer
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating given by the customer (1 to 5)
    ReviewText TEXT,                         -- Text of the review
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the review was created
    FOREIGN KEY (PackageID) REFERENCES TravelPackages(PackageID) ON DELETE CASCADE -- Cascade delete
);

-- Indexes for optimizing queries
CREATE INDEX idx_package_name ON TravelPackages(PackageName); -- Index for package name
CREATE INDEX idx_destination_name ON Destinations(DestinationName); -- Index for destination name
CREATE INDEX idx_activity_name ON Activities(ActivityName); -- Index for activity name
CREATE INDEX idx_customer_name ON CustomerReviews(CustomerName); -- Index for customer name
```
