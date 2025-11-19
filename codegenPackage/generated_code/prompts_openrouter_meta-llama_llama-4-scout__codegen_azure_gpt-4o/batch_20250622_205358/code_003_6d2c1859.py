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
-- Database schema for a travel company like Magic Egypt Tours

-- Table to store information about tour packages
CREATE TABLE TourPackages (
    PackageID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each tour package
    PackageName VARCHAR(255) NOT NULL,        -- Name of the tour package
    Description TEXT,                         -- Detailed description of the tour package
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the tour package
    DurationDays INT NOT NULL,                -- Duration of the tour package in days
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the package was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about excursions
CREATE TABLE Excursions (
    ExcursionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each excursion
    TourPackageID INT NOT NULL,                 -- Foreign key referencing TourPackages
    ExcursionName VARCHAR(255) NOT NULL,        -- Name of the excursion
    Description TEXT,                           -- Detailed description of the excursion
    Location VARCHAR(255) NOT NULL,             -- Location of the excursion
    DurationHours INT NOT NULL,                 -- Duration of the excursion in hours
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the excursion
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the excursion was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (TourPackageID) REFERENCES TourPackages(PackageID) ON DELETE CASCADE -- Ensures data integrity
);

-- Table to store customer reviews
CREATE TABLE CustomerReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each review
    TourPackageID INT NOT NULL,              -- Foreign key referencing TourPackages
    CustomerName VARCHAR(255) NOT NULL,      -- Name of the customer
    Rating INT NOT NULL CHECK (Rating BETWEEN 1 AND 5), -- Rating between 1 and 5
    ReviewText TEXT,                         -- Detailed review text
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the review was created
    FOREIGN KEY (TourPackageID) REFERENCES TourPackages(PackageID) ON DELETE CASCADE -- Ensures data integrity
);

-- Indexes for efficient data retrieval
CREATE INDEX idx_tour_package_name ON TourPackages(PackageName); -- Index for quick search by package name
CREATE INDEX idx_excursion_name ON Excursions(ExcursionName);    -- Index for quick search by excursion name
CREATE INDEX idx_customer_name ON CustomerReviews(CustomerName); -- Index for quick search by customer name
```
