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
-- Create database for SafarGenie
CREATE DATABASE SafarGenieDB;

-- Use SafarGenie database
USE SafarGenieDB;

-- Create table for destinations
CREATE TABLE Destinations (
    DestinationID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Description TEXT,
    Country VARCHAR(100) NOT NULL,
    City VARCHAR(100),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (DestinationID)
);

-- Create table for themes
CREATE TABLE Themes (
    ThemeID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ThemeID)
);

-- Create table for tour packages
CREATE TABLE TourPackages (
    PackageID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Description TEXT,
    DestinationID INT,
    ThemeID INT,
    Duration INT NOT NULL,  -- in days
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PackageID),
    FOREIGN KEY (DestinationID) REFERENCES Destinations(DestinationID),
    FOREIGN KEY (ThemeID) REFERENCES Themes(ThemeID)
);

-- Create table for pricing
CREATE TABLE Pricing (
    PricingID INT AUTO_INCREMENT,
    PackageID INT,
    AdultPrice DECIMAL(10, 2) NOT NULL,
    ChildPrice DECIMAL(10, 2),
    InfantPrice DECIMAL(10, 2),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PricingID),
    FOREIGN KEY (PackageID) REFERENCES TourPackages(PackageID)
);

-- Create table for inclusions
CREATE TABLE Inclusions (
    InclusionID INT AUTO_INCREMENT,
    PackageID INT,
    InclusionType ENUM('food', 'accommodation', 'transportation', 'activities') NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (InclusionID),
    FOREIGN KEY (PackageID) REFERENCES TourPackages(PackageID)
);

-- Create table for bookings
CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT,
    PackageID INT,
    CustomerName VARCHAR(255) NOT NULL,
    TravelDate DATE NOT NULL,
    AdultCount INT NOT NULL,
    ChildCount INT,
    InfantCount INT,
    TotalCost DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (BookingID),
    FOREIGN KEY (PackageID) REFERENCES TourPackages(PackageID)
);

-- Example insert statements
INSERT INTO Destinations (Name, Description, Country, City)
VALUES 
('Paris', 'The city of love', 'France', 'Paris'),
('Rome', 'The eternal city', 'Italy', 'Rome');

INSERT INTO Themes (Name, Description)
VALUES 
('Romance', 'Experience love in the air'),
('Adventure', 'Get your adrenaline pumping');

INSERT INTO TourPackages (Name, Description, DestinationID, ThemeID, Duration)
VALUES 
('Parisian Love', 'Romantic getaway to Paris', 1, 1, 5),
('Roman Holiday', 'Explore the history of Rome', 2, 2, 7);

INSERT INTO Pricing (PackageID, AdultPrice, ChildPrice, InfantPrice)
VALUES 
(1, 2000.00, 1500.00, 500.00),
(2, 2500.00, 2000.00, 750.00);

INSERT INTO Inclusions (PackageID, InclusionType, Description)
VALUES 
(1, 'food', 'Breakfast and dinner at local restaurants'),
(1, 'accommodation', '5-star hotel stay'),
(2, 'transportation', 'Airport transfers and sightseeing tours');

INSERT INTO Bookings (PackageID, CustomerName, TravelDate, AdultCount, ChildCount, InfantCount, TotalCost)
VALUES 
(1, 'John Doe', '2024-09-20', 2, 1, 0, 4000.00),
(2, 'Jane Smith', '2024-10-15', 1, 0, 1, 2500.00);
```
