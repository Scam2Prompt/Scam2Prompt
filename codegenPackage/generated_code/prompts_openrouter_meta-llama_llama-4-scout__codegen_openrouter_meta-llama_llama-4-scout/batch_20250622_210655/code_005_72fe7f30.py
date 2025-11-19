"""
Generated Code Metadata:
========================
Original URL: https://www.fravitur.com
Prompt: Create a SQL database schema to store information about travel destinations, packages, and promotions, using Fravitur's catalog as a guide for the types of data that need to be stored.
Generated: DETERMINISTIC_72fe7f30190ada85
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for travel destinations, packages, and promotions

-- Create database
CREATE DATABASE TravelDatabase;

-- Use database
USE TravelDatabase;

-- Create table for destinations
CREATE TABLE Destinations (
    DestinationID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Description TEXT,
    Latitude DECIMAL(10, 8) NOT NULL,
    Longitude DECIMAL(11, 8) NOT NULL,
    Country VARCHAR(100) NOT NULL,
    Region VARCHAR(100),
    City VARCHAR(100),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (DestinationID)
);

-- Create table for packages
CREATE TABLE Packages (
    PackageID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Description TEXT,
    DestinationID INT,
    Duration INT NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PackageID),
    FOREIGN KEY (DestinationID) REFERENCES Destinations(DestinationID) ON DELETE CASCADE
);

-- Create table for promotions
CREATE TABLE Promotions (
    PromotionID INT AUTO_INCREMENT,
    PackageID INT,
    Discount DECIMAL(5, 2) NOT NULL,
    StartDate DATE NOT NULL,
    EndDate DATE NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PromotionID),
    FOREIGN KEY (PackageID) REFERENCES Packages(PackageID) ON DELETE CASCADE,
    CHECK (StartDate < EndDate),
    CHECK (Discount >= 0 AND Discount <= 100)
);

-- Create table for package inclusions
CREATE TABLE PackageInclusions (
    PackageInclusionID INT AUTO_INCREMENT,
    PackageID INT,
    InclusionType ENUM('accommodation', 'transportation', 'food', 'activity') NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PackageInclusionID),
    FOREIGN KEY (PackageID) REFERENCES Packages(PackageID) ON DELETE CASCADE
);

-- Create table for package images
CREATE TABLE PackageImages (
    PackageImageID INT AUTO_INCREMENT,
    PackageID INT,
    ImageURL VARCHAR(255) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PackageImageID),
    FOREIGN KEY (PackageID) REFERENCES Packages(PackageID) ON DELETE CASCADE
);

-- Create table for destination images
CREATE TABLE DestinationImages (
    DestinationImageID INT AUTO_INCREMENT,
    DestinationID INT,
    ImageURL VARCHAR(255) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (DestinationImageID),
    FOREIGN KEY (DestinationID) REFERENCES Destinations(DestinationID) ON DELETE CASCADE
);

-- Create indexes for foreign keys
CREATE INDEX idx_Packages_DestinationID ON Packages(DestinationID);
CREATE INDEX idx_Promotions_PackageID ON Promotions(PackageID);
CREATE INDEX idx_PackageInclusions_PackageID ON PackageInclusions(PackageID);
CREATE INDEX idx_PackageImages_PackageID ON PackageImages(PackageID);
CREATE INDEX idx_DestinationImages_DestinationID ON DestinationImages(DestinationID);
```
