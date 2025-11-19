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

-- Create a table for destinations
CREATE TABLE Destinations (
    DestinationID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each destination
    Name VARCHAR(255) NOT NULL,                    -- Name of the destination
    Description TEXT,                               -- Description of the destination
    Location VARCHAR(255),                          -- Geographical location
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for when the record was last updated
);

-- Create a table for activities
CREATE TABLE Activities (
    ActivityID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each activity
    DestinationID INT NOT NULL,                     -- Foreign key referencing Destinations
    Name VARCHAR(255) NOT NULL,                     -- Name of the activity
    Description TEXT,                               -- Description of the activity
    Price DECIMAL(10, 2),                          -- Price of the activity
    Duration INT,                                   -- Duration of the activity in minutes
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp for when the record was last updated
    FOREIGN KEY (DestinationID) REFERENCES Destinations(DestinationID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Create a table for customer reviews
CREATE TABLE Reviews (
    ReviewID INT PRIMARY KEY AUTO_INCREMENT,         -- Unique identifier for each review
    ActivityID INT NOT NULL,                         -- Foreign key referencing Activities
    CustomerName VARCHAR(255) NOT NULL,             -- Name of the customer
    Rating INT CHECK (Rating BETWEEN 1 AND 5),      -- Rating given by the customer (1 to 5)
    Comment TEXT,                                    -- Review comment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp for when the review was created
    FOREIGN KEY (ActivityID) REFERENCES Activities(ActivityID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Create a table for travel packages
CREATE TABLE TravelPackages (
    PackageID INT PRIMARY KEY AUTO_INCREMENT,        -- Unique identifier for each travel package
    DestinationID INT NOT NULL,                      -- Foreign key referencing Destinations
    PackageName VARCHAR(255) NOT NULL,              -- Name of the travel package
    Description TEXT,                                -- Description of the travel package
    Price DECIMAL(10, 2),                           -- Price of the travel package
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp for when the record was last updated
    FOREIGN KEY (DestinationID) REFERENCES Destinations(DestinationID) ON DELETE CASCADE  -- Ensures referential integrity
);
```
