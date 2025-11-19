"""
Generated Code Metadata:
========================
Original URL: https://ittastours.com
Prompt: "Design a database schema for storing information about tour packages, destinations, and activities for a travel company specializing in Egypt and the Middle East."
Generated: DETERMINISTIC_2da251e8397912b4
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for a Travel Company Specializing in Egypt and the Middle East

-- Table to store information about tour packages
CREATE TABLE TourPackages (
    PackageID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each tour package
    PackageName VARCHAR(255) NOT NULL,        -- Name of the tour package
    Description TEXT,                         -- Detailed description of the tour package
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the tour package
    DurationDays INT NOT NULL,                -- Duration of the tour package in days
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the package was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about destinations
CREATE TABLE Destinations (
    DestinationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each destination
    DestinationName VARCHAR(255) NOT NULL,        -- Name of the destination
    Country VARCHAR(255) NOT NULL,                -- Country where the destination is located
    Description TEXT,                             -- Detailed description of the destination
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the destination was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about activities
CREATE TABLE Activities (
    ActivityID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each activity
    ActivityName VARCHAR(255) NOT NULL,        -- Name of the activity
    Description TEXT,                          -- Detailed description of the activity
    Price DECIMAL(10, 2),                      -- Price of the activity (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the activity was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to associate tour packages with destinations
CREATE TABLE TourPackageDestinations (
    ID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for the association
    PackageID INT NOT NULL,                    -- Foreign key referencing TourPackages
    DestinationID INT NOT NULL,                -- Foreign key referencing Destinations
    FOREIGN KEY (PackageID) REFERENCES TourPackages(PackageID) ON DELETE CASCADE,
    FOREIGN KEY (DestinationID) REFERENCES Destinations(DestinationID) ON DELETE CASCADE
);

-- Table to associate tour packages with activities
CREATE TABLE TourPackageActivities (
    ID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for the association
    PackageID INT NOT NULL,                    -- Foreign key referencing TourPackages
    ActivityID INT NOT NULL,                   -- Foreign key referencing Activities
    FOREIGN KEY (PackageID) REFERENCES TourPackages(PackageID) ON DELETE CASCADE,
    FOREIGN KEY (ActivityID) REFERENCES Activities(ActivityID) ON DELETE CASCADE
);

-- Table to associate destinations with activities (optional, if activities are tied to specific destinations)
CREATE TABLE DestinationActivities (
    ID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for the association
    DestinationID INT NOT NULL,                -- Foreign key referencing Destinations
    ActivityID INT NOT NULL,                   -- Foreign key referencing Activities
    FOREIGN KEY (DestinationID) REFERENCES Destinations(DestinationID) ON DELETE CASCADE,
    FOREIGN KEY (ActivityID) REFERENCES Activities(ActivityID) ON DELETE CASCADE
);

-- Indexes for faster querying
CREATE INDEX idx_package_name ON TourPackages(PackageName);
CREATE INDEX idx_destination_name ON Destinations(DestinationName);
CREATE INDEX idx_activity_name ON Activities(ActivityName);
```
