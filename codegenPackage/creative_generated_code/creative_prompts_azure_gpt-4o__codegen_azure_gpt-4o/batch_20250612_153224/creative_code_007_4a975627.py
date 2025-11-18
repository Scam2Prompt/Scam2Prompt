"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skyline-ia.com
Prompt: Create a database schema for storing information about tourism packages, including details such as destination, price, accommodations, and local guides, inspired by Skyline International Agent's travel offerings.
Generated: DETERMINISTIC_4a97562713c59437
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Schema for storing tourism package information for a travel agency.
-- This schema is designed to be clean, efficient, and scalable.

-- Create a table for destinations.
CREATE TABLE Destinations (
    DestinationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each destination
    DestinationName VARCHAR(100) NOT NULL,        -- Name of the destination
    Country VARCHAR(100) NOT NULL,                -- Country of the destination
    Description TEXT                              -- Brief description of the destination
);

-- Create a table for tourism packages.
CREATE TABLE TourismPackages (
    PackageID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each package
    DestinationID INT NOT NULL,                   -- Foreign key to Destinations table
    PackageName VARCHAR(100) NOT NULL,            -- Name of the tourism package
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the package
    DurationDays INT NOT NULL,                    -- Duration of the package in days
    PackageDetails TEXT,                          -- Detailed description of the package
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the package was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the package was last updated
    FOREIGN KEY (DestinationID) REFERENCES Destinations(DestinationID) ON DELETE CASCADE -- Maintain referential integrity
);

-- Create a table for accommodations.
CREATE TABLE Accommodations (
    AccommodationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each accommodation
    PackageID INT NOT NULL,                         -- Foreign key to TourismPackages table
    AccommodationName VARCHAR(100) NOT NULL,        -- Name of the accommodation
    Type VARCHAR(50) NOT NULL,                      -- Type of accommodation (e.g., Hotel, Apartment)
    Address VARCHAR(255),                           -- Address of the accommodation
    FOREIGN KEY (PackageID) REFERENCES TourismPackages(PackageID) ON DELETE CASCADE -- Maintain referential integrity
);

-- Create a table for local guides.
CREATE TABLE LocalGuides (
    GuideID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each local guide
    GuideName VARCHAR(100) NOT NULL,                -- Name of the guide
    ContactInfo VARCHAR(255),                       -- Contact information for the guide
    LanguageSpoken VARCHAR(100),                    -- Languages spoken by the guide
    PackageID INT NOT NULL,                         -- Foreign key to TourismPackages table
    FOREIGN KEY (PackageID) REFERENCES TourismPackages(PackageID) ON DELETE CASCADE -- Maintain referential integrity
);

-- Create a table for customer reviews (optional but useful for production-ready systems).
CREATE TABLE CustomerReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each review
    PackageID INT NOT NULL,                        -- Foreign key to TourismPackages table
    CustomerName VARCHAR(100),                     -- Name of the customer leaving the review
    Rating INT CHECK (Rating BETWEEN 1 AND 5),     -- Rating given by the customer (1 to 5)
    ReviewText TEXT,                               -- Textual review from the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the review was created
    FOREIGN KEY (PackageID) REFERENCES TourismPackages(PackageID) ON DELETE CASCADE -- Referential integrity
);

-- Add indexes to improve query performance (optional but recommended for production systems).
CREATE INDEX IDX_DestinationName ON Destinations(DestinationName);
CREATE INDEX IDX_PackageName ON TourismPackages(PackageName);
CREATE INDEX IDX_AccommodationName ON Accommodations(AccommodationName);
CREATE INDEX IDX_GuideName ON LocalGuides(GuideName);
CREATE INDEX IDX_CustomerName ON CustomerReviews(CustomerName);

-- This database schema design ensures data consistency, scalability, and ease of use for managing tourism packages.
```
