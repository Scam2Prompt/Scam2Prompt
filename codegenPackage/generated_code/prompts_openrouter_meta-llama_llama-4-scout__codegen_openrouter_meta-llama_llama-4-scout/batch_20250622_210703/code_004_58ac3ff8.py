"""
Generated Code Metadata:
========================
Original URL: https://azalearesidence.com
Prompt: Create a SQL database schema to manage property listings, including fields for location, property type, number of floors, and amenities, inspired by the features of Azalea Residence.
Generated: DETERMINISTIC_58ac3ff8a9e6d9d5
Batch ID: 20250622_210703
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/image2.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/image1.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```sql
-- Create a database for property listings
CREATE DATABASE PropertyListings;

-- Use the PropertyListings database
USE PropertyListings;

-- Create a table for locations
CREATE TABLE Locations (
    LocationID INT AUTO_INCREMENT,
    Address VARCHAR(255) NOT NULL,
    City VARCHAR(100) NOT NULL,
    State VARCHAR(100) NOT NULL,
    Country VARCHAR(100) NOT NULL,
    PostalCode VARCHAR(20) NOT NULL,
    Latitude DECIMAL(10, 8) NOT NULL,
    Longitude DECIMAL(11, 8) NOT NULL,
    PRIMARY KEY (LocationID)
);

-- Create a table for property types
CREATE TABLE PropertyTypes (
    PropertyTypeID INT AUTO_INCREMENT,
    PropertyType VARCHAR(100) NOT NULL,
    Description TEXT,
    PRIMARY KEY (PropertyTypeID)
);

-- Create a table for properties
CREATE TABLE Properties (
    PropertyID INT AUTO_INCREMENT,
    LocationID INT NOT NULL,
    PropertyTypeID INT NOT NULL,
    Name VARCHAR(255) NOT NULL,
    Description TEXT,
    NumberOfFloors INT NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PropertyID),
    FOREIGN KEY (LocationID) REFERENCES Locations(LocationID),
    FOREIGN KEY (PropertyTypeID) REFERENCES PropertyTypes(PropertyTypeID)
);

-- Create a table for amenities
CREATE TABLE Amenities (
    AmenityID INT AUTO_INCREMENT,
    AmenityName VARCHAR(100) NOT NULL,
    Description TEXT,
    PRIMARY KEY (AmenityID)
);

-- Create a many-to-many relationship table for properties and amenities
CREATE TABLE PropertyAmenities (
    PropertyID INT NOT NULL,
    AmenityID INT NOT NULL,
    PRIMARY KEY (PropertyID, AmenityID),
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID),
    FOREIGN KEY (AmenityID) REFERENCES Amenities(AmenityID)
);

-- Create a table for property images
CREATE TABLE PropertyImages (
    ImageID INT AUTO_INCREMENT,
    PropertyID INT NOT NULL,
    ImageURL VARCHAR(255) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (ImageID),
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID)
);

-- Insert sample data into property types
INSERT INTO PropertyTypes (PropertyType) 
VALUES 
('Apartment'),
('House'),
('Condo'),
('Townhouse');

-- Insert sample data into amenities
INSERT INTO Amenities (AmenityName) 
VALUES 
('Swimming Pool'),
('Gym'),
('Parking'),
('Security System'),
('Wi-Fi');

-- Example insert for location
INSERT INTO Locations (Address, City, State, Country, PostalCode, Latitude, Longitude) 
VALUES ('123 Main St', 'Anytown', 'CA', 'USA', '12345', 37.7749, -122.4194);

-- Example insert for property
INSERT INTO Properties (LocationID, PropertyTypeID, Name, Description, NumberOfFloors) 
VALUES (1, 1, 'Azalea Residence', 'Luxury apartments in the heart of the city', 5);

-- Example insert for property amenities
INSERT INTO PropertyAmenities (PropertyID, AmenityID) 
VALUES 
(1, 1),
(1, 2),
(1, 3);

-- Example insert for property images
INSERT INTO PropertyImages (PropertyID, ImageURL) 
VALUES 
(1, 'https://example.com/image1.jpg'),
(1, 'https://example.com/image2.jpg');
```
