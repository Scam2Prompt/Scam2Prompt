"""
Generated Code Metadata:
========================
Original URL: https://www.stellarviewrealty.com
Prompt: Create a SQL database schema to store and manage real estate listings similar to those offered by StellarView Realty, including fields for property features and contact information.
Generated: DETERMINISTIC_0dd79b9b5df4ff0e
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for real estate listings
CREATE DATABASE RealEstateListings;

-- Use the database
USE RealEstateListings;

-- Create a table for property types
CREATE TABLE PropertyTypes (
    PropertyTypeID INT AUTO_INCREMENT,
    PropertyType VARCHAR(50) NOT NULL,
    PRIMARY KEY (PropertyTypeID)
);

-- Create a table for property statuses
CREATE TABLE PropertyStatuses (
    PropertyStatusID INT AUTO_INCREMENT,
    PropertyStatus VARCHAR(50) NOT NULL,
    PRIMARY KEY (PropertyStatusID)
);

-- Create a table for agents
CREATE TABLE Agents (
    AgentID INT AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    PRIMARY KEY (AgentID)
);

-- Create a table for properties
CREATE TABLE Properties (
    PropertyID INT AUTO_INCREMENT,
    AgentID INT NOT NULL,
    PropertyTypeID INT NOT NULL,
    PropertyStatusID INT NOT NULL,
    Address VARCHAR(255) NOT NULL,
    City VARCHAR(100) NOT NULL,
    State VARCHAR(100) NOT NULL,
    ZipCode VARCHAR(20) NOT NULL,
    Price DECIMAL(18, 2) NOT NULL,
    SquareFootage INT NOT NULL,
    LotSize DECIMAL(10, 2) NOT NULL,
    Bedrooms INT NOT NULL,
    Bathrooms INT NOT NULL,
    PRIMARY KEY (PropertyID),
    FOREIGN KEY (AgentID) REFERENCES Agents(AgentID),
    FOREIGN KEY (PropertyTypeID) REFERENCES PropertyTypes(PropertyTypeID),
    FOREIGN KEY (PropertyStatusID) REFERENCES PropertyStatuses(PropertyStatusID)
);

-- Create a table for property features
CREATE TABLE PropertyFeatures (
    PropertyFeatureID INT AUTO_INCREMENT,
    PropertyID INT NOT NULL,
    Feature VARCHAR(100) NOT NULL,
    PRIMARY KEY (PropertyFeatureID),
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID)
);

-- Create a table for property amenities
CREATE TABLE PropertyAmenities (
    PropertyAmenityID INT AUTO_INCREMENT,
    PropertyID INT NOT NULL,
    Amenity VARCHAR(100) NOT NULL,
    PRIMARY KEY (PropertyAmenityID),
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID)
);

-- Create a table for property showing schedules
CREATE TABLE ShowingSchedules (
    ShowingScheduleID INT AUTO_INCREMENT,
    PropertyID INT NOT NULL,
    ShowingDate DATE NOT NULL,
    ShowingTime TIME NOT NULL,
    AgentID INT NOT NULL,
    PRIMARY KEY (ShowingScheduleID),
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID),
    FOREIGN KEY (AgentID) REFERENCES Agents(AgentID)
);

-- Create a table for offers
CREATE TABLE Offers (
    OfferID INT AUTO_INCREMENT,
    PropertyID INT NOT NULL,
    OfferPrice DECIMAL(18, 2) NOT NULL,
    OfferDate DATE NOT NULL,
    AgentID INT NOT NULL,
    PRIMARY KEY (OfferID),
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID),
    FOREIGN KEY (AgentID) REFERENCES Agents(AgentID)
);

-- Insert sample data into property types table
INSERT INTO PropertyTypes (PropertyType)
VALUES 
('Residential'),
('Commercial'),
('Condo'),
('Townhouse'),
('Farm');

-- Insert sample data into property statuses table
INSERT INTO PropertyStatuses (PropertyStatus)
VALUES 
('Active'),
('Pending'),
('Sold'),
('Expired'),
('Withdrawn');

-- Insert sample data into agents table
INSERT INTO Agents (FirstName, LastName, Email, Phone)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890'),
('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210');

-- Insert sample data into properties table
INSERT INTO Properties (AgentID, PropertyTypeID, PropertyStatusID, Address, City, State, ZipCode, Price, SquareFootage, LotSize, Bedrooms, Bathrooms)
VALUES 
(1, 1, 1, '123 Main St', 'Anytown', 'CA', '12345', 500000.00, 2000, 0.25, 3, 2),
(2, 2, 1, '456 Elm St', 'Othertown', 'NY', '67890', 750000.00, 3000, 0.50, 4, 3);

-- Insert sample data into property features table
INSERT INTO PropertyFeatures (PropertyID, Feature)
VALUES 
(1, 'Pool'),
(1, 'Backyard'),
(2, 'Fireplace'),
(2, 'Deck');

-- Insert sample data into property amenities table
INSERT INTO PropertyAmenities (PropertyID, Amenity)
VALUES 
(1, 'Gym'),
(1, 'Clubhouse'),
(2, 'Parking Garage'),
(2, 'Doorman');

-- Insert sample data into showing schedules table
INSERT INTO ShowingSchedules (PropertyID, ShowingDate, ShowingTime, AgentID)
VALUES 
(1, '2024-09-17', '10:00:00', 1),
(2, '2024-09-18', '14:00:00', 2);

-- Insert sample data into offers table
INSERT INTO Offers (PropertyID, OfferPrice, OfferDate, AgentID)
VALUES 
(1, 475000.00, '2024-09-16', 2),
(2, 725000.00, '2024-09-17', 1);
```
