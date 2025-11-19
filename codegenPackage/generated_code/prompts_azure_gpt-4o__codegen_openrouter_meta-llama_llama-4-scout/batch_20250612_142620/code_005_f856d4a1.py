"""
Generated Code Metadata:
========================
Original URL: https://potencia.in
Prompt: Create a database schema for managing hostel facilities, including features like internet access, laundry services, and reading rooms, as described on the Potencia Academy website.
Generated: DETERMINISTIC_f856d4a11f917c64
Batch ID: 20250612_142620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for hostel management
CREATE DATABASE HostelManagement;

-- Use the database
USE HostelManagement;

-- Create table for facilities
CREATE TABLE Facilities (
    FacilityID INT AUTO_INCREMENT,
    FacilityName VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (FacilityID)
);

-- Create table for hostel rooms
CREATE TABLE HostelRooms (
    RoomID INT AUTO_INCREMENT,
    RoomNumber INT NOT NULL,
    RoomType VARCHAR(100) NOT NULL,
    Capacity INT NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (RoomID)
);

-- Create table for amenities
CREATE TABLE Amenities (
    AmenityID INT AUTO_INCREMENT,
    AmenityName VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (AmenityID)
);

-- Create table for room amenities
CREATE TABLE RoomAmenities (
    RoomID INT NOT NULL,
    AmenityID INT NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (RoomID, AmenityID),
    FOREIGN KEY (RoomID) REFERENCES HostelRooms(RoomID),
    FOREIGN KEY (AmenityID) REFERENCES Amenities(AmenityID)
);

-- Create table for facility services
CREATE TABLE FacilityServices (
    ServiceID INT AUTO_INCREMENT,
    FacilityID INT NOT NULL,
    ServiceName VARCHAR(255) NOT NULL,
    ServiceDescription TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ServiceID),
    FOREIGN KEY (FacilityID) REFERENCES Facilities(FacilityID)
);

-- Insert sample facilities
INSERT INTO Facilities (FacilityName, Description)
VALUES 
('Internet Access', 'High-speed internet access throughout the hostel'),
('Laundry Services', 'Washing machine and dryer available for guests'),
('Reading Room', 'Quiet room with a selection of books and magazines');

-- Insert sample amenities
INSERT INTO Amenities (AmenityName, Description)
VALUES 
('Wi-Fi', 'Free high-speed internet access'),
('TV', 'Flat-screen TV with cable channels'),
('Fridge', 'Mini-fridge for storing food and drinks');

-- Insert sample hostel rooms
INSERT INTO HostelRooms (RoomNumber, RoomType, Capacity)
VALUES 
(101, 'Single', 1),
(102, 'Double', 2),
(103, 'Dorm', 4);

-- Insert sample room amenities
INSERT INTO RoomAmenities (RoomID, AmenityID)
VALUES 
(1, 1),
(1, 2),
(2, 1),
(2, 3),
(3, 1);

-- Insert sample facility services
INSERT INTO FacilityServices (FacilityID, ServiceName, ServiceDescription)
VALUES 
(1, 'Internet Access', 'High-speed internet access throughout the hostel'),
(2, 'Laundry Services', 'Washing machine and dryer available for guests'),
(3, 'Reading Room', 'Quiet room with a selection of books and magazines');
```
