"""
Generated Code Metadata:
========================
Original URL: https://bestholidaysallindia.com
Prompt: "Design a database schema to store information about domestic tour packages, including destinations like Shimla-Manali, Kerala, and Uttrakhand, and their corresponding prices."
Generated: DETERMINISTIC_22c2f7f7906a9fd4
Batch ID: 20250622_212152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for tour packages
CREATE DATABASE TourPackages;

-- Use the TourPackages database
USE TourPackages;

-- Create a table for destinations
CREATE TABLE Destinations (
    DestinationID INT AUTO_INCREMENT,
    DestinationName VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (DestinationID)
);

-- Create a table for tour packages
CREATE TABLE TourPackages (
    PackageID INT AUTO_INCREMENT,
    DestinationID INT,
    PackageName VARCHAR(255) NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    Duration INT NOT NULL,
    Includes VARCHAR(255),
    Excludes VARCHAR(255),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PackageID),
    FOREIGN KEY (DestinationID) REFERENCES Destinations(DestinationID)
);

-- Create a table for package itineraries
CREATE TABLE PackageItineraries (
    ItineraryID INT AUTO_INCREMENT,
    PackageID INT,
    Day INT NOT NULL,
    Activity VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ItineraryID),
    FOREIGN KEY (PackageID) REFERENCES TourPackages(PackageID)
);

-- Create a table for package bookings
CREATE TABLE PackageBookings (
    BookingID INT AUTO_INCREMENT,
    PackageID INT,
    CustomerName VARCHAR(255) NOT NULL,
    BookingDate DATE NOT NULL,
    TravelDate DATE NOT NULL,
    TotalCost DECIMAL(10, 2) NOT NULL,
    Status VARCHAR(50) NOT NULL DEFAULT 'Pending',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (BookingID),
    FOREIGN KEY (PackageID) REFERENCES TourPackages(PackageID)
);

-- Insert sample destinations
INSERT INTO Destinations (DestinationName, Description)
VALUES 
('Shimla-Manali', 'Himachal Pradesh hill stations'),
('Kerala', 'South Indian backwaters and beaches'),
('Uttrakhand', 'Himalayan foothills and pilgrimage sites');

-- Insert sample tour packages
INSERT INTO TourPackages (DestinationID, PackageName, Price, Duration, Includes, Excludes)
VALUES 
(1, 'Shimla-Manali Delight', 15000.00, 7, 'Accommodation, meals, sightseeing', 'Travel, personal expenses'),
(2, 'Kerala Backwaters', 12000.00, 5, 'Accommodation, meals, boat rides', 'Travel, personal expenses'),
(3, 'Uttrakhand Pilgrimage', 10000.00, 6, 'Accommodation, meals, temple visits', 'Travel, personal expenses');

-- Insert sample package itineraries
INSERT INTO PackageItineraries (PackageID, Day, Activity, Description)
VALUES 
(1, 1, 'Travel to Shimla', 'Check-in to hotel'),
(1, 2, 'Shimla sightseeing', 'Visit Mall Road, Jakhu Temple'),
(1, 3, 'Travel to Manali', 'Check-in to hotel'),
(2, 1, 'Travel to Kochi', 'Check-in to hotel'),
(2, 2, 'Backwaters boat ride', 'Explore Kerala backwaters'),
(3, 1, 'Travel to Haridwar', 'Check-in to hotel'),
(3, 2, 'Haridwar sightseeing', 'Visit Har Ki Pauri, Chandi Devi Temple');

-- Insert sample package bookings
INSERT INTO PackageBookings (PackageID, CustomerName, BookingDate, TravelDate, TotalCost)
VALUES 
(1, 'John Doe', '2024-09-01', '2024-09-15', 15000.00),
(2, 'Jane Smith', '2024-08-15', '2024-08-20', 12000.00),
(3, 'Bob Johnson', '2024-07-01', '2024-07-08', 10000.00);
```
