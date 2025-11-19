"""
Generated Code Metadata:
========================
Original URL: https://safargenie.com
Prompt: "Design a database schema for storing information about tour packages, including destinations, themes, and pricing, for a travel company like SafarGenie."
Generated: DETERMINISTIC_ce88cd8598fba7c7
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about tour packages for a travel company

-- Table to store information about destinations
CREATE TABLE Destinations (
    DestinationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each destination
    Name VARCHAR(255) NOT NULL,                   -- Name of the destination
    Country VARCHAR(255) NOT NULL,                -- Country where the destination is located
    Description TEXT,                             -- Brief description of the destination
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store information about themes
CREATE TABLE Themes (
    ThemeID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each theme
    Name VARCHAR(255) NOT NULL,                   -- Name of the theme (e.g., Adventure, Relaxation)
    Description TEXT,                             -- Brief description of the theme
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store information about tour packages
CREATE TABLE TourPackages (
    PackageID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each tour package
    Name VARCHAR(255) NOT NULL,                   -- Name of the tour package
    DestinationID INT NOT NULL,                   -- Foreign key referencing Destinations table
    ThemeID INT NOT NULL,                         -- Foreign key referencing Themes table
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the tour package
    DurationDays INT NOT NULL,                    -- Duration of the tour package in days
    Description TEXT,                             -- Brief description of the tour package
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (DestinationID) REFERENCES Destinations(DestinationID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (ThemeID) REFERENCES Themes(ThemeID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store additional images for destinations
CREATE TABLE DestinationImages (
    ImageID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each image
    DestinationID INT NOT NULL,                   -- Foreign key referencing Destinations table
    ImageURL VARCHAR(2083) NOT NULL,              -- URL of the image
    Caption VARCHAR(255),                         -- Optional caption for the image
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (DestinationID) REFERENCES Destinations(DestinationID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store reviews for tour packages
CREATE TABLE PackageReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each review
    PackageID INT NOT NULL,                       -- Foreign key referencing TourPackages table
    ReviewerName VARCHAR(255) NOT NULL,           -- Name of the reviewer
    Rating INT CHECK (Rating BETWEEN 1 AND 5),    -- Rating given by the reviewer (1 to 5)
    Comment TEXT,                                 -- Optional comment by the reviewer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (PackageID) REFERENCES TourPackages(PackageID) ON DELETE CASCADE -- Cascade delete
);

-- Indexes for optimizing queries
CREATE INDEX idx_destinations_name ON Destinations(Name);
CREATE INDEX idx_themes_name ON Themes(Name);
CREATE INDEX idx_tourpackages_name ON TourPackages(Name);
CREATE INDEX idx_tourpackages_price ON TourPackages(Price);
CREATE INDEX idx_reviews_packageid ON PackageReviews(PackageID);
```
